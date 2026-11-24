# __The Feynman Rules of the Four Colours Left–Right Model: The Vertices of the Twenty-One and the Sixteen__

## Introduction

The standing of this article, stated first because everything below depends on it. **The Lagrangian is the corpus's, the group is the corpus's, and the rules are transcription.** Nothing here is a framework result: the twenty-one generators, the sixteen fermions and one covariant derivative are the content of [The Four Colours Left–Right Model](the-four-colours-left-right-model.html), and the matrix algebra is the content of [The Commutation Table of the Twenty-One Generators](the-commutation-table-of-the-twenty-one-generators-441-entries-164-nonzero-and-six-rules.html). **What the article adds is the dictionary those two articles do not print**: which of the twenty-one couples to which pair of the sixteen, with what group factor, at what normalisation, and with which sign.

**Four things, and they are the four sections that carry weight.**

- **The vertex list.** The twenty-one gauge fields against the sixteen fermions, read entry by entry off the printed arrays. Every boson–fermion vertex matrix is named below by the two fermion lines it joins, and on the eight states of one chirality there are $88$ nonzero entries in total.
- **The normalisation.** The printed arrays are not orthonormal in the trace: $\operatorname{tr}(G^{\dagger}G)=2$ for the planes and the colour diagonals, $12$ for the corner, and $1$ for the weak arrays. **A canonical kinetic term therefore forces a family-dependent rescaling, and that rescaling is what makes "one coupling" a statement about the normalised basis and not about the printed one.** No article in the corpus says this before the rules are written, and it is the reason a rule copied in the printed basis carries the wrong relative weight.
- **The two-index rule.** Every vertex is $X\otimes\mathbb{1}_2$ on the quartet times the doublet slot. **A colour rotation cannot change a doublet slot and a weak rotation cannot change a colour line**, and that one bracket decides the shape of every vertex in the table.
- **One coupling per block, and no equality.** $g_4$, $g_L$ and $g_R$ stay symbolic throughout. The frame fixes what each multiplies and fixes no value.

**What the article does not do, and cannot.** It does not derive a fermion action from the algebra. The spin-$\tfrac12$ sector has twelve electroweak articles and six strong ones and **no action in either**, because a fermion kinetic term needs the sector's connection acting on the fermion's carrier and neither a chiral $\mathrm{SU}(2)_L$ nor a colour $\mathrm{SU}(3)_c$ is in $\mathbb{B}$; that is the ledger of [the internal note on the spin of the Lagrangian articles](../articles_internal/internal-note-on-the-spin-of-the-lagrangian-articles.html). **The fermion Lagrangian used here is transcribed, and every rule that contains a fermion is a rule of the transcribed Lagrangian.** The article stays at tree level: the corpus's scattering content is tree level, and loops would need the renormalisation that [the S-matrix article](the-s-matrix-in-biquaternionic-form.html) records as open.

## Conventions

**The corpus's coordinates, stated once.** The derivative is $\partial/\partial R_{\imath}$ and the metric is the identity $(1,1,1,1)$ on the biquaternion coordinates, so every index is low and every contraction is a plain sum, $\sum_{\imath}X_{\imath}Y_{\imath}=X\cdot Y$, with no sign hidden in the summation. **A display here and the same display in a text with a mostly-minus metric differ by the sign of every summed pair**, which is why the sums are written out. The measure is $\mathrm{d}^{4}r$.

**The indices.** The quartet index runs over $(t,x,y,z)$, and the fermion tables of [the classification](classification-of-the-fermions-in-the-four-colours-left-right-model-one-generation-sixteen-fields-thirty-two-states-closed-under-cp-and-not-under-c.html) name the same three directions $r,g,b$; **the two namings are one convention and this article uses $(t,x,y,z)$ inside every matrix and $(r,g,b)$ inside every table about quarks.** The doublet index runs over two values per chirality, written $\uparrow$ and $\downarrow$ in the classification and $u,d$ here. The family index runs over three and never mixes with either. **The Lorentz index is $\imath$ and $\jmath$**, and it is low everywhere because the metric is the identity.

**The matrices, and the one place where a convention must be declared.** The printed arrays are anti-hermitian: $A_{jk}=E_{jk}-E_{kj}$ is real antisymmetric, $iS_{jk}=i(E_{jk}+E_{kj})$ is imaginary symmetric, and $iD$, $d_2$, $d_3$ are imaginary diagonal. **A Feynman rule needs hermitian generators and a canonical kinetic term**, so the rule uses

$$
t_{a}=i\,G_{a}\big/\sqrt{2\operatorname{tr}(G_{a}^{\dagger}G_{a})},
\qquad
\operatorname{tr}(t_{a}t_{b})=\tfrac12\delta_{ab},
$$

