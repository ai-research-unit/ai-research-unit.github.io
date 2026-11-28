# __The Lagrangian and the Primordial Force: The $\mathrm{SU}(4)$ Action, One Coupling on Fifteen Generators__

## Introduction

This article writes the $\mathrm{SU}(4)$ action in one display, derives the equations of motion and the constraints the display implies, and states what the display is: a matrix transcription of the Yang–Mills action onto fifteen generators, and not an action built from the algebra's own elements.

The pieces of the action exist in the corpus as fragments. *The Feynman Rules of the Model* writes one covariant derivative and four pieces and then reads rules off them; the scalar census counts sixteen real components and says in as many words that it establishes no potential; the Yukawa sector diagonalises one matrix. **No article writes them in one display and derives from them.** This one does, and it is the article the block exists for: every other force block of the corpus carries its Lagrangian article, and the primordial force carried none.

The parent is *The Lagrangian and the Non-Abelian Connections*, which writes $-\tfrac12\operatorname{tr}(\sum_{\imath,\jmath}\mathbb{F}_{\imath\jmath}\mathbb{F}_{\imath\jmath})$ for $\mathrm{SU}(2)$ and proves that the trace which makes the density invariant is the matrix trace and not the corpus's informational reduction $2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2)$. **That step does not change here.** What changes is the size of the matrix and the status of the result, and the status is the harder half.

Three things are established.

*First, the display.* With $Ξ$ the scalar and $\xi_f$ the sixteen Weyl fields,

$$
\mathcal{L}
=-\tfrac14\sum_{a,\imath,\jmath}F_{a,\imath\jmath}F_{a,\imath\jmath}
+\sum_{f}\bar\xi_{f}\Bigl(-i\sum_{\imath}\varepsilon_{\imath}\gamma_{\imath}D_{\imath}\Bigr)\xi_{f}
+\operatorname{tr}\bigl(D_{\imath}Ξ\bigr)^{\dagger}\bigl(D_{\imath}Ξ\bigr)-V(Ξ)
+\mathcal{L}_{\mathrm{gf}}+\mathcal{L}_{\mathrm{gh}}+\mathcal{L}_{\mathrm{Yuk}} ,
$$

with one covariant derivative, $D_{\imath}=\partial_{\imath}-ig_4\sum_{a=1}^{15}A_{a,\imath}t_{a}$, and one connection coupling. **The coupling is the same $g_4$ in the representative, fermion and scalar kinetic terms**, and that identity is the whole content of the words *one force*. **The display carries seven terms and four dynamical pieces**, the other three being the fixing, the ghosts and the Yukawa. **One force does not mean one parameter**: the scalar's six coefficients $\mu_{\Phi}^{2}$, $\mu_{2}^{2}$, $\lambda_{1}$, $\lambda_{2}$, $\lambda_{3}$ and $\lambda_{4}$, the Yukawa matrix $y$, the parameter $\zeta$ and the topological angle $\theta_{4}$ are nine more numbers, and §*What the Display Does Not Contain* lists them.

*Second, the equations and the count.* The stationarity condition is $\sum_{\imath}\varepsilon_{\imath}D_{\imath}F_{a,\imath\jmath}=+g_4\,j_{a,\jmath}$, with the current built from the sixteen and the scalar matrix; the temporal component is a Gauss law per generator, fifteen in all; and the constraint algebra fixes the degrees of freedom to $15\times2$ for the connections, $32$ states for the fermions and $16$ real for the scalar.

*Third, the status, and it is the point of the article.* $\mathrm{SU}(2)$ is written *in* the algebra; $\mathrm{SU}(4)$ is written *on* it. The compact group of $\mathbb{B}$ is $\mathrm{U}(2)$, of real dimension four, and fifteen generators do not fit inside four. **So the action below is a transcription and not a derivation**, and it stands with $\mathrm{SU}(3)$ on the transcribed side of the ceiling, not with $\mathrm{SU}(2)$ on the derived side. *The Compact Sector of the Biquaternions Is $\mathfrak{u}(2)$: No $\mathfrak{su}(3)$ Among the Operators* owns the argument; this article states where its display falls in it.

What is not new. The Yang–Mills action with matter is standard, and its derivation is a page of any text. What the corpus contributes is the identification of the fifteen printed arrays with a set $t_{a}$ satisfying $\operatorname{tr}(t_{a}t_{b})=\tfrac12\delta_{ab}$ — one integer rotation and one rescaling, done in §*The Normalisation* — the trace-versus-pairing distinction, and the ceiling statement.

## Conventions

The conventions are restated so that every sign below is checkable from this page.

**The algebra and the coordinates.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with $e_t=1$ and $\vec e_{\imath}^{2}=-e_t$, $\imath=x,y,z$; the material sector is $\mathbb{B}_\Phi$, where the time coefficient is imaginary, $Q_t=iq'_t$. The coordinates are $R_{\imath}=(R_t,R_x,R_y,R_z)$, the derivatives are $\partial_{\imath}=\partial/\partial R_{\imath}$, and the measure is $d^4r$. **Every index is low and every sum carries its weight**, as in *Index and Notation Conventions*: $\sum_{\imath}\varepsilon_{\imath}$ for a spacetime contraction with $\varepsilon_{\imath}=(1,-1,-1,-1)$, and the unit metric $\delta_{\imath\jmath}$ raises nothing.

**The generators.** Two sets, and the difference between them is one factor of $i$ and one rescaling. $G_{a}$, $a=1,\dots,15$, are the printed arrays of the boson block — the twelve planes $A_{\imath\jmath}$ and $iS_{\imath\jmath}$ and the three diagonal directions $M_{j}=E_{jj}-E_{tt}$ — taken anti-Hermitian, $G_{a}^{\dagger}=-G_{a}$ and $\operatorname{tr}G_{a}=0$, with the vacuum direction $iD=i\sum_{j}M_{j}$ their sum and not a sixteenth array. $t_{a}$ are the normalised Hermitian generators of §*The Normalisation*, $t_{a}=iG_{a}/2$ for the twelve planes, $t_{j}=-A_{j}/\sqrt{8}$ for the three diagonal directions with $A_{j}=\sum_{k}M_{k}-2M_{j}$ (the printed generator there is $iA_{j}$, so the minus is the factor $i$ of the convention folded in), and $t_{15}=i(iD)/\sqrt{24}=-D/\sqrt{24}$, so that $\operatorname{tr}(t_{a}t_{b})=\tfrac12\delta_{ab}$ and every $t_{a}$ is Hermitian. **The action is written in $t_{a}$**; the printed $G_{a}$ are what the count, the trace norms and the commutation table are computed from. The cell names are the grid's, and *Classification of the Bosons* fixes them.

**The bracket.** $[G_{a},G_{b}]=\sum_{c}f^{c}_{\ ab}G_{c}$ in the printed basis, and $[t_{a},t_{b}]=i\sum_{c}F^{c}_{\ ab}t_{c}$ in the Hermitian one, with

$$
F^{c}{}_{ab}=\sqrt{\frac{n_{c}}{2\,n_{a}n_{b}}}\;f^{c}{}_{ab},\qquad
t_{a}=\frac{iG_{a}}{\sqrt{2\,n_{a}}},\qquad
n_{a}:=\operatorname{tr}\bigl(G_{a}^{\dagger}G_{a}\bigr)=2\ \text{(all fifteen)},\qquad
n_{15}=\operatorname{tr}\bigl(D^{2}\bigr)=12\ \text{(the vacuum direction, not one of the fifteen)} .
$$

