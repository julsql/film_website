from django.db import connections

"Id, Emplacement, Titre, Réalisateur, Langue, Date, Durée, Colorisation, Voix, Disque, Type, Acteurs, Liens"


def exec_req_all(req):
    with connections['default'].cursor() as cur:
        cur.execute(req)
        return cur.fetchall()


def exec_req_one(req):
    with connections['default'].cursor() as cur:
        cur.execute(req)
        return cur.fetchone()


def alea():
    req = "SELECT Id, Titre, Réalisateur, Langue, Date, Durée, Colorisation, Voix, Disque, Type, Acteurs FROM Films " \
          "ORDER BY RAND() LIMIT 1;"
    result = exec_req_one(req)

    try:
        infos = {'Id': result[0], 'Titre': result[1], 'Réalisateur': result[2], 'Langue': result[3], 'Date': result[4],
                 'Durée': result[5], 'Colorisation': result[6], 'Voix': result[7], 'Disque': result[8],
                 'Type': result[9], 'Acteurs': result[10].split(',')}
    except AttributeError:
        infos = {'Id': result[0], 'Titre': result[1], 'Réalisateur': result[2], 'Langue': result[3], 'Date': result[4],
                 'Durée': result[5], 'Colorisation': result[6], 'Voix': result[7], 'Disque': result[8],
                 'Type': result[9]}
    return infos


def recherche_film(id=None, titre=None, real=None, lang=None, date=None, duree=None, color=None, voix=None, disque=None,
                   type=None, acteurs=None):
    if id is None and titre is None and real is None and lang is None and date is None and duree is None and color is None and voix is None and disque is None and type is None and acteurs is None:
        req = "SELECT Id, Titre, Réalisateur FROM Films"
    else:
        req = "SELECT Id, Titre, Réalisateur FROM Films WHERE"
        if id != "":
            req += f" Id={id} AND"
        if titre != "":
            req += f" Titre LIKE '%{titre}%' AND"
        if real != "":
            req += f" Réalisateur LIKE '%{real}%' AND"
        if lang != "":
            req += f" Langue LIKE '%{lang}%' AND"
        if date != "":
            req += f" Date={date} AND"
        if duree != "":
            req += f" Durée<{duree} AND"
        if color != "":
            req += f" Colorisation LIKE '%{color}%' AND"
        if voix != "":
            req += f" Voix LIKE '%{voix}%' AND"
        if disque != "":
            req += f" Disque LIKE '%{disque}%' AND"
        if type != "":
            req += f" Type LIKE '%{type}%' AND"
        if acteurs != "":
            for acteur in acteurs.split(" "):
                req += f" Acteurs LIKE '%{acteur}%' AND"

        req = req[:-4] + ";"

    print(req)
    result_req = exec_req_all(req)
    infos = []

    for result in result_req:
        infos.append({'Id': result[0], 'Titre': result[1], 'Réalisateur': result[2]})
    return infos


"Id, Emplacement, Titre, Réalisateur, Langue, Date, Durée, Colorisation, Voix, Disque, Type, Acteurs, Liens"


def page(id):
    req = "SELECT Id, Emplacement, Titre, Langue, Date, Durée, Colorisation, Voix, Disque, Type, " \
          "Liens, Acteurs, Réalisateur FROM Films WHERE Id={};".format(id)
    result = exec_req_one(req)
    print(result)
    infos = {}
    titles = ["Id", "Emplacement", "Titre", "Langue", "Date", "Durée", "Colorisation", "Voix", "Disque",
              "Type", "Liens"]
    for i in range(len(titles)):
        try:
            infos[titles[i]] = int(result[i])
        except:
            infos[titles[i]] = result[i]

    acteurs_result = result[11]
    if acteurs_result is not None:
        acteurs_result = acteurs_result.split(",")
        acteurs = []
        for acteur in acteurs_result:
            lien = get_link(acteur)
            acteurs.append({'nom': acteur, 'link': lien})
        infos["Acteurs"] = acteurs

    realisateur = result[12]
    if realisateur is not None:
        lien = get_link(realisateur)
        infos["Réalisateur"] = {'nom': realisateur, 'link': lien}
    return infos


def get_link(artiste):
    req = f"SELECT Lien FROM Artistes WHERE Nom LIKE '%{artiste}%'"
    return exec_req_one(req)[0]


def stat():
    nombre = exec_req_one("SELECT count(*) as nombre FROM Films;")[0]
    duree = int(exec_req_one("SELECT sum(Durée) as somme FROM Films;")[0])
    artistes = exec_req_one("SELECT count(*) as somme FROM artistes;")[0]
    infos = {'nombre': nombre, 'duree': duree, 'artistes': artistes}
    return infos