**with $G_{a}$ the printed array and the rescaling the subject of the section after next.** Every vertex then carries exactly one factor of $t_{a}$ per external gauge leg, and the translation from an algebra statement to a rule is: **one $i$ and one rescaling per gauge leg, and nothing else.** Charges, $B-L$ and selection rules are unaffected, because they are read from the algebra and not from the normalisation.

**Momenta.** Incoming at every vertex, $p_1+p_2+p_3=0$ at a three-point vertex. The gauge parameter is $\zeta$, with $\zeta=1$ the Feynman gauge. The couplings $g_4$, $g_L$, $g_R$ are symbolic and positive.

## The Lagrangian the Rules Come From

**One covariant derivative covers all twenty-one fields, and the whole gauge content is that one line.**

$$
D_{\imath}=\partial_{\imath}-ig_4\sum_{a=1}^{15}A_{a,\imath}T_{a}
-ig_L\sum_{i=1}^{3}W_{L,i,\imath}\tau_{i}
-ig_R\sum_{i=1}^{3}W_{R,i,\imath}\tau_{i} .
$$

**Every index is low, the sums are written, and no index is summed by convention.** The labels $a$ and $i$ count generators and are not frame slots.

**Four pieces, and the vertex budget is in the third column.**

$$
\mathcal{L}=-\tfrac14\sum_{a,\imath,\jmath}F_{a,\imath\jmath}F_{a,\imath\jmath}
+\sum_{f}\bar\xi_{f}\Bigl(-i\sum_{\imath}\gamma_{\imath}D_{\imath}\Bigr)\xi_{f}
+\bigl(D_{\imath}\Phi\bigr)^{\dagger}\bigl(D_{\imath}\Phi\bigr)-V(\Phi)
+\mathcal{L}_{\mathrm{gf}}+\mathcal{L}_{\mathrm{gh}}+\mathcal{L}_{\mathrm{Yuk}} .
$$

| piece | fields | vertices it produces |
| --- | --- | --- |
| $-\tfrac14\sum FF$ | the twenty-one | three-gauge and four-gauge |
| fermion kinetic | the sixteen | fermion–gauge, one per generator per chiral block |
| scalar kinetic | the bidoublet and the $\mathbf{15}$ | gauge–scalar, two- and three-point |
| $V(\Phi)$ | the scalars | scalar self-couplings, four-point and lower |
| $\mathcal{L}_{\mathrm{gf}}$, $\mathcal{L}_{\mathrm{gh}}$ | ghosts | ghost–gauge |
| $\mathcal{L}_{\mathrm{Yuk}}$ | fermions and scalars | Yukawa, a $3\times3$ in the family index |

**The gauge block is where the corpus is strongest and the fermion block is where it is thinnest**, and the rules inherit that asymmetry. The three-gauge and four-gauge vertices are computed from the commutation table and are exact. **The fermion–gauge vertex is exact as a matrix and transcribed as a dynamical statement**: the matrix $(t_{a})_{ij}$ is a printed array, and the claim that the fermion propagates with that coupling is the imported half.

## The Normalisation, Before Any Rule

**Three trace norms, and they are different.**

$$
\operatorname{tr}(G^{\dagger}G)=
\begin{cases}
2, & A_{jk},\ iS_{jk},\ d_{2},\ d_{3},\\
12, & iD,\\
1, & T^{L}_{a},\ T^{R}_{a} .
\end{cases}
$$

**The consequence is immediate and it is not cosmetic.** A canonical gauge kinetic term is $-\tfrac14\sum_{a}(\partial_{\imath}A_{a,\jmath}-\partial_{\jmath}A_{a,\imath})^{2}$, and the trace form of $\operatorname{tr}(F_{\imath\jmath}F_{\imath\jmath})$ in the printed basis is not diagonal with one coefficient. **With $A_{\imath}=A^{a}_{\imath}G_{a}$ and $\operatorname{tr}(G_{a}G_{b})=T_{a}\delta_{ab}$ the kinetic term is $\tfrac12T_{a}(\partial A^{a})^{2}$, and canonical normalisation needs $A^{a}\to A^{a}/\sqrt{2T_{a}}$.**

**The basis is not orthogonal either, and the trace-norm table reports the norms and omits the one off-diagonal.** Evaluating the whole $15\times15$ Gram matrix $\langle G_{a},G_{b}\rangle=\operatorname{tr}(G_{a}^{\dagger}G_{b})$ leaves exactly one nonzero off-diagonal entry:

$$
\langle d_{2},d_{3}\rangle=\operatorname{tr}\bigl(d_{2}^{\dagger}d_{3}\bigr)=-1,
\qquad
\langle G_{a},G_{b}\rangle=0\ \text{for every other pair}.
$$