**So the coefficients are not the same numbers, and the difference is two things rather than one**: the $i$, which is the Hermiticity of $t_{a}$ against the anti-Hermiticity of $G_{a}$, and the trace norm $n_{a}$, which is the normalisation. **Two instances, both checkable from the table.** For three planes $n_{c}/2n_{a}n_{b}=\tfrac14$: $[A_{tx},A_{ty}]=-A_{xy}$ has $f=-1$ and $F=-\tfrac12$. For the vacuum direction in and a plane out, $n_{c}/2n_{a}n_{b}=2/48=\tfrac{1}{24}$: $[iD,A_{tx}]=-4iS_{tx}$ has $f=-4$ and $F=-4/\sqrt{24}=-0.8165$. **The two numbers differ because the vacuum direction's norm is six times a plane's**, and the rescaling is not a relabelling: a vertex read off an $f$ is wrong by that factor. **The $i$ decides the sign structure of every vertex that touches the scalar** (§*The Scalar Piece*); **the rescaling is what turns the same vertex into a number.** The coefficients are real and antisymmetric in $a$ and $b$, read off the commutation table: of the $105$ independent pairs, $80$ brackets are nonzero, and the number of distinct index triples is $31$ in the printed basis and $29$ once the two spatial diagonals are rotated to the orthonormal pair. **They are not totally antisymmetric in all three indices as they stand**, because $d_{2}$ and $d_{3}$ are not orthogonal: total antisymmetry belongs to the lowered $f_{abc}$ and holds only in the orthonormal basis.


**The traces.** $\operatorname{tr}$ is the matrix trace on $\mathbb{B}\cong M_2(\mathbb{C})$ enlarged to the $4\times4$ matrices that represent $\mathfrak{su}(4)$; $\mathrm{Sc}$ is the coefficient of $e_t$ in an element of $\mathbb{B}$. **The two are different functionals and only the first is used in the action**, for the reason §*The Trace and Not the Reduction* gives.

**The fields.** $A_{a,\imath}$ is the connection of generator $a$, real; $F_{a,\imath\jmath}$ its field strength; $\xi_{f}$, $f=1,\dots,16$, the Weyl fields of $2\cdot\mathbf{4}\oplus2\cdot\bar{\mathbf{4}}$; $Ξ$ the scalar, a $4\times4$ Hermitian matrix in the indices and carrying no copy index, so $15+1=16$ real parameters; $\gamma_{\imath}$ the Dirac matrices, written low.

## The Display

**The pieces and what each one is for.**

| piece | field | what it supplies |
| --- | --- | --- |
| $-\tfrac14\sum F F$ | the fifteen | the propagator and both self-couplings |
| fermion kinetic | the sixteen | the fermion–connection vertex, one matrix per generator |
| scalar kinetic | $Ξ$, sixteen real | the representative–scalar vertex and the mass of the six |
| $V(Ξ)$ | $Ξ$ | the scalar self-couplings |
| $\mathcal{L}_{\mathrm{gf}}$, $\mathcal{L}_{\mathrm{gh}}$ | fifteen ghosts | the fixing the representative and ghost vertices |
| $\mathcal{L}_{\mathrm{Yuk}}$ | fermions and $Ξ$ | one matrix in the family index |

**Why the connection piece is written with $\tfrac14$ and the element form with $\tfrac12$.** The two are the same number read in two bases. With $F_{\imath\jmath}=\sum_{a}F_{a,\imath\jmath}t_{a}$, the normalised generators of §*The Normalisation* and not the printed arrays, and $\operatorname{tr}(t_{a}t_{b})=\tfrac12\delta_{ab}$,

$$
\operatorname{tr}\Bigl(\sum_{\imath,\jmath}F_{\imath\jmath}F_{\imath\jmath}\Bigr)
=\tfrac12\sum_{a,\imath,\jmath}F_{a,\imath\jmath}F_{a,\imath\jmath},
$$

so $-\tfrac12\operatorname{tr}(\sum FF)=-\tfrac14\sum_{a}FF$. **The coefficient is not a choice**: it is fixed once the generators are normalised, and the normalisation is fixed by the requirement that the kinetic term of $A_{a,\imath}$ be canonical. **Written with the printed $G_{a}$ instead, the trace norms are $2$ on the fifteen and $12$ on the vacuum direction, and the coefficient is not $\tfrac14$** — which is why every vertex in this block is read from $t_{a}$ and not from $G_{a}$.

**Why nothing else appears at dimension four.** The invariant, parity-even, dimension-four functionals of the fifteen alone are the square of the curvature and nothing else. **A cubic is excluded by dimension and not by a trace identity**: $F$ carries dimension two, so $\operatorname{tr}(F^{3})$ carries six, and $\operatorname{tr}(t_{a}t_{b}t_{c})$ does *not* vanish for $\mathrm{SU}(4)$ — it is the symmetric invariant $d_{abc}$, which is nonzero for every $N\ge3$ and vanishes only for $\mathrm{SU}(2)$, which is why the false reason is easy to believe. A term with a derivative of the curvature has dimension five. **One further term exists and is not written**: the topological density $\operatorname{tr}(\mathbb{F}\wedge\mathbb{F})$, whose integral is quantised and whose coefficient $\theta_4$ is a free parameter of the Lagrangian and not a function of the group. It is named here and left to *The $\mathrm{SU}(4)$ Instanton*, **which also shows that it is redundant above $M_C$**, where the sixteen are massless and a chiral rotation removes it. **It is also the one dimension-four term the group allows that is odd under $CP$**, and that is worth one sentence because the corpus says elsewhere that the sixteen is closed under $CP$: the closure is a statement about the field list, a $CP$ map exists and permutes it, while the Lagrangian's $CP$ is a statement about the values of the mass phases $\arg\det m$ and of the Yukawa phases, and neither is fixed by the group. **So the model can be $CP$-conserving and it is not $CP$-symmetric by construction**, and the difference is a measurement rather than a convention.

**The fermion piece in the corpus's coordinates.** The kinetic term is

$$
\mathcal{L}_{\psi}=\sum_{f}\bar\xi_{f}\Bigl(-i\sum_{\imath}\varepsilon_{\imath}\gamma_{\imath}D_{\imath}\Bigr)\xi_{f},
\qquad
D_{\imath}\xi_{f}=\partial_{\imath}\xi_{f}-ig_4\sum_{a}A_{a,\imath}\,\begin{pmatrix}t_{a}\otimes\mathbb{1}_{2}&0\\0&-t_{a}^{T}\otimes\mathbb{1}_{2}\end{pmatrix}\xi_{f},
$$

**The two blocks are the quartet half and the conjugate half.** The $8\times8$ matrix is block-diagonal on the index and tensored with $\mathbb 1_{2}$ on the copy index, so each of the fifteen acts on the sixteen components as one sign on the $\mathbf4$ and the other on the $\bar{\mathbf4}$. The $\varepsilon_{\imath}$ on the Dirac contraction is the weight the corpus prints everywhere else, and it is what makes this a Minkowski Dirac operator and not a Euclidean one. **The minus in the lower block is not a convention**: the conjugate of a $\mathbf4$ transforms with $-t_{a}^{T}$, and *The Fermion–Connection vertex in the Quartet Basis* prints the $-t_{a}^{T}$ on its conjugate half for this reason. **That minus is also what makes the anomaly cancel**: the $\mathrm{SU}(4)^3$ index is $+1$ on each quartet and $-1$ on each antiquartet, and a vertex that forgot the sign would make the index $+4$ instead of $0$.

**The copy index is untouched by every generator.** That is the one structural statement the fermion piece makes: the sixteen are $\xi^{\alpha}_{i}$ with the quartet index slow and the copy index fast, so each array acts as $X\otimes\mathbb{1}_{2}$ on the quartet half and $-X^{T}\otimes\mathbb{1}_{2}$ on the conjugate half, and the two-index rule of *The Fermion–Connection vertex in the Quartet Basis* is *recovered* here rather than assumed. **The piece contains no mass and no chirality projection**; both would need a second structure and the group supplies neither.

