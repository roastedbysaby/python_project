import csv
import pandas as pd


csv_file_to_open = "immeuble.csv"
with open(csv_file_to_open) as immFile:
    data = csv.reader(immFile)
    
    immeuble_and_numero_dossier = []
    matricule = []
    numero_dossier = []
    for row in data:
        if row[0] != "Matricule":
            immeuble_and_numero_dossier.append(row[0])


    immeuble_and_numero_dossier.pop(0)
    #print(immeuble_and_numero_dossier)

    for new_rows in immeuble_and_numero_dossier:
        if len(new_rows) == 8:
            matricule.append(new_rows)
        if len(new_rows) == 30:
            numero_dossier.append(new_rows)

    # print("Les matricule ")
    # print(" ")
    # print(matricule)
    # print("Les numero de dossier")
    # print(" ")
    # print(numero_dossier)

    """Create dataFrame converter """



    dataFrame = pd.DataFrame(
        { 
            "Numero de Dossier": pd.Series(matricule),
            "Matricule" : pd.Series(numero_dossier),
        
        }
    )

    dataframe = dataFrame.astype(str)

    ##  CSV FILE CREATOR
    new_file_csv = "result_immeuble.csv"

    dataFrame.to_csv(new_file_csv, index= False)


    print( "==== ROW ====")
    print( "==== ROW ====")

    print(" NUMERO DOSSIER")
    print(len(matricule))
    print("MATRICULE")
    print(len(numero_dossier)) 


    





        