**The planes are mutually orthogonal, the real and imaginary planes of the same pair are orthogonal, the corner is orthogonal to all fourteen others, and the two colour diagonals overlap.** In the two-dimensional colour Cartan the Gram matrix is $\begin{pmatrix}2&-1\\-1&2\end{pmatrix}$, with eigenvalues $1$ and $3$, so the two orthogonal combinations are

$$
d_{2}+d_{3}=i\operatorname{diag}(0,1,0,-1)\ \text{of norm}^{2}\ 2,
\qquad
d_{2}-d_{3}=i\operatorname{diag}(0,1,-2,1)\ \text{of norm}^{2}\ 6 .
$$

**So canonical normalisation takes one rotation in the colour Cartan and then one rescaling per direction, and the two steps do not commute with each other.** That single rotation is the only place in the whole normalisation where two printed arrays have to be mixed before a rule can be written.

**One check closes the section.** With the rotation done and every array rescaled, the fifteen orthonormal generators satisfy $\sum_{a=1}^{15}t_{a}^{2}=-\tfrac{15}{8}\mathbb{1}$, which is $(N^{2}-1)/2N$ at $N=4$. **Without the rotation the same sum is not a multiple of the identity**: it gives $\operatorname{diag}(-1.875,-1.792,-2.042,-1.792)$ on $(t,x,y,z)$, and the failure sits entirely in the colour block because $d_{2}$ and $d_{3}$ both vanish on $e_{t}$. **A reader who checks the lepton line alone will see the right number and conclude wrongly that no rotation is needed.**

**The rescaling, stated per family.**

$$
\text{planes: } \tfrac12,
\qquad
\text{corner: } \tfrac{1}{\sqrt{24}},
\qquad
\text{colour Cartan: one rotation, then } \tfrac12\ \text{and}\ \tfrac{1}{\sqrt{12}},
\qquad
\text{weak arrays: } \tfrac{1}{\sqrt2}.
$$

**What that does to a coupling, in one ratio.** A single $g_4$ multiplying unrescaled arrays is not a single coupling: the effective strength of the corner is $1/\sqrt{24}$ of the printed one and that of a weak array is $1/\sqrt2$, so the corner is weaker than a weak array by $\sqrt{2/24}=1/\sqrt{12}=0.2887$. **A reader who evaluates a vertex in the printed basis and compares it with another family's gets a factor of $\sqrt{12}$ that is a normalisation and not physics.**

**Where the normalisation does not matter at all.** Charges, $B-L$ eigenvalues, masslessness, the six-and-nine split of the adjoint mass matrix, and every selection rule are basis-independent statements about the algebra. **The normalisation enters exactly one place: the relative weight of a vertex against another vertex**, which is the place where a Feynman rule is not an algebra statement. **And it enters the masses**, since a mass computed as $\operatorname{tr}([X,\Phi_0]^{\dagger}[Y,\Phi_0])$ is quoted in the printed basis and carries $T_{a}$.

## Propagators, After the Mixing

**The twenty-one lines, and the mixing is not optional**: three of them are not mass eigenstates.

| line | count | mass$^{2}$ | note |
| --- | --- | --- | --- |
| gluons $A_{a}$, $a$ in the $\mathfrak{su}(3)$ corner | $8$ | $0$ | exact, colour is a stabiliser |
| photon | $1$ | $0$ | the null direction $W^{3}_{L}+W^{3}_{R}+\sqrt{2/3}\,B'$ |
| $W^{\pm}_{L}$ | $2$ | $\tfrac14 g_L^{2}v^{2}$ | holds for any couplings |
| $W^{\pm}_{R}$ | $2$ | $\tfrac14 g_R^{2}v_R^{2}$ | holds for any couplings |
| $Z$ | $1$ | $0.4\,g^{2}v^{2}$ | the coefficient moves with $g_4/g_R$ |
| $Z_R$ | $1$ | $\tfrac58 g^{2}v_R^{2}$ at equal couplings | moves with $g_4/g_R$ |
| leptoquarks $\bar X^{\alpha}$, $X^{\alpha}$ | $6$ | $\tfrac12 g_4^{2}v_R^{2}$ each | the only massive coloured states |

**Nine massless and twelve massive, and the two zeros have two different reasons**: the colour eight are fixed by a stabiliser and the photon is an eigenvector of the neutral block. That ledger is [the mass matrix article](the-mass-matrix-of-the-twenty-one-gauge-bosons-four-blocks-one-mixing-and-the-nine-zeros.html)'s, and it is quoted here because a propagator needs a mass and the neutral propagator needs a mixing.

**The six leptoquark masses are quoted twice in the corpus, in two normalisations.** The classification article gives $\tfrac12g_4^{2}v_R^{2}$ per leptoquark; [the adjoint mass matrix article](the-adjoint-mass-matrix-of-the-fifteen-one-number-per-plane.html) gives $32v^{2}$ per plane with $g_4$ absorbed into its own $v$ and $\Phi_0=vD$. **They are one computation in two bases, and this article quotes the first, because a Feynman rule needs the coupling restored.** The conversion is not re-derived here, and a reader who mixes the two will get a factor of the trace norm.

