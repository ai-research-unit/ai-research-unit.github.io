# __The Feynman Rules of the $\mathrm{SU}(4)$ Model: The Vertices of the Fifteen and the Sixteen__

## Introduction

**The group is one group, the coupling is one coupling, and the rules follow from three lines.** The fifteen are the generators of $\mathfrak{su}(4)$; the sixteen are two quartets and two antiquartets of Weyl fields; one covariant derivative couples them. **Everything below is transcription plus one rotation and three rescalings**, and the rescaling is the only place a convention can go wrong.

**Four things carry the weight.**

- **The vertex list.** The fifteen fields against the sixteen fermions, read entry by entry off the printed arrays. **There are $64$ nonzero entries on the quartet half and $64$ on the conjugate half, so $128$ in all**, and the split is $48+8+8$ per half: twelve planes, two colour diagonals, and the corner, each counted with its two copies.
- **The normalisation.** The printed arrays are not orthonormal in the trace. **Thirteen have $\operatorname{tr}(G^{\dagger}G)=2$, the rotated colour diagonal has $6$ and the corner has $12$**, and one pair is not even orthogonal. A canonical kinetic term therefore forces a family-dependent rescaling, and that rescaling is the whole of §*The Normalisation, Before Any Rule*.
- **The two-index rule.** Every fermion–gauge vertex is $X\otimes\mathbb 1_{2}$: an array on the quartet times the identity on the copy index. **A gauge rotation cannot tell the two copies apart**, and that one bracket decides the shape of the whole table.
- **One coupling, and no ratio.** $g_4$ stays symbolic. **The model has no second coupling, so it has no coupling ratio to fix and no matching problem to inherit.**

**What the article does not do.** It does not derive a fermion action from the algebra: the fermion kinetic term uses the quartet's connection acting on the quartet carrier, and the claim that it does is imported, not proved. **The matrices are exact; the dynamical statement that a fermion propagates with them is the imported half**, and it is marked as such in every section where it is used.

## Conventions

**The coordinates, stated once.** The derivative is $\partial/\partial R_{\imath}$, the metric is $\delta_{\imath\jmath}=(1,1,1,1)$, and every index is low: a contraction is a plain sum, $\sum_{\imath}X_{\imath}Y_{\imath}$, with no sign hidden in the metric.

**The quartet index runs over $(t,x,y,z)$**, and the three colour lines are $x,y,z$ under the names $r,g,b$ used in [the fermion classification](classification-of-the-fermions-in-the-su4-model-sixteen-weyl-fields-closed-under-c-and-cp.html). **The two namings are one convention**, and this article writes $x,y,z$ when it reads an array and $r,g,b$ when it names a particle.

**The generators are anti-Hermitian and traceless, and the arrays are read by columns.** The printed matrices are the $G_{a}$ of [the construction article](construction-of-the-axf-matrices-of-the-fifteen-generators.html); a matrix unit $E_{\imath\jmath}$ has a $1$ in row $\imath$, column $\jmath$. **The generators the rules are written in are Hermitian**, $t_{a}=iG_{a}/\sqrt{2n_{a}}$ with $n_{a}=\operatorname{tr}(G_{a}^{\dagger}G_{a})$ equal to $2$ for the thirteen planes and diagonals and $12$ for the corner, the colour diagonal $c_{3}=d_{2}-d_{3}$ being taken at its own norm $6$, so that $t_{a}^{\dagger}=t_{a}$ and $\operatorname{tr}(t_{a}t_{b})=\tfrac12\delta_{ab}$; [The Lagrangian and the Primordial Force](the-lagrangian-and-the-primordial-force.html) fixes that passage once. **The printed arrays carry the anti-Hermitian convention and the $i$ that makes them Hermitian is one step, the trace-norm rescaling the other, and a vertex read off a printed array without both is wrong by the product.**

**The bookkeeping of the sixteen.** The four Weyl fields of the quartet are $\xi_{i}$ with $i\in\{t,r,g,b\}$, the four of the conjugate quartet are $\bar\xi^{i}$, and each comes in two copies labelled by an index the model does not gauge. **Sixteen fields, thirty-two states, and the copy index is a degeneracy and not a charge.**

## The Lagrangian the Rules Come From

**One covariant derivative covers all fifteen fields.**

