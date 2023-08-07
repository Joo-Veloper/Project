import Link from 'next/link';
import DarkModeToggleButton from './darkmode-toggle-button';

export default function Header(){
    return(
        <>
            <header className="text-gray-600 body-font">
                <div className="container mx-auto flex flex-wrap p-5 flex-col md:flex-row items-center">
                    <Link legacyBehavior href="/">
                        <a className="flex title-font font-medium items-center text-gray-900 mb-4 md:mb-0">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" className="w-10 h-10 text-white p-2 bg-indigo-500 rounded-full" viewBox="0 0 24 24">
                                <path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"></path>
                            </svg>
                            <span className="ml-3 text-xl">SeungJoo's Portfolio</span>
                        </a>
                    </Link>
                   
                    <nav className="md:ml-auto flex flex-wrap items-center text-base justify-center">
                    

                        <Link legacyBehavior href="/">
                            <a className="mr-5 hover:text-gray-900">HOME</a>
                        </Link>

                        <Link legacyBehavior href="/projects">
                            <a className="mr-5 hover:text-gray-900">PROJECT</a>
                        </Link>

                        <a href="https://onebyeone.tistory.com/"className="mr-5 hover:text-gray-900">BLOG</a>
                       
                    </nav>
                    {/*다크모드 토글 버튼*/}
                    <DarkModeToggleButton/>
                </div>
                </header>
        </>
    );
}