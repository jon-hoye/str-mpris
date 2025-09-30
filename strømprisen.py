import customtkinter
import os
import requests
from datetime import datetime
from PIL import ImageGrab

#hente dato og tid
current_datetime = datetime.now()


#dato
år = current_datetime.year

måned_feil_formattert = current_datetime.month

måned = f"{måned_feil_formattert:02d}"

dag_feil_formattert = current_datetime.day

dag = f"{dag_feil_formattert:02d}"

time = current_datetime.hour

minutt = current_datetime.minute


def område(valg):
   if valg == "øst":
      vispris("NO1")
   elif valg == "sør":
      vispris("NO2")
   elif valg == "midt":
        vispris("NO3")
   elif valg == "nord":
      vispris("NO4")
   elif valg == "vest":
      vispris("NO5")





def billigste_strøm_idag(område):

  url = f"https://www.hvakosterstrommen.no/api/v1/prices/{år}/{måned}-{dag}_{område}.json"
  response = requests.get(url, verify=False)
  data3 = response.json() 

  cheapest_hour = None
  for hour in data3:
      if cheapest_hour is None or hour['NOK_per_kWh'] < cheapest_hour['NOK_per_kWh']:
          cheapest_hour = hour

  start_tid = cheapest_hour['time_start'][11:16]

  return start_tid




customtkinter.set_appearance_mode("dark")

customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()

root.geometry("700x600")

root.title("Strømpris")


root.iconbitmap("icon.ico")




frametop = customtkinter.CTkFrame(master=root)
frametop.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

frame = customtkinter.CTkFrame(master=frametop, fg_color="gray15", corner_radius= 10)
frame.grid(row=2, column=1, sticky="nsew", padx=10, pady=4)

frame2 = customtkinter.CTkFrame(master=frametop, fg_color="gray15", corner_radius= 10)
frame2.grid(row=3, column=1, sticky="sew", padx=10, pady=4)


# Configure the root window grid
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

def rowconfig_frametop():
  frametop.grid_rowconfigure(0, weight=1)
  frametop.grid_rowconfigure(1, weight=1)
  frametop.grid_rowconfigure(2, weight=1)
  frametop.grid_rowconfigure(3, weight=1)

  frametop.grid_columnconfigure(0, weight=1)
  frametop.grid_columnconfigure(1, weight=1)
  frametop.grid_columnconfigure(2, weight=1)

rowconfig_frametop()

def rowconfig_frame():
  frame.grid_rowconfigure(0, weight=1)
  frame.grid_rowconfigure(1, weight=1)
  frame.grid_rowconfigure(2, weight=1)

  frame.grid_columnconfigure(0, weight=1)
  frame.grid_columnconfigure(1, weight=1)
  frame.grid_columnconfigure(2, weight=1)
  frame.grid_columnconfigure(3, weight=1)
  frame.grid_columnconfigure(4, weight=1)
  frame.grid_columnconfigure(5, weight=1)
  frame.grid_columnconfigure(6, weight=1)
  frame.grid_columnconfigure(7, weight=1)
  frame.grid_columnconfigure(8, weight=1)
  frame.grid_columnconfigure(9, weight=1)
  frame.grid_columnconfigure(10, weight=1)
  frame.grid_columnconfigure(11, weight=1)
  frame.grid_columnconfigure(12, weight=1)
  frame.grid_columnconfigure(13, weight=1)
  frame.grid_columnconfigure(14, weight=1)
  frame.grid_columnconfigure(15, weight=1)
  frame.grid_columnconfigure(16, weight=1)
  frame.grid_columnconfigure(17, weight=1)
  frame.grid_columnconfigure(18, weight=1)
  frame.grid_columnconfigure(19, weight=1)
  frame.grid_columnconfigure(20, weight=1)
  frame.grid_columnconfigure(21, weight=1)
  frame.grid_columnconfigure(22, weight=1)
  frame.grid_columnconfigure(23, weight=1)

rowconfig_frame()

def rowconfig_frame2():
  frame2.grid_rowconfigure(0, weight=1)
  frame2.grid_rowconfigure(1, weight=1)

  frame2.grid_columnconfigure(0, weight=1)
  frame2.grid_columnconfigure(1, weight=1)
  frame2.grid_columnconfigure(2, weight=1)

rowconfig_frame2()




label = customtkinter.CTkLabel(master=frametop, text=f"Strømpris {dag}.{måned}.{år}", font=("roboto", 24, "bold"))
label.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)



combobox = customtkinter.CTkComboBox(
    master=frametop,
    values=["øst", "sør", "midt", "nord", "vest"],
    command=område, state="readonly")
combobox.grid(row=1, column=1, sticky="ew", padx=10, pady=10)

combobox.set("vest")