**The scalar piece.** With $Ξ$ a Hermitian $4\times4$ transforming as $Ξ\mapsto UΞ U^{\dagger}$,

$$
\mathcal{L}_{\Phi}=\operatorname{tr}\bigl(D_{\imath}Ξ\bigr)^{\dagger}\bigl(D_{\imath}Ξ\bigr)-V(Ξ),
\qquad
D_{\imath}Ξ=\partial_{\imath}Ξ-ig_4\sum_{a}A_{a,\imath}[t_{a},Ξ] .
$$

**The $i$ in the scalar's derivative, because this is the one place a base change silently destroys a vertex.** With $t_{a}$ Hermitian and $Ξ$ Hermitian, the commutator $[t_{a},Ξ]$ is anti-Hermitian, so $-ig_4[t_{a},Ξ]$ is Hermitian and $D_{\imath}Ξ$ is Hermitian, as the derivative of a Hermitian field must be. **The $i$ is also what makes the two orderings add**: $(DΞ)^{\dagger}(DΞ)$ expands to $\operatorname{tr}(\partialΞ)^{2}-2ig_4\operatorname{tr}(\partial_{\imath}Ξ[A_{\imath},Ξ])+g_4^{2}\operatorname{tr}([A_{\imath},Ξ])^{2}$, and the two cross terms carry the same sign because the dagger flips one of them. **The representative–scalar three-point vertex is therefore $-2ig_4\operatorname{tr}(\partial_{\imath}Ξ[A_{\imath},Ξ])$, and it is not optional.** Written instead with the anti-Hermitian $G_{a}$ and the same $i$ — which is what a careless substitution of the printed arrays does — the two orderings cancel exactly, $\operatorname{tr}(CP)=\operatorname{tr}(PC)$, and the vertex vanishes identically: **the numbers do not change, the sign of the coupling's $i$ relative to the generator's does, and the interaction disappears.** That is why the display is written in $t_{a}$.

**The commutator, because the matrix index is what the mass operator needs.** $\bar\xiΞ\xi$ is a singlet only if $Ξ$ carries one lower and one upper index, and $\bar{\mathbf4}\otimes\mathbf4=\mathbf{15}\oplus\mathbf1$ is exactly the adjoint plus the singlet. **The trace in the kinetic term is then the canonical invariant of degree two.** A second one exists — $(\partial_{\imath}\operatorname{tr}Ξ)^{2}$, the kinetic term of the trace mode alone — and one rescaling of the singlet removes it: that rescaling sets the two blocks to the same normalisation and moves only coefficients that are already free. **So the kinetic term has one physical structure and not two, and that is a statement about canonical normalisation rather than about the group.** The covariant derivative acts by commutation because that is how a generator acts on an object with one index of each kind.

**A quartet would have been cheaper and would have had no mass term.** Its derivative is $t_{a}Ξ$ with no commutator and its potential has one quartic instead of two. $\mathbf4\otimes\mathbf4=\mathbf6\oplus\mathbf{10}$ contains no $\bar{\mathbf4}$, so no $\bar\xiΞ\xi$ exists, and the sixteen would be massless at every scale with no Yukawa sector at all. **The extra structure is the price of the fermion masses**, and *The Scalar Content* records the argument in full.

**$Ξ$ carries two indices and nothing else.** The matrix is Hermitian, so sixteen real parameters: $15$ for the traceless part, which is $\dim\mathrm{SU}(4)$ and is the algebra's, and $1$ for the trace, which is not. **Nothing is multiplied**, and the sixteen of the scalar is the same kind of count as the fifteen of the vectors.

**What this costs, stated so the census and this article agree.** Sixteen real components at the scale of the display, and the eating is the restructuring's: six directions, one per broken generator of $\mathrm{SU}(4)$. **So six go and ten survive**, this article counts the phase before the eating, and *The Scalar Content* counts what the restructuring removes and what it leaves.

**The potential, written and not derived, and the field is not constrained.** The matrix carries one index of each line kind, and the trace is the only contraction available. **$Ξ$ is a general Hermitian matrix and no condition is imposed on it**: its sixteen components are sixteen components, the trace among them. **The trace is a symmetry singlet**, since $Ξ\mapsto UΞ U^{\dagger}$ leaves $\operatorname{tr}Ξ$ untouched, so no connection interaction sees it: it enters the action through the kinetic term and the potential, and through no vertex that carries a generator. **"Fifteen generators, so fifteen scalar directions" is the tempting count and it is wrong**: a generator is traceless because $\mathfrak{su}(4)$ removes the trace, and that is a statement about the algebra, not about a field. **A constraint on a field is not a convention either**, for the reason a Proca field keeps its fourth component: the condition that removes a mode is a consequence of an equation of motion, or it is nothing.

**So the potential is written on the whole matrix.**

$$
V(Ξ)=\mu_{\Phi}^{2}\operatorname{tr}Ξ^{2}+\mu_{2}^{2}\bigl(\operatorname{tr}Ξ\bigr)^{2}
+\lambda_{1}\operatorname{tr}Ξ^{4}+\lambda_{2}\bigl(\operatorname{tr}Ξ^{2}\bigr)^{2}
+\lambda_{3}\bigl(\operatorname{tr}Ξ\bigr)^{2}\operatorname{tr}Ξ^{2}+\lambda_{4}\bigl(\operatorname{tr}Ξ\bigr)^{4},
$$

and the group fixes none of the six coefficients. **Two quartics and not one in the traceless channel**, because $\operatorname{tr}(Ξ^{4})$ and $(\operatorname{tr}Ξ^{2})^{2}$ are different contractions of four matrix indices and neither is a function of the other. **A cubic $\operatorname{tr}Ξ^{3}$ is also invariant, real and allowed**, and this potential leaves it out: *The Primordial Potential* computes the threshold at which it would matter, and its absence is a truncation stated and not a symmetry. **A fifth quartic, $\operatorname{tr}Ξ^{3}\operatorname{tr}Ξ$, is allowed as well**, and it is removed by declaring the potential even in the trace; that is a second truncation of the same kind, and it is the one that keeps $\operatorname{tr}Ξ=0$ a stationary value rather than a shifted one.

**The trace has its own quadratic and its own sign, and that sign is what puts the trace at the origin.** The symmetric minimum is $\mu_{\Phi}^{2}>0$ and $\mu_{2}^{2}>0$, so $\langleΞ\rangle=0$ and the group is exact: the first sign holds the matrix at the origin, the second holds its trace there. **The broken phase is not simply the other sign of $\mu_{\Phi}^{2}$**: as *The Primordial Potential* shows, once the trace is pinned at zero the declared vacuum $\operatorname{diag}(-3,1,1,1)$ is the minimum in the branch $\lambda_{1}<0$, and the even split is the minimum in the branch $\lambda_{1}>0$. **So the vacuum is two signs and not one** — one for the shape and one for the trace — and *The Restructuring of the Primordial Force* reads the branch the corpus declares.

**What tracelessness of the vacuum is, and what it is not.** Expand along the identity, $Ξ=Ξ_{0}+c\,\mathbb 1$ with $\operatorname{tr}Ξ_{0}=0$. Every invariant is polynomial in $c$: $\operatorname{tr}Ξ=4c$, $\operatorname{tr}Ξ^{2}=\operatorname{tr}Ξ_{0}^{2}+4c^{2}$, and $\operatorname{tr}Ξ^{4}=\operatorname{tr}Ξ_{0}^{4}+4c\operatorname{tr}Ξ_{0}^{3}+6c^{2}\operatorname{tr}Ξ_{0}^{2}+4c^{4}$, so

