import ast


class Antiplagiat:
    
    """ Данный класс позволяет вычислить степень схожести между двумя кодами:
    если степень схожести больше 0.5, то второй код (text_2) был списан с первого кода (text_1)."""
    
    def __init__(self, text_1, text_2):
        
        self.text_1 = text_1
        self.text_2 = text_2
        
    def parsik(self, text):
        
        """Данная функция преобразует наш код, который мы получаем в виде строки, в синтаксическое дерево."""
        
        code = ast.parse(text)

        normalized_code = ast.dump(code)
        
        return normalized_code
    
    def similarity(self):
        
        """Данная функция выдает коэффициент схожести двух строк, используя функцию levenshtein.""" 
        
        
        normalized_code1 = self.parsik(self.text_1)
        normalized_code2 = self.parsik(self.text_2)
        
        distance = self.levenshtein(normalized_code1, normalized_code2)
        similarity = 1 - (distance / max(len(normalized_code1), len(normalized_code2)))

        return round(similarity, 3)
    
    def levenshtein(self, text1, text2):
        
        """Данная функция показывает расстояние Левенштейна между двумя строками, 
        определяемое как минимальное число односимвольных правок (вставок, удалений или замен), 
        необходимых для преобразования одной строки в другую."""
    
        d = [[0]*(len(text2)+1) for i in range(len(text1)+1)]
    
        for i in range(len(text1)+1):
            d[i][0] = i
    
        for j in range(len(text2)+1):
            d[0][j] = j
        
        for i in range(1, len(text1)+1):
            for j in range(1, len(text2)+1):
                c = int(text1[i-1]!=text2[j-1])
                d[i][j] = min(d[i-1][j]+1, d[i][j-1]+1, d[i-1][j-1]+c)     
            
        return d[len(text1)][len(text2)]