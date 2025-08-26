from typing import Optional
from dotenv import load_dotenv
import os

class CustomLoadEnv:
    @staticmethod
    def load_config(

                    varibals_for_load:list[str],
                    from_custom_env:Optional[bool] = False,
                    env_file_name:Optional[str] = None):

        """Это функция будет загружать переменные из файлов с расширением .env.
        В varibals_for_load укажите какие параметры она будет загружать ввиде листа пример ["MY_PARAM1","MY_PARAM2"]
        В from_custom_env True или False означает будет ли у env файла какое-то кастамное имя если True то в env_file_name укажите его.
         Если оставьте env_file_name не тронутым
         По дефолту from_custom_env равно False"""

        if from_custom_env:
            load_dotenv(env_file_name)
            all_varibals = {}
            for var in varibals_for_load:
                all_varibals[var] = os.getenv(var)

            return all_varibals
        else:
            load_dotenv()
            all_varibals_not_custom = {}
            for var in varibals_for_load:
                all_varibals_not_custom[var] = os.getenv(var)
            return all_varibals_not_custom