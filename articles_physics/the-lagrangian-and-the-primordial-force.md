# __The Lagrangian and the Primordial Force: The $\mathrm{SU}(4)$ Action, One Coupling on Fifteen Generators__

## Introduction

This article writes the $\mathrm{SU}(4)$ action in one display, derives the equations of motion and the constraints the display implies, and states what the display is: a matrix transcription of the Yang–Mills action onto fifteen generators, and not an action built from the algebra's own elements.

The pieces of the action exist in the corpus as fragments. *The Feynman Rules of the Model* writes one covariant derivative and four pieces and then reads rules off them; the scalar census counts sixteen real components and says in as many words that it establishes no potential; the Yukawa sector diagonalises one matrix. **No article writes them in one display and derives from them.** This one does, and it is the article the block exists for: every other force block of the corpus carries its Lagrangian article, and the primordial force carried none.

The parent is *The Lagrangian and the Non-Abelian Gauge Fields*, which writes $-\tfrac12\operatorname{tr}(\sum_{\imath,\jmath}\mathbb{F}_{\imath\jmath}\mathbb{F}_{\imath\jmath})$ for $\mathrm{SU}(2)$ and proves that the trace which makes the density gauge invariant is the matrix trace and not the corpus's informational reduction $2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2)$. **That step does not change here.** What changes is the size of the matrix and the status of the result, and the status is the harder half.

Three things are established.

*First, the display.* With $Ξ$ the scalar and $\xi_f$ the sixteen Weyl fields,

$$
\mathcal{L}
=-\tfrac14\sum_{a,\imath,\jmath}F_{a,\imath\jmath}F_{a,\imath\jmath}
+\sum_{f}\bar\xi_{f}\Bigl(-i\sum_{\imath}\varepsilon_{\imath}\gamma_{\imath}D_{\imath}\Bigr)\xi_{f}
+\operatorname{tr}\bigl(D_{\imath}Ξ\bigr)^{\dagger}\bigl(D_{\imath}Ξ\bigr)-V(Ξ)
+\mathcal{L}_{\mathrm{gf}}+\mathcal{L}_{\mathrm{gh}}+\mathcal{L}_{\mathrm{Yuk}} ,
$$

with one covariant derivative, $D_{\imath}=\partial_{\imath}-ig_4\sum_{a=1}^{15}A_{a,\imath}t_{a}$, and one gauge coupling. **The coupling is the same $g_4$ in the gauge, fermion and scalar kinetic terms**, and that identity is the whole content of the words *one force*. **The display carries seven terms and four dynamical pieces**, the other three being the gauge-fixing, the ghosts and the Yukawa. **One force does not mean one parameter**: the scalar's $\mu_{\Phi}^{2}$, $\lambda_{1}$ and $\lambda_{2}$, the Yukawa matrix $y$, the gauge parameter $\zeta$ and the topological angle $\theta_{4}$ are six more numbers, and §*What the Display Does Not Contain* lists them.

*Second, the equations and the count.* The stationarity condition is $\sum_{\imath}\varepsilon_{\imath}D_{\imath}F_{\imath\jmath}=g_4\,j_{\jmath}$, with the current built from the sixteen and the scalar matrix; the temporal component is a Gauss law per generator, fifteen in all; and the constraint algebra fixes the degrees of freedom to $15\times2$ for the gauge fields, $32$ states for the fermions and $16$ real for the scalar.

*Third, the status, and it is the point of the article.* $\mathrm{SU}(2)$ is written *in* the algebra; $\mathrm{SU}(4)$ is written *on* it. The compact group of $\mathbb{B}$ is $\mathrm{U}(2)$, of real dimension four, and fifteen generators do not fit inside four. **So the action below is a transcription and not a derivation**, and it stands with $\mathrm{SU}(3)$ on the transcribed side of the ceiling, not with $\mathrm{SU}(2)$ on the derived side. *Why the Biquaternion Algebra Reaches $SU(2)$ but Not $SU(3)$* owns the argument; this article states where its display falls in it.

What is not new. The Yang–Mills action with matter is standard, and its derivation is a page of any text. What the corpus contributes is the identification of the fifteen printed arrays with a set $t_{a}$ satisfying $\operatorname{tr}(t_{a}t_{b})=\tfrac12\delta_{ab}$ — one rotation and three rescalings, done in §*The Normalisation* — the trace-versus-pairing distinction, and the ceiling statement.

## Conventions

The conventions are restated so that every sign below is checkable from this page.

**The algebra and the coordinates.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with $e_t=1$ and $\vec e_{\imath}^{2}=-e_t$, $\imath=x,y,z$; the material sector is $\mathbb{B}_\Phi$, where the time coefficient is imaginary, $Q_t=iq'_t$. The coordinates are $R_{\imath}=(R_t,R_x,R_y,R_z)$, the derivatives are $\partial_{\imath}=\partial/\partial R_{\imath}$, and the measure is $d^4r$. **Every index is low and every sum carries its weight**, as in *Index and Notation Conventions*: $\sum_{\imath}\varepsilon_{\imath}$ for a spacetime contraction with $\varepsilon_{\imath}=(1,-1,-1,-1)$, and the unit metric $\delta_{\imath\jmath}$ raises nothing.

**The generators.** Two sets, and the difference between them is one factor of $i$ and one rescaling. $G_{a}$, $a=1,\dots,15$, are the printed arrays of the boson block — the twelve planes $A_{\imath\jmath}$ and $iS_{\imath\jmath}$, the two colour diagonals $d_{2}$ and $d_{3}$ and the corner $iD$ — taken anti-Hermitian, $G_{a}^{\dagger}=-G_{a}$ and $\operatorname{tr}G_{a}=0$. $t_{a}$ are the normalised Hermitian generators of §*The Normalisation*, $t_{a}=iG_{a}/2$ for the thirteen arrays of norm $2$, $t_{c_{3}}=i(d_{2}-d_{3})/\sqrt{12}$ and $t_{15}=iG_{15}/\sqrt{24}$, so that $\operatorname{tr}(t_{a}t_{b})=\tfrac12\delta_{ab}$. **The action is written in $t_{a}$**; the printed $G_{a}$ are what the count, the trace norms and the commutation table are computed from. The cell names are the grid's, and *Classification of the Bosons* fixes them.