**The propagators.**

| line | factor |
| --- | --- |
| gauge boson $a$, $\imath\jmath$, mass $M$ | $\dfrac{-i\delta_{ab}}{k^{2}-M^{2}+i\epsilon}\left[\delta_{\imath\jmath}-(1-\zeta)\dfrac{k_{\imath}k_{\jmath}}{k^{2}-\zeta M^{2}}\right]$ |
| fermion $ij$, mass $m$ | $\dfrac{i\bigl(m-\sum_{\imath}\gamma_{\imath}k_{\imath}\bigr)_{ij}}{k^{2}-m^{2}+i\epsilon}$ |
| ghost $ab$ | $\dfrac{i\delta_{ab}}{k^{2}-\zeta M^{2}+i\epsilon}$ |
| scalar $IJ$, mass $M$ | $\dfrac{i\delta_{IJ}}{k^{2}-M^{2}+i\epsilon}$ |

**For the neutral block the propagator is not diagonal in the parents.** The photon and the $Z$ are combinations of $W^{3}_{L}$, $W^{3}_{R}$ and $B'$, so a vertex written on the parents is off-diagonal in the mass basis and the rotation of [The Photon as the Unbroken Mixture](the-photon-as-the-unbroken-mixture.html) sits between the two. **Every rule below is written in the parent basis**, which is the basis of the twenty-one arrays, and the rotation is applied once at the end of a computation and not once per vertex.

## The Vertex List

**Every vertex of the model, its count, and where its factor comes from.**

