class Interaction:
    def __init__(self):
        self.__filename = "scores.txt"

    def writeNewScore(self, score: str, encoding="UTF-8"):
        try:
            with open(self.__filename, encoding=encoding, mode="a") as file:
                file.write(score + ";")
        except (ValueError, ZeroDivisionError) as error:
            print("Chybné zadání!")
            print(error)
            print(type(error))
            return False
        except FileNotFoundError as error:
            print("Nebylo možné otevřít soubor")
            print(error)
            print(type(error))
            return False
        else:
            print("Vše je v pořádku")
        finally:
            file.close()
        return True

    def __readScores(self, encoding="UTF-8"):
        try:
            with open(self.__filename, encoding=encoding) as file:
                data = file.read()
        except (ValueError, ZeroDivisionError) as error:
            print("Chybné zadání!")
            print(error)
            print(type(error))
        except FileNotFoundError as error:
            print("Nebylo možné otevřít soubor")
            print(error)
            print(type(error))
        else:
            print("Vše je v pořádku")
        finally:
            file.close()
        return data

    def getHighestScore(self):
        all_scores = self.__readScores()
        all_scores = all_scores.split(";")
        all_scores.pop()
        print(all_scores)
        if len(all_scores) < 1:
            return str(len(all_scores))
        return max(all_scores)
