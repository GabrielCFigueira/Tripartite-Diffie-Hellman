#!/usr/bin/python3

import math
from pynitefields import *
from util import *

if __name__ == "__main__":
    prime = 482677778157700435350444108563600470389539607291135742953085077414483299007817968457323051999107203153032937333023591271636050696817523671646492380723773419011
    poly = [1,0,1]
    p = Point(FieldElement(prime, 2, [44190300200219570605979955052143576952357255515115686851170191818316842095486907625480884395317616863401927551006066189692708095924815897927498508535823262371,0], irre_poly=poly),FieldElement(prime,2,[26090947680860922395540330613428690525406329616428470738073031338841260885477380307130420220342204765301865163480203757570223664606235381540801075563801118751,0], irre_poly=poly))
    q = Point(FieldElement(prime, 2, [417418390151798179157327683814659014460849518350508436411447781417311430237331232958577456865429161040089806217226455983348248260335272068783343983410685645620, 0], irre_poly=poly), FieldElement(prime,2,[0,85984079438328066829535503806402848425113755688042614534609435398882015068450504353865472815063531531657210019063972911218641810155964304683033635085838106425], irre_poly=poly))
    s = Point(FieldElement(prime, 2, [0,0], irre_poly=poly), FieldElement(prime, 2, [0,0], irre_poly=poly))
    ec = EllipticCurve(FieldElement(prime, 2, [1,0], irre_poly=poly), FieldElement(prime, 2, [0,0], irre_poly=poly))
    order = 593917583375891588584754753148372137203682206097

    print(WeilPairing(p,q,s,order,ec))
    print(TatePairing(addPoint(p, negatePoint(q), ec),addPoint(p, q, ec),order,ec, prime, 2))
