import { useTheme } from 'next-themes'
export default function DarkModeToggleButton(){
    //theme : 현재값 getter
    //settheme : 현재값 바꾸기 setter

    
    const { theme, setTheme } = useTheme()

    return(
        <>
            <button 
                className="
                    inline-flex items-center 
                    border-0 py-1 px-3 rounded text-base mt-4 md:mt-0
                    focus:outline-none
                    bg-gray-100  
                    hover:bg-gray-50
                    hover:text-orange-500
                    dark:bg-slate-600
                    dark:text-slate-400
                    dark:hover:bg-slate-700
                    dark:hover:text-yellow-300
                "
                type="button"
                onClick={() => setTheme(theme === 'dark' ? 'light' : 'dark')}
            >
                    {/*라이트모드*/}
                    <svg xmlns="http://www.w3.org/2000/svg" 
                            fill="none" viewBox="0 0 24 24" 
                            stroke-width="1.5" stroke="currentColor" 
                            className="visible dark:invisible dark:h-0 dark:w-0 h-5 w-5">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M3.75 13.5l10.5-11.25L12 10.5h8.25L9.75 21.75 12 13.5H3.75z" />
                    </svg>


                    {/*다크모드*/}
                    <svg xmlns="http://www.w3.org/2000/svg" 
                            fill="none" viewBox="0 0 24 24" 
                            stroke-width="1.5" stroke="currentColor" 
                            className="invisible dark:visible dark:h-5 dark:w-5 h-0 w-0">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M11.412 15.655L9.75 21.75l3.745-4.012M9.257 13.5H3.75l2.659-2.849m2.048-2.194L14.25 2.25 12 10.5h8.25l-4.707 5.043M8.457 8.457L3 3m5.457 5.457l7.086 7.086m0 0L21 21" />
                    </svg>





            </button>
        </>
    );

}