**The bracket.** $[G_{a},G_{b}]=\sum_{c}f^{c}_{\ ab}G_{c}$ and, in the Hermitian basis, $[t_{a},t_{b}]=i\sum_{c}f^{c}_{\ ab}t_{c}$ with the same real coefficients. **That factor of $i$ is the whole difference between the two bases, and it decides the sign structure of every vertex that touches the scalar** (§*The Scalar Piece*). The coefficients are real and antisymmetric in $a$ and $b$, read off the commutation table: of the $105$ independent pairs, $80$ brackets are nonzero, and the number of distinct index triples is $31$ in the printed basis and $29$ once the two colour diagonals are rotated to the orthonormal pair. **They are not totally antisymmetric in all three indices as they stand**, because $d_{2}$ and $d_{3}$ are not orthogonal: total antisymmetry belongs to the lowered $f_{abc}$ and holds only in the orthonormal basis.

**The traces.** $\operatorname{tr}$ is the matrix trace on $\mathbb{B}\cong M_2(\mathbb{C})$ enlarged to the $4\times4$ matrices that represent $\mathfrak{su}(4)$; $\mathrm{Sc}$ is the coefficient of $e_t$ in an element of $\mathbb{B}$. **The two are different functionals and only the first is used in the action**, for the reason §*The Trace and Not the Reduction* gives.

**The fields.** $A_{a,\imath}$ is the gauge field of generator $a$, real; $F_{a,\imath\jmath}$ its field strength; $\xi_{f}$, $f=1,\dots,16$, the Weyl fields of $2\cdot\mathbf{4}\oplus2\cdot\bar{\mathbf{4}}$; $Ξ$ the scalar, a $4\times4$ Hermitian matrix in the colour indices and carrying no copy index, so $15+1=16$ real parameters; $\gamma_{\imath}$ the Dirac matrices, written low.

## The Display

**The pieces and what each one is for.**

| piece | field | what it supplies |
| --- | --- | --- |
| $-\tfrac14\sum F F$ | the fifteen | the propagator and both self-couplings |
| fermion kinetic | the sixteen | the fermion–gauge vertex, one matrix per generator |
| scalar kinetic | $Ξ$, sixteen real | the gauge–scalar vertex and the mass of the six |
| $V(Ξ)$ | $Ξ$ | the scalar self-couplings |
| $\mathcal{L}_{\mathrm{gf}}$, $\mathcal{L}_{\mathrm{gh}}$ | fifteen ghosts | the gauge-fixing and ghost vertices |
| $\mathcal{L}_{\mathrm{Yuk}}$ | fermions and $Ξ$ | one matrix in the family index |

**Why the gauge piece is written with $\tfrac14$ and the element form with $\tfrac12$.** The two are the same number read in two bases. With $F_{\imath\jmath}=\sum_{a}F_{a,\imath\jmath}t_{a}$, the normalised generators of §*The Normalisation* and not the printed arrays, and $\operatorname{tr}(t_{a}t_{b})=\tfrac12\delta_{ab}$,

$$
\operatorname{tr}\Bigl(\sum_{\imath,\jmath}F_{\imath\jmath}F_{\imath\jmath}\Bigr)
=\tfrac12\sum_{a,\imath,\jmath}F_{a,\imath\jmath}F_{a,\imath\jmath},
$$

so $-\tfrac12\operatorname{tr}(\sum FF)=-\tfrac14\sum_{a}FF$. **The coefficient is not a choice**: it is fixed once the generators are normalised, and the normalisation is fixed by the requirement that the kinetic term of $A_{a,\imath}$ be canonical. **Written with the printed $T_{a}$ instead, the trace norms are $2$ and $12$ and the coefficient is not $\tfrac14$** — which is why every vertex in this block is read from $t_{a}$ and not from $T_{a}$.

**Why nothing else appears at dimension four.** The gauge invariant, parity-even, dimension-four functionals of the fifteen alone are the square of the curvature and nothing else. A cubic term vanishes because $\operatorname{tr}$ of an odd number of generators is zero, and a term with a derivative of the curvature has dimension five. **One further term exists and is not written**: the topological density $\operatorname{tr}(\mathbb{F}\wedge\mathbb{F})$, whose integral is quantised and whose coefficient $\theta_4$ is a free parameter of the theory and not a function of the group. It is named here and left to *The $\mathrm{SU}(4)$ Instanton*.

**The fermion piece in the corpus's coordinates.** The kinetic term is

$$
\mathcal{L}_{\psi}=\sum_{f}\bar\xi_{f}\Bigl(-i\sum_{\imath}\varepsilon_{\imath}\gamma_{\imath}D_{\imath}\Bigr)\xi_{f},
\qquad
D_{\imath}\xi_{f}=\partial_{\imath}\xi_{f}-ig_4\sum_{a}A_{a,\imath}\,\begin{pmatrix}t_{a}\otimes\mathbb{1}_{2}&0\\0&-t_{a}^{T}\otimes\mathbb{1}_{2}\end{pmatrix}\xi_{f},
$$

