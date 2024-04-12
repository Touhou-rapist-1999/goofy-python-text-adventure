import time
import random
import inventory
import stats
import story_branch1
from make_choices import make_choice

def itemcall(item, healthx, luckx, repx):
    
    if(healthx!=0):
        healthy = statists.gethealth() + healthx
        statists.sethealth((healthy))
    if(luckx!=0):
        lucky = statists.getluck() + luckx
        statists.setluck((lucky))
    if(repx!=0):
        repy = statists.getrep() + repx
        statists.setrep((repy))
    invent.giveitem(item)

def damage(pain, path):
    health = statists.gethealth()
    statists.sethealth(health-pain)
    if(statists.gethealth() <= 0):
        print("Du bist gestorben.\n")
        time.sleep(1)
    elif(path=='none'):
         return
    else:
        path()

def main():
    global invent 
    invent = inventory.inv()
    global statists
    statists = stats.stats0(5, 0, 0)    

    print("\nDu befindest dich im dunklen Wald.")
    time.sleep(1)
    print("Hörst du ein merkwürdiges Geräusch. Willst du dem Geräusch folgen oder im Wald bleiben?")

    choices = ["Dem Geräusch folgen", "Im Wald bleiben"]
    choice = make_choice(choices)

    if choice == 1:
        print("\nDu folgst dem Geräusch und entdeckst eine verlassene Hütte.")
        time.sleep(1)
        print("In der Hütte findest du eine wertvolle Belohnung.")
        plastikapfel = inventory.item("Plastikapfel")
        itemcall(plastikapfel, 1, 0, 0)
        print("Du hast nun einen Plastikapfel, deine HP ist um 1 erhöht.")
        time.sleep(1)
        print("du gehst wieder aus der Hütte heraus und triffst auf eine freundliche Kreatur.")
        time.sleep(1)
        print("Aber die Kreatur ist doch nicht freundlich. -2HP.")
        damage(2, story_branch_2_2)
        
    else:   
        print("\nDu bleibst im Wald und triffst auf eine freundliche Kreatur.")
        time.sleep(1)
        print("Aber die Kreatur ist doch nicht freundlich. -2HP")
        damage(2, story_branch_2_2)
        

def story_branch_2_2():

    print("\nDu bist immernoch im dunklen Wald.")
    time.sleep(1)
    print("Möchtest du stehen bleiben oder versuchen, den Wald zu verlassen?")
    choices = ["stehen bleiben", "Den Wald verlassen"]
    choice = make_choice(choices)

    if choice == 1:
        print("\nDu bleibst im Wald und triffst mal wieder auf eine freundliche Kreatur.")
        if "Amulet" in invent.items:
                    if((statists.getluck()-random.randint(0,1))>1) or "Waldcheck" not in invent.items:
                        print("Diesmal ist sie wirklich freundlich.")
                        time.sleep(1)
                        print("Du benutzt die Chance um sie über einen Stein zu locken. Sie stolpert hinüber und stirbt.")
                        time.sleep(1)
                        print("Gratulation.")
                    else:
                        print("Sie greift dich an, bevor du etwas machen kannst und du verlierst -2HP.")
                        damage(2, 'none')
                        print("Du entkommst ihr durch massives im Kreis rennen und landest genau da wo du vorher standest.")
                        invent.removeitem("Waldcheck")
                        
        else:
            time.sleep(1)
            print("Aber die Kreatur ist immernoch nicht freundlich. (-2HP)")
            damage(2, story_branch_2_2)
    else:
        print("\nDu stolperst über einen Stein und verlierst 1HP.")
        time.sleep(1)
        damage(1, story_branch_2_2chance)
                
def story_branch_2_2chance():
    if(random.randint(0,1)==1 or "Waldcheck" in invent.items):
                print("Du entkommst dem Wald.")
                story_branch_2_2_1()
    elif "Waldcheck" not in invent.items:
                print("Du entkommst dem Wald nicht.")
                waldcheck = inventory.item("Waldcheck")
                itemcall(waldcheck, 0, 0, 0)
                story_branch_2_2()
    else:
         print("Du entkommst dem Wald.")
         story_branch_2_2_1()
                
           
        
def story_branch_2_2_1():
    
    print("\nDu kannst außerhalb vom Wald gut über die Landschaft blicken.")
    print("Am Horizont ist ein Schloss.")
    print("Gehst du zum Schloss, oder wieder in den Wald?")
    
    choices = ["Zum Schloss gehen", "Zurück zum Wald"]
    choice = make_choice(choices)

    if choice == 1:
        print("\nDu kommst dem Schloss näher.")
        if(random.randint(0,1)==1):
                print("Du wirst von Banditen angegriffen, die dir die Unterhose über den Kopf ziehen. -1HP.")
                damage(1, story_branch_2_2_1_1)
        else:
                story_branch_2_2_1_1()
    else:
        print("\nDu gehst zurück in den Wald.")
        story_branch_2_2()
    
def story_branch_2_2_1_1():
    print("\nDu erreichst das Schloss.")
    if(statists.getreputation()>=0):
        print("Ein Wächter fragt ob du eine Hexe gesehen hast.")
    
        choices = [">Ja, deine Mutter.<", ">Noch nicht.<"]
        choice = make_choice(choices)
    
        if choice == 1:
            print(">DU RÜDIGER!!!!<")
            time.sleep(1)
            print(">Das ist Amtsbeleidigung!! Ich werde dafür sorgen, dass du das bereust!!!")
            print("Aus der ferne hörst du >HANS, HOL DEN FLAMMENWERFER!<")
            print("Es ist wohl Zeit zu gehen (zum Wald zurück zu rennen). Dabei stolperst du an einem Stein. -1HP.")
            beleidiger = inventory.item("Beleidiger")
            itemcall(beleidiger, 0, 0, -5)
            damage(1, story_branch_2_2)
        else:
            print(">Haben sie Acht! Es lauert eine in dieser Gegend. Willkommen in unserem Schloss.<")
            story_branch_2_2_1_2()
    else:
         print("Der Wächter erkennt dich wieder. Bevor du was sagen kannst kommt der Strahl eines Flammenwerfers dir entgegen. -10HP.")
         damage(20, main)

        
def story_branch_2_2_1_2():    
        print("\nDie Königin persönlich empfängt dich.")
        amulet = inventory.item("Amulet")
        if "Amulet" in invent.items:
            print(">Warum bist du wieder hier? Du sollst doch das Monster bekämpfen?<")
            print("Sie schickt dich zurück in den Wald.")
            story_branch_2_2()
        else:
            print(">Du siehst mir aus wie ein tapferer Held. Ich habe etwas für dich.<")
            print("Sie gibt dir ein Amulet.") 
            itemcall(amulet, 5, 2, 0)
            time.sleep(1)
            print(">Töte hiermit die Kreatur des Forstes.<")
            print("Somit gehst du zurück in den Wald.")
            story_branch_2_2()