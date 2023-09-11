class ReadFile:
    def open_file(self):
        archivo = open('Files/File.txt', 'r')
        self.text = archivo.read()
        archivo.close()

    def check_text(self):
        with open('Files/File_out.txt', 'w') as Text_out:
            character = input('Enter character: ')
            for caracter in self.text:
                if caracter == ' ':
                    Text_out.write('\n')
                elif caracter == character:
                    Text_out.write('\n')
                    Text_out.write(character)
                    Text_out.write('\n')    
                        
                else:
                    Text_out.write(caracter)