$$
V=V(Ξ_{0})+4\lambda_{1}\langle\operatorname{tr}Ξ_{0}^{3}\rangle\,c+\Bigl(4\mu_{\Phi}^{2}+16\mu_{2}^{2}+(6\lambda_{1}+8\lambda_{2}+16\lambda_{3})\langle\operatorname{tr}Ξ_{0}^{2}\rangle\Bigr)c^{2}+4\bigl(\lambda_{1}+4\lambda_{2}+16\lambda_{3}+64\lambda_{4}\bigr)c^{4}.
$$

**The linear term is the one a one-line condition drops, and it does not vanish.** For the declared shape $\operatorname{tr}Ξ_{0}^{3}=-24v^{3}\ne0$, so $\operatorname{tr}Ξ=0$ is stationary only if $\lambda_{1}=0$ — and $\lambda_{1}<0$ is precisely the branch that shape needs. **The trace therefore settles at $c=-2\lambda_{1}\langle\operatorname{tr}Ξ_{0}^{3}\rangle/B$, with $B$ the $c^{2}$ coefficient of the display, and what has to be positive is $B$**:

$$
\mu_{\Phi}^{2}+4\mu_{2}^{2}+\Bigl(\tfrac32\lambda_{1}+2\lambda_{2}+4\lambda_{3}\Bigr)\langle\operatorname{tr}Ξ_{0}^{2}\rangle>0 .
$$

**That is not $\mu_{2}^{2}+\lambda_{3}\langle\operatorname{tr}Ξ^{2}\rangle>0$**, which deletes $\mu_{\Phi}^{2}$, $\lambda_{1}$ and $\lambda_{2}$ and rescales what is left; the shorter form is what a potential whose quartics all carry the trace would give, and this one's do not. **The one-line form in *The Primordial Potential* omits the linear term as well, and the shape that article declares is the case where it is largest.** **Tracelessness is not a condition on the field**, and the difference shows in the count: sixteen components at this scale, six eaten, ten survivors. **And the slide costs nothing in the sector**, because the identity commutes with every generator, $[\mathbb 1,t_{a}]=0$, so a shift $\Xi_{0}\mapsto\Xi_{0}+c\,\mathbb 1$ leaves the mass matrix $[\Xi_{0},[\Xi_{0},\cdot\,]]$ unchanged: the same $32v^{2}$, the same nine massless, the same six eaten. **So the vacuum is traceless to leading order and not exactly.** The identity is invisible to the force and visible only to the scalar potential, which is why the corpus's numbers survive the correction untouched.

**This is the one place where the article writes coefficients the group does not supply, and it says so**: the scalar census refuses the potential on purpose, and the refusal is correct at that article's scope.

### Two Quartics and Not One, and the Three the Trace Adds

**The count is a count of contractions, and it is the price of the matrix index.**

| scalar | degree-two invariants | degree-three | degree-four invariants | quartics |
|---|---|---|---|---|
| the quartet $\mathbf4$ | $1$ | $0$ | $1$ | $1$ |
| the traceless matrix $\mathbf{15}$ | $1$ | $1$ | $2$ | $2$ |
| the Hermitian matrix $\mathbf{15}\oplus\mathbf1$ | $2$ | $3$ | $5$ | $5$ |

**The row that matters is the last, because the field is the whole matrix, and a matrix has two ways to contract four indices where a vector has one.** $\operatorname{tr}(Ξ^{2})^{2}$ pairs the indices within each pair, $(\operatorname{tr}Ξ^{2})^{2}$ pairs them across, and the difference between the two is a genuine deformation of the potential's shape. **A vector cannot tell the two apart**, which is why the quartet reading had one quartic and looked economical. **Keeping the trace adds one quadratic, two cubics and three quartics**: $(\operatorname{tr}Ξ)^{2}$; $(\operatorname{tr}Ξ)^{3}$ and $\operatorname{tr}Ξ^{2}\operatorname{tr}Ξ$; then $(\operatorname{tr}Ξ)^{2}\operatorname{tr}Ξ^{2}$, $(\operatorname{tr}Ξ)^{4}$ and $\operatorname{tr}Ξ^{3}\operatorname{tr}Ξ$. **The display writes four of the five quartics and sets the last to zero**: $\operatorname{tr}Ξ^{3}\operatorname{tr}Ξ$ is the only one that needs an odd power of the matrix, and the potential here uses $Ξ$ only through $Ξ^{2}$ and $\operatorname{tr}Ξ$. **That is a declared choice of coefficients and not a symmetry the group supplies**; two of the four written carry the trace, and that is the honest price of a field that is not constrained.

**What the second term of that pair buys.** It is what allows a minimum whose direction is not decided by the quadratic term alone, so the vacuum's *shape* — in particular whether the traceless part of $Ξ$ is a rank-one projector and not a multiple of the identity — is a dynamical question rather than a declared one. **The corpus's vacuum is that shape**, $Ξ\propto D$ with $D=\operatorname{diag}(-3,1,1,1)$, which is $-4$ times the traceless part of the rank-one projector $\operatorname{diag}(1,0,0,0)$. **The matrix is not itself rank one** — it is invertible, with four nonzero eigenvalues — and it is the traceless part alone that the two quartics see.

**What it costs.** Six free numbers in a block whose virtue is that it has one coupling. **The sector has one parameter and the scalar sector has six**, and the asymmetry is not a defect of the writing: it is the number of invariants a matrix admits once no condition is put on it.

**The fixing the representative and ghost pieces.** $\mathcal{L}_{\mathrm{gf}}=-\tfrac{1}{2\zeta}\sum_{a}\bigl(\sum_{\imath}\varepsilon_{\imath}\partial_{\imath}A_{a,\imath}\bigr)^{2}$ with one parameter $\zeta$ for the whole group, and $\mathcal{L}_{\mathrm{gh}}=\sum_{a}\bar c_{a}\bigl(-\sum_{\imath}\varepsilon_{\imath}\partial_{\imath}D_{\imath}\bigr)c_{a}$ with fifteen ghosts in the adjoint. **One parameter and not four**, which is the difference between this block and the electroweak one: there the four factors each carried a parameter and the mixing made them unequal.

**The Yukawa piece, named and not written.** One contraction of the matrix and one matrix in the copy index,

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

**There is exactly one invariant contraction, and it uses all sixteen components.** Write it as $\bar\xi^{\alpha}\,Ξ\,\xi^{\beta}$ with $\alpha,\beta$ the copy index. **The matrix $Ξ$ is not irreducible — it is $\mathbf{15}\oplus\mathbf1$ — so the same contraction can be read in two channels**,

$$
\bar\xi\,Ξ\,\xi=\bar\xi\,Ξ_{15}\,\xi+\bar\xi\,Ξ_{1}\,\xi,
\qquad
Ξ_{15}=Ξ-\tfrac14(\operatorname{tr}Ξ)\,\mathbb 1,
\qquad
Ξ_{1}=\tfrac14(\operatorname{tr}Ξ)\,\mathbb 1 .
$$

**Each channel is an independent invariant, so the ledger could carry two coefficients; it carries one**, the matrix $y_{\alpha\beta}$ of the display above. **That is a choice as much as a count.** The trace channel is dropped because it vanishes on the condensate — see the next paragraph — so **no mass, no mixing and no mass relation can depend on a coefficient multiplying it**; what it would change is the coupling of the fluctuation $\delta\operatorname{tr}Ξ$ to a fermion pair, and nothing in the corpus uses that coupling. **A second coefficient with no consequence in the spectrum is a footnote and not a term**, which is why it is not written.

**Where the mass then comes from is a sharper statement, and it is the one the rest of the block uses.** The vacuum is $Ξ_0=vD$ with

$$
\operatorname{tr}D=-3+1+1+1=0 ,
$$

**so the trace channel vanishes at the minimum and the whole mass matrix is the traceless channel's**,

$$
M_{\imath\jmath}=y\,v\,D_{\imath}\delta_{\imath\jmath},
$$

