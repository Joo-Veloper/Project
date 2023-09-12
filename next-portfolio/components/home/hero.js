import Animation from "./animation";
import Link from 'next/link';

export default function Hero() {
    return(
        
        <>
            <div className="lg:flex-grow md:w-1/2 lg:pr-24 md:pr-16 flex flex-col md:items-start md:text-left mb-16 md:mb-0 items-center text-center">
                <h1 className="title-font sm:text-4xl text-3xl mb-4 font-medium text-gray-900">
                    안녕하세요 탐구하고자 하는 의지로 새로운 Framework와 Server에 도전하는
                <br className="hidden lg:inline-block"/>
                    개발자 박승주 입니다
                </h1>
                <p className="mb-8 leading-relaxed">
                    첫번째 Node.js 와 Python을 이용해 백 엔드 개발에 관심이 있는 개발자
                    두번째 새로운 것을 도전하는 것을 좋아하고 무엇을 하든 포기하지 않고 부딪혀보는 개발자
                    세번째 개인 프로젝트를 통해 이론과 실무감각을 쌓아가는 개발자
                    네번째 이익 보다는 목표에 도달하기 위해 노력하는 개발자
                </p>
                
                <div className="flex justify-center">
                    <Link legacyBehavior href ="projects">
                        <a className="btn-project,inline-flex text-white bg-indigo-500 border-0 py-2 px-6 focus:outline-none hover:bg-indigo-600 rounded text-lg">
                            Going to see a project
                        </a>
                    </Link>
                </div>
            </div>
            <div className="lg:max-w-lg lg:w-full md:w-1/2 w-5/6">
                <Animation/> 
            </div>
        </>
    );
}