**The two blocks are the quartet half and the conjugate half.** The $8\times8$ matrix is block-diagonal on the colour index and tensored with $\mathbb 1_{2}$ on the copy index, so each of the fifteen acts on the sixteen components as one sign on the $\mathbf4$ and the other on the $\bar{\mathbf4}$. The $\varepsilon_{\imath}$ on the Dirac contraction is the weight the corpus prints everywhere else, and it is what makes this a Minkowski Dirac operator and not a Euclidean one. **The minus in the lower block is not a convention**: the conjugate of a $\mathbf4$ transforms with $-t_{a}^{T}$, and *The Fermion–Gauge Vertex in the Quartet Basis* prints the $-t_{a}^{T}$ on its conjugate half for this reason. **That minus is also what makes the anomaly cancel**: the $\mathrm{SU}(4)^3$ index is $+1$ on each quartet and $-1$ on each antiquartet, and a vertex that forgot the sign would make the index $+4$ instead of $0$.

**The copy index is untouched by every generator.** That is the one structural statement the fermion piece makes: the sixteen are $\xi^{\alpha}_{i}$ with the quartet index slow and the copy index fast, so each array acts as $X\otimes\mathbb{1}_{2}$ on the quartet half and $-X^{T}\otimes\mathbb{1}_{2}$ on the conjugate half, and the two-index rule of *The Fermion–Gauge Vertex in the Quartet Basis* is *recovered* here rather than assumed. **The piece contains no mass and no chirality projection**; both would need a second structure and the group supplies neither.

**The scalar piece.** With $Ξ$ a Hermitian $4\times4$ transforming as $Ξ\mapsto UΞ U^{\dagger}$,

$$
\mathcal{L}_{\Phi}=\operatorname{tr}\bigl(D_{\imath}Ξ\bigr)^{\dagger}\bigl(D_{\imath}Ξ\bigr)-V(Ξ),
\qquad
D_{\imath}Ξ=\partial_{\imath}Ξ-ig_4\sum_{a}A_{a,\imath}[t_{a},Ξ] .
$$

**The $i$ in the scalar's derivative, because this is the one place a base change silently destroys a vertex.** With $t_{a}$ Hermitian and $Ξ$ Hermitian, the commutator $[t_{a},Ξ]$ is anti-Hermitian, so $-ig_4[t_{a},Ξ]$ is Hermitian and $D_{\imath}Ξ$ is Hermitian, as the derivative of a Hermitian field must be. **The $i$ is also what makes the two orderings add**: $(DΞ)^{\dagger}(DΞ)$ expands to $\operatorname{tr}(\partialΞ)^{2}-2ig_4\operatorname{tr}(\partial_{\imath}Ξ[A_{\imath},Ξ])+g_4^{2}\operatorname{tr}([A_{\imath},Ξ])^{2}$, and the two cross terms carry the same sign because the dagger flips one of them. **The gauge–scalar three-point vertex is therefore $-2ig_4\operatorname{tr}(\partial_{\imath}Ξ[A_{\imath},Ξ])$, and it is not optional.** Written instead with the anti-Hermitian $G_{a}$ and the same $i$ — which is what a careless substitution of the printed arrays does — the two orderings cancel exactly, $\operatorname{tr}(CP)=\operatorname{tr}(PC)$, and the vertex vanishes identically: **the numbers do not change, the sign of the coupling's $i$ relative to the generator's does, and the interaction disappears.** That is why the display is written in $t_{a}$.

**The commutator, because the matrix index is what the mass operator needs.** $\bar\xiΞ\xi$ is a singlet only if $Ξ$ carries one lower and one upper colour index, and $\bar{\mathbf4}\otimes\mathbf4=\mathbf{15}\oplus\mathbf1$ is exactly the adjoint plus the singlet. **The trace in the kinetic term is then the only invariant of degree two**, and the covariant derivative acts by commutation because that is how a generator acts on an object with one index of each kind.

**A quartet would have been cheaper and would have had no mass term.** Its derivative is $t_{a}Ξ$ with no commutator and its potential has one quartic instead of two. $\mathbf4\otimes\mathbf4=\mathbf6\oplus\mathbf{10}$ contains no $\bar{\mathbf4}$, so no $\bar\xiΞ\xi$ exists, and the sixteen would be massless at every scale with no Yukawa sector at all. **The extra structure is the price of the fermion masses**, and *The Scalar Content* records the argument in full.

**$Ξ$ carries two colour indices and nothing else.** The matrix is Hermitian, so sixteen real parameters, and they are the algebra's: $15$ for the traceless part, which is $\dim\mathrm{SU}(4)$, and $1$ for the trace. **Nothing is multiplied**, and the sixteen of the scalar is the same kind of count as the fifteen of the vectors.

**What this costs, stated so the census and this article agree.** Sixteen real components at the scale of the display, and the eating is the transition's: six directions, one per broken generator of $\mathrm{SU}(4)$. **So six go and ten survive**, this article counts the phase before the eating, and *The Scalar Content* counts what the transition removes and what it leaves.

**The potential, written and not derived.** The matrix carries one index of each colour kind, and the trace is the only contraction available. Two invariants of degree four are independent,

$$
V(Ξ)=\mu_{\Phi}^{2}\operatorname{tr}Ξ^{2}+\lambda_{1}\operatorname{tr}Ξ^{4}+\lambda_{2}\bigl(\operatorname{tr}Ξ^{2}\bigr)^{2},
$$

and the group fixes neither $\mu_{\Phi}^{2}$ nor the two quartics. **Two quartics and not one**, because $\operatorname{tr}(Ξ^{2})^{2}$ and $(\operatorname{tr}Ξ^{2})^{2}$ are different contractions of four matrix indices and neither is a function of the other. **A cubic $\operatorname{tr}Ξ^{3}$ is also invariant, real and allowed**, and this potential leaves it out: *The Primordial Potential* computes the threshold at which it would matter, and its absence is a truncation stated and not a symmetry.