def vispris(område):

  start_tid = billigste_strøm_idag(område)

  for widget in frame.winfo_children():
    widget.destroy()
  
  valgt_område = område
  url = f"https://www.hvakosterstrommen.no/api/v1/prices/{år}/{måned}-{dag}_{valgt_område}.json"
  response = requests.get(url, verify=False)
  data2 = response.json() 






#tegne strømprisgrafen
  for i in range(24):
    prisdata = data2[i]["NOK_per_kWh"]

    if i == time:
      farge = "white"
      txt2 = customtkinter.CTkLabel(master=frame, width = 5, height = 10, corner_radius= 2,
                                    text=f"(NÅ)", text_color="white", font=("roboto", 10, "bold"))
      txt2.grid(row=1, column=i, padx=2, pady=5, sticky="new")

      priskr = round(((data2[i]["NOK_per_kWh"])*100), 1)

      canvas_width = 10
      fixed_canvas_height = 500 
          
      rect_height = max(data2[i]["NOK_per_kWh"]*400, 10) 
      rect_height = min(rect_height, fixed_canvas_height)  

      canvas = customtkinter.CTkCanvas(master=frame, width=canvas_width, height=fixed_canvas_height, 
                                    bg=frame.cget("fg_color"), highlightthickness=0)
      canvas.grid(row=0, column=i, padx=3, pady=0, sticky="sew")
          
      canvas.create_rectangle(0, fixed_canvas_height - rect_height, 500, fixed_canvas_height, 
                                fill=farge, outline="", width=1)
          
      txt = customtkinter.CTkLabel(master=frame, bg_color="black", width = 5, height = 10,
                                      text=f"{priskr}", text_color="white", font=("roboto", 7.5, "bold"))
      txt.grid(row=0, column=i, padx=2, pady=5, sticky="sew")
      continue

    if data2[i]['time_start'][11:16] == start_tid:
      farge = "lightblue"
    elif prisdata < 0.3:
        farge = "lightgreen"
    elif prisdata < 0.6:
        farge = "yellow2"
    else:
        farge = "indian red"



    priskr = round(((data2[i]["NOK_per_kWh"])*100), 1)

    canvas_width = 10
    fixed_canvas_height = 500
    
    rect_height = max(data2[i]["NOK_per_kWh"]*400, 10)  
    rect_height = min(rect_height, fixed_canvas_height)  

    canvas = customtkinter.CTkCanvas(master=frame, width=canvas_width, height=fixed_canvas_height, 
                               bg=frame.cget("fg_color"), highlightthickness=0)
    canvas.grid(row=0, column=i, padx=3, pady=0, sticky="sew")
    
    canvas.create_rectangle(0, fixed_canvas_height - rect_height, 500, fixed_canvas_height, 
                          fill=farge, outline="", width=1)
    
    txt = customtkinter.CTkLabel(master=frame, bg_color="black", width = 5, height = 10,
                                text=f"{priskr}", text_color="white", font=("roboto", 7.5, "bold"))
    txt.grid(row=0, column=i, padx=2, pady=5, sticky="sew")


    txt2 = customtkinter.CTkLabel(master=frame, width = 5, height = 10, corner_radius= 2,
                                text=f"Kl {i:02d}", text_color="white", font=("roboto", 7.5, "bold"))
    txt2.grid(row=1, column=i, padx=2, pady=5, sticky="new")



vispris("NO5")




#screenshot
def capture_window():
    x = root.winfo_rootx()
    y = root.winfo_rooty()  
    width = root.winfo_width() 
    height = root.winfo_height()  

    screenshot = ImageGrab.grab(bbox=(x, y, x + width, y + height - 225))
    screenshot.save("strømpris.png")



#send screenshot
def send():
   capture_window()
   mailadresse = entry1.get()
   entry1.delete(0, "end")
   send_mail(mailadresse)





#mailgun api
#Sett inn din api key og link under, eller implementer en annen api

def send_mail(mailadresse):
    tittel = f"Hei! Her er strømmprisen i dag!"
    melding = f""

    return requests.post(
  		"",
  	  auth=("api", os.getenv('API_KEY', '')),
      files=[("inline", open("strømpris.png", "rb"))],
  	  data={"from": "",
			"to": f"{mailadresse}",
  			"subject": f"{tittel}",
  			"text": f"{melding}",
        "html": '<html>Strømprisen idag: <img src="cid:strømpris.png"></html>'})

  




#knapp og entry field til sending av mail
button = customtkinter.CTkButton(master=frame2, text="Send på mail", command=send, fg_color="green", font=("roboto", 12, "bold"),
                                  corner_radius=32, width=100)

button.grid(row=1, column=1, padx=10, pady=5, sticky="ns")




entry1 = customtkinter.CTkEntry(master=frame2, placeholder_text= "Skriv mailadresse", font=("roboto", 12, "bold"), width=200)
entry1.grid(row=0, column=1, sticky="ew", padx=10, pady=5)



entry1.bind("<Return>", lambda event: send())


root.mainloop()