$$
D_{\imath}=\partial_{\imath}-ig_4\sum_{a=1}^{15}A_{a,\imath}t_{a} .
$$

**One sum, fifteen fields, one coupling.** The index $a$ is a name and not a frame slot. **The three sums and three couplings of the left–right frame are gone, and nothing is missing**: the factors they multiplied are not in this group.

**Four pieces, and the vertex budget is in the third column.**

$$
\mathcal{L}=-\tfrac14\sum_{a,\imath,\jmath}F_{a,\imath\jmath}F_{a,\imath\jmath}
+\sum_{f}\bar\xi_{f}\Bigl(-i\sum_{\imath}\gamma_{\imath}D_{\imath}\Bigr)\xi_{f}
+\operatorname{tr}\bigl(D_{\imath}Ξ\bigr)^{\dagger}\bigl(D_{\imath}Ξ\bigr)-V(Ξ)
+\mathcal{L}_{\mathrm{gf}}+\mathcal{L}_{\mathrm{gh}}+\mathcal{L}_{\mathrm{Yuk}} .
$$

| piece | fields | vertices it produces |
| --- | --- | --- |
| $-\tfrac14\sum FF$ | the fifteen | three-gauge and four-gauge |
| fermion kinetic | the sixteen | fermion–gauge, one matrix per generator |
| scalar kinetic | $Ξ$, sixteen real components | gauge–scalar, two- and three-point |
| $V(Ξ)$ | $Ξ$ | scalar self-couplings, four-point and lower |
| $\mathcal{L}_{\mathrm{gf}}$, $\mathcal{L}_{\mathrm{gh}}$ | fifteen ghosts | ghost–gauge |
| $\mathcal{L}_{\mathrm{Yuk}}$ | fermions and $Ξ$ | Yukawa, one matrix in the family index |

**The gauge block is where the corpus is strongest and the fermion block is where it is thinnest**, and the rules inherit the asymmetry. **The three-gauge vertices are exact**, computed from the bracket table; **the fermion–gauge vertex is exact as a matrix and imported as a dynamical statement.**

**The scalar is the Hermitian $4\times4$, and its size is the algebra's.** $\mathbf{15}\oplus\mathbf1$ is a traceless part of fifteen real entries plus a real trace: $15+1=16$ real components, and $\dim\mathrm{SU}(4)=15$ is where the fifteen comes from. The condensate is $\langleΞ\rangle=v\operatorname{diag}(-3,1,1,1)$, and $15-9=6$ of its components are eaten by the sextet. **The matrix index is not a choice**: $\bar\xiΞ\xi$ is a singlet only for $Ξ\in\bar{\mathbf4}\otimes\mathbf4=\mathbf{15}\oplus\mathbf1$, while $\mathbf4\otimes\mathbf4=\mathbf6\oplus\mathbf{10}$ has no $\bar{\mathbf4}$. The count is [the classification](classification-of-the-bosons-in-the-su4-model-one-grid-fifteen-generators-nine-massless-six-heavy.html)'s, and [The Scalar Content](the-scalar-content-one-matrix-and-ten-survivors.html) is the census behind it.

## The Normalisation, Before Any Rule

**The printed arrays are anti-Hermitian, and their trace norms come in two values.**

| family | arrays | $\operatorname{tr}(G^{\dagger}G)$ | norm |
| --- | --- | --- | --- |
| the twelve planes $A_{\imath\jmath}$, $iS_{\imath\jmath}$ | $12$ | $2$ | $\sqrt2$ |
| the two colour diagonals $d_{2}$, $d_{3}$ | $2$ | $2$ | $\sqrt2$ |
| the corner $iD$ | $1$ | $12$ | $2\sqrt3$ |

**One pair is not orthogonal, and it is the only one.** The Gram matrix of the fifteen has exactly one nonzero off-diagonal entry, $\langle d_{2},d_{3}\rangle=-1$; every other pair is orthogonal. **So the printed fifteen are a basis and not an orthonormal frame**, and the Gram is positive definite with eigenvalues $1$, twelve copies of $2$, $3$ and $12$.

**The repair is one rotation and then three rescalings.**

$$
c_{2}=d_{2}+d_{3},\qquad c_{3}=d_{2}-d_{3},\qquad
\langle c_{2},c_{2}\rangle=2,\quad \langle c_{3},c_{3}\rangle=6,\quad \langle c_{2},c_{3}\rangle=0 .
$$

**After the rotation the fifteen are orthogonal, with norm $2$ for thirteen of them, $6$ for $c_{3}$ and $12$ for the corner.** A canonical kinetic term $\operatorname{tr}(t_{a}t_{b})=\tfrac12\delta_{ab}$ then fixes

$$
t_{a}=\frac{iG_{a}}{2}\ \ (13\ \text{arrays}),\qquad
t_{c_{3}}=\frac{i(d_{2}-d_{3})}{\sqrt{12}}\ \ (c_{3}),\qquad
t_{15}=\frac{iG_{15}}{\sqrt{24}}\ \ (\text{the corner}),
$$

so the corner's coupling is weaker than a plane's by $2/\sqrt{24}=1/\sqrt6=0.4082$, and $c_{3}$'s by $1/\sqrt3$. **Those numbers are consequences of the trace, not of the group**: the corner is the one diagonal removed from the fundamental and is longer than a plane by $\sqrt6$, and $c_{3}$ by $\sqrt3$.

**Why this matters for every rule below.** A vertex read off the printed array is off by this factor, and a cross section read off a vertex is off by its square. **Relative to the printed arrays the coefficient is $1/2$ for the planes, $1/\sqrt{12}$ for $c_{3}$ and $1/\sqrt{24}$ for the corner**; relative to one another the three families stand as $1:\tfrac{1}{\sqrt3}:\tfrac{1}{\sqrt6}$ for the plane, $c_{3}$ and the corner. **The table below states the corner's ratio once, so that no other table has to repeat it.**

## Propagators

**Nine massless and six massive, and no mixing anywhere.** The mass matrix of the fifteen is $m^{2}(X)=v^{2}\operatorname{tr}\bigl(X^{\dagger}[D,[D,X]]\bigr)$ with $D=\operatorname{diag}(-3,1,1,1)$, and its two eigenvalues are $0$ and $32v^{2}$, with multiplicities nine and six.

| field | count | $m^{2}$ | propagator |
| --- | --- | --- | --- |
| the eight gluons, $\mathfrak{su}(3)$ | $8$ | $0$ | $i\delta_{ab}(-g_{\imath\jmath}+k_{\imath}k_{\jmath}/k^{2})/(k^{2}+i\epsilon)$ |
| $B'$, the corner direction | $1$ | $0$ | the same form, no index |
| the sextet $X^{\alpha}$, $\bar X^{\alpha}$ | $6$ | $32v^{2}$ | $i\delta_{ab}(-g_{\imath\jmath}+k_{\imath}k_{\jmath}/m^{2})/(k^{2}-m^{2}+i\epsilon)$ |
| the fifteen ghosts | $15$ | $0$ on nine, $\xi\,32v^{2}$ on six | $i\delta_{ab}/(k^{2}-\xi m^{2}+i\epsilon)$ |
| the sixteen fermions | $16$ | $0$ | $i\bar\sigma^{\imath}k_{\imath}/k^{2}$ per Weyl field |
| $Ξ$'s ten surviving components | $10$ | $2\lambda_{1}v^{2}$ on the radial mode at $\lambda_{2}=0$ | $i/(k^{2}-m^{2}+i\epsilon)$ |

**There is no mixing matrix to invert.** A four-factor propagator section would have to rotate four neutral fields and produce a photon and a $Z$; **here the mass matrix is already diagonal in the basis of planes, and the rotation is the identity.** The mixing below $M_C$ is downstream, and it is not in this Lagrangian.

**Two of the nine are massless for two different reasons, and the difference is not cosmetic.** The eight gluons are massless because their generators commute with $D$, which is an exact statement about the stabiliser. **The corner is massless because it is $D$ itself**: $[D,[D,iD]]=0$ for any diagonal, so the direction of the condensate cannot be lifted by the condensate. **A ninth massless field that is massless for a different reason is the one place where a counting argument can go wrong.**

**The sextet's mass is the same number for all six.** $32v^{2}$ comes from $2(1-(-3))^{2}=(4)^{2}\cdot2$: a plane that carries one $t$ index costs $2(1+3)^{2}$ and a plane that carries two colour indices costs zero. **The value is verified per plane** in [the detail article](the-15-axf-matrices-of-the-bosons-in-detail.html).

