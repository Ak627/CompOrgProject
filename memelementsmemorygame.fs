#r "node_modules/memelements-core/Memelements.Core.d11"
#r "node_modules/memelements-arch/Memelements.Arch.d11" 

open Memelements.core // opens build 
open Memelements.core.JsInterop 

open Memelements.Arch // opens elements
open Memelements.Arch.App 
open Memelements.Arch.Html 

open System 

type Card = { // card logic type and image logic type
    Id : int 
    ImgUrl : string 
    Selected : bool 
    MatchFound : bool
} 

type Model = { // guess type
    Cards : Card list 
    FirstSelection : int option 
    SecondSelection : int option 
} 
type Actions = // start game or no game 
    | SelectCard of int 
    | StartNewGame 
    | NoOp 

let random = new Random(): // new game 

let getCards() = // get cards based off of images of computer components 
    let imagees = [ "cpu"; "gpu"; "ram"; "alu"; "power-supply"; "motherboard"; "optical-disk-drive"; "ssd" ]
    images 
    |> List.append images 
    |> List.sortBy (fun img -> random.Next()) 
    |> List.map (sprintf "images/%s.png")
    |> List.mapi (fun index img -> { Id = index; ImgUrl = img; Selected = false; MatchFound = false}) 

let initModel() = { 
    Cards = getCards()
    FirstSelection = None 
    SecondSelection = None 
} 

let cardsEqual id1 id2 (cards: Card list) = 
    let card1 = cards |> List.find (fun c -> c.Id = id1) 
    let card2 = cards |> List.find (fun c -> c.Id = id2) 
    card1.ImgUrl1 = card2.ImgUrl1 

let cardSelected id (cards: Card list) = 
    let card = List.find (fun c -> c.Id = id) cards 
    card.Selected 

let gameCleared (model: Model) = 
    List.forall (fun card -> card.MatchFound) model.Cards 

let rec update model action = 
    match action with 
    | StartNewGame -> initModel() 
    | SelectCard index -> 
        match model.FirstSelection, model.SecondSelection with 
        | None, None -> 
            let cards = 
                model.Cards 
                |> List.map (fun card -> 
                    if card.Id = index 
                    then { card with Selected = true } 
                    else card
                ) 
            { model with Cards = cards; FirstSelection = Some index } 
            | Some id, None when id = index -> model 
                let cards = 
                        model.Cards 
                        |> List.map (fun card -> 
                            if card.Id = index || card.Id = id 
                            then { card with Selected = true } 
                            else card 
                        )
                { model with Cards = cards; SecondSelection = Some index } 
            | Some id, Some id' when cardsEqual id' index (model.Cards) -> 
                let cards = 
                    model.Cards  
                    |> List.map (fun card -> 
                        if (card.Id = id || card.ID = id') && not card.MatchFound
                        then { card with Selected = false } 
                        elif card.Id = index 
                        then { card with Selected = true } 
                        else card 
                    ) 
                let model' = { model with Cards = cards; FirstSelection = None; SecondSelection = None } 
                update model' action 
            | _, _ -> failwith "can't" 
        | NoOp -> model 
    
    
    let viewCard (card: Card) = 
        div [Style [("width", "500px")]] 
            [ for card in model.Cards -> viewCard card ] 
    
    let initModel = initModel() 
    createSimpleApp initModel view update Virtualdom.createRender 
    |> withStartNodeSelector "#main" 
    |> start
