from abc import ABC
from openai import OpenAI
from copy import deepcopy

from src.utils import ConsoleHelpers


class Agent(ABC):
    def __init__(
            self,
            name: str,
            role: str,
            opening_statement_instructions: str,
            model: str = "gpt-3.5-turbo"
    ):
        self.client = OpenAI()
        self.model: str = model
        self.name: str = name
        self.role: str = role
        self.opening_statement_instructions: str = opening_statement_instructions
        self.opening_statement: str = ""
        self.context: list[dict[str, str]] = []
        self.conversation_summary: str = ""

        self.add_to_context("system", self.role)
        self.opening_statement = self.generate_opening_statement()

    def add_to_context(self, role: str, content: str):
        self.context.append({"role": role, "content": content})

    def generate_opening_statement(self) -> str:
        context_with_only_the_role: list[dict[str, str]] = self.get_context_copy()[:1]
        context_with_only_the_role.append({"role": "user", "content": self.opening_statement_instructions})
        completion = self.client.chat.completions.create(model=self.model, messages=context_with_only_the_role)
        opening_statement: str = completion.choices[0].message.content
        return opening_statement

    def get_context_copy(self) -> list[dict[str, str]]:
        context_copy: list[dict[str, str]] = deepcopy(self.context)
        return context_copy

    def take_input_and_generate_response(self, user_input: str) -> str:
        self.take_user_input(user_input)
        response = self.generate_response()
        return response

    def take_user_input(self, user_input: str) -> None:
        self.context.append({"role": "user", "content": user_input})

    def generate_response(self) -> str:
        completion = self.client.chat.completions.create(model=self.model, messages=self.context)
        response: str = completion.choices[0].message.content
        self.context.append({"role": "assistant", "content": response})
        return response

    def attach_name(self, message: str) -> str:
        return f"[{self.name}]: {message}"

    def reset_context(self) -> None:
        context_but_only_the_role_description: list[dict[str, str]] = self.context[:1]
        self.context = context_but_only_the_role_description

    def attach_name_and_convert_to_block_text(self, agent_response: str) -> str:
        response: str = agent_response
        response_with_name: str = self.attach_name(response)
        response_with_name_as_block_text: str = ConsoleHelpers.convert_to_block_text(response_with_name)
        return response_with_name_as_block_text

    def has_user_asked_to_end_conversation(self):
        context_copy: list[dict[str, str]] = self.get_context_copy()
        context_copy.append(
            {
                "role": "user",
                "content": ("If I want to move on, skip to the next process or end the conversation: "
                            "Respond with \"1\". If not: Respond with \"0\".")
            }
        )
        completion = self.client.chat.completions.create(model=self.model, messages=context_copy)
        response: str = completion.choices[0].message.content

        should_end_conversation: bool = False
        if response == "1":
            should_end_conversation = True
        return should_end_conversation