**Which sign gives which vacuum, stated because the two branches are not one.** The symmetric minimum is $\mu_{\Phi}^{2}>0$, so that $\langleΞ\rangle=0$ and the group is exact. **The broken phase is not simply the other sign of $\mu_{\Phi}^{2}$**: as *The Primordial Potential* shows, the declared vacuum $\operatorname{diag}(-3,1,1,1)$ is a minimum of this two-quartic potential only in the branch $\lambda_{1}<0$ with $\operatorname{tr}Ξ=0$ imposed, while in the branch $\lambda_{1}>0$ the minimum is the even split. **So the vacuum is a choice of sign as well as of size**, and *The Breaking of the Primordial Force* reads the branch the corpus declares.

**This is the one place where the article writes coefficients the group does not supply, and it says so**: the scalar census refuses the potential on purpose, and the refusal is correct at that article's scope.

### Two Quartics and Not One

**The count is a count of contractions, and it is the price of the matrix index.**

| scalar | degree-two invariants | degree-three | degree-four invariants | quartics |
|---|---|---|---|---|
| the quartet $\mathbf4$ | $1$ | $0$ | $1$ | $1$ |
| the traceless matrix $\mathbf{15}$ | $1$ | $1$ | $2$ | $2$ |
| the singlet $\mathbf1$ | $1$ | $1$ | $1$ | $1$ |

**The row that matters is the traceless one, because $\operatorname{tr}Ξ=0$ is the corpus's declaration** (§*The Primordial Potential*). **A matrix has two ways to contract four indices and a vector has one.** $\operatorname{tr}(Ξ^{2})^{2}$ pairs the indices within each pair, $(\operatorname{tr}Ξ^{2})^{2}$ pairs them across, and the difference between the two is a genuine deformation of the potential's shape. **A vector cannot tell the two apart**, which is why the quartet reading had one quartic and looked economical. **The third row is the price of keeping the trace**: through $\operatorname{tr}Ξ$ it turns the quadratic into two and would add a third quartic, $(\operatorname{tr}Ξ)^{4}$ and the mixed terms, which is why the census and this display impose the traceless condition rather than carry them.

**What the second quartic buys.** It is what allows a minimum whose direction is not decided by the quadratic term alone, so the vacuum's *shape* — in particular whether $Ξ$ is proportional to a rank-one matrix or to a multiple of the identity — is a dynamical question rather than a declared one. **The corpus's vacuum is rank one**, $Ξ\propto D\otimes d$ with $D=\operatorname{diag}(-3,1,1,1)$, and the second quartic is what makes that a choice the potential can prefer.

**What it costs.** One more free number in a block whose virtue is that it has one coupling. **The gauge sector has one parameter and the scalar sector has three**, and the asymmetry is not a defect of the writing: it is the number of invariants a matrix admits.

**The gauge-fixing and ghost pieces.** $\mathcal{L}_{\mathrm{gf}}=-\tfrac{1}{2\zeta}\sum_{a}\bigl(\sum_{\imath}\varepsilon_{\imath}\partial_{\imath}A_{a,\imath}\bigr)^{2}$ with one parameter $\zeta$ for the whole group, and $\mathcal{L}_{\mathrm{gh}}=\sum_{a}\bar c_{a}\bigl(-\sum_{\imath}\varepsilon_{\imath}\partial_{\imath}D_{\imath}\bigr)c_{a}$ with fifteen ghosts in the adjoint. **One parameter and not four**, which is the difference between this block and the electroweak one: there the four factors each carried a gauge parameter and the mixing made them unequal.

**The Yukawa piece, named and not written.** One operator per scalar block and one matrix in the copy index,

$$
\mathcal{L}_{\mathrm{Yuk}}=y_{\alpha\beta}\,\bar\xi^{\alpha}Ξ\,\xi^{\beta}+\text{h.c.},
$$

and *The Yukawa Sector* owns its invariance, its diagonalisation and the mass relation that follows. **This article states only that the operator exists here and could not exist under the quartet reading.**

### The Operator the Matrix Index Makes Possible

**One contraction, read on the indices.**

$$
\bar\xi\in\bar{\mathbf4},\qquad Ξ\in\bar{\mathbf4}\otimes\mathbf4=\mathbf{15}\oplus\mathbf1,\qquad \xi\in\mathbf4,
\qquad
\bar{\mathbf4}\otimes(\mathbf{15}\oplus\mathbf1)\otimes\mathbf4\supset\mathbf1 .
$$

**There is exactly one invariant contraction, and it uses all sixteen components.** Write the contraction as $\bar\xi\,Ξ\,\xi$; since $\mathbf{15}$ and $\mathbf1$ are separate irreducible blocks, it splits into two operators,

$$
\mathcal{L}_{\mathrm{Yuk}}=y\,\bar\xi\,Ξ_{15}\,\xi+y'\,\bar\xi\,Ξ_{1}\,\xi+\text{h.c.},
$$

**so a complete ledger carries two coefficients and this one carries a single matrix $y$.** The model sets $y'$ to zero — a choice, stated here and not derived.

**Where the mass then comes from is a sharper statement, and it is the one the rest of the block uses.** The vacuum is $Ξ_0=vD$ with

$$
\operatorname{tr}D=-3+1+1+1=0 ,
$$

**so the singlet block vanishes at the minimum and the whole mass matrix is the adjoint block's**,

$$
M_{\imath\jmath}=y\,v\,D_{\imath}\delta_{\imath\jmath},
$$

which is the matrix *The Yukawa Sector* diagonalises, and which gives $m_\ell=3m_q$ within a copy. **A reader who takes "only the trace part contributes" literally gets $\operatorname{tr}D=0$ and therefore massless fermions**, which is the one reading of this section that the arithmetic forbids.

**What a quartet would have given.** Nothing: $\mathbf4\otimes\mathbf4=\mathbf6\oplus\mathbf{10}$, and neither term contains a $\bar{\mathbf4}$, so the product $\bar{\mathbf4}\otimes\mathbf4\otimes\mathbf4$ has no singlet. **The table in §*The Scalar Content* is the whole argument**, and it is the reason the matrix reading is the model's.

