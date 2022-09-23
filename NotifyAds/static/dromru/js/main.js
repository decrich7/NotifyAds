
    window.formApi = 'https://api.craftum.com/api/forms';
    const REWRITING_SCRIPTS_NAMES = ['module-map', 'module-timer', 'module-slider']
    const CORE_SCRIPTS_NAMES = [
        ...REWRITING_SCRIPTS_NAMES,
        'module-button',
        'module-form',
        'module-cart',
        'module-compare',
        'module-animation',
        'module-menu',
        'module-step-animation',
        'module-timer',
        'module-video',
        'module-zoom',
        'module-scroll-button'
    ]

    const SCRIPTS = ['module-button.js?hash=3c4ace4645c2a75dcbc4070cc2ea96f7', 'module-menu.js?hash=3c4ace4645c2a75dcbc4070cc2ea96f7']

    const actualSortedScripts = SCRIPTS.filter(
        s => CORE_SCRIPTS_NAMES.some(
            b => s.startsWith(b)
        )
    ).sort(a => REWRITING_SCRIPTS_NAMES.some(n => a.startsWith(n)) ? -1 : 1)

    const run = async (scripts) => {
        for (const script of scripts) {
            try {
                const module = await import(`./${script}`)
                await module.default(SCRIPTS)
            } catch (e) {
                console.error(e)
            }
        }
    }

    run(actualSortedScripts)

    const anchorBlock = localStorage.getItem('anchorBlock')
    if (anchorBlock) {
    const stickyHeader = document.querySelector('.cli-sticky')
    let stickyHeight = 0
    if (!!stickyHeader) stickyHeight = parseInt(getComputedStyle(stickyHeader).height)

    const blocks = Array.from(document.querySelectorAll('[data-style]'))
    const target = blocks.find(b => b.dataset.style.includes(anchorBlock))

    if (target) {
        const bodyRect = document.body.getBoundingClientRect()
        const rect = target.getBoundingClientRect()
        const offset = rect.top - bodyRect.top - stickyHeight
        document.body.scrollTo({
            top: offset,
            behavior: 'smooth'
        })
    }
    localStorage.removeItem('anchorBlock')
    }