which is the matrix *The Yukawa Sector* diagonalises, and which gives $m_\ell=3m_q$ within a copy. **A reader who takes "only the trace part contributes" literally gets $\operatorname{tr}D=0$ and therefore massless fermions**, which is the one reading of this section that the arithmetic forbids.

**What a quartet would have given.** Nothing: $\mathbf4\otimes\mathbf4=\mathbf6\oplus\mathbf{10}$, and neither term contains a $\bar{\mathbf4}$, so the product $\bar{\mathbf4}\otimes\mathbf4\otimes\mathbf4$ has no singlet. **The table in §*The Scalar Content* is the whole argument**, and it is the reason the matrix reading is the model's.

**What the fermion copy index adds.** $y_{\alpha\beta}$ is a $2\times2$ matrix on the two Weyl fields that share a index, so the pair is mixed by the Yukawa and not by the sector. **Two eigenvalues, one diagonalisation, and the condensate's two entries $(-3v_C,+v_C)$ multiplying them**, which is the arithmetic of the mass relation and belongs to the article that computes it.

## The Normalisation, and Why the Frame Is Sheared

**The printed arrays are anti-Hermitian, and in the symmetric frame every one of the fifteen has the same trace norm.**

| family | arrays | $\operatorname{tr}\bigl(G^{\dagger}G\bigr)$ | $\operatorname{tr}\bigl(G^{2}\bigr)$ |
| --- | --- | --- | --- |
| the twelve planes, $A_{\imath\jmath}$ and $iS_{\imath\jmath}$ | $12$ | $2$ | $-2$ |
| the three frame directions $M_{j}=E_{jj}-E_{tt}$ | $3$ | $2$ | $-2$ |
| the sum $iD=i\sum_{j}M_{j}$ | not among the fifteen | $12$ | $-12$ |

**The one defect of the frame is obliqueness, and it is the price of the symmetry.** $\operatorname{tr}(M_{j}M_{k})=2\delta_{jk}+(1-\delta_{jk})$, so the three directions are at $60^{\circ}$ to one another and the Gram of the fifteen has eigenvalues twelve copies of $2$, one $4$ on the sum direction and $1$ twice. **The fifteen are a basis and not an orthonormal frame**, for a reason of the basis and not of the group: the permutation of $x,y,z$ cannot fix an orthogonal triple, because an orthogonal triple in this space is a triple of differences and any two of them share the sum direction.

**The repair is one integer rotation and one rescaling.**
$$
A_{j}=\sum_{k}M_{k}-2M_{j},\qquad
\operatorname{tr}\bigl(A_{j}A_{k}\bigr)=4\delta_{jk},\qquad
A_{j}=W_{jj},
$$
**which is the orthogonal sibling of the frame, obtained by the invertible integer matrix $J-2\mathbb 1$.** A canonical kinetic term $\operatorname{tr}(t_{a}t_{b})=\tfrac12\delta_{ab}$ then fixes
$$
t_{a}=\frac{iG_{a}}{2}\ \ (12\ \text{planes}),\qquad
t_{j}=-\frac{A_{j}}{\sqrt{8}}\ \ (3\ \text{diagonal directions}),\qquad
t_{15}=\frac{i(iD)}{\sqrt{24}}=-\frac{D}{\sqrt{24}}\ \ (\text{the vacuum direction, not a fourth diagonal}).
$$
**The last of the three is a direction and not a sixteenth array.** $A_{x}+A_{y}+A_{z}=D$, so
$$
t_{15}=-\frac{D}{\sqrt{24}}=-\frac{t_{x}+t_{y}+t_{z}}{\sqrt3},
$$
**a combination of the three frame directions, normalised to $\operatorname{tr}(t_{15}^{2})=\tfrac12$.** The fifteen are the twelve planes and the three $A_{j}$; the label $t_{15}$ is kept because the vacuum direction is what the potential and every mass term are written along. **A display that lists the three frame directions and the sum as four items has sixteen arrays and fifteen generators**, and no normalisation can repair a count.

**Check.** For a plane, $\operatorname{tr}(t_{a}t_{a})=-\tfrac14(-2)=\tfrac12$; for a frame direction, $\operatorname{tr}(t_{j}t_{j})=\tfrac{1}{8}\cdot 4=\tfrac12$; for the sum, $\operatorname{tr}(t_{15}t_{15})=\tfrac{12}{24}=\tfrac12$. **Both families of generators give one half, and so does the normalized sum, which is the statement that the normalisation succeeds — and it succeeds with three coefficients, not two, as before.** **What the frame buys is that the diagonal coefficient is one number instead of two**: the old basis needed $c_{3}=d_{2}-d_{3}$ with a norm of its own, and the symmetric frame needs only the single integer rotation $A_{j}$.

**The $1/\sqrt6$ is the sum's, and it does not move.** $\sqrt{12/2}=\sqrt6$: the vacuum direction is longer than a plane by that factor, because its entries are $-3$ and $1$ where a plane's are $\pm1$. **That is a property of $D$ and not of the frame**, so a vertex that touches $B'$ and is read off the printed arrays carries the same $1/\sqrt6$ as before, and the change of diagonal basis leaves it untouched. **The factor is a conversion and not a coupling**: in the normalised $t_{a}$ every generator has $\operatorname{tr}(t^{2})=\tfrac12$, the vacuum direction among them, so a vertex written in $t_{a}$ carries no $\sqrt6$ anywhere; the $1/\sqrt6$ appears exactly when a vertex is read off the printed arrays $G_{a}$, where the sum has trace norm $12$ against a plane's $2$, and it goes in the direction that divides.

**Why the rescaling is not cosmetic.** A vertex read off a printed array is off by this factor, and a cross section read off a vertex is off by its square. **The factor is stated once, here, so that the articles that print a vertex restate it rather than re-derive it.**

### The Trace and Not the Reduction

**The density must be invariant under $\mathbb{F}_{\imath\jmath}\mapsto U\mathbb{F}_{\imath\jmath}U^{-1}$**, and only the cyclicity of the matrix trace gives that in one line:

$$
\operatorname{tr}\Bigl(\sum_{\imath,\jmath}U\mathbb{F}_{\imath\jmath}U^{-1}U\mathbb{F}_{\imath\jmath}U^{-1}\Bigr)
=\operatorname{tr}\Bigl(\sum_{\imath,\jmath}\mathbb{F}_{\imath\jmath}\mathbb{F}_{\imath\jmath}\Bigr).
$$

**The corpus's informational reduction does not have that property.** $2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2)$ is bilinear, symmetric and real on the material sector, but it is not cyclic, so a density built from it would change under a local transformation and the theory would not be a connection theory. **The two functionals agree only where one factor is a scalar**, and a field strength is not a scalar. The proof is *The Lagrangian and the Non-Abelian Connections*'s; it is cited here rather than repeated, and it is the sharpest technical statement in either article.

**Reality and sign.** For anti-Hermitian $\mathbb{F}_{\imath\jmath}$, $\operatorname{tr}(\mathbb{F}_{\imath\jmath}\mathbb{F}_{\imath\jmath})$ is real, and $\operatorname{tr}(\mathbb{F}_{\imath\jmath}^{\dagger}\mathbb{F}_{\imath\jmath})=-\operatorname{tr}(\mathbb{F}^{2})$ is non-negative. **Reality is what the anti-Hermiticity buys, and that much is not a convention.** **Positivity is a different statement and it belongs to the Hamiltonian, not to the Lagrangian**: the density $-\tfrac12\operatorname{tr}(\sum\mathbb{F}\mathbb{F})$ is $\tfrac12\sum_{a}(E_{a}^{2}-B_{a}^{2})$ once the corpus's weights are applied to the summed pairs, so it changes sign between an electric and a magnetic configuration. **The energy that is bounded below is $\tfrac12\sum_{a}(E_{a}^{2}+B_{a}^{2})\ge0$**, and it is positive for the same reason.