## The Vertex List

**The vertex is $ig_{4}\gamma_{\imath}(t_{a})_{ij}$ for a fermion in the quartet, and $ig_{4}\gamma_{\imath}(-t_{a}^{T})^{ij}$ for one in the conjugate.** The matrices $(t_{a})$ are the printed arrays up to the rescaling of the previous section. **The list is short because the group is one group**: fifteen fields, sixteen fermions, one table.

**The count, and how it is built.**

| family | quartet entries per array | arrays | with the copy index |
| --- | --- | --- | --- |
| the twelve planes | $2$ | $12$ | $48$ |
| the two colour diagonals | $2$ | $2$ | $8$ |
| the corner $iD$ | $4$ | $1$ | $8$ |
| **the quartet half** | | | $\mathbf{64}$ |
| **the conjugate half, $-t_{a}^{T}$** | the same | the same | $\mathbf{64}$ |
| **total nonzero fermion–gauge entries** | | | $\mathbf{128}$ |

**The two-index rule, and it is one line.** Every vertex is $X\otimes\mathbb 1_{2}$ with $X$ an array on the quartet. **A gauge rotation acts on the quartet index only, so it cannot change the copy label**, and the sixteen fermions therefore couple in two identical copies. **Nothing in the model distinguishes them**, and no rule below can.

**What each family does to a fermion line.**

| family | the array | the lines it joins | the charge it carries |
| --- | --- | --- | --- |
| planes $A_{ab}$, $a,b$ both colour | $2$ entries, colour–colour | quark to quark | gluon, $B-L=0$ |
| planes $A_{ta}$, $iS_{ta}$ | $2$ entries, $t$ to colour | lepton to quark | $B-L=\mp\tfrac43$, $Q=\mp\tfrac23$ |
| colour diagonals $d_{2}$, $d_{3}$ | $2$ entries, colour–colour | quark to quark | gluon, $B-L=0$ |
| the corner $iD$ | $4$ entries, diagonal | lepton to lepton, quark to quark | $B-L=0$ |

**The leptoquark vertex conserves $B-L$ exactly, and the arithmetic is one line.** The lepton line carries $B-L=-1$, the colour line $+\tfrac13$, and the boson $-\tfrac43$: $-1=\tfrac13-\tfrac43$. **The charge is read off the commutator** $[iD,E_{ta}]=-4iE_{ta}$, so the boson's $D$-eigenvalue is $-4$ and its $B-L$ is $-4/3$ under $B-L=\tfrac13D$.

**The corner couples to every line and to none of them twice.** $iD$ is diagonal with entries $-3,1,1,1$, so it gives one vertex on each of the four lines and none off the diagonal. **That is why it is the direction the condensate can sit on**: a diagonal generator does not move a fermion between cells.

## The Three-Gauge Vertices

**Every three-gauge vertex is a structure constant, and the structure constants are the bracket table.**

$$
\Gamma_{abc}^{\imath\jmath\ell}(k_{1},k_{2},k_{3})=g_{4}f_{abc}\bigl[(k_{1}-k_{2})^{\ell}g^{\imath\jmath}+(k_{2}-k_{3})^{\imath}g^{\jmath\ell}+(k_{3}-k_{1})^{\jmath}g^{\ell\imath}\bigr].
$$

**The count is exact, and the number of triples depends on the basis the brackets are read in.** Of the $\binom{15}{2}=105$ pairs, **$80$ have a nonzero bracket in either basis**. The number of distinct index triples is **$31$ in the printed basis and $29$ once $d_{2},d_{3}$ are rotated to $c_{2},c_{3}$**, because the rotation mixes the two colour diagonals and lets two triples that were separate stand on one. **The rules are written in the orthonormal basis, so the vertex runs over $29$ triples**; the six brackets tabulated below are printed-basis values, and that is why $31$ is the number to expect from them.

**Six brackets, computed and printed.**

| bracket | value |
| --- | --- |
| $[A_{tx},A_{ty}]$ | $-A_{xy}$ |
| $[A_{tx},iS_{tx}]$ | $2i(E_{tt}-E_{xx})$ |
| $[d_{2},d_{3}]$ | $0$ |
| $[iD,d_{2}]$ | $0$ |
| $[iD,A_{ta}]$ | $-4iS_{ta}$ |
| $[iD,iS_{ta}]$ | $-4iA_{ta}$ |

**The last two are the grading, and they are the reason the sextet is a sextet.** $D$ does not commute with a plane carrying a $t$ index; it maps the real plane to the imaginary one and back, with the same factor $-4$. **So the six mixed planes form three two-dimensional blocks of definite $D$-charge**, and the whole sextet is heavy for one reason.

**The four-gauge vertex is the contact term $g_{4}^{2}f_{abc}f_{cde}$ and it is dense.** Every generator that appears in two triples contributes, and the count is not worth tabulating: **what matters is that it is fixed by the same $29$ triples and introduces no new number.**

## Ghosts, Gauge Fixing and the Scalar Vertices

**One fixing parameter, because there is one group.** The Feynman–'t Hooft choice $\mathcal{L}_{\mathrm{gf}}=-\tfrac{1}{2\xi}\sum_{a}(\partial_{\imath}A_{a,\imath})^{2}$ gives fifteen ghosts, one per generator, with masses $0$ on the nine and $\xi\,32v^{2}$ on the six. **A second fixing parameter would be a symptom of a second factor**, and the model has none.

**The ghost–gauge vertex is $g_{4}f_{abc}k_{\imath}$**, with the momentum on the outgoing ghost. **The count of nonzero vertices is again $29$ triples**, and the vanishing ones vanish for the same reason.

**The scalar vertices come from the kinetic term and the potential, and the model fixes neither coupling.** The gauge–scalar two-point vertex is the mass matrix restricted to the six eaten directions; the three-point vertex is $-2ig_{4}$ times $\operatorname{tr}(\partial_{\imath}Ξ[t_{a},Ξ])$, **with the $2$ from the commutator's two orderings and the $i$ from the covariant derivative** — a vertex quoted as $g_4$ times the commutator is off by that factor. **The potential $V(Ξ)$ is written with two quadratics and four quartics, and the model predicts none of them**: $v$ is a ratio of coefficients, and the radial mass is the second derivative of $V$ along the condensate (*The Primordial Potential*). **The two quadratics that carry the trace shift no vector mass**, because the identity commutes with all fifteen generators.

**The eaten six and the surviving ten.** Six components of $Ξ$ become the longitudinal polarisations of the sextet; **the remaining ten are physical here**, one radial mode and nine orthogonal to the vacuum. **An eaten component has no propagator of its own**, and a table that lists sixteen scalar propagators is listing six that do not exist.

## What the Rules Do Not Contain

**No $W$, no $Z$, no photon.** The model has one unbroken $\mathrm{U}(1)$ and eight gluons; **the electroweak connections arrive at $M_C$, and so do their vertices.** A rule set that printed a $Wff$ vertex would be printing a vertex of a different Lagrangian.

**No fermion masses and no mixing angles.** The sixteen Weyl fields are massless until the condensate gives them a Yukawa matrix, and that matrix is [the Yukawa article](the-yukawa-sector-of-the-su4-model-one-matrix-and-its-diagonalisation.html). **No CKM matrix and no PMNS matrix**: both need two factors and a second condensate.

**No value for $g_{4}$ and no loop correction.** The coupling is symbolic throughout. **The rules are tree level**: a one-loop statement would need a regulator, a renormalisation scheme, and a counterterm Lagrangian, and none of the three is in the corpus.

**No prediction from the algebra.** Every vertex here is a transcription. **The model's content is the group and the content, not the rules**, and the rules are the place where a transcription error would be invisible.

## The Checks