| vertex | count | factor | source |
| --- | --- | --- | --- |
| fermion–gauge | $88$ nonzero entries per chirality | $-ig\,\gamma_{\imath}(t_{a})_{ij}$ | fermion kinetic |
| three-gauge | $164$ nonzero brackets | $g f_{abc}$ times the momenta | $-\tfrac14\sum FF$ |
| four-gauge | pairs of generators | $-ig^{2}$ times the group combination | $-\tfrac14\sum FF$ |
| ghost–gauge | $164$, the same $f_{abc}$ | $-g f_{abc}p_{\imath}$ | $\mathcal{L}_{\mathrm{gh}}$ |
| gauge–scalar | counted, not printed | $g^{2}$ and $g\,(p+p')$ | $|D\Phi|^{2}$ |
| scalar self | counted, not printed | from $V$ | $V(\Phi)$ |
| Yukawa | $3\times3$ per channel | not written in the corpus | $\mathcal{L}_{\mathrm{Yuk}}$ |

**The count in the first row is the one worth computing, and it is smaller than a first guess.** The vertex matrix of a gauge field is its own $4\times4$ array, and a printed array is sparse: a plane has two nonzero entries, not a full row, the corner has four, and each colour diagonal has two. **Doubling for the doublet slot and summing the twenty-one,**
$$
\underbrace{48}_{\text{twelve planes}\times2\times2}+\underbrace{16}_{\text{corner }8\, +\, \text{two diagonals }4+4}+\underbrace{24}_{\text{three weak arrays}\times8}=88,
$$
**so one chirality has eighty-eight nonzero fermion–gauge entries and the model has $176$ counting both blocks.** Each joins one quartet line to one quartet line, or one doublet slot to one doublet slot, and never both. **Eighty-eight numbers per chirality, and the printed arrays already contain all of them.**

**The three-gauge count is the commutation table's.** Of the $441$ pairs exactly $164$ fail to commute, and each nonzero bracket $[G_{a},G_{b}]=f_{abc}G_{c}$ is a three-point vertex with legs $a$, $b$, $c$ and factor $g f_{abc}$. **The article does not list $164$ vertices; it lists what the six rules say they are**, because the six rules are the compact form of the table and they were verified entry by entry in the commutation article.

**What is not in the table is a number.** No vertex carries a value, because no coupling has a value, because the frame does not fix one. **The rules are a shape and a factor; the numbers belong to the coupling article and to the data.**

## The Fermion–Gauge Vertex

**One line, and every fermion vertex is that line.**

$$
\Gamma^{a}_{\imath}=-ig_{4}\,\gamma_{\imath}\,\bigl(t_{a}\otimes\mathbb{1}_{2}\bigr),
\qquad
\bigl[\Gamma^{a}_{\imath},\ \mathbb{1}_{4}\otimes\tau_{i}\bigr]=0 .
$$

**The bracket is the whole of the two-index rule.** A generator of $\mathrm{SU}(4)$ acts on the quartet and is the identity on the doublet; a generator of either $\mathrm{SU}(2)$ acts on the doublet and is the identity on the quartet. **So the vertex never mixes the two indices, and a vertex that did would not be a gauge vertex of this model.**

**On the $\bar{\mathbf{4}}$ the generator is the transpose with a sign.**

$$
t_{a}\ \text{on}\ (\mathbf{4},\mathbf{2},\mathbf{1}):\ t_{a},
\qquad
t_{a}\ \text{on}\ (\bar{\mathbf{4}},\mathbf{1},\mathbf{2}):\ -t_{a}^{\mathsf{T}} .
$$

**The minus is the conjugate of the anti-hermitian generator**, and it is the reason the same gauge field couples with opposite sign to a quark and to an antiquark. **Which chirality sits in which block is the model's declaration**: the left doublet in the $\mathbf{4}$ and the right doublet in the $\bar{\mathbf{4}}$, so $W_{L}$ couples to the left block and $W_{R}$ to the right.

**The four classes of the fifteen, read on the lepton line.** With the quartet ordered $(e_{t},e_{x},e_{y},e_{z})$ and the action read by columns:

| class | count | what it does to $e_{t}$ |
| --- | --- | --- |
| the colour planes and the colour diagonals through the triple | $8$ | annihilates it |
| the corner $iD$ | $1$ | multiplies it by $-3i$ |
| the six mixed planes $A_{ta}$, $iS_{ta}$ | $6$ | sends it into the colour triple |

**Eight, one, six, and the sum is fifteen.** That classification is [the lepton-flavour article](lepton-flavour-in-the-four-colours-model-nothing-turns-the-lepton.html)'s and it is computed there; it is quoted here because it is the selection rule of the fermion–gauge vertex. **No generator of the fifteen returns a direction inside the lepton line except a multiple of $e_{t}$**, so no gauge vertex turns a lepton into a lepton, and lepton flavour has no gauge channel.

**Worked, a gluon vertex.** With $A_{xy}$ the red–green plane and $t_{xy}$ its normalised generator,

$$
\Gamma_{xy,\imath}=-ig_{4}\gamma_{\imath}\bigl(t_{xy}\otimes\mathbb{1}_{2}\bigr),
\qquad
u^{r}\to u^{g},\quad d^{r}\to d^{g},\quad Q(u^{r})=Q(u^{g})=+\tfrac23 ,
$$

**and the doublet slot is carried through unchanged in both rows.** The two entries have the same coefficient, which is the statement that a gluon is colour-blind to the doublet index. **A vertex with different coefficients in the two rows would be a colour rotation that knew the weak index, and the algebra has no such entry.**

**Worked, a leptoquark vertex.** With $A_{tx}$ the red plane through the lepton line,

$$
\Gamma_{tx,\imath}=-ig_{4}\gamma_{\imath}\bigl(t_{tx}\otimes\mathbb{1}_{2}\bigr),
\qquad
u^{r}\to\nu_{L},\quad d^{r}\to e_{L},
$$

$$
Q(u^{r})=+\tfrac23\to Q(\nu_{L})=0,
\qquad
Q(d^{r})=-\tfrac13\to Q(e_{L})=-1,
\qquad
\Delta Q=-\tfrac23\ \text{in both}.
$$

**The same matrix, the same charge transfer, two different final particles**, because the array moved the line and the slot stayed. **The balance in both rows is the check that the two-index reading is the right one**, and it is the fermion half of the $B-L$ statement of [the leptoquark article](the-leptoquarks-of-the-four-colours-left-right-model-six-states-one-bound-and-why-proton-decay-does-not-bite.html): the boson carries $B-L=\pm\tfrac43$ and every vertex conserves $B-L$ exactly.

**Worked, the corner.** With $iD$ and its normalised generator $t_{D}$,

$$
\Gamma_{D,\imath}=-ig_{4}\gamma_{\imath}\bigl(t_{D}\otimes\mathbb{1}_{2}\bigr),
\qquad
e_{t}\to-3i\,e_{t},
\qquad
e_{x}\to+i\,e_{x},
$$

**which is $B-L$ and not electric charge**: the phase is $-3i$ on the lepton line and $+i$ on each colour line, uniform in the doublet slot. **A vertex that assigned the same quantum number to $u^{r}$ and $d^{r}$ is exactly this one**, and that is why the electric charge is not a vertex of the twenty-one.

**Worked, a weak vertex.** With $\tau_{3}$ on the doublet,

$$
\Gamma^{L}_{3,\imath}=-ig_{L}\gamma_{\imath}\bigl(\mathbb{1}_{4}\otimes\tau_{3}\bigr),
\qquad
u^{a}\to+\tfrac12\,u^{a},\qquad d^{a}\to-\tfrac12\,d^{a},
$$

**the same on every colour line.** The array cannot tell red from blue, and it does not try. **Its ladder partner $\tau_{1}\pm i\tau_{2}$ is the only vertex in the model that changes a doublet slot**, and it is a $2\times2$ object, not one of the twenty-one.

## The Three-Gauge Vertices

**The rule has the shape the non-abelian kinetic term forces, and the corpus's coefficients are the six rules.**

$$
\Gamma_{abc,\imath\jmath\rho}(p_{1},p_{2},p_{3})=g f_{abc}\Bigl[(p_{1}-p_{2})_{\rho}\delta_{\imath\jmath}+(p_{2}-p_{3})_{\imath}\delta_{\jmath\rho}+(p_{3}-p_{1})_{\jmath}\delta_{\rho\imath}\Bigr],
$$

**with $f_{abc}$ real because the corpus's generators are anti-hermitian and its bracket carries no $i$.** For hermitian generators $t_{a}=iG_{a}$ the same numbers appear and the identity $[t_{a},t_{b}]=if_{abc}t_{c}$ holds with the same $f$.

**Six brackets, computed, and they are the ones a reader is most likely to need.**

| bracket | value |
| --- | --- |
| $[A_{tx},A_{xy}]$ | $+A_{ty}$ |
| $[A_{tx},A_{ty}]$ | $-A_{xy}$ |
| $[A_{tx},A_{tz}]$ | $-A_{xz}$ |
| $[A_{xy},A_{yz}]$ | $+A_{xz}$ |
| $[A_{tx},iS_{xy}]$ | $+iS_{ty}$ |
| $[A_{xy},iS_{yz}]$ | $+iS_{xz}$ |

**Two of those deserve a sentence.** $[A_{tx},A_{ty}]=-A_{xy}$ says that **two leptoquark planes produce a colour plane with a minus sign**, so the mixed band closes on the colour band and not the other way round. And $[A_{tx},iS_{tx}]$ is the one bracket of the twelve planes that is not a plane:

$$
[A_{tx},iS_{tx}]=-\tfrac23\,iD-\tfrac43\,d_{2}-\tfrac23\,d_{3},
$$

**which is why the three diagonals are a consequence of the planes and not an independent block.** Both statements were checked numerically and both are in the commutation table's Parts I and II.

**The four-gauge vertex.**

$$
\Gamma_{abcd,\imath\jmath\rho\sigma}=-ig^{2}\Bigl[f_{abe}f_{cde}\bigl(\delta_{\imath\rho}\delta_{\jmath\sigma}-\delta_{\imath\sigma}\delta_{\jmath\rho}\bigr)+\text{two permutations}\Bigr],
$$

**with no derivation here**, since the term is the square of the commutator and the algebra of that square is [the QCD article](the-lagrangian-and-quantum-chromodynamics-the-triplet-the-octet-and-the-feynman-rules.html)'s. **What differs is the number of indices that can be nonzero**: $f$ is dense on the fifteen, with $164$ nonzero entries of $441$, and the printed arrays carry no small structure, so the four-gauge vertex of this model is a dense object with no simplification. **That is a cost of the group and not of the notation.**

**The sign convention, stated once.** With $D_{\imath}=\partial_{\imath}-ig_{4}A_{a,\imath}T_{a}$ the three-gauge vertex carries $+g$. **A text with the opposite sign in $D_{\imath}$ carries $-g$; the odd vertices flip and the even ones do not**, and that asymmetry is the derivative count: the cubic term carries one derivative and the quartic none, so in momentum space the $i$ from the derivative cancels the $i$ of a cubic vertex and the quartic keeps it.

## Ghosts, Gauge Fixing and the Scalar Vertices

**The ghost sector is the $\mathrm{SU}(4)$ one and it is imported unchanged.** With an $R_{\xi}$ gauge the ghost has mass $\xi M^{2}$ in the gauge-boson mass eigenbasis, the ghost–gauge vertex is $-g f_{abc}p_{\imath}$, and the Goldstone equivalence theorem holds at high energy. **The one thing this model adds to that is the number of brothers**: the twenty-one gauge fields eat twelve Goldstones, and the corpus counts twenty-four real scalar components of which twelve are eaten and twelve survive. **A ghost calculation here is a ghost calculation of a rank-five group with a product structure, and its arithmetic is heavier than its content.**

**The gauge–scalar vertices are counted and not written.** Two-point vertices are the mass matrix; three-point vertices are the cubic couplings of the potential, one per generator pair; four-point vertices are the quartic. **The corpus writes the scalar potential and the scalar spectrum and does not write the cubic couplings**, and [the scalar sector article](the-scalar-sector-of-the-four-colours-left-right-model-twenty-four-real-components-twelve-eaten-twelve-surviving.html) is where that ledger lives. **A rule for a gauge–scalar vertex would need those couplings, so this article stops at the count and says so rather than printing a general formula that the corpus cannot yet instantiate.**

**The Yukawa vertices are a $3\times3$ and are not a gauge rule at all.** They are in [the Yukawa sector article](the-yukawa-sector-of-the-four-colours-left-right-model-fermion-mass-matrices-and-their-diagonalisation.html), they carry the family index, and no frame fixes them. **A reader who wants a fermion mass from this article will not find one, and the reason is structural: a mass needs a $3\times3$ the algebra does not supply.**

## What the Rules Do Not Contain

**They do not contain a coupling value.** No $g_4$, no $g_L$, no $g_R$, no $\sin\theta_{W}$ from the frame, and no equality among the three. **A vertex is a shape and a symbol; the symbol is the coupling article's.**

**They do not contain a loop.** Every rule above is tree level. **The corpus's scattering content is tree level and its renormalisation is in a separate family**, so a one-loop amplitude from these rules would need a counterterm this article does not supply.

**They do not contain a derivation of the fermion Lagrangian.** The fermion–gauge vertex is exact as a matrix $(t_{a})_{ij}$ and imported as dynamics. **Case by case: the matrix entries are the corpus's, the claim that a fermion propagates with them is the transcription**, and the ledger of [the spin note](../articles_internal/internal-note-on-the-spin-of-the-lagrangian-articles.html) is the authority for which half is which.

**They do not contain a fermion mass, a mixing angle or a lifetime.** Those need the Yukawa matrices, the rotation of the neutral block, and a hadronic matrix element, and each of the three is in its own article.

## The Checks

| check | computation | result |
| --- | --- | --- |
| the trace norms | $\operatorname{tr}(G^{\dagger}G)$ for the three families | $2$, $12$, $1$ |
| the corner's norm | $\operatorname{tr}(D^{2})=9+1+1+1$ | $12$ |
| the weak norm | $\tfrac14\bigl(\operatorname{tr}A_{ta}^{2}+\operatorname{tr}A_{bc}^{2}\bigr)$ | $1$ |
| the bracket identity | $[A_{tx},A_{xy}]$ | $+A_{ty}$ |
| the two leptoquark planes | $[A_{tx},A_{ty}]$ | $-A_{xy}$ |
| the plane with its partner | $[A_{tx},iS_{tx}]$ | $-\tfrac23iD-\tfrac43d_{2}-\tfrac23d_{3}$ |
| the two-plane closure | $[A_{xy},iS_{yz}]$ | $+iS_{xz}$ |
| the four classes of the fifteen on $e_{t}$ | $8+1+6$ | $15$ |
| the fermion–gauge entries, one chirality | $48+16+24$ | $88$ |
| the nonzero brackets | the commutation table | $164$ of $441$ |
| the normalisation ratio, corner to weak | $\sqrt{2/24}$ | $0.2887$ |
| the fifteen, orthonormalised | $\sum_{a=1}^{15}t_{a}^{2}$ | $-\tfrac{15}{8}\mathbb{1}$ |
| the fifteen, unrotated | the same sum without the rotation | $-1.875$, $-1.792$, $-2.042$, $-1.792$ |
| the $B-L$ transfer, leptoquark, both rows | $\Delta Q$ | $-\tfrac23$ in both |
| the nine and twelve of the spectrum | $8+1$ and $6+2+2+1+1$ | $9$ and $12$ |

## Summary

**The rules of this model are the rules of one Lagrangian, and the Lagrangian is the corpus's.** One covariant derivative with three symbolic couplings, four pieces, and a vertex list of seven types. **The dictionary is the contribution**: the twenty-one gauge fields against the sixteen fermions give $88$ nonzero vertex entries per chirality, all of them entries of the printed arrays, and the three-gauge sector is the commutation table's $164$ nonzero brackets.

**Three things had to be settled before a rule could be written.** The normalisation, because the printed arrays carry three different trace norms and a canonical kinetic term forces a family-dependent rescaling of $\tfrac12$, $1/\sqrt{24}$ and $1/\sqrt2$. The generator convention, because the corpus's arrays are anti-hermitian and a rule needs hermitian generators, so the translation is one $i$ and one rescaling per gauge leg. And the two-index rule, because every vertex is $X\otimes\mathbb{1}_{2}$ and that bracket decides that no gauge vertex mixes the quartet index with the doublet index.

**The fermion–gauge vertex is where the algebra and the physics meet and where the ledger has to be honest.** The matrix is exact: the fifteen act on the quartet, the selection rule is eight annihilate the lepton line, one multiplies it, six move it into the triple, and no generator turns a lepton into a lepton. The dynamics is transcribed, because the spin-$\tfrac12$ sector has no action from the algebra and the corpus says so before this article prints a rule.

**What the article hands on is a shape and a normalisation and no numbers.** Couplings symbolic, loops absent, scalars counted and not instantiated, Yukawa elsewhere. **A reader who wants an amplitude needs one more article, and it is [the three diagrams](three-diagrams-of-the-four-colours-model-the-kaon-the-proton-chain-and-a-gluon-exchange.html) that applies these rules twice with a number and once with a colour factor.**

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $A_{jk}$, $iS_{jk}$ | Real and imaginary plane arrays, $A_{jk}=E_{jk}-E_{kj}$, $iS_{jk}=i(E_{jk}+E_{kj})$ |
| $iD$, $d_{2}$, $d_{3}$ | The corner $i\operatorname{diag}(-3,1,1,1)$ and the two colour diagonals |
| $T^{L}_{a}$, $T^{R}_{a}$ | The weak arrays, $-\tfrac12(A_{ta}\pm A_{bc})$, $(a,b,c)$ cyclic |
| $G_{a}$ | A printed array, any of the twenty-one |
| $t_{a}$ | Its normalised generator, $iG_{a}/\sqrt{2\operatorname{tr}(G_{a}^{\dagger}G_{a})}$ |
| $f_{abc}$ | Structure constants, $[G_{a},G_{b}]=f_{abc}G_{c}$, real |
| $g_{4}$, $g_{L}$, $g_{R}$ | The three couplings, symbolic and independent |
| $\xi_{f}$ | A fermion field of family $f$, in the $\mathbf{16}$ |
| $\tau_{i}$ | $\sigma_{i}/2$, acting on the doublet slot |
| $\gamma_{\imath}$ | The Dirac matrix in the direction $\imath$, index low |
| $\zeta$ | Gauge parameter, $\zeta=1$ the Feynman gauge |
| $v$, $v_{R}$ | The two vacuum values, $v^{2}=\kappa^{2}+\kappa'^{2}$ |
| $\kappa$, $\kappa'$ | The bidoublet's two vacuum entries |
| $u,d$ | The doublet slots, $\uparrow$ and $\downarrow$ in the classification |
| $r,g,b$ | The three colour directions, $x,y,z$ in every matrix |
| $\mathbf{4}$, $\bar{\mathbf{4}}$ | The two chiral blocks, $(\mathbf{4},\mathbf{2},\mathbf{1})$ and $(\bar{\mathbf{4}},\mathbf{1},\mathbf{2})$ |
| $\bar X^{\alpha}$, $X^{\alpha}$ | The leptoquarks of charge $-\tfrac23$ and $+\tfrac23$ |
| $\mathcal{L}_{\mathrm{gf}}$, $\mathcal{L}_{\mathrm{gh}}$ | Gauge fixing and ghosts |
| $88$ | The number of nonzero fermion–gauge vertex entries in one chirality |

## Further Reading

- [The Four Colours Left–Right Model](the-four-colours-left-right-model.html). The group, the sixteen, the one covariant derivative, and the declaration this article takes as given.
- [The Commutation Table of the Twenty-One Generators](the-commutation-table-of-the-twenty-one-generators-441-entries-164-nonzero-and-six-rules.html). The $164$ nonzero brackets and the six rules the three-gauge vertices are read from.
- [The Twenty-One AXF Matrices of the Bosons in Detail](the-21-axf-matrices-of-the-bosons-in-detail.html). Every printed array, with its entries and its spectrum.
- [The Five Counts of the Twenty-One](the-five-counts-of-the-twenty-one-twenty-four-cells-six-planes-twenty-one-arrays-fifteen-directions.html). The trace norms $2$, $12$, $1$, which the normalisation section uses.
- [The Lagrangian and Quantum Chromodynamics: The Triplet, the Octet and the Feynman Rules](the-lagrangian-and-quantum-chromodynamics-the-triplet-the-octet-and-the-feynman-rules.html). The worked model of this article's format, and the derivation of a three- and a four-point vertex.
- [The Feynman Propagator in Biquaternionic Form](the-feynman-propagator-in-biquaternionic-form.html). The two-point function, and the $i\epsilon$ the algebra supplies without the orientation.
- [The S-Matrix in Biquaternionic Form](the-s-matrix-in-biquaternionic-form.html). The Dyson series and the contraction that turns these rules into amplitudes.
- [Gauge Fixing in the Electroweak Theory: $R_\xi$ Gauges, Ghosts and the Goldstone Equivalence Theorem](gauge-fixing-in-the-electroweak-theory-r-xi-gauges-ghosts-and-the-goldstone-equivalence-theorem.html). The ghost sector this article borrows.
- [The Mass Matrix of the Twenty-One Gauge Bosons](the-mass-matrix-of-the-twenty-one-gauge-bosons-four-blocks-one-mixing-and-the-nine-zeros.html). The masses and the one mixing the propagators are written in.
- [The Fermion–Gauge Vertex in the Quartet Basis](the-fermion-gauge-vertex-in-the-quartet-basis-the-fifteen-read-on-the-sixteen.html). The companion, which takes the vertex of the section above and prints all fifteen matrices on the sixteen fields.