## The Variation: One Equation and Fifteen Gauss Laws

**The curvature's variation is the covariant derivative of the variation**, $\delta\mathbb{F}_{\imath\jmath}=D_{\imath}\delta\mathbb{A}_{\jmath}-D_{\jmath}\delta\mathbb{A}_{\imath}$, so stationarity of the connection piece alone gives $D_{\imath}F_{\imath\jmath}=0$. With the matter pieces present,

$$
\sum_{\imath}\varepsilon_{\imath}D_{\imath}F_{a,\imath\jmath}=+g_4\Bigl(\sum_{f}\bar\xi_{f}\,\gamma_{\jmath}\,t_{a}\,\xi_{f}+2i\operatorname{tr}\bigl(\bigl(D_{\jmath}Ξ\bigr)\bigl[t_{a},Ξ\bigr]\bigr)\Bigr),
$$

**The fermion term is a vector current and the scalar term is bilinear in $Ξ$.** Three things about that line are worth stating, because each is easy to lose in a display assembled from parts.

**One $g_4$ and one sign, and the sign is plus.** Both terms come from the same variation of the same action, so both carry one power of $g_4$ and the same sign; factoring the $g_4$ out, $\sum_{\imath}\varepsilon_{\imath}D_{\imath}F_{a,\imath\jmath}=+g_4\,j_{a,\jmath}$ with $j$ the bracket, **is the same equation and the form the strong sector prints**. **The plus is what the weighted variation gives**: $\delta S_g/\delta A_{a,\nu}=\varepsilon_{\nu}\sum_{\imath}\varepsilon_{\imath}D_{\imath}F_{a,\imath\nu}$ and $\delta S_\Phi/\delta A_{a,\nu}=-2ig_4\varepsilon_{\nu}\operatorname{tr}((D_{\nu}Ξ)[t_{a},Ξ])$, so the two $\varepsilon_{\nu}$ cancel, the minus stays on the matter side, and **moving it across the equation is where the plus comes from**. A display that keeps a minus on the right has let one of the two $\varepsilon_{\nu}$ go. **The sibling article on the scalar matrix writes the same equation with $g_4$ inside $j$**, $\sum_{\imath}\varepsilon_{\imath}D_{\imath}F_{a,t\imath}=-2ig_4\operatorname{tr}((D_{t}Ξ)[t_{a},Ξ])$, **and the two agree because $F_{t\imath}=-F_{\imath t}$**: moving the index order across the equation flips the left side and the current together, so neither version is a different theory and a reader who compares the two without the index order will find a sign that is not there.

**One $\varepsilon$ per contraction.** The $\varepsilon_{\jmath}$ on the left is the weight of the contracted derivative; the current carries a lower index and no $\varepsilon$ of its own. **The fermion bilinear is therefore $\sum_{f}\bar\xi_{f}\gamma_{\jmath}t_{a}\xi_{f}$ and not $\sum_{f}\bar\xi_{f}\varepsilon_{\jmath}\gamma_{\jmath}t_{a}\xi_{f}$**, and the two differ by a sign on the three spatial components while agreeing on the temporal one — **which is why a stray $\varepsilon$ there survives every check of the Gauss law and shows up only in the current's spatial part.**

**The factor two is the commutator's two orderings.** The scalar term is $\partial\mathcal{L}_{\Phi}/\partial A_{a,\jmath}=-2ig_4\operatorname{tr}((D_{\jmath}Ξ)[t_{a},Ξ])$: the $2$ is $\{D_{\jmath}Ξ,[t_{a},Ξ]\}$ against the trace, and the $i$ is what makes the two orderings add rather than cancel (§*The Scalar Piece*). **Deleting either is not a normalisation choice**; the factor multiplies the three-point vertex, so a cross section moves by four.

**The copy index is not summed.** $t_{a}$ acts on the index alone, so the fermion bilinear carries one $t_{a}$ and no trace over the copy index; **an index that appears nowhere cannot be summed**, and a $\sum_{\alpha=1}^{2}$ in front of a trace over the spatial block is an index that appears nowhere.

**The scalar current is quadratic above $M_C$ and linear below it**, and that shift is the whole mechanism of the mass: with $Ξ=v+\delta Ξ$ the current splits into a piece in the fluctuation $\delta Ξ$ and a piece in $\delta Ξ\,\delta Ξ$, and the first is the $A$–$\delta Ξ$ mixing that a mass term is. Above the restructuring only the second piece is present, so no one-scalar emission exists and every direction stays massless — which is why the unbroken phase has no mass term and needs none.

**The current is covariantly conserved.** Local invariance of the matter action makes $\sum_{\imath}\varepsilon_{\imath}D_{\imath}j_{\imath}$ vanish once the matter fields are on shell, so the conservation is a consequence of the invariance and not a further condition. **The ordinary divergence $\sum_{\imath}\varepsilon_{\imath}\partial_{\imath}j_{\imath}$ is not zero**, because it carries the $[A_{\imath},j_{\imath}]$ term. **So no symmetry charge exists**, exactly as in the strong sector: the charge is defined only for the residual $\mathrm{SU}(3)\times\mathrm{U}(1)$ below $M_C$, and above it there is a current and no charge.

**The temporal component of the equation is not an equation of motion but a constraint.** $\sum_{\imath}\varepsilon_{\imath}D_{\imath}F_{a,\imath t}=+g_{4}j_{a,t}$ contains no second time derivative of $A_{a,t}$, so it fixes $A_{a,t}$ in terms of the other fields: **a Gauss law per generator, fifteen in all.** Each is first class, so each removes two degrees of freedom from a four-component field, and the count is

$$
4\times15\ \longrightarrow\ 2\times15=30
$$

for the connections, before fixing the representative and with the ghosts counted separately.

**The count, side by side.**

| field | components | on shell |
| --- | --- | --- |
| the fifteen $A_{a,\imath}$ | $4\times15=60$ | $30$ |
| the sixteen $\xi_{f}$ | $4\times16=64$ real (two complex components each) | $32$ states |
| $Ξ$ | $15+1=16$ real | $16$ real |
| the ghosts $c_{a}$, $\bar c_{a}$ | $2\times15$ | $0$, loops only |

**The ghosts are not asymptotic states, and counting them again subtracts the vectors twice.** The ghosts restore unitarity in loops and contribute nothing on shell, exactly as in the strong sector; **a row that reads $-2\times15$ against the already-reduced $30$ leaves no vector state at all.** The on-shell total of this phase is therefore

$$
30+32+16=78 ,
$$

and the count is a statement about this phase only.

**The scalar's sixteen are all physical in this phase**, because no direction has been eaten: the eating is the restructuring's and it leaves ten. **That is the arithmetic the two articles divide between them** — this one counts the phase, *The Scalar Content* counts what the restructuring removes.

## The Ceiling: Transcription and Not Derivation

**The action above is correct as a Yang–Mills action for $\mathrm{SU}(4)$. It is not an algebra result, and the difference is measurable.**

The dimension of the algebra's compact group is four. $\mathbb{B}\cong M_2(\mathbb{C})$ has compact part $\mathrm{U}(2)=\mathrm{SU}(2)\times\mathrm{U}(1)$, of real dimension $3+1=4$, and a Lie algebra of fifteen generators does not embed in a four-dimensional one. **The $\mathrm{SU}(2)$ action of *The Lagrangian and the Non-Abelian Connections* is written in the algebra because its three generators are three of the algebra's own directions.** **The fifteen are not elements of $\mathbb{B}$ at all**: $\mathbb{B}\cong M_{2}(\mathbb{C})$ holds $2\times2$ matrices and these are $4\times4$, so what the algebra fails to contain is the *representation* and not the algebra — $\mathfrak{su}(4)$ is realised on $\mathbb{C}^{4}$, a realisation is a choice, and the choice is one $\mathbb{B}$ cannot make. **The action is written on that representation.**