**What the fermion copy index adds.** $y_{\alpha\beta}$ is a $2\times2$ matrix on the two Weyl fields that share a colour index, so the pair is mixed by the Yukawa and not by the gauge sector. **Two eigenvalues, one diagonalisation, and the condensate's two entries $(-3v_C,+v_C)$ multiplying them**, which is the arithmetic of the mass relation and belongs to the article that computes it.

## The Normalisation, and Why the Corner Is Different

**The printed arrays are anti-Hermitian and their trace norms take two values.**

| family | arrays | $\operatorname{tr}\bigl(G^{\dagger}G\bigr)$ | $\operatorname{tr}\bigl(G^{2}\bigr)$ |
| --- | --- | --- | --- |
| the twelve planes, $A_{\imath\jmath}$ and $iS_{\imath\jmath}$ | $12$ | $2$ | $-2$ |
| the colour diagonals $d_{2}$, $d_{3}$ | $2$ | $2$ | $-2$ |
| the corner $iD$ | $1$ | $12$ | $-12$ |

**One pair among the fifteen is not orthogonal, and it is the only one.** $\operatorname{tr}(d_{2}d_{3})=+1$, so the Gram entry $\langle d_{2},d_{3}\rangle=-\operatorname{tr}(d_{2}d_{3})=-1$ while every other pair vanishes. **The printed fifteen are a basis and not an orthonormal frame**, and the Gram has eigenvalues $1$, twelve copies of $2$, $3$ and $12$.

**The repair is one rotation and then three rescalings.**

$$
c_{2}=d_{2}+d_{3},\qquad c_{3}=d_{2}-d_{3},\qquad
\langle c_{2},c_{2}\rangle=2,\quad\langle c_{3},c_{3}\rangle=6,\quad\langle c_{2},c_{3}\rangle=0 .
$$

After the rotation the fifteen are orthogonal, with norm $2$ for thirteen of them, $6$ for $c_{3}$ and $12$ for the corner. **The rotation is not a convenience**: it is what makes the two colour phases orthogonal, and $c_{3}$ pays for it with a norm three times a plane's. **A canonical kinetic term $\operatorname{tr}(t_{a}t_{b})=\tfrac12\delta_{ab}$ then fixes**

$$
t_{a}=\frac{iG_{a}}{2}\ \ (13\ \text{arrays}),\qquad
t_{c_{3}}=\frac{i(d_{2}-d_{3})}{\sqrt{12}}\ \ (c_{3}),\qquad
t_{15}=\frac{iG_{15}}{\sqrt{24}}\ \ (\text{the corner}).
$$

**Check.** For the corner, $\operatorname{tr}(t_{15}t_{15})=-\tfrac{1}{24}\operatorname{tr}(G_{15}G_{15})=\tfrac{12}{24}=\tfrac12$; for a plane, $\operatorname{tr}(t_{a}t_{a})=-\tfrac14(-2)=\tfrac12$; and for $c_{3}$, $-\tfrac{1}{12}(-6)=\tfrac12$. **All three families give one half, which is the statement that the normalisation succeeds — and it succeeds with three coefficients, not two.** The corner's coefficient is smaller than a plane's by $2/\sqrt{24}=1/\sqrt6$, and $c_{3}$'s by $2/\sqrt{12}=1/\sqrt3$; **both factors are consequences of the trace and not of the group**, the corner's length being $\sqrt6$ times a plane's and $c_{3}$'s $\sqrt3$ times.

**Why the rescaling is not cosmetic.** A vertex read off a printed array is off by this factor, and a cross section read off a vertex is off by its square. **The factor is stated once, here, so that the articles that print a vertex restate it rather than re-derive it.**

### The Trace and Not the Reduction

**The density must be invariant under $\mathbb{F}_{\imath\jmath}\mapsto U\mathbb{F}_{\imath\jmath}U^{-1}$**, and only the cyclicity of the matrix trace gives that in one line:

$$
\operatorname{tr}\Bigl(\sum_{\imath,\jmath}U\mathbb{F}_{\imath\jmath}U^{-1}U\mathbb{F}_{\imath\jmath}U^{-1}\Bigr)
=\operatorname{tr}\Bigl(\sum_{\imath,\jmath}\mathbb{F}_{\imath\jmath}\mathbb{F}_{\imath\jmath}\Bigr).
$$

**The corpus's informational reduction does not have that property.** $2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2)$ is bilinear, symmetric and real on the material sector, but it is not cyclic, so a density built from it would change under a gauge transformation and the theory would not be a gauge theory. **The two functionals agree only where one factor is a scalar**, and a field strength is not a scalar. The proof is *The Lagrangian and the Non-Abelian Gauge Fields*'s; it is cited here rather than repeated, and it is the sharpest technical statement in either article.

**Reality and sign.** For anti-Hermitian $\mathbb{F}_{\imath\jmath}$, $\operatorname{tr}(\mathbb{F}_{\imath\jmath}\mathbb{F}_{\imath\jmath})$ is real, and $\operatorname{tr}(\mathbb{F}_{\imath\jmath}^{\dagger}\mathbb{F}_{\imath\jmath})=-\operatorname{tr}(\mathbb{F}^{2})$ is non-negative. **Reality is what the anti-Hermiticity buys, and that much is not a convention.** **Positivity is a different statement and it belongs to the Hamiltonian, not to the Lagrangian**: the density $-\tfrac12\operatorname{tr}(\sum\mathbb{F}\mathbb{F})$ is $\tfrac12\sum_{a}(E_{a}^{2}-B_{a}^{2})$ once the corpus's weights are applied to the summed pairs, so it changes sign between an electric and a magnetic configuration. **The energy that is bounded below is $\tfrac12\sum_{a}(E_{a}^{2}+B_{a}^{2})\ge0$**, and it is positive for the same reason.

## The Variation: One Equation and Fifteen Gauss Laws

**The curvature's variation is the covariant derivative of the variation**, $\delta\mathbb{F}_{\imath\jmath}=D_{\imath}\delta\mathbb{A}_{\jmath}-D_{\jmath}\delta\mathbb{A}_{\imath}$, so stationarity of the gauge piece alone gives $D_{\imath}F_{\imath\jmath}=0$. With the matter pieces present,

$$
D_{\imath}F_{a,\imath\jmath}=-g_4\Bigl(\sum_{f}\bar\xi_{f}\,\varepsilon_{\jmath}\gamma_{\jmath}\,t_{a}\,\xi_{f}+2i\operatorname{tr}\bigl(\bigl(D_{\jmath}Ξ\bigr)\bigl[t_{a},Ξ\bigr]\bigr)\Bigr),
$$

**The fermion term is a vector current and the scalar term is bilinear in $Ξ$.** Three things about that line are worth stating, because each is easy to lose in a display assembled from parts.

**One $g_4$ and one sign.** Both terms come from the same variation of the same action, so both carry one power of $g_4$ and the same sign; **factoring the $g_4$ out, $D_{\imath}F=g_4j$ with $j$ the bracket, is the same equation and the form the strong sector prints.** A display that lets $g_4$ multiply one term and not the other has two different theories under one symbol.

**The factor two is the commutator's two orderings.** The scalar term is $\partial\mathcal{L}_{\Phi}/\partial A_{a,\jmath}=-2ig_4\operatorname{tr}((D_{\jmath}Ξ)[t_{a},Ξ])$: the $2$ is $\{D_{\jmath}Ξ,[t_{a},Ξ]\}$ against the trace, and the $i$ is what makes the two orderings add rather than cancel (§*The Scalar Piece*). **Deleting either is not a normalisation choice**; the factor multiplies the three-point vertex, so a cross section moves by four.

**The copy index is not summed.** $t_{a}$ acts on the colour index alone, so the fermion bilinear carries one $t_{a}$ and no trace over the copy index; **an index that appears nowhere cannot be summed**, and a $\sum_{\alpha=1}^{2}$ in front of a trace over colour is an index that appears nowhere.

**The scalar current is quadratic above $M_C$ and linear below it**, and that shift is the whole mechanism of the mass: with $Ξ=v+\delta Ξ$ the current splits into a piece in the fluctuation $\delta Ξ$ and a piece in $\delta Ξ\,\delta Ξ$, and the first is the $A$–$\delta Ξ$ mixing that a mass term is. Above the transition only the second piece is present, so no one-scalar emission exists and every direction stays massless — which is why the unbroken phase has no mass term and needs none.

**The current is covariantly conserved.** Gauge invariance of the matter action makes $D_{\imath}j_{\imath}$ vanish once the matter fields are on shell, so the conservation is a consequence of the invariance and not a further condition. **The ordinary divergence $\partial_{\imath}j_{\imath}$ is not zero**, because it carries the $[A_{\imath},j_{\imath}]$ term. **So no gauge charge exists**, exactly as in the strong sector: the charge is defined only for the residual $\mathrm{SU}(3)\times\mathrm{U}(1)$ below $M_C$, and above it there is a current and no charge.

**The temporal component of the equation is not an equation of motion but a constraint.** $D_{\imath}F_{a,\imath t}=-g_{4}j_{a,t}$ contains no second time derivative of $A_{a,t}$, so it fixes $A_{a,t}$ in terms of the other fields: **a Gauss law per generator, fifteen in all.** Each is first class, so each removes two degrees of freedom from a four-component field, and the count is

$$
4\times15\ \longrightarrow\ 2\times15=30
$$

for the gauge fields, before gauge fixing and with the ghosts counted separately.

**The count, side by side.**

| field | components | on shell |
| --- | --- | --- |
| the fifteen $A_{a,\imath}$ | $4\times15=60$ | $30$ |
| the sixteen $\xi_{f}$ | $4\times16=64$ real | $32$ states |
| $Ξ$ | $15+1=16$ real | $16$ real |
| the ghosts $c_{a}$, $\bar c_{a}$ | $2\times15$ | $0$, loops only |

**The ghosts are not asymptotic states, and counting them again subtracts the vectors twice.** The ghosts restore unitarity in loops and contribute nothing on shell, exactly as in the strong sector; **a row that reads $-2\times15$ against the already-reduced $30$ leaves no vector state at all.** The on-shell total of this phase is therefore

$$
30+32+16=78 ,
$$

and the count is a statement about this phase only.

**The scalar's sixteen are all physical in this phase**, because no direction has been eaten: the eating is the transition's and it leaves ten. **That is the arithmetic the two articles divide between them** — this one counts the phase, *The Scalar Content* counts what the transition removes.

## The Ceiling: Transcription and Not Derivation

**The action above is correct as a Yang–Mills action for $\mathrm{SU}(4)$. It is not an algebra result, and the difference is measurable.**

The dimension of the algebra's compact group is four. $\mathbb{B}\cong M_2(\mathbb{C})$ has compact part $\mathrm{U}(2)=\mathrm{SU}(2)\times\mathrm{U}(1)$, of real dimension $3+1=4$, and a Lie algebra of fifteen generators does not embed in a four-dimensional one. **The $\mathrm{SU}(2)$ action of *The Lagrangian and the Non-Abelian Gauge Fields* is written in the algebra because its three generators are three of the algebra's own directions. The $\mathrm{SU}(4)$ action is written on a $4\times4$ matrix representation that the algebra does not contain.**

**What transcription costs, item by item.**

