from web_scraper import __version__
from web_scraper.scraper import get_citations_needed_count,get_citations_needed_report



def test_version():
    assert __version__ == '0.1.0'


def test_count():
    URL = 'https://en.wikipedia.org/wiki/Gun' 
    assert get_citations_needed_count(URL) == None

def test_citations():
    URL = 'https://en.wikipedia.org/wiki/Gun' 
    actuall = ['In contemporary military and naval parlance the term gun has a very specific meaning and refers solely to any large-calibre, direct-fire, high-velocity, flat-trajectory artillery piece employing an explosive-filled hollowed metal shell or solid bolt as its primary projectile.[citation needed] This later usage contrasts with large-calibre, high-angle, low-velocity, indirect-fire weapons such as howitzers, mortars, and grenade launchers which invariantly employ explosive-filled shells. In other military use, the term "gun" refers primarily to direct fire weapons that capitalize on their muzzle velocity for penetration or range. In modern parlance, these weapons are breech-loaded and built primarily for long range fire with a low or almost flat ballistic arc. A variation is the howitzer or gun-howitzer designed to offer the ability to fire both low or high-angle ballistic arcs. In this use, example guns include naval guns. A less strict application of the word is to identify one artillery weapon system or non-machine gun projectile armament on aircraft.[citation needed]\n', 'A related military use of the word is in describing gun-type fission weapon. In this instance, the "gun" is part of a nuclear weapon and contains an explosively propelled sub-critical slug of fissile material within a barrel to be fired into a second sub-critical mass in order to initiate the fission reaction. Potentially confused with this usage are small nuclear devices capable of being fired by artillery or recoilless rifle.[citation needed]\n', 'Shotguns are normally civilian weapons used primarily for hunting. These weapons are typically smooth bored and fire a shell containing small lead or steel balls. Variations use rifled barrels or fire other projectiles including solid lead slugs, a Taser XREP projectile capable of stunning a target, or other payloads. In military versions, these weapons are often used to burst door hinges or locks in addition to antipersonnel uses.[citation needed]\n']
    expected = get_citations_needed_report(URL)
    assert actuall==expected