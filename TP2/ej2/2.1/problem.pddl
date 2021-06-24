(define (problem encomiendas-nacionales) 
(:domain avionAA)
(:objects 
    Airbus380-315
    UHA
    MIS
    MEN
    STF
    ROS
    SALTA
    EZEIZA
    CARGA1
    CARGA2
    CARGA3
    CARGA4
    CARGA5
    CARGA6
    CARGA7
    CARGA8
    CARGA9
    CARGA10
    CARGA11
    CARGA12
    CARGA13
    CARGA14
    CARGA15
    CARGA16
   
)

(:init
    
    (avion Airbus380-315)    
    (aeropuerto UHA)
    (aeropuerto MIS)
    (aeropuerto MEN)
    (aeropuerto STF)
    (aeropuerto ROS)
    (aeropuerto SALTA)
    (aeropuerto EZEIZA)
    (carga CARGA1)
    (carga CARGA2)
    (carga CARGA3)
    (carga CARGA4)
    (carga CARGA5)
    (carga CARGA6)
    (carga CARGA7)
    (carga CARGA8)
    (carga CARGA9)
    (carga CARGA10)
    (carga CARGA11)
    (carga CARGA12)
    (carga CARGA13)
    (carga CARGA14)
    (carga CARGA15)
    (carga CARGA16)
    
       
    (en Airbus380-315 EZEIZA)   
    (en CARGA1 MEN)
    (en CARGA2 MEN)
    (en CARGA3 UHA)
    (en CARGA4 SALTA)
    (en CARGA5 STF)
    (en CARGA6 MIS)
    (en CARGA7 EZEIZA)
    (en CARGA8 MEN)
    (en CARGA9 ROS)
    (en CARGA10 ROS)
    (en CARGA11 STF)
    (en CARGA12 SALTA)
    (en CARGA13 MIS)
    (en CARGA14 MIS)
    (en CARGA15 UHA)
    (en CARGA16 UHA)
       
)

(:goal 
    (and
        (en CARGA1 ROS)
        (en CARGA2 ROS)
        (en CARGA3 ROS)
        (en CARGA4 ROS)
        (en CARGA5 EZEIZA)
        (en CARGA6 EZEIZA)      
        (en CARGA7 EZEIZA)
        (en CARGA8 SALTA)
        (en CARGA9 UHA)
        (en CARGA10 UHA)
        (en CARGA11 ROS)
        (en CARGA12 MIS)
        (en CARGA13 MEN)
        (en CARGA14 MEN)
        (en CARGA15 MIS)
        (en CARGA16 SALTA)