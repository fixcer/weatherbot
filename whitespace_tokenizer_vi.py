import typing
from typing import Any, Optional, Text, Dict, List, Type

from rasa.nlu.components import Component
from rasa.nlu.config import RasaNLUModelConfig
from rasa.nlu.training_data import Message, TrainingData
from rasa.constants import DOCS_URL_COMPONENTS
from rasa.nlu.tokenizers.tokenizer import Token, Tokenizer
import rasa.utils.common as common_utils

from pyvi import ViTokenizer, ViPosTagger, ViUtils

if typing.TYPE_CHECKING:
    from rasa.nlu.model import Metadata

class VietnameseTokenizer(Tokenizer):

    @classmethod
    def required_packages(cls) -> List[str]:

        return ["pyvi"]

    defaults = {}

    supported_language_list = ["vi"]

    def __init__(self, component_config: Dict[Text, Any] = None) -> None:
        super().__init__(component_config)

    def tokenize(self, message: Message, attribute: Text) -> List[Token]:
        text = message.get(attribute)
        words = ViTokenizer.tokenize(text).split()

        words = [word.replace('_', ' ') for word in words]

        return self._convert_words_to_tokens(words, text)