**What transcription costs, item by item.**

- *The trace.* The invariant density needs a cyclic trace on $\mathbb{C}^{4}$. The algebra supplies one on $\mathbb{C}^{2}$; the enlargement to $\mathbb{C}^{4}$ is a choice of representation, and the fifteen arrays are its matrices.
- *The curl and the cross product.* In the algebra the $\mathrm{SU}(2)$ bracket is the algebra's own product. Here the coefficients are read off a table of $105$ pairs, and the $80$ nonzero brackets among them — $84$ in the symmetric frame, and §*The Checks* says which count belongs to which frame — are the structure constants.
- *The invariant density of the algebra.* $2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2)$ exists on every element of $\mathbb{B}$ and is not available for this action, because it is not cyclic. **So the one pairing the algebra owns is exactly the one the action cannot use**, and this is the precise sense in which the primordial force is transcribed.

**What transcription does not cost.** The group's content, its representation theory, its anomaly arithmetic and its mass spectrum are all exact. **The three species of statement must be kept apart**: the identity $2\cdot\mathbf{4}\oplus2\cdot\bar{\mathbf{4}}$ is algebra; the matrices $t_{a}$ are a representation; the action is a transcription. Nothing in the block is stronger than the second.

## What Is Not Claimed

**Four statements this article does not make, the ones a hostile reader would supply if it were silent.**

- *Not a derivation of the group, nor of the representation.* $\mathrm{SU}(4)$ is transcribed and nothing here selects fifteen over another count; the $\mathbf4$ and its conjugate are chosen, and a different carrier gives a different vertex table and the same structure.
- *Not a derivation of the six potential coefficients, nor of the Yukawa's entries*; the vacuum's tracelessness is a consequence to leading order, the shift along the identity is of order $\lambda_{1}v^{3}/\mu_{2}^{2}$ (§*The Display*), and neither number is computed here.
- *Not a claim that the bracket counts are properties of the group*: $80$ and $84$, $29$ and $31$, are counts in frames, and a count quoted without its frame has quoted nothing.
- *Not an identification with a measured multiplet, and not a quantum statement*: no particle is placed in a representation here, the masses are *The Yukawa Sector*'s, the running is another article's, and no number on this page is renormalised.

**What would count against it**: a vertex computed from the printed arrays that disagrees with the normalised one by anything other than the stated $\sqrt6$; a bracket count that depends on the frame in a way §*The Checks* denies; a scalar spectrum at the restructuring that lacks the $32v^{2}$ pattern the mass matrix gives.

## What the Display Does Not Contain

**Six absences, each deliberate.**

- *No mass for the fifteen.* A mass term $\tfrac12m^{2}\sum_{a,\imath}A_{a,\imath}A_{a,\imath}$ is not invariant, and none is written. The masses come from $\langleΞ\rangle$ and are the restructuring's.
- *No potential coefficients.* $\mu_{\Phi}^{2}$, $\mu_{2}^{2}$ and the four quartics are the six parameters the group does not fix.
- *No Yukawa value.* One matrix, its entries free, its spectrum measured.
- *No value of $g_4$.* The coupling multiplies the action and does not cancel from the equation, because the commutator carries one power of it and the derivative none; but its value is a boundary condition taken from below, and *The Primordial Coupling* owns it.
- *No loop.* The running, the anomalous dimensions and the effective potential are one-loop objects and the classical action says nothing about them.
- *No $\theta_4$.* The topological term is admitted by the group, is not written in the display, and its coefficient is free in the Lagrangian.

## The Checks

**Fourteen rows, each recomputed from the printed arrays and not quoted.**

| statement | value |
| --- | --- |
| $\operatorname{tr}\bigl(G^{\dagger}G\bigr)$ for a plane | $2$ |
| $\operatorname{tr}\bigl(G^{\dagger}G\bigr)$ for the twelve planes and the three frame directions | $2$ on all fifteen |
| $\operatorname{tr}\bigl(D^{2}\bigr)$ for $D=M_x+M_y+M_z$ | $12$ |
| $\operatorname{tr}(M_{j}M_{k})$, the three nonzero off-diagonals of the Gram | $2\delta_{jk}+(1-\delta_{jk})$ |
| $\operatorname{tr}(A_{j}A_{k})$ with $A_{j}=\sum_kM_k-2M_j$ | $4\delta_{jk}$ |
| $\operatorname{tr}(A_{j}A_{k})-\bigl[\text{the same in }M\bigr]$ | $3\delta_{jk}-1=3\mathbb 1-J$, singular along the sum; the rotation itself is $A=(J-2\mathbb 1)M$, invertible |
| $\operatorname{tr}(t_{a}t_{a})$ for a plane, $t_{a}=iG_{a}/2$ | $\tfrac12$ |
| $\operatorname{tr}(t_{j}t_{j})$ for a frame direction, $t_{j}=-A_{j}/\sqrt{8}$ | $\tfrac12$ |
| $\operatorname{tr}(t_{15}t_{15})$ for the vacuum direction, $t_{15}=-D/\sqrt{24}=(t_{x}+t_{y}+t_{z})/\sqrt3$ | $\tfrac12$, and it is a combination of the three, not a sixteenth array |
| nonzero brackets of the fifteen | $84$ of $105$ in the $M$ frame, $80$ in the frame of the two differences and the sum |
| distinct nonzero triples $\{a,b,c\}$ | $31$ in the $M$ frame, $29$ in the frame of the two differences and the sum |
| $[A_{tx},A_{ty}]=-A_{xy}$ in both bases | $f=-1$, $F^{c}_{\ ab}=-\tfrac12$ |
| $[iD,A_{tx}]=-4iS_{tx}$ in both bases | $f=-4$, $F^{c}_{\ ab}=-4/\sqrt{24}=-0.8165$ |
| $F^{c}_{\ ab}$ against $\sqrt{n_{c}/2n_{a}n_{b}}\,f^{c}_{\ ab}$, every bracket | worst error $0$ |

**The normalisation is what makes the display's coefficient $\tfrac14$ and not a parameter**, and the vacuum direction's length is what makes the ratio $1/\sqrt6$ appear in every vertex that touches $B'$.

## Summary

The $\mathrm{SU}(4)$ Lagrangian is one coupling on fifteen generators and seven terms: the curvature's square, the sixteen's kinetic term, the scalar matrix's kinetic term and its potential, and the fixing the representative, ghost and Yukawa pieces. **One $g_4$ enters the curvature and both covariant derivatives**, and that identity, not any vertex, is what the words *one force* mean. **The other nine numbers — $\mu_{\Phi}^{2}$, $\mu_{2}^{2}$, the four quartics, $y$, $\zeta$ and $\theta_{4}$ — are parameters and not the couplings of a second and third force.** **The scalar sector's six are the price of a field that carries no condition**: the trace adds one quadratic and two quartics, and the identity part of the vacuum is invisible to the force, so none of the masses moves.

The normalisation is one integer rotation and one rescaling. The printed fifteen fail to be orthogonal in the three diagonal directions, $\operatorname{tr}(M_{j}M_{k})=2\delta_{jk}+(1-\delta_{jk})$; the rotation $A_{j}=\sum_{k}M_{k}-2M_{j}$ repairs it, with norm $4$; and $t_{a}=iG_{a}/2$, $t_{j}=i(iA_{j})/\sqrt{8}=-A_{j}/\sqrt{8}$, $t_{15}=i(iD)/\sqrt{24}=-D/\sqrt{24}$ then give $\operatorname{tr}(t_{a}t_{b})=\tfrac12\delta_{ab}$ on the fifteen — the twelve planes and the three $A_{j}$ — and $t_{15}=(t_{x}+t_{y}+t_{z})/\sqrt3$ is the normalised sum direction, a combination of the three and not a sixteenth generator. The vacuum direction is longer than a plane by $\sqrt6$, so a vertex that touches $B'$ and is read off the printed arrays carries the factor $1/\sqrt6$; **in the normalised $t_{a}$ there is no such factor**, and the $\sqrt6$ comes from the trace and not from the group.

