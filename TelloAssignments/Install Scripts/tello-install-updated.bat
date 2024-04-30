necho=1/*>nul&@cls
@echo off

echo [94m *******       **     ****     **** ********** ********   ******  **      **
echo /**////**     ****   /**/**   **/**/////**/// /**/////   **////**/**     /**
echo /**   /**    **//**  /**//** ** /**    /**    /**       **    // /**     /**
echo /*******    **  //** /** //***  /**    /**    /******* /**       /**********
echo /**///**   **********/**  //*   /**    /**    /**////  /**       /**//////**
echo /**  //** /**//////**/**   /    /**    /**    /**      //**    **/**     /**
echo /**   //**/**     /**/**        /**    /**    /******** //****** /**     /**
echo //     // //      // //         //     //     ////////   //////  //      // [0m
echo.
echo.
echo [31m ********** ******** **       **         *******           ******    *******   ****     ** ******** **   ********
echo /////**/// /**///// /**      /**        **/////**         **////**  **/////** /**/**   /**/**///// /**  **//////
echo     /**    /**      /**      /**       **     //**       **    //  **     //**/**//**  /**/**      /** **      // 
echo     /**    /******* /**      /**      /**      /**      /**       /**      /**/** //** /**/******* /**/**         
echo     /**    /**////  /**      /**      /**      /**      /**       /**      /**/**  //**/**/**////  /**/**    *****
echo     /**    /**      /**      /**      //**     **       //**    **//**     ** /**   //****/**      /**//**  ////** 
echo     /**    /********/********/******** //*******         //******  //*******  /**    //***/**      /** //******** 
echo     //     //////// //////// ////////   ///////           //////    ///////   //      /// //       //   ////////[0m
echo.

timeout /t 2 /nobreak >nul
echo This program is for use with Windows computers, and Tello *standard* drones. (Not EDUs)
echo.
echo There are 3 steps this program follows.
echo 1. Download Python. Python is downloaded from: https://www.python.org/ftp/python/3.12.3/python-3.12.3-amd64.exe
echo 2. Install Python. This program allows the python installer ask for administrator privileges on your device and work autonomously with the default install settings.
echo 3. Use Pip (Python package manager) to install the required packages, and if pip is missing, it will install that as well.
pause


echo [92m
echo ------------------------------------------------------
echo              Downloading python 3.12.3
echo ------------------------------------------------------
curl -L -O https://www.python.org/ftp/python/3.12.3/python-3.12.3-amd64.exe

echo This will ask for administrator privileges for the install. Press "Yes"

start /WAIT python-3.12.3-amd64.exe /passive InstallAllUsers=1 PrependPath=1 Include_test=0

echo ------------------------------------------------------
echo                   Downloading pip
echo ------------------------------------------------------
:downpip
 py -m pip install --upgrade pip
:downpipend
echo ------------------------------------------------------
echo                   Downloading opencv-python
echo ------------------------------------------------------
:downpip
 py -m pip install opencv-python 
:downpipend
echo ------------------------------------------------------
echo                   Downloading numpy
echo ------------------------------------------------------
:downpip
py -m pip install numpy
:downpipend
echo ------------------------------------------------------
echo                   Downloading tello-python
echo ------------------------------------------------------
:downpip
 py -m pip install djitellopy
:downpipend
echo ------------------------------------------------------
echo                   Downloading decoder
echo ------------------------------------------------------
 :downpip
 py -m pip install sqlalchemy
 :downpipend
echo [0m

echo [92m
echo  ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** *****          
echo  ///// ///// ///// ///// ///// ///// ///// ///// ///// ///// ///// ///// ///// ///// ///// ///// ///// ///// ///// ///// ///// /////
echo.
echo.
echo.
echo                                Zp            kO                                
echo                              OOm              pOO                              
echo                           pOOO                  OOOw                           
echo                        QZOOOd                    oOOOZw                        
echo                       mZOOO                        OOZZm                       
echo                     Y^^mZO                            OZZ`Y                     
echo                    Ywdh(OO            mZ            Y0vhdwC                    
echo                   Zmwdm    cY    ^^""^^^^^^^^^^^^^^"^^    YC    mbwmZ                   
echo                 wmmmp   C      Jw;^^`^^`````^^^^;OY      C   pmmmm                 
echo                Zmmwd     dJ     p;^^^^^^^^^^^^^^^^^^^^;mC    Jh     hwmmZ                
echo              OZmh          dY  J0;^^````^^^^^^^^^^;YO  Yw          hmZZ              
echo            pZZ               Q0p0;^^^^^^^^`^^^^^^^^^^IzbOC               ZZp            
echo                                YC;^^^^^^^^^^^^^^^^^^^^IcX                                
echo                                 ZI^^^^^^^^^^^^^^^^^^^^IZ                                 
echo                                 OI^^^^^^^^^^^^^^^^^^^^IO                                 
echo                                 OI^^^^^^^^^^^^^^^^^^^^IO                                 
echo                                 O;^^^^^^^^^^^^^^^^^^^^IO                                 
echo                                Xm;^^^^^^^^^^^^^^^^^^^^;ZX                                
echo            dOO               0Q QI^^^^^^^^".rc^^^^IO 0Q               OOb            
echo              OOOh           Q   YI^^^^^^^^^^^^^^^^^^^^IC   Cw          dOOO              
echo                OOOZo     CC     XI:"mmmmmm::IX     Cd     hZOOO                
echo                 wOOOZ   J      Jw QXXXXXXXXQ ZY      J   ZOOOZ                 
echo                   ZOZw0    XJJ                   JY    OwZOO                   
echo                    Ywwa/Op                          d0XammC                    
echo                     Q'dmZ                            Zmp.C                     
echo                       dwmmZ                        Ommwd                       
echo                        kpmmmp                    hmmmp#                        
echo                           bmmZ                  ZZmd                           
echo                              ZZw              pZm                              
echo                                ZZ            mZ
echo.
echo.                                
echo Successfully Downloaded and Installed All Software.
echo Developed By: Andrew Whalen 
echo Updated By: Liev Dorfman
echo [0m
pause
exit