- *The trace.* The invariant density needs a cyclic trace on $\mathbb{C}^{4}$. The algebra supplies one on $\mathbb{C}^{2}$; the enlargement to $\mathbb{C}^{4}$ is a choice of representation, and the fifteen arrays are its matrices.
- *The curl and the cross product.* In the algebra the $\mathrm{SU}(2)$ bracket is the algebra's own product. Here the coefficients are read off a table of $105$ pairs, and the $80$ nonzero brackets among them are the structure constants.
- *The invariant density of the algebra.* $2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2)$ exists on every element of $\mathbb{B}$ and is not available for this action, because it is not cyclic. **So the one pairing the algebra owns is exactly the one the action cannot use**, and this is the precise sense in which the primordial force is transcribed.

**What transcription does not cost.** The group's content, its representation theory, its anomaly arithmetic and its mass spectrum are all exact. **The three species of statement must be kept apart**: the identity $2\cdot\mathbf{4}\oplus2\cdot\bar{\mathbf{4}}$ is algebra; the matrices $T_{a}$ are a representation; the action is a transcription. Nothing in the block is stronger than the second.

## What the Display Does Not Contain

**Six absences, each deliberate.**

- *No mass for the fifteen.* A mass term $\tfrac12m^{2}\sum_{a,\imath}A_{a,\imath}A_{a,\imath}$ is not gauge invariant, and none is written. The masses come from $\langleΞ\rangle$ and are the transition's.
- *No potential coefficients.* $\mu_{\Phi}^{2}$, $\lambda_{1}$ and $\lambda_{2}$ are the three parameters the group does not fix.
- *No Yukawa value.* One matrix, its entries free, its spectrum measured.
- *No value of $g_4$.* The coupling multiplies the action and does not cancel from the equation, because the commutator carries one power of it and the derivative none; but its value is a boundary condition taken from below, and *The Primordial Coupling* owns it.
- *No loop.* The running, the anomalous dimensions and the effective potential are one-loop objects and the classical action says nothing about them.
- *No $\theta_4$.* The topological term is admitted by the group, is not written in the display, and its coefficient is free.

## The Checks

**Eleven numbers, each recomputed from the printed arrays and not quoted.**

| statement | value |
| --- | --- |
| $\operatorname{tr}\bigl(G^{\dagger}G\bigr)$ for a plane | $2$ |
| $\operatorname{tr}\bigl(G^{\dagger}G\bigr)$ for $d_{2}$ and $d_{3}$ | $2$, $2$ |
| $\operatorname{tr}\bigl(G^{\dagger}G\bigr)$ for the corner $iD$ | $12$ |
| $\operatorname{tr}(d_{2}d_{3})$, the one nonzero off-diagonal of the Gram | $+1$ |
| $\langle c_{2},c_{2}\rangle$ with $c_{2}=d_{2}+d_{3}$ | $2$ |
| $\langle c_{3},c_{3}\rangle$ with $c_{3}=d_{2}-d_{3}$ | $6$ |
| $\langle c_{2},c_{3}\rangle$ | $0$ |
| $\operatorname{tr}(t_{a}t_{a})$ for a plane, $t_{a}=iG_{a}/2$ | $\tfrac12$ |
| $\operatorname{tr}(t_{15}t_{15})$ for the corner, $t_{15}=iG_{15}/\sqrt{24}$ | $\tfrac12$ |
| nonzero brackets of the fifteen | $80$ of $105$ |
| nonzero brackets $f^{c}_{\ ab}$ | $80$, over $31$ distinct triples in the printed basis |

**The normalisation is what makes the display's coefficient $\tfrac14$ and not a parameter**, and the corner's length is what makes the ratio $1/\sqrt6$ appear in every vertex that touches $B'$.

## Summary

The $\mathrm{SU}(4)$ Lagrangian is one coupling on fifteen generators and seven terms: the curvature's square, the sixteen's kinetic term, the scalar matrix's kinetic term and its potential, and the gauge-fixing, ghost and Yukawa pieces. **One $g_4$ enters the curvature and both covariant derivatives**, and that identity, not any vertex, is what the words *one force* mean. **The other six numbers — $\mu_{\Phi}^{2}$, $\lambda_{1}$, $\lambda_{2}$, $y$, $\zeta$ and $\theta_{4}$ — are parameters and not the couplings of a second and third force.**

The normalisation is one rotation and three rescalings. The printed fifteen fail to be orthogonal in exactly one place, $\operatorname{tr}(d_{2}d_{3})=+1$; the rotation $c_{2}=d_{2}+d_{3}$, $c_{3}=d_{2}-d_{3}$ repairs it, with norms $2$ and $6$; and $t_{a}=iG_{a}/2$, $t_{c_{3}}=i(d_{2}-d_{3})/\sqrt{12}$, $t_{15}=iG_{15}/\sqrt{24}$ then give $\operatorname{tr}(t_{a}t_{b})=\tfrac12\delta_{ab}$ for all fifteen. The corner is longer than a plane by $\sqrt6$, so every vertex that touches $B'$ carries the factor $1/\sqrt6$, and that factor comes from the trace and not from the group.

The variation gives one equation and fifteen constraints. $D_{\imath}F_{a,\imath\jmath}=-g_4j_{a,\jmath}$ with a fermion term and a scalar term, the scalar one vanishing at $\langleΞ\rangle=0$; the temporal component is a Gauss law per generator; thirty degrees of freedom survive for the gauge fields, thirty-two states for the fermions and sixteen real for the scalar, and **the ghosts contribute nothing on shell, so the total is seventy-eight.**

The trace is the matrix trace and not the informational reduction. Only cyclicity makes the density invariant, $2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2)$ is not cyclic, and the two agree only where one factor is a scalar. **This is the sharpest technical point of the article**: the one pairing the algebra owns is the one the action cannot use.

The status is transcription. The algebra's compact group is four-dimensional and the group has fifteen generators, so the action is written on a $4\times4$ representation and not in the algebra. $\mathrm{SU}(4)$ stands with $\mathrm{SU}(3)$ on the transcribed side of the ceiling; only $\mathrm{SU}(2)$, and its abelian factor, stand on the derived side.