The variation gives one equation and fifteen constraints. $D_{\imath}F_{a,\imath\jmath}=+g_4j_{a,\jmath}$ with a fermion term and a scalar term, the scalar one vanishing at $\langleΞ\rangle=0$; the temporal component is a Gauss law per generator; thirty degrees of freedom survive for the connections, thirty-two states for the fermions and sixteen real for the scalar, and **the ghosts contribute nothing on shell, so the total is seventy-eight.**

The trace is the matrix trace and not the informational reduction. Only cyclicity makes the density invariant, $2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2)$ is not cyclic, and the two agree only where one factor is a scalar. **This is the sharpest technical point of the article**: the one pairing the algebra owns is the one the action cannot use.

The status is transcription. The algebra's compact group is four-dimensional and the group has fifteen generators, so the action is written on a $4\times4$ representation and not in the algebra. $\mathrm{SU}(4)$ stands with $\mathrm{SU}(3)$ on the transcribed side of the ceiling; only $\mathrm{SU}(2)$, and its abelian factor, stand on the derived side.

Six things are deliberately absent: a mass for the fifteen, the potential's coefficients, the Yukawa's value, the value of $g_4$, every loop, and $\theta_4$. Each absence is a place where another article of the block begins.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A_{a,\imath}$, $F_{a,\imath\jmath}$ | Connection and field strength of generator $a$, $a=1,\dots,15$ |
| $g_4$ | The primordial coupling, one value for the whole group |
| $G_{a}$, $t_{a}$ | The printed anti-Hermitian array, and its rescaled form with $\operatorname{tr}(t_{a}t_{b})=\tfrac12\delta_{ab}$ |
| $G_{a}$ | The printed anti-Hermitian array; the action is written in $t_{a}=iG_{a}/2$, $t_{j}=-A_{j}/\sqrt{8}$, $t_{15}=-D/\sqrt{24}$ |
| $M_{j}=E_{jj}-E_{tt}$ | the three diagonal generators, the symmetric frame, $\operatorname{tr}(M_jM_k)=2\delta_{jk}+(1-\delta_{jk})$ |
| $A_{j}=\sum_kM_k-2M_j$ | the orthogonal sibling, $\operatorname{tr}(A_jA_k)=4\delta_{jk}$ |
| $d_{2}$, $d_{3}$ | the broken phase's two spatial differences, $\tfrac12(M_x-M_y)$ and $\tfrac12(M_y-M_z)$ |
| $iD$ | The vacuum direction, $\operatorname{diag}(-3i,i,i,i)=i\sum_{j}M_{j}$, trace norm $12$; its normalised form is $t_{15}=-D/\sqrt{24}=(t_{x}+t_{y}+t_{z})/\sqrt3$, a combination of the three, not a generator |
| $f^{c}_{\ ab}$ | Structure constants, $[G_{a},G_{b}]=\sum_{c}f^{c}_{\ ab}G_{c}$ and $[t_{a},t_{b}]=i\sum_{c}f^{c}_{\ ab}t_{c}$ |
| $\xi_{f}$, $\bar\xi_{f}$ | The sixteen Weyl fields, $f=1,\dots,16$ |
| $Ξ$ | The scalar, a Hermitian $4\times4$, $16$ real components |
| $V(Ξ)$ | $\mu_{\Phi}^{2}\operatorname{tr}Ξ^{2}+\mu_{2}^{2}(\operatorname{tr}Ξ)^{2}+\lambda_{1}\operatorname{tr}Ξ^{4}+\lambda_{2}(\operatorname{tr}Ξ^{2})^{2}+\lambda_{3}(\operatorname{tr}Ξ)^{2}\operatorname{tr}Ξ^{2}+\lambda_{4}(\operatorname{tr}Ξ)^{4}$, six free coefficients |
| $\mu_{2}^{2}$ | the coefficient of $(\operatorname{tr}Ξ)^{2}$; positive, and that sign is what puts the trace at the origin to leading order |
| $y_{\alpha\beta}$ | The Yukawa matrix in the family index |
| $j_{a,\jmath}$ | The total current: a fermion term and a scalar term |
| $\zeta$ | The one parameter of the group |
| $c_{a}$, $\bar c_{a}$ | The fifteen ghosts in the adjoint |
| $\theta_4$ | The coefficient of $\operatorname{tr}(\mathbb{F}\wedge\mathbb{F})$, free in the Lagrangian, not written; redundant above $M_C$ where the sixteen are massless |
| $\mathbb{F}_{\imath\jmath}$ | The element form, $\sum_{a}F_{a,\imath\jmath}G_{a}$, anti-Hermitian; the same combination in $t_{a}$ is Hermitian |
| $\operatorname{tr}$ | The matrix trace; not the informational reduction $2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2)$ |
| $d^4r$ | The measure; coordinates $R_{\imath}$, all indices low |

## Further Reading

- [The Yang–Mills Equation in Biquaternionic Form](the-yang-mills-equation-in-biquaternionic-form.html). The parent: the $\mathrm{SU}(2)$ action, the trace-versus-reduction proof, and the ceiling in its original form.
- [The Feynman Rules of the Model: The Vertices of the Fifteen and the Sixteen](the-feynman-rules-of-the-su4-model-the-vertices-of-the-fifteen-and-the-sixteen.html). The rules this action produces, and the normalisation stated once more before any rule.
- [The $\mathrm{SU}(4)$ Model: Four Lines, Fifteen Generators, One Declaration of Rank Three](the-su4-model-four-lines-fifteen-generators-one-declaration.html). The content, the anomaly count and the one covariant derivative that this article writes an action for.
- [Classification of the Bosons: Nine Massless and Six Heavy](classification-of-the-bosons-in-the-su4-model-one-grid-fifteen-generators-nine-massless-six-heavy.html). The grid, the cell names, and which of the fifteen is which.
- [The Fifteen AXF Matrices of the Bosons in Detail](the-15-axf-matrices-of-the-bosons-in-detail.html). The printed entries from which the trace norms of §*The Normalisation* were recomputed.
- [The Commutation Table of the Fifteen Generators](the-commutation-table-of-the-fifteen-generators-225-entries-105-independent-80-nonzero-and-five-rules.html). The $105$ pairs, the $80$ nonzero brackets and the triples they fall into.
- [The Scalar Content](the-scalar-content-one-matrix-and-ten-survivors.html). The census that counts the sixteen and refuses the potential this article writes.
- [The Fermion–Connection Vertex in the Quartet Basis](the-fermion-connection-vertex-in-the-quartet-basis-the-fifteen-read-on-the-sixteen.html). The two-index rule that §*The Display* recovers from the copy index.
- [The Restructuring of the Primordial Force and the Mass of the Six Leptoquarks](the-breaking-of-the-primordial-force-and-the-mass-of-the-six-leptoquarks.html). The other sign of $\mu_{\Phi}^{2}$, where the potential's minimum moves off the origin.
- [The Compact Sector of the Biquaternions Is $\mathfrak{u}(2)$](the-compact-sector-of-the-biquaternions-is-u2.html). The dimension bound that makes §*The Ceiling* a statement about the algebra.
- [The Lagrangian and the Quantum Chromodynamics: The Triplet, the Octet and the Feynman Rules](the-lagrangian-and-quantum-chromodynamics-the-triplet-the-octet-and-the-feynman-rules.html). The same construction for three lines, transcribed as this one is, with the $R$ ratio and the group factors that the primordial block has no analogue of.
