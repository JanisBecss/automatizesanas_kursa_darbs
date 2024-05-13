import search_2
import translate
import excel

def main():
    edieni = []
    svars_g = []
    kalorijas = tauki = oglhidrati = proteini = 0
    print()
    print("Sveiki! Jums jāievada pārtikas produkta nosaukums, kad prasīs 'Ko ēdāt:'")
    print("Kad prasīs 'Cik g apēdāt:' jums jāievada TIKAI skaitlis!")
    print("Lūdzu rakstiett vispārīgākus produktu nosaukumus, piem., 'vistas cepetis'->'vista' , 'piena spēks'->'proteīna piens'")
    print("Kad visi produkti sarakstīti, uz jautājumu 'Ko ēdāt:' ievadiet atbildi 'x'")
    print("Programma automātiski aprēķinās kopējo kaloriju, tauku, ogļhidrātu, proteīnu daudzumu")
    print("Kopējo uzturvērtību daudzumu izvadīs uz ekrāna un saglabās Excel failā")
    print("Jūs varat startēt programmu neierobežotu reižu skaitu, Excel failā atbilstošās vērtības tiks pieskaitītas atbilstošā datuma rindā.")
    print("Vairāku ierakstu gadījumā, programma var apstrādāt datus ilgāku laika posmu.")

    while True:
        ediens_lv = str(input("Ko ēdāt: "))
        if ediens_lv.lower() == "x":
            break
        edieni.append(ediens_lv)
        svars = float(input("Cik g apēdāt: "))
        svars_g.append(svars)

    edieni_eng = translate.tulkosana(edieni)

    for i in range(len(edieni_eng)):
        uzturvertiba = search_2.mekletajs(edieni_eng[i])
        kalorijas += uzturvertiba[0] * (svars_g[i] / 100)
        tauki += uzturvertiba[1] * (svars_g[i] / 100)
        oglhidrati += uzturvertiba[2] * (svars_g[i] / 100)
        proteini += uzturvertiba[3] * (svars_g[i] / 100)
        
    
    excel.write_to_file(kalorijas, tauki, oglhidrati, proteini)
    print(f"Kalorijas: {kalorijas}cal Tauki: {tauki}g Ogļhidrāti: {oglhidrati}g Proteīni: {proteini}g")
    print("Dati saglabāti!")

if __name__ == "__main__":
    main()