Six things are deliberately absent: a mass for the fifteen, the potential's coefficients, the Yukawa's value, the value of $g_4$, every loop, and $\theta_4$. Each absence is a place where another article of the block begins.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A_{a,\imath}$, $F_{a,\imath\jmath}$ | Gauge field and field strength of generator $a$, $a=1,\dots,15$ |
| $g_4$ | The primordial coupling, one value for the whole group |
| $T_{a}$, $t_{a}$ | The printed array, and its rescaled form with $\operatorname{tr}(t_{a}t_{b})=\tfrac12\delta_{ab}$ |
| $G_{a}$ | The printed anti-Hermitian array; the action is written in $t_{a}=iG_{a}/2$, $t_{c_{3}}=i(d_{2}-d_{3})/\sqrt{12}$, $t_{15}=iG_{15}/\sqrt{24}$ |
| $d_{2}$, $d_{3}$ | The two colour diagonals; $\operatorname{tr}(d_{2}d_{3})=+1$ |
| $c_{2}$, $c_{3}$ | The rotated diagonals $d_{2}\pm d_{3}$, orthogonal, norms $2$ and $6$ |
| $iD$ | The corner, $\operatorname{diag}(-3i,i,i,i)$, trace norm $12$ |
| $f^{c}_{\ ab}$ | Structure constants, $[G_{a},G_{b}]=\sum_{c}f^{c}_{\ ab}G_{c}$ and $[t_{a},t_{b}]=i\sum_{c}f^{c}_{\ ab}t_{c}$ |
| $\xi_{f}$, $\bar\xi_{f}$ | The sixteen Weyl fields, $f=1,\dots,16$ |
| $Ξ$ | The scalar, a Hermitian $4\times4$, $16$ real components |
| $V(Ξ)$ | $\mu_{\Phi}^{2}\operatorname{tr}Ξ^{\dagger}Ξ+\lambda_{1}\operatorname{tr}(Ξ^{\dagger}Ξ)^{2}+\lambda_{2}(\operatorname{tr}Ξ^{\dagger}Ξ)^{2}$, three free coefficients |
| $y_{\alpha\beta}$ | The Yukawa matrix in the family index |
| $j_{a,\jmath}$ | The total current: a fermion term and a scalar term |
| $\zeta$ | The one gauge parameter of the group |
| $c_{a}$, $\bar c_{a}$ | The fifteen ghosts in the adjoint |
| $\theta_4$ | The coefficient of $\operatorname{tr}(\mathbb{F}\wedge\mathbb{F})$, free, not written |
| $\mathbb{F}_{\imath\jmath}$ | The element form, $\sum_{a}F_{a,\imath\jmath}G_{a}$, anti-Hermitian; the same combination in $t_{a}$ is Hermitian |
| $\operatorname{tr}$ | The matrix trace; not the informational reduction $2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2)$ |
| $d^4r$ | The measure; coordinates $R_{\imath}$, all indices low |

## Further Reading

- [The Lagrangian and the Non-Abelian Gauge Fields](the-lagrangian-and-the-non-abelian-gauge-fields.html). The parent: the $\mathrm{SU}(2)$ action, the trace-versus-reduction proof, and the ceiling in its original form.
- [The Feynman Rules of the Model: The Vertices of the Fifteen and the Sixteen](the-feynman-rules-of-the-su4-model-the-vertices-of-the-fifteen-and-the-sixteen.html). The rules this action produces, and the normalisation stated once more before any rule.
- [The $\mathrm{SU}(4)$ Model: Four Colours, Fifteen Generators, One Declaration](the-su4-model-four-colours-fifteen-generators-one-declaration.html). The content, the anomaly count and the one covariant derivative that this article writes an action for.
- [Classification of the Bosons: Nine Massless and Six Heavy](classification-of-the-bosons-in-the-su4-model-one-grid-fifteen-generators-nine-massless-six-heavy.html). The grid, the cell names, and which of the fifteen is which.
- [The Fifteen AXF Matrices of the Bosons in Detail](the-15-axf-matrices-of-the-bosons-in-detail.html). The printed entries from which the trace norms of §*The Normalisation* were recomputed.
- [The Commutation Table of the Fifteen Generators](the-commutation-table-of-the-fifteen-generators-225-entries-105-independent-80-nonzero-and-five-rules.html). The $105$ pairs, the $80$ nonzero brackets and the triples they fall into.
- [The Scalar Content](the-scalar-content-one-matrix-and-ten-survivors.html). The census that counts the sixteen and refuses the potential this article writes.
- [The Fermion–Gauge Vertex in the Quartet Basis](the-fermion-gauge-vertex-in-the-quartet-basis-the-fifteen-read-on-the-sixteen.html). The two-index rule that §*The Display* recovers from the copy index.
- [The Breaking of the Primordial Force and the Mass of the Six Leptoquarks](the-breaking-of-the-primordial-force-and-the-mass-of-the-six-leptoquarks.html). The other sign of $\mu_{\Phi}^{2}$, where the potential's minimum moves off the origin.
- [Why the Biquaternion Algebra Reaches $SU(2)$ but Not $SU(3)$](why-the-biquaternion-algebra-reaches-su-2-but-not-su-3.html). The dimension bound that makes §*The Ceiling* a statement about the algebra.
- [The Lagrangian and the Quantum Chromodynamics: The Triplet, the Octet and the Feynman Rules](the-lagrangian-and-quantum-chromodynamics-the-triplet-the-octet-and-the-feynman-rules.html). The same construction for three colours, transcribed as this one is, with the $R$ ratio and the colour factors that the primordial block has no analogue of.
- [The Standard Model and the Lagrangian: Four Sectors in One Expression](the-standard-model-and-the-lagrangian-four-sectors-in-one-expression.html). The sign rule, and where the primordial sector sits among the four.