| check | statement | result |
| --- | --- | --- |
| generator count | $\dim\mathfrak{su}(4)=15$ | $15$ |
| nonzero array entries | twelve planes $2$ each, two diagonals $2$ each, corner $4$ | $32$ |
| fermion–gauge entries per half | $32\times2$ copies | $64$ |
| fermion–gauge entries in all | $64+64$ | $128$ |
| trace norms | thirteen at $2$, $c_{3}$ at $6$, the corner at $12$ | $2$, $6$, $12$ |
| off-diagonal Gram | one pair, $\langle d_{2},d_{3}\rangle=-1$ | $-1$ |
| orthogonal basis | $c_{2}=d_{2}+d_{3}$, $c_{3}=d_{2}-d_{3}$ | norms $2$, $6$ |
| corner rescaling | $2/\sqrt{24}=1/\sqrt6$ | $0.408$ |
| spectrum | $15=9+6$ | nine at $0$, six at $32v^{2}$ |
| stabiliser | $[D,t_{a}]=0$ on the nine | $9$ |
| nonzero brackets | of $105$ pairs | $80$ |
| nonzero three-gauge triples | antisymmetric $f_{abc}$, orthonormal basis | $29$ ($31$ printed) |
| ghost count | one per generator | $15$ |
| eaten scalars | $\dim$ coset $=15-9$ | $6$ |

## Summary

**One covariant derivative, one coupling, fifteen fields, sixteen fermions.** The fermion–gauge vertex is $X\otimes\mathbb 1_{2}$ and has $128$ nonzero entries; the three-gauge vertex is $f_{abc}$ with $29$ nonzero triples; the spectrum is nine massless and six at $32v^{2}$; and the scalar is a $4\times4$ Hermitian matrix with sixteen real components, six of them eaten by the sextet. **No copy index acts on the scalar**: the copy index is a fermion label, so it eats nothing.

**The normalisation is the only place a convention can go wrong**, and it is fixed by two lengths: the corner is $\sqrt6$ longer than a plane and $c_{3}$ is $\sqrt3$ longer, so their couplings are $0.4082$ and $0.5774$ of a plane's after a canonical kinetic term.

**What the rules do not contain is the low-energy list**, and it is short because the group is one group: no $W$, no $Z$, no photon, no mixing matrix, no coupling ratio, and no fermion mass without the condensate.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $G_{a}$, $a=1\dots15$ | the printed anti-Hermitian arrays |
| $t_{a}$ | the generator made Hermitian and rescaled, $t_{a}=iG_{a}/\sqrt{2\operatorname{tr}(G_{a}^{\dagger}G_{a})}$, so $\operatorname{tr}(t_{a}t_{b})=\tfrac12\delta_{ab}$ |
| $A_{a,\imath}$ | the fifteen connections |
| $\xi_{i}$, $\bar\xi^{i}$ | the quartet and conjugate-quartet Weyl fields, two copies each |
| $Ξ$ | the Hermitian $4\times4$ scalar, sixteen real components |
| $D=\operatorname{diag}(-3,1,1,1)$ | the condensate direction |
| $d_{2}$, $d_{3}$, $c_{2}$, $c_{3}$ | the two colour diagonals and their orthogonal combinations |
| $f_{abc}$ | the structure constants of the fifteen |
| $\xi$ | the fixing parameter, not the fermion |

## Further Reading

- [The $\mathrm{SU}(4)$ Model: Four Colours, Fifteen Generators, One Declaration](the-su4-model-four-colours-fifteen-generators-one-declaration.html). The group, the content, and the declaration this article transcribes.
- [The Commutation Table of the Fifteen Generators](the-commutation-table-of-the-fifteen-generators-225-entries-105-independent-80-nonzero-and-five-rules.html). The $80$ nonzero brackets and the five rules that generate them.
- [The Fifteen AXF Matrices of the Bosons in Detail](the-15-axf-matrices-of-the-bosons-in-detail.html). Every array, its entries, and its mass.
- [The Fermion–Gauge Vertex in the Quartet Basis](the-fermion-gauge-vertex-in-the-quartet-basis-the-fifteen-read-on-the-sixteen.html). The $128$ entries, one generator at a time.
- [The Yukawa Sector of the $\mathrm{SU}(4)$ Model](the-yukawa-sector-of-the-su4-model-one-matrix-and-its-diagonalisation.html). Where the fermion masses come from.
- [Three Diagrams of the $\mathrm{SU}(4)$ Model](three-diagrams-of-the-su4-model-the-kaon-the-proton-chain-and-a-gluon-exchange.html). Three rules from this list, drawn.
- [The Classification of the Fermions](classification-of-the-fermions-in-the-su4-model-sixteen-weyl-fields-closed-under-c-and-cp.html). The sixteen, the $B-L$ column, and the two copies.
