# __The Spectral Triple of the Biquaternion Algebra__

## Introduction

A spectral triple is a triple $(\mathcal{A},\mathcal{H},D)$ consisting of an algebra $\mathcal{A}$ represented on a Hilbert space $\mathcal{H}$ together with a self-adjoint operator $D$ whose resolvent is compact and whose commutators with the algebra are bounded. The triple is the object from which Connes' non-commutative geometry recovers the data of a Riemannian spin manifold: the algebra generalises the functions, the Hilbert space generalises the spinors, and the Dirac operator generalises both the metric and the differential structure. Two consequences of the definition are worth stating at once, because they are the reason the construction is of interest to this series: the **distance** on the state space is recovered from $D$ by a supremum over the algebra, and the **bosonic fields**, including the gauge fields, appear as inner fluctuations of $D$, $D\mapsto D+\sum a_i[D,b_i]$. The construction and its axioms are standard (Connes 1995; Connes and Marcolli 2008).

This article asks whether the biquaternion algebra $\mathbb{B}$ supports such a triple, and what the framework's structures contribute to it. The scalar imaginary of the algebra satisfies $i^2=-1$ throughout; it is the central unit of the complexification, not a quaternion unit. The findings are the following.

1. **The algebra, the Hilbert space and the Dirac operator are already present.** The framework's algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$. Its chiral spinor space is the Dirac module $\Delta=S\oplus S^{\mathrm{c}}$ of *The Unpolarized Module of the Biquaternion Algebra*, of complex dimension four (or, in the field-theoretic setting, the square-integrable sections of $\Delta$ on spacetime), and the operator is the framework's Dirac operator,
    $$
    \mathcal{D}=i\tilde\nabla+D_F,
    $$
    with $\tilde\nabla=\sum_\mu e_\mu\,\partial/\partial Q_\mu$ the biquaternion gradient, acting on the left, and $D_F$ the chirality-odd mass. Self-adjointness for the Hermitian form is not automatic, $(i\tilde\nabla)^{\dagger}=i\tilde\nabla^{\natural}$, and the candidate fails it: the coefficient $ie_t$ is anti-Hermitian, as the criterion requires, and the three $i\vec e_k$ are Hermitian, so the operator is self-adjoint in the time direction and skew in the spatial ones. It is self-adjoint for the indefinite Dirac form instead. The algebra acts through its real form $\mathbb{B}_{\mathbb{R}}$, by the defining representation on $S$ and by the conjugate on $S^{\mathrm{c}}$. A candidate triple therefore exists: $(\mathbb{B}_{\mathbb{R}},L^2(\Delta),\mathcal{D})$, or its almost-commutative generalisation $C^\infty(M)\otimes\mathbb{B}_{\mathbb{R}}$. The simple module $S$ alone cannot carry the chirality: every $\mathbb{B}$-linear operator on it is scalar, so the only grading of $S$ is trivial; the two Peirce copies $S_+\cong S_-$ are copies, not chiral halves. What the article checks is which axioms this candidate satisfies and which it does not. Three of them fail: the boundedness of the commutators with the non-central matrix elements under the left action, the first-order condition on the chiral module, and the oddness of the operator under a grading of its own module. Self-adjointness fails as well, and it fails for a reason of the same kind: the Clifford coefficients are algebra elements and their Hermiticity is the signature.

2. **The framework's real-form involution $\flat$ is an antilinear involution, and this is the article's sharpest algebraic point.** The spectral triple's real structure $J$ is an antilinear operator whose sign $J^2=\pm1$, together with the two signs of its commutation with $D$ and with the chirality, gives the triple's **KO-dimension**. The framework's real-form involution is $\flat=-{}^{*}$, and it was verified explicitly that
    $$
    \flat^2 = +1
    $$
    on the algebra. The Euclidean frame's candidate charge conjugation is the left action $\psi\mapsto-\vec e_z\psi$; it is real and antisymmetric in the frame of the four units, squares to $-1$, and commutes with the chirality, so the associated antilinear operator $J_C=CK$ has $J_C^2=-1$ and $J_C\chi=-\chi J_C$. That pair is the quaternionic class of Connes' table, $n\equiv2$ with $(\epsilon,\epsilon'')=(-1,-1)$, and it is the class the Standard-Model finite geometry uses at $n\equiv6$; four-dimensional Euclidean geometry is the real class $n\equiv4$ with $(\epsilon,\epsilon',\epsilon'')=(+1,+1,+1)$, whose sign agrees with the framework's. So $\flat$ is of the real type that four-dimensional geometry has, and what it cannot supply is the quaternionic sign the Standard-Model finite geometry needs: reaching $\epsilon=-1$ requires the module's quaternionic (right) structure, which is exactly the framework's statement that the Clifford algebra is $\mathrm{Cl}_{1,3}\cong M_2(\mathbb{H})$. A central phase cannot supply the minus, because $(\lambda\flat)^2=|\lambda|^2\flat^2=+1$. Stating this precisely is the article's main contribution, and it is a genuine, checkable statement about the algebra rather than a re-description.

3. **The spectral dimension is four, and the framework's metric-as-output is the spectral triple's distance formula read backwards.** The triple's dimension is read from the eigenvalue growth of $D$: if the eigenvalues grow like $n^{1/d}$, the triple has dimension $d$. For the biquaternion Dirac operator on four-dimensional spacetime — that is, for the almost-commutative triple, the finite factor alone having spectral dimension zero — the eigenvalues grow like $n^{1/4}$ and the spectral dimension is four. The same Seeley–DeWitt data that control the heat-kernel coefficients of *The Functional Determinant in Biquaternionic Form* and *The Trace Anomaly in Biquaternionic Form* control this growth: the exponent $d$ of the small-$t'$ expansion is the spectral dimension, and the coefficient that expansion marks as divergent is $a_{d/2}$, which at $d=4$ is $a_2$. The framework's claim that the Minkowski signature is an *output* of the level-1 form read on the material sector is the same shape of statement as the spectral triple's claim that the distance is an output of $D$: in both cases the geometric data is extracted from the algebraic one.

4. **The framework is not a non-commutative geometry of the Standard Model kind.** Connes' and Chamseddine's spectral action program builds the Standard Model from an almost-commutative triple $\mathcal{A}=C^\infty(M)\otimes\mathcal{A}_F$ with a finite-dimensional factor $\mathcal{A}_F$, and it requires specific axioms — the first-order condition, orientability, Poincaré duality, and the KO-dimension — to select the finite geometry. The biquaternion algebra is $(2\times2)$-matrix-like over $\mathbb{C}$, and its finite factor would have to be examined against those axioms; the boundedness and first-order conditions are examined in the body, and orientability, Poincaré duality, and the reproduction of the Standard Model's particle content are not. The Standard-Model spectral triple is therefore a neighbouring construction and not a result of this series. What this article establishes is the candidate, the real-structure obstacle, the dimension, and the three axiom failures; the model-building is elsewhere.

5. **The article stands apart from the rest of the subcategory, and is last for that reason.** Everything before it has been quantum field theory: states, operator algebras, path integrals, finite-temperature and non-equilibrium machinery, and the two structural quantum effects. The spectral triple is a construction in non-commutative geometry, and its appearance here is as the algebraic interpretation of the framework's objects. It is included because the biquaternion algebra's non-commutativity and its module make the construction natural, and it is placed last because it uses the objects the other articles establish without being used by them.

The sections that follow treat, in order: the definition and the axioms; the biquaternion candidate and its elementary properties; the real structure and the KO signs; the spectral dimension and the heat kernel; the distance formula and the metric as output; inner fluctuations and the spectral action; the almost-commutative triple and the finite geometry; the ledger of what is established and what is interpretation; and a closing section, *The Legacy Pauli Gamma Formulation*, where the two-sided frame is written out as gamma matrices, followed by a summary and a table of notation.

## Spectral Triples and Their Axioms

The definition and the axioms are stated as the standard literature gives them.

**The definition.** A spectral triple $(\mathcal{A},\mathcal{H},D)$ consists of a unital $*$-algebra $\mathcal{A}$ of bounded operators on a separable Hilbert space $\mathcal{H}$, together with a self-adjoint operator $D$ on $\mathcal{H}$ such that $(1+D^2)^{-1/2}$ is compact and $[D,a]$ is bounded for every $a\in\mathcal{A}$. The last two conditions are the analytic content: the compactness of the resolvent is what makes the eigenvalue spectrum discrete and gives the triple a dimension, and the boundedness of the commutators is what makes $D$ a first-order operator.

**The axioms.** The axioms of a non-commutative spin geometry are, in outline: **dimension**, the eigenvalue growth of $D$ fixing an integer $d$; **regularity**, that the algebra and its commutators with $D$ lie in the smooth domain of the derivation $[D,\cdot]$; **finiteness**, that the smooth domain of the algebra is a finitely generated projective module; **reality**, the existence of an antilinear $J$ with
$$
J^2=\epsilon I,
\qquad
JD=\epsilon'DJ,
\qquad
J\chi=\epsilon''\chi J,
\qquad
\epsilon,\epsilon',\epsilon''\in\{\pm1\},
$$
whose signs give the **KO-dimension** of the triple, with $\chi$ the chirality operator in even dimensions; **first order**, $[[D,a],Jb^*J^{-1}]=0$; **orientability**, the existence of a Hochschild cycle representing the volume form; and **Poincaré duality**, the non-degeneracy of the intersection form on the $K$-theory. The list is standard (Connes 1995, 1996; Connes and Marcolli 2008) and is cited rather than re-derived. The sign convention is the one in which a closed spin manifold of dimension $m$ has KO-dimension $m\bmod8$, so four-dimensional Euclidean geometry has $(\epsilon,\epsilon',\epsilon'')=(+1,+1,+1)$ and the Standard-Model finite geometry, at $n=6$, has $(-1,+1,-1)$. The corpus's *Spectral Triples and Noncommutative Geometry* prints rows 4 and 6 of its table the other way round; the difference is reported in the section on the real structure, and the arithmetic below follows the convention just stated.

**Which axioms are cheap and which are not.** For a commutative algebra of functions on a spin manifold all of them hold, and that is the theorem that the construction generalises the manifold. For a finite-dimensional non-commutative algebra some of them are algebraic and checkable directly — reality, first order, orientability — while dimension, finiteness and Poincaré duality require structure that a bare matrix algebra does not supply. Boundedness is the exception in the other direction: it looks analytic and harmless, and it is the condition the biquaternion algebra fails, for a reason that is algebraic — its Clifford coefficients are elements of the algebra. The biquaternion algebra is finite-dimensional, and this division is what the next section reports.

## The Biquaternion Candidate

The candidate is assembled from objects the rest of the series already uses, and the assembly is checked before any axiom is asserted.

**The two actions.** An element $a$ acts on an element $\psi$ of the algebra in three ways: on the left, $\psi\mapsto a\psi$; on the right, $\psi\mapsto\psi b$; and on both sides at once, $\psi\mapsto a\psi b$. The left and right actions commute, $(a\psi)b=a(\psi b)$. They are not of one kind: a right action commutes with every left action and is a map of the left module $\mathbb{B}$ to itself, while a left action commutes with every right action and is a map of the right module, failing to commute with left multiplication by a non-central element. Below, $a\cdot$ denotes the left action and $\cdot b$ the right action. The distinction between the sides is the article's subject, and it is stated once here and used throughout: an action is named by the side it acts on and by the element it uses, never by a letter that stands for an operator.

Two facts are used below. The sixteen maps $\psi\mapsto e_\mu\psi e_\nu$, one for each pair of units, span all $\mathbb{C}$-linear maps of $\mathbb{B}$ to itself, which is $\operatorname{End}_{\mathbb{C}}(\mathbb{B})\cong M_4(\mathbb{C})$, so every operator this article writes is one of them or a sum. And because a right action commutes with every left action, a grading that is a right action is invisible to a gradient that acts on the left — which is where the grading of this triple fails. A block matrix appears only where no action of the algebra on itself can represent the object: for the mass operator, which is not $\mathbb{B}_{\mathbb{R}}$-linear, and for the block form of the grading it opposes.

**The algebra and the module.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}\cong M_2(\mathbb{C})$ as a complex algebra, and its real form is $\mathbb{B}_{\mathbb{R}}$. The representation is the defining one on $S$ and its conjugate on $S^{\mathrm{c}}$: for $a\in\mathbb{B}_{\mathbb{R}}$,
$$
a\cdot(s,t)=(as,\bar a\,t),\qquad s\in S,\ t\in S^{\mathrm{c}},
$$
with $\bar a$ the complex conjugate, which is the action on the conjugate module.
The module $\Delta=S\oplus S^{\mathrm{c}}$ is four-complex-dimensional, and the two summands are conjugate, not copies. That is the difference between $\Delta$ and the regular module $S\oplus S$: the regular module's two summands are the Peirce copies, and the chiral module's two summands are a representation and its conjugate.

**The Hilbert space.** The inner product is the Hermitian one,
$$
\langle\tilde\Psi,\tilde\Phi\rangle
=\mathrm{Sc}\bigl(\tilde\Psi^{*}\tilde\Phi\bigr)
=\tfrac12\,\mathrm{Tr}\bigl(\tilde\Psi^{*}\tilde\Phi\bigr),
$$
which is positive definite,
$$
\langle\tilde\Psi,\tilde\Psi\rangle=\sum_{\mu}\lvert\Psi_\mu\rvert^2>0
\quad(\tilde\Psi\neq0).
$$
It is the Hermitian form of *Norm and Pairing Conventions*, not the plain bilinear form: the plain form is indefinite, and it cannot be the Hilbert-space inner product. The completion of $\Delta$ in this form is the candidate $\mathcal{H}$.

**The operator.** The Dirac operator is
$$
\mathcal{D}=i\tilde\nabla+D_F,
\qquad
\tilde\nabla=\sum_\mu e_\mu\,\frac{\partial}{\partial Q_\mu},
$$
with $D_F$ the mass of the next paragraph. The gradient is an element with derivative coefficients, and $\tilde\nabla\psi$ means its left action on $\psi$; no other action is meant anywhere below. With respect to the Hermitian form the gradient's adjoint reverses its units,
$$
\tilde\nabla^{\dagger}=-\tilde\nabla^{\natural},
\qquad
(i\tilde\nabla)^{\dagger}=i\tilde\nabla^{\natural},
$$
so $i\tilde\nabla$ is not self-adjoint for that form. The criterion is fixed by the derivative: since $(\partial/\partial x_\mu)^{\dagger}=-\partial/\partial x_\mu$, an operator $\sum_\mu A_\mu\partial/\partial x_\mu$ with constant coefficients is self-adjoint exactly when every $A_\mu$ is anti-Hermitian. Here $ie_t$ is anti-Hermitian but the three $i\vec e_k$ are Hermitian, so the operator is self-adjoint on the time direction and skew on the three spatial ones, and the defect is the Minkowski signature itself. The Euclidean frame of *The Legacy Pauli Gamma Formulation* is the opposite case, all four of its generators being Hermitian; there the coefficients $-iE_\mu$ are anti-Hermitian and $-i\sum_\mu E_\mu\partial/\partial Q_\mu$ is self-adjoint for the same form, with square $-\Box$, since $\Box=\tilde\nabla\tilde\nabla^{\natural}=\sum_\mu\partial^2/\partial Q_\mu^2$ and the frame's generators square to $+1$. That is Connes' normalisation, and it is the frame in which the signs are all of one kind. The framework's operator is self-adjoint for the Dirac (Krein) form, and whether the triple can use a positive-definite form and keep a self-adjoint $D$ is part of the open problem, not a consequence of the algebra.

**The Dirac equation in two forms.** The framework writes the Dirac equation in two forms, and the displays should be kept separate because they answer different questions. The defining form is the chiral pair,
$$
\tilde\nabla\tilde\Psi_R=m\tilde\Psi_L,
\qquad
\tilde\nabla^{\natural}\tilde\Psi_L=m\tilde\Psi_R,
$$
with the gradient acting on the right-chiral field and its conjugate on the left-chiral one, and the mass coupling the two. The pair is one operator, the pair operator of *Operator and Calculus Conventions*,
$$
\mathbb{D}(\Psi_L,\Psi_R)=\bigl(\tilde\nabla\Psi_R,\ \tilde\nabla^{\natural}\Psi_L\bigr),
\qquad
\mathbb{D}^2=\Box I,
$$
and the massive equation is $(\mathbb{D}-m)\Psi=0$, whose two components are the pair. The two-sided form, from the two-sided operator theory of *The Feynman Propagator in Biquaternionic Form*, is
$$
\mathcal{N}F=\Bigl(-\tilde\nabla^{\natural}-mi\,\overline{\,\cdot\,}\,\vec e_z\Bigr)F=0,
$$
with the mass acting on the right through conjugation. The dictionary between the two-sided field and the chiral pair is $\tilde\Psi_R=-i\overline{F}\,\vec e_z$, so the three displays describe one physics: the first is the chirality form, the second the pair operator written once, and the third the two-sided form. The spectral triple's candidate operator is $\mathcal{D}=i\tilde\nabla+D_F$: the gradient in the same chirality basis, with the chirality-odd mass added.

**The chirality.** The chirality is right multiplication by the element $-i\vec e_z$,
$$
\chi:\psi\longmapsto-i\psi\vec e_z=\psi\,(-i\vec e_z),
$$
the second form holding because $i$ is central; its central form is the sign of the double,
$$
\chi=i\tilde\Xi_{\mathrm{ad}}=e_+-e_-,
\qquad
\chi^2=e_t,
$$
and it is represented differently on the two modules, which is why the article carries two forms of it.

- On the regular module it is that right action, $\psi\mapsto-i\psi\vec e_z$: self-adjoint for the Hermitian form, of square $I_4$, and commuting with every left action.
- On the chiral module $\Delta$ it is the block matrix $\operatorname{diag}(-I_2,I_2)$, because it grades the two summands $S$ and $S^{\mathrm{c}}$.

The two matrices are unitarily equivalent — both are Hermitian with eigenvalues $+1,+1,-1,-1$ — and neither form is a decoration. The block form is the eigenbasis form, which is why it is the one used for $D_F$ and in the tables; the regular-module form shows $\chi$ to be a right action, and that is what decides on which side a grading can work.

The Peirce index is right multiplication by $i\vec e_z$,
$$
P:\psi\longmapsto i\psi\vec e_z,
$$
so as maps $\chi=-P$. The two gradings are the same action up to sign, and they grade different modules: $P$ grades the regular module's two Peirce copies $S_+\cong S_-$, while $\chi$ grades the chiral halves $S$ and $S^{\mathrm{c}}$ of $\Delta$. The Peirce index is therefore a copy label, and only the grading $\chi$ is the chirality; the difference is the module, not the action. On $\Delta$ the pattern is the almost-commutative one: the grading is the finite chirality, it commutes with every left action and anticommutes with the mass, so the mass is odd and the gradient, being a left action, is even. Neither statement is available for the right action, and the reason is immediate: $\chi$ is itself a right action, so it commutes with right multiplication by $e_t$ and by $\vec e_z$ and anticommutes with right multiplication by $\vec e_x$ and by $\vec e_y$, the commutator attaining size $2$ there.

**What $\chi$ does not grade.** The gradient is even under $\chi$ and the mass is odd, so $\mathcal{D}=i\tilde\nabla+D_F$ is neither, and the reason is algebraic rather than a choice of signs: $\chi$ is a right action and the gradient a left action, so they commute whatever the coefficients. The operator that differentiates therefore cannot see the grading, and within $\mathcal{D}$ only the mass sees it. This is why a graded triple needs $\Gamma=G_M\otimes\chi$: the oddness of $D$ is carried by the manifold chirality $G_M$ and not by $\mathcal{D}$ alone. The finite triple $(\mathbb{B}_{\mathbb{R}},\Delta,D_F)$ is graded and odd; it is the whole operator on $\Delta$ that has no grading. This is the same collapse seen from the other side: the framework has one module where the construction has two factors.

**The mass.** The mass is the off-diagonal operator
$$
D_F=m\,\beta+\bar m\,\beta^{*},
\qquad
\beta:S^{\mathrm{c}}\to S,
\quad
\langle s,\beta(t)\rangle=s^{\dagger}t,
$$
between the two summands; in the block basis $(S,S^{\mathrm{c}})$ it is
$$
D_F=\begin{pmatrix}0&m\\ \bar m&0\end{pmatrix}.
$$
This is the matrix of the operator, not an action of the algebra on itself: $D_F$ is not $\mathbb{B}_{\mathbb{R}}$-linear for $m\neq0$. It is Hermitian, $D_F^2=|m|^2I$, its eigenvalues are $\pm|m|$ each with multiplicity two, and it is odd under the chirality,
$$
\chi D_F+D_F\chi=0.
$$

**The commutator with the algebra.** For $a\in\mathbb{B}_{\mathbb{R}}$ the left action $a\cdot$ is $a$ on $S$ and $\bar a$ on $S^{\mathrm{c}}$, and the two terms separate,
$$
[\mathcal{D},a\cdot]=[i\tilde\nabla,a\cdot]+[D_F,a\cdot].
$$
The mass term is explicit in the $S,S^{\mathrm{c}}$ blocks,
$$
[D_F,a\cdot](s,t)=\bigl(m(\bar a-a)t,\ \bar m(a-\bar a)s\bigr),
$$
written for the central mass $m\in\mathbb{C}$; for a biquaternionic mass the order matters, and $m(\bar a-a)$ is replaced by $m\bar a-am$. The asymmetry between $a$ and $\bar a$ is the whole content: the two halves of $\Delta$ carry the defining representation and its conjugate, and it is because they differ that the mass fails to commute with the algebra. On the regular module the same matrix would act as $a$ on both halves, and the commutator would vanish.

The commutator is not, however, nonzero for every non-scalar $a$, and saying which elements it does vanish on is worth the precision. The conjugation here is the one carried by the coordinate identification $S^{\mathrm{c}}\to S$, and on the four units it reads $\overline{e_t}=e_t$, $\overline{\vec e_y}=\vec e_y$, $\overline{\vec e_x}=-\vec e_x$, $\overline{\vec e_z}=-\vec e_z$. So $[D_F,a\cdot]=0$ exactly when $a$ lies in $\mathbb{R}[\vec e_y]$, the copy of $\mathbb{C}$ spanned over $\mathbb{R}$ by $\vec e_y$ inside $\mathbb{B}_{\mathbb{R}}$ — a commutative subalgebra, and the largest one on which the mass commutes with the left action. For $\vec e_x$ and $\vec e_z$ the commutator is $2m$ times an off-diagonal block. The parallel with Connes' two-point space is exact in this one respect: there the finite algebra $\mathbb{C}\oplus\mathbb{C}$ is abelian and the condition holds. What the mass tolerates is a commutative subalgebra, and the non-abelian part of $\mathbb{B}_{\mathbb{R}}$ is where it fails.

**The same fact in the companion's coordinates.** *The Unpolarized Module of the Biquaternion Algebra* writes the conjugate action in the $\epsilon$-dressed model,
$$
\rho(a)=\operatorname{diag}\bigl(\mathsf M_2(a),\ \epsilon\,\overline{\mathsf M_2(a)}\,\epsilon^{-1}\bigr),
\qquad
\epsilon=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
$$
On the four units the dressing changes nothing, $\epsilon\overline{\mathsf M_2(e_\mu)}\epsilon^{-1}=\mathsf M_2(e_\mu)$, so the two blocks look alike and the algebra appears to act in the same way on both halves. It does not: the dressing conjugates the coefficient of $e_t$, so $\rho(i)=\operatorname{diag}(iI_2,-iI_2)$, and $\rho(a)\ne\operatorname{diag}(\mathsf M_2(a),\mathsf M_2(a))$ for a general $a\in\mathbb{B}_{\mathbb{R}}$. The two frames differ by the matrix $\operatorname{diag}(I_2,\epsilon)$ in the second summand; under it the mass is no longer the plain matrix but
$$
\begin{pmatrix}0&m\epsilon\\ \bar m\epsilon^{-1}&0\end{pmatrix},
$$
and the commutator is the one computed above, zero on $\mathbb{R}[\vec e_y]$ and of size $2|m|$ for $\vec e_x$ and $\vec e_z$. Nothing depends on the frame; what depends on it is whether the conjugation sits in the action or in the operator. The statement both readings share is the abstract one: $D_F$ is not $\mathbb{B}_{\mathbb{R}}$-linear, which is what $\operatorname{Hom}_{\mathbb{B}_{\mathbb{R}}}(S,S^{\mathrm{c}})=0$ forbids. This article computes in the plain coordinates, where the scalars of $\Delta$ act as $\lambda(\psi,t)=(\lambda\psi,\bar\lambda t)$.

**The order of the gradient commutator.** The gradient term is *not* zeroth order, and this is the first place where the algebra meets the Clifford coefficients. Because $a$ is a constant of the finite algebra, $\partial/\partial x_\mu(a\psi)=a\,\partial \psi/\partial x_\mu$, so
$$
[i\tilde\nabla,a\cdot]\psi=i\sum_\mu[e_\mu,a]\,\frac{\partial\psi}{\partial Q_\mu},
$$
which carries a derivative whenever $a$ fails to commute with the units. The principal symbol states the criterion exactly: the symbol of $\tilde\nabla$ is Clifford multiplication by $\sum_\mu\xi_\mu e_\mu$, so the commutator is bounded precisely when
$$
\Bigl[\sum_\mu\xi_\mu e_\mu,\,a\Bigr]=0\quad\text{for every }\xi,
$$
that is, precisely when $a$ commutes with all four units. The centralizer of the units in $\mathbb{B}$ is the complex line $\mathbb{C}e_t$, and the three cases follow.

- A scalar multiplier $f$ commutes with the units, and the commutator is the zeroth-order $[i\tilde\nabla,f\cdot]=i\,(\tilde\nabla f)\cdot$, hence bounded. This is the classical statement for functions, and it is the reason the naive formula $[i\tilde\nabla,a\cdot]=i\,(\tilde\nabla a)\cdot$ holds for them and fails for the rest of the algebra.
- A non-central matrix multiplier $a\in\mathbb{B}_{\mathbb{R}}$ gives a first-order commutator, hence an unbounded one on the field-theoretic module: the **bounded-commutator condition fails for the left action of the matrix factor**. On the finite module the condition is vacuous — every operator on $\mathbb{C}^4$ is bounded — so the failure is a statement about $L^2(\Delta)$, the sections over spacetime, and not about the finite geometry. Note what makes it fail: in Connes' almost-commutative triple the continuum operator is $D_M\otimes I_F$ and carries no element of the finite algebra, so its commutators with the finite factor vanish. Here the Clifford coefficients of the gradient are themselves elements of the algebra and are four of them, and that is what turns the commutator first order.
- The right action passes: for a constant factor $[\tilde\nabla,\cdot a]=0$ identically, and for a function the commutator is the bounded two-sided action $[\tilde\nabla,\cdot f]\psi=\sum_\mu e_\mu\psi\,\partial f/\partial Q_\mu$.

The asymmetry is the structural point. The four units are the Clifford coefficients and elements of the algebra at once, so an action on the same side as the units is seen by them; the side that the Clifford coefficients do not see is the right one. The symbol check is exact, and it is read in the defining $2\times2$ representation: at $\xi=(0.3,-0.7,1.1,0.4)$, the largest entry of $[\sum_\mu\xi_\mu e_\mu,a]$ is $2.2$ for $\vec e_x$, $1.4$ for $\vec e_y$, $2.6$ for $\vec e_z$, and exactly $0$ for $e_t$ and for the central scalars such as $ie_t$. The commutator is bilinear, so a general $a$ scales these numbers by its own coefficients; the units are the meaningful comparison, and none of the three non-central units gives zero.

**The first-order condition.** With the candidate real structure read from $\flat$, written $J_{\flat}$ on the module, the condition is
$$
[[\mathcal{D},a\cdot],J_{\flat}b^{*}J_{\flat}^{-1}]=0.
$$
The two minus signs from $\flat=-{}^{*}$ cancel in the combination, so $J_{\flat}b^{*}J_{\flat}^{-1}$ is the opposite action. What the opposite action *is* depends on the module, and the two candidates sit on different modules; that is the whole subtlety of this axiom here.

- **On the regular module** it is the right action $\cdot b$, and left and right actions commute. The gradient's commutator is a left action times derivatives, and a derivative commutes with a right action, so
    $$
    \bigl[[i\tilde\nabla,a\cdot],\cdot b\bigr]=0
    $$
    identically (maximum entry over the sixteen index pairs: $0$), and the condition is decided by the mass.
- **On $\Delta$** it is not an action but $\operatorname{diag}(b^{\mathsf T},\bar b^{\mathsf T})$, transposition on $S$ and its conjugate on $S^{\mathrm{c}}$. No left multiplication commutes with that unless it is central, so the gradient's commutator survives:
    $$
    \Bigl[\pi\Bigl(\bigl[\textstyle\sum_\mu\xi_\mu e_\mu,a\bigr]\Bigr),\ \operatorname{diag}(b^{\mathsf T},\bar b^{\mathsf T})\Bigr]=0
    $$
    for all $b$ exactly when $\bigl[\sum_\mu\xi_\mu e_\mu,a\bigr]$ is a scalar, that is, exactly when $a$ is central.

The two candidates therefore separate, and they separate at different places.

- **The vector-like candidate** lives on the regular module, where its mass is the right action $\cdot m$ with $m$ central and real, which is self-adjoint for the Hermitian form. A right action commutes with every left action, so $[D_F,a\cdot]=0$ and
    $$
    \boxed{\;[[\mathcal{D},a\cdot],\cdot b]=0\quad\text{for all }a,b\in\mathbb{B}_{\mathbb{R}}\;}
    $$
    Both terms vanish exactly rather than approximately, so the condition holds for this candidate on this module. The bounded-commutator condition of the previous paragraph still fails for its left action, and the boxed statement is a statement about the regular module: it does not transfer to $\Delta$. Nor is the success free of charge. The regular module's only grading is the Peirce index $P$, and the mass commutes with it, as does the gradient: the mass is a right action and right actions commute with one another, and the gradient is a left action. The whole operator is therefore even under $P$, and this candidate has no odd grading at all. On $\Delta$ the finite part is at least odd, because the mass is off-diagonal there. The two candidates therefore fail different axioms: the vector-like one keeps the first-order condition and loses every grading, and the chiral one keeps the odd finite part and loses the first-order condition.
- **The chiral triple** lives on $\Delta$, and there the condition is the intersection of two. The gradient admits the centre $\mathbb{C}e_t$ only, because a scalar symbol is what the transposition cannot see; the mass admits the fixed set $\mathbb{R}[\vec e_y]$ only, because $[D_F,a\cdot]$ is the off-diagonal $m(\bar a-a)$ and the conjugation fixes $e_t$ and $\vec e_y$. Neither set contains the other, and their intersection is the real scalars $\mathbb{R}e_t$: $a=\vec e_y$ passes the mass and fails the gradient, and $a=(1+i)e_t$ passes the gradient and fails the mass, since $\bar a\ne a$ for a non-real scalar and the second summand sees $\bar\lambda$. **The chiral triple therefore satisfies the first-order condition exactly on $\mathbb{R}e_t$, and fails it on every other element of $\mathbb{B}_{\mathbb{R}}$.**

**What the candidate does not supply.** Five things are worth separating from what it does supply.

- The side on which the matrix factor can act is constrained. Bounded commutators hold for the right action and fail for the left on the non-central elements, while the grading holds for the left action and fails for the right, because $\chi$ is itself a right action. No single side carries both, and the obstruction in both cases is the same: the Clifford coefficients are elements of the algebra. The first-order condition is a third, separate failure: on $\Delta$ the gradient's symbol already breaks it for every element outside the real scalars, because the opposite action there is a transposition rather than a right multiplication.
- The operator has no grading on its own module. $\chi$ commutes with the gradient and anticommutes with the mass, so $\mathcal{D}$ is neither even nor odd under $\chi$; the grading of a full triple is $G_M\otimes\chi$, which grades the product $L^2(S)\otimes\Delta$ and not $\Delta$ alone.
- The Hilbert space and the operator do not decide the finite geometry. In Connes' construction the finite algebra and the finite Dirac operator are constrained by the axioms and by the requirement that the spectral action reproduce the Standard Model; here the finite operator is the framework's mass, and the finite algebra is $\mathbb{B}_{\mathbb{R}}$, but the constraints are not imposed and the particle content is not derived.
- The algebra is matrix-like, and the finite geometry of the Standard Model is not a matrix algebra. The Standard-Model finite algebra is $\mathbb{C}\oplus\mathbb{H}\oplus M_3(\mathbb{C})$, and $\mathbb{B}_{\mathbb{R}}$ is not that algebra; the two can be compared, but not identified.
- The real structure is the algebra's involution rather than the module's quaternionic structure. The involution is what the framework's $\flat$ gives, and the quaternionic structure is an additional datum on $\Delta$; the next section states the difference and its consequence for the sign of $J^2$.

## The Real Structure and the KO-Dimension

The real structure is where the framework's algebra and the spectral triple's axioms meet, and the meeting is a sign.

**The involution.** The framework's real-form involution is
$$
\flat=-{}^{*},
\qquad
\flat(\tilde Q)=-\tilde Q^{*},
$$
and its fixed space is the material sector $\mathbb{M}_-$. It is conjugate-linear, because ${}^{*}$ is, and therefore an antilinear map on the algebra. Its square is computed directly:
$$
\flat(\flat(\tilde Q))
=\flat\bigl(-\tilde Q^{*}\bigr)
=-\bigl(-\tilde Q^{*}\bigr)^{*}
=\tilde Q,
$$
so
$$
\boxed{\;\flat^2=+1\;}.
$$
The framework's involution is therefore an antilinear **involution**, so the candidate real structure has $\epsilon=+1$. This was verified on explicit matrices and is quoted in the established list below.

**The global minus and the order-one condition.** The map $\flat$ is $-1$ times the star anti-automorphism, and the product rule is
$$
(\tilde Q_1\tilde Q_2)^\flat
=-\tilde Q_2^\flat\tilde Q_1^\flat.
$$
On the module that involution is the antilinear operator $J_{\flat}(\psi)=-\psi^{*}$, of square $+1$, and the two minus signs cancel in the order-one combination:
$$
J_{\flat}b^{*}J_{\flat}^{-1}=\cdot b,
$$
the right action.
The global minus is therefore immaterial for the first-order condition, but it must be kept in the signs of the algebra and in the product rule above.

**The Euclidean candidate.** For comparison, the Euclidean frame carries an antisymmetric operator of square $-1$, offered in the literature as a charge conjugation. In that frame
$$
E_4:\psi\longmapsto i\psi\vec e_x,
\qquad
E_k:\psi\longmapsto-\vec e_k\psi\vec e_y
\quad(k=1,2,3),
$$
and the four are not of one kind: $E_4$ is a right action, while the three $E_k$ act on both sides. All four are Hermitian, square to $+1$, and pairwise anticommute. Their product is the chirality,
$$
E_1E_2E_3E_4:\psi\longmapsto-i\psi\vec e_z,
\qquad
(E_1E_2E_3E_4)^2=I_4,
$$
a right action. The candidate for the charge conjugation is the left action
$$
C:\psi\longmapsto-\vec e_z\psi=E_1E_2,
\qquad
C^2=-I_4,
\qquad
[C,E_1E_2E_3E_4]=0,
$$
real and antisymmetric in the frame of the four units.
The antilinear operator built from it is $J_C=CK$, with $K$ complex conjugation, and because $C$ is real,
$$
J_C^2=C\bar C=C^2=-1.
$$
The operator $C$ conjugates each generator to its transpose up to sign, and the signs are not uniform in this frame:
$$
CE_1C^{-1}=-E_1^{\mathsf T},
\quad
CE_2C^{-1}=-E_2^{\mathsf T},
\quad
CE_3C^{-1}=+E_3^{\mathsf T},
\quad
CE_4C^{-1}=-E_4^{\mathsf T}.
$$
Three minus signs and one plus. Uniformity of those signs, not the sign of the square, is where this operator fails the definition of a charge conjugation.

Two of the three signs are reached here, and they come out as a pair. The chirality $\chi$ is Hermitian, and in the basis of the four units its matrix has purely imaginary entries, so $K$ maps it to $-\chi$; $C$ is real in that basis and commutes with it, hence $J_C\chi J_C^{-1}=C\bar\chi C^{-1}=-\chi$ and $\epsilon''=-1$. The value is not an accident of this frame, but showing that needs the right transformation rule. An antilinear map changes frame by conjugating its matrix, $M\mapsto U^{-1}M\bar U$, and not by transforming the two factors separately; with that rule $J_C^2$ and $J_C\chi J_C^{-1}$ are carried to themselves, whereas transforming $C$ and $K$ apart, as though $J_C$ were a product of two linear factors, gives a different antilinear map and in general a different sign. That is why the block form $\chi=\operatorname{diag}(-I_2,I_2)$, convenient for $D_F$ and for the tables, is not the frame in which to read $\epsilon''$ off the matrix $C$ alone.

Two properties of $J_C$ are then immediate. The operator $C$ is unitary, so $J_C$ is an isometry; and $J_C^2=C\bar C=C^2=-1$ because $C$ is real. A rescaling $J_C\mapsto\lambda J_C$ with $|\lambda|=1$ changes neither $J_C^2$, where the factor is $|\lambda|^2=1$, nor $J_C\chi J_C^{-1}$, where the phase cancels. Both signs are therefore properties of the pair $(C,\chi)$, and the pair $(\epsilon,\epsilon'')=(-1,-1)$ is the $n\equiv2$ line of Connes' table, not the $n\equiv4$ one.

What is compared with the framework's $\flat$ is consequently $\epsilon$ alone, the sign of $J_C^2=C\bar C$, which for real $C$ is the sign of $C^2$; the sign $\epsilon'$ of $J_CD=\epsilon'DJ_C$ involves $D$ itself and is not computed.

**Which table.** The two dictionaries that matter here disagree, and the disagreement is not about this frame. Connes' table gives $(+1,+1,+1)$ for $n\equiv4$ and $(-1,+1,-1)$ for $n\equiv6$, so four-dimensional Euclidean spin geometry is of the real class and the Standard-Model finite geometry, which sits at $n=6$, is of the quaternionic one. The table of *Spectral Triples and Noncommutative Geometry* prints $(-1,+1,+1)$ at $n=4$ and $(+1,+1,-1)$ at $n=6$, that is the two rows exchanged: its $\epsilon$ at $n=4$ is minus where Connes' is plus, and its $\epsilon$ at $n=6$ is plus where Connes' is minus. Under Connes' table the four-dimensional sign is $+1$, the same as $\flat^2$, and this is what the geometry says: a four-dimensional Euclidean triple has $J^2=+1$.

**What $C$ shows.** The pattern settles the question of what it is. $C$ has $C^2=-1$ and commutes with $\chi$, and its transposition signs are not uniform; a charge conjugation proper needs a single sign for all four generators and, in four dimensions, $J^2=+1$. This operator is therefore not the dimension-four charge conjugation, and the frame's $-1$ is not a normalisation slip to be corrected: it is the quaternionic sign, and it belongs to the module's quaternionic structure, which is the class the Standard-Model finite geometry needs. So the comparison resolves, and it resolves against the corpus's row rather than against the frame.

**The reconciliation.** The framework's $\flat^2=+1$ is the real sign, and the sign it does not give is the quaternionic one, $\epsilon=-1$. The difference is a fact about the algebra and the module rather than a relabelling. The module carries a quaternionic structure, an antilinear map $\mathcal{J}$ with $\mathcal{J}^2=-1$, and it is this structure, not the central circle, that can supply the missing minus. A central phase $\lambda$ cannot: composing $\flat$ with it gives
$$
(\lambda\flat)^2=\lvert\lambda\rvert^2\flat^2=+1.
$$
The exact relation between $\flat$ and $\mathcal{J}$ is not constructed here, and the article marks that as open; what is established is that the algebra's involution has $+1$ and that the module's quaternionic structure is the only candidate for the other sign. The framework's statement that $\mathrm{Cl}_{1,3}\cong M_2(\mathbb{H})$ is its record of that structure.

**The consequence.** The biquaternion algebra's natural real-form involution has the $+$ sign, and a spectral triple built on it must import the quaternionic structure — from the module, not from the algebra — to reach the quaternionic sign $\epsilon=-1$ that the Standard-Model finite geometry carries at $n\equiv6$. This is a precise statement about where the framework's data lives, and it is the kind of distinction the conventions article's separation of the levels is designed to keep straight: the algebra's involution, the module's quaternionic structure, and the central phase are three different objects, and only one of them supplies the quaternionic sign.

## The Spectral Dimension and the Heat Kernel

The triple's dimension is read from the operator's spectrum, and the framework's heat-kernel data are the same data.

**Dimension from the spectrum.** If the eigenvalues $\lambda_n$ of $D$ are ordered by magnitude, the spectral dimension is the $d$ for which the counting function grows as $N(\Lambda)\sim\Lambda^d$. The growth is a statement about the principal symbol, and the biquaternion gradient's is exact. The symbol of $\tilde\nabla$ at $\xi$ is $\sum_\mu\xi_\mu e_\mu$, a $2\times2$ matrix whose quaternion norm is $\xi_t^2+\xi_x^2+\xi_y^2+\xi_z^2$: the four generators contribute $+\xi_\mu^2$ each, because $e_t^2=+1$ and $\vec e_k^2=-1$ while $\vec e_k^{\natural}=-\vec e_k$. Hence
$$
\sigma(\tilde\nabla)\sigma(\tilde\nabla)^{\natural}=|\xi|^2I,
\qquad
\det\sigma(\tilde\nabla)=|\xi|^2,
$$
both nonzero off $\xi=0$, and the symbol is invertible there. Note that $\sigma^2$ is *not* a multiple of the identity — its scalar part is $\xi_t^2-|\vec\xi|^2$ — so the ellipticity is read from the quaternion norm and from the determinant, not from the square. It is the square that is scalar in the Euclidean frame, where the four generators anticommute: there $D=-i\sum_\mu E_\mu\partial/\partial Q_\mu$ gives $D^2=-\sum_\mu\partial^2/\partial Q_\mu^2$, of Laplace type, and the $t'^{-2}$ growth that gives $d=4$ is the symbol's and not an assumption. Equivalently the trace of the heat kernel grows as
$$
\boxed{\;\mathrm{Tr}\,\exp(-t'D^2)\;\sim\;{t'}^{-d/2}\quad(t'\to0^+)\;},
$$
and the coefficients of the small-$t'$ expansion are the Seeley–DeWitt coefficients $a_n$ of the determinant article, in its normalisation
$$
K(t')\sim(4\pi t')^{-d/2}\sum_{n\ge0}a_n\,{t'}^{n}.
$$
The dimension is the exponent of the prefactor $(4\pi t')^{-d/2}$, of which $a_0$ is the constant part; the coefficient of the logarithmic divergence is $a_{d/2}$, which in four dimensions is $a_2$, the quantity the determinant and anomaly articles evaluate. So the two statements are one: the growth fixes $d=4$, and $d=4$ names which of their coefficients is the divergent one. The framework adds its multiplicity: the trace runs over the module, whose four complex dimensions multiply the density of eigenvalues, and the anisotropy of the level-2 metric does not enter because the heat-kernel statement is the Euclidean one, the Euclidean rotation being the framework's sector identification of the functional-integral article.

**What the framework contributes.** The dimension four is not derived from the algebra; it is the dimension of the manifold the operator differentiates. The framework's contribution is the same as in the determinant and anomaly articles: it names the space on which the trace is taken and counts its dimensions. It is worth saying plainly, because the spectral triple's literature sometimes reads a dimension out of a finite geometry, that here the finite algebra's module is four-complex-dimensional and the four-dimensionality comes from the differential operator.

**The finite part.** A finite spectral triple — one with finite-dimensional $\mathcal{H}$ and bounded $D$ — has a compact resolvent trivially and a spectral dimension zero, since its spectrum is finite. The biquaternion algebra's finite triple therefore has spectral dimension zero; a *dimensionful* triple requires the algebra $C^\infty(M)\otimes\mathbb{B}$ and a first-order elliptic operator. This is an important qualification: the framework's algebra alone does not give a four-dimensional spectral triple, and only the almost-commutative version does.

## The Distance Formula and the Metric as Output

The construction's most distinctive feature is that the metric is recovered from the operator, and the framework has its own version of the same move.

**The distance formula.** For a spectral triple with a commutative algebra the distance between two states is
$$
d(\varphi,\omega)
=\sup_{a\in\mathcal{A}}\bigl\{\lvert\varphi(a)-\omega(a)\rvert:\lVert[D,a]\rVert\le1\bigr\},
$$
and for $\mathcal{A}=C^\infty(M)$ with $D$ the Dirac operator this reproduces the geodesic distance. The metric is therefore an *output* of the operator and the algebra, not an input. This is standard (Connes 1995; Connes and Marcolli 2008).

**The framework's analogous move.** The framework's metric is likewise an output: the Lorentzian signature is not postulated but is the level-1 biquaternion norm read on the material sector with the time coefficient written $ict'$, and the minus sign comes from $i^2=-1$ alone. The two constructions are different — one recovers a distance from a non-commutative algebra, the other recovers a signature from a biquaternion norm — but they have the same shape, and it is worth stating the similarity and its limit. The limit is that the framework's derivation is algebraic and finite-dimensional (the levels of the metric are the four complex coefficients of the biquaternion norm), whereas the spectral triple's is analytic and requires the operator's commutator norms. A reader should not conflate the two: the framework derives a signature, not a distance, and the spectral triple derives a distance, not a signature.

**The almost-commutative case.** If one takes $\mathcal{A}=C^\infty(M)\otimes\mathbb{B}_{\mathbb{R}}$, then the triple is almost commutative, and the distance formula recovers the product geometry $M\times F$ for a finite geometry $F$. Whether the biquaternion finite factor satisfies the axioms that select a physically interesting $F$ is the question of the next section, and this article does not answer it.

## Inner Fluctuations, Gauge Fields, and the Spectral Action

The model-building content of the construction is stated, and its status in this series is fixed.

**Inner fluctuations.** A spectral triple admits a modification of the operator by an inner fluctuation,
$$
D\;\longrightarrow\;D_A=D+\sum_i a_i\,[D,b_i],
$$
with $a_i,b_i\in\mathcal{A}$ and the sum self-adjoint, and the fluctuation is what plays the role of a gauge field. For $\mathcal{A}=C^\infty(M)$ it is a one-form and produces the Maxwell field; for an almost-commutative triple it produces the Yang–Mills fields and the Higgs field. The gauge group is read off from the unitaries of the algebra modulo the central phase, which acts as a multiple of the identity and is not seen by the states. This is standard (Connes 1996; Chamseddine and Connes 1997) and is cited.

**The spectral action.** The bosonic action is the spectral action
$$
S_{\mathrm{spec}}=\mathrm{Tr}\,f\!\left(\frac{D_A}{\Lambda}\right),
$$
which expands in the heat-kernel coefficients as the sum of the volume term, the Einstein–Hilbert term, the Yang–Mills terms, and the scalar potential, with the coefficients read from the $a_n$ of the previous section; the expansion is the standard result of the Chamseddine–Connes program. The framework's connection to it is exactly the heat-kernel connection: the same coefficients that the functional-determinant and trace-anomaly articles evaluate expand the spectral action. This is a genuine structural link, and it is the reason the spectral triple is included in this subcategory at all.

**The framework's status regarding it.** The series does not construct the Standard Model from the biquaternion spectral triple, and this article does not either. The gauge-field and particle-physics categories are the appropriate place for the gauge group, the fermion content, and the anomaly-cancellation conditions, and the almost-commutative triple's axioms would have to be checked there. What this article establishes is that the framework's objects can be assembled into a candidate triple, that the algebra's involution has the $+$ sign and needs the module's quaternionic structure for the $-$ sign, and that the heat-kernel coefficients the framework already uses are the spectral action's coefficients.

## The Almost-Commutative Triple and the Finite Geometry

The physical form of a spectral triple is almost commutative, and the framework's mass term turns out to sit exactly where the finite geometry's operator belongs.

**The product geometry.** An almost-commutative triple takes the algebra, Hilbert space, and operator as
$$
\mathcal{A}=C^\infty(M)\otimes\mathcal{A}_F,
\qquad
\mathcal{H}=L^2(S)\otimes\mathcal{H}_F,
\qquad
D=D_M\otimes I_F+G_M\otimes D_F,
$$
with $D_M$ the Dirac operator of the manifold, $G_M$ the chirality of its spinor factor, written with a capital to distinguish it from the finite chirality $\chi$, $D_F$ a finite matrix acting on $\mathcal{H}_F$, and the second term the only coupling to the finite geometry. The two gradings must not be confused: $G_M$ grades $L^2(S)$, while $\chi$ grades the chiral halves of $\Delta$, and it is $G_M$ that makes $D$ odd with respect to the manifold spinors. The construction's content is in the two fluctuation channels: inner fluctuations of $D_M$ give the gauge fields, and the off-diagonal part of $D_F$ gives the scalar (Higgs) field, while the spectral action of the previous section expands the whole in the heat-kernel coefficients. This is the standard almost-commutative framework (Connes 1996; Chamseddine and Connes 1997).

**The finite operator is the framework's mass term.** For the biquaternion candidate, $\mathcal{A}_F=\mathbb{B}_{\mathbb{R}}$ and $\mathcal{H}_F=\Delta=S\oplus S^{\mathrm{c}}\cong\mathbb{C}^4$, so $D_F$ is a $4\times4$ matrix with two $2\times2$ off-diagonal blocks. The requirement that $D_F$ be odd under the chirality — that it anticommute with $\chi$ — fixes the block form. On the regular module the chirality is the right action by $-i\vec e_z$, and the mass is the off-diagonal operator
$$
D_F=m\,\beta+\bar m\,\beta^{*},
\qquad
\chi D_F+D_F\chi=0.
$$
In the block basis $(S,S^{\mathrm{c}})$ the two operators are
$$
D_F=\begin{pmatrix}0&m\\ \bar m&0\end{pmatrix},
\qquad
\chi=\begin{pmatrix}-I_2&0\\0&I_2\end{pmatrix}.
$$
This was verified explicitly: the anticommutator vanishes identically, and $D_F^2=|m|^2I$ gives the two eigenvalues $\pm|m|$, each with multiplicity two, the expected particle and antiparticle masses. The identification is exact: **the series' off-diagonal mass is a finite Dirac operator of an almost-commutative spectral triple**, and it is odd under the chirality because it couples $S$ to $S^{\mathrm{c}}$. It does **not** couple the two Peirce copies: that copy flip is $\mathbb{B}$-linear and is not the chiral mass.

**Consequences.** Three consequences follow and are worth stating.

- The framework's mass term is not an added ingredient of its spectral triple; it is the triple's finite part, and the triple's product structure is what relates the mass to the chirality.
- The gauge fields are inner fluctuations of $D_M$ and the scalar field is the off-diagonal part of $D_F$, so the framework's gauge-field and mass content sit in the two channels the construction provides, without a further postulate.
- The gauge group would be the unitaries of the algebra modulo the central phase, which acts as a scalar and is invisible on states; with the framework's involution there are no unitaries to take in the first place. Since $\flat=-{}^{*}$, the condition $u^{\flat}u=1$ reads $-u^{*}u=1$, that is $u^{*}u=-1$, which no matrix satisfies because $u^{*}u$ is positive semidefinite. The pair $(\mathbb{B}_{\mathbb{R}},\flat)$ is therefore not a $C^{*}$-algebra, and $\flat$ is an antilinear involution on the algebra rather than a positive one. Under the $C^{*}$ involution ${}^{*}$ the unitaries of $\mathbb{B}\cong M_2(\mathbb{C})$ are $\mathrm{U}(2)$, and the quotient by the central $\mathrm{U}(1)$, a scalar phase that no state sees, is $\mathrm{PU}(2)\cong\mathrm{SO}(3)$, which is not the Standard-Model group. Either way the physical model-building — the fermion content, the anomaly-cancellation conditions, and the group — belongs to the gauge-field category and is not pursued here.

**The scale.** The finite operator's entries have the dimensions of mass, and the spectral action's expansion builds the scalar potential out of them, so the framework's $m$ is the finite geometry's scale. In the Standard-Model triple this is the mechanism that ties the scalar sector to the finite geometry instead of postulating it, and it produces, at tree level, a relation between the Higgs mass and the gauge couplings at the unification scale. Whether the biquaternion factor produces a comparable relation is not computed here; what is established is only that $m$ is where a finite geometry's scale would sit.

## What Is Established and What Is Interpretation

**Established (framework and algebra).**

- The biquaternion candidate triple: algebra $\mathbb{B}_{\mathbb{R}}$ (or $C^\infty(M)\otimes\mathbb{B}_{\mathbb{R}}$), Hilbert space the completion of $\Delta=S\oplus S^{\mathrm{c}}$ under the Hermitian form, operator $\mathcal{D}=i\tilde\nabla+D_F$. The Hilbert space and the operator are the series' own objects, and no new structure is introduced; $\tilde\nabla^{\dagger}=-\tilde\nabla^{\natural}$, so $i\tilde\nabla$ has adjoint $i\tilde\nabla^{\natural}$, and $i\tilde\nabla$ is not self-adjoint for the Hermitian form: the criterion asks for anti-Hermitian coefficients, which $ie_t$ is and the three $i\vec e_k$ are not.
- The framework's real-form involution satisfies $\flat^2=+1$ exactly: $\flat(\tilde Q)=-\tilde Q^{*}$ gives $\flat(\flat(\tilde Q))=\tilde Q$; verified on explicit quaternion matrices, so the candidate real structure $J_{\flat}$ has $\epsilon=+1$, the sign of a four-dimensional Euclidean geometry. The product rule is $(\tilde Q_1\tilde Q_2)^\flat=-\tilde Q_2^\flat\tilde Q_1^\flat$, and on the module the two minus signs cancel in $J_{\flat}b^{*}J_{\flat}^{-1}=\cdot b$, the right action.
- The Euclidean frame's antisymmetric operator of square $-1$ is $C:\psi\mapsto-\vec e_z\psi=E_1E_2$ in the frame $E_4:\psi\mapsto i\psi\vec e_x$, $E_k:\psi\mapsto-\vec e_k\psi\vec e_y$. The four frame operators are Hermitian, square to $+1$, and pairwise anticommute; the chirality $E_1E_2E_3E_4$, the right action by $-i\vec e_z$, squares to $+1$; $C$ is real and antisymmetric in the frame of the four units, $C^2=-I_4$, and $[C,E_1E_2E_3E_4]=0$. $C$ conjugates each generator to its transpose up to sign, and the sign is not uniform in this frame. The antilinear operator $J_C=CK$ therefore has $J_C^2=C^2=-1$ and $J_C\chi=-\chi J_C$, the quaternionic pattern $(\epsilon,\epsilon'')=(-1,-1)$. Both signs are fixed by the pair $(C,\chi)$ alone: they are invariant under a rescaling of $J$ and under a change of frame, so neither is a normalisation. $\epsilon'$ is not reached, because it involves $D$. The pattern is Connes' $n\equiv2$ (equivalently $n\equiv6$), while four-dimensional Euclidean geometry is $n\equiv4$ with $(+1,+1,+1)$; the table of *Spectral Triples and Noncommutative Geometry* has these two rows exchanged, and that disagreement is reported at the end of the section. The framework's own sign is $+1$: it agrees with the four-dimensional Euclidean sign and is not the quaternionic one, and the quaternionic sign can come only from the module's structure (equivalently $\mathrm{Cl}_{1,3}\cong M_2(\mathbb{H})$), not from a central phase, since composition with a central phase leaves $\epsilon=+1$.
- The order of the gradient commutator is decided by the Clifford coefficients: $[i\tilde\nabla,a\cdot]=i\sum_\mu[e_\mu,a]\partial/\partial Q_\mu$ is zeroth order exactly when $a$ commutes with all four units, so the left action of the matrix factor fails the bounded-commutator condition and only the central scalars and the functions pass it. The right action passes it identically for a constant factor and by a two-sided action for functions, and it fails the grading, since the chirality is itself a right action. The symbol check is exact: at $\xi=(0.3,-0.7,1.1,0.4)$ the largest entry of $[\sum_\mu\xi_\mu e_\mu,a]$ in the defining representation is $2.2$ for $\vec e_x$, $1.4$ for $\vec e_y$, $2.6$ for $\vec e_z$, and exactly $0$ for $e_t$ and $ie_t$. Being bilinear in $a$, the commutator scales with $a$'s coefficients, so only the units give a scale-free comparison.
- The first-order condition is decided by the module. On the regular module the gradient contributes nothing, $[[i\tilde\nabla,a\cdot],\cdot b]=0$ identically, because its commutator is a left action and a left action commutes with a right one; there the condition holds for the vector-like candidate, whose mass is a central right action. On $\Delta$ the opposite action is $\operatorname{diag}(b^{\mathsf T},\bar b^{\mathsf T})$ rather than a right action, the gradient's symbol survives, and the condition holds only on $\mathbb{R}e_t$: the gradient admits the centre $\mathbb{C}e_t$, the mass admits $\mathbb{R}[\vec e_y]$, and the condition is their intersection.
- The grading is a finite one. The chirality $\chi$, the right action by $-i\vec e_z$, commutes with every left action and so with the gradient, and anticommutes with the mass, $\{\chi,D_F\}=0$ (verified, residual $0$); $\mathcal{D}$ on $\Delta$ is therefore neither even nor odd under $\chi$. The finite triple $(\mathbb{B}_{\mathbb{R}},\Delta,D_F)$ is graded and odd; the grading of a full triple is $G_M\otimes\chi$ with $G_M$ the manifold chirality.
- The series' off-diagonal mass is a finite Dirac operator: $D_F=m\beta+\bar m\beta^{*}$ on $\Delta=S\oplus S^{\mathrm{c}}$ is $\left(\begin{smallmatrix}0&m\\ \bar m&0\end{smallmatrix}\right)$ in the block basis, anticommutes with the chirality $\chi=\operatorname{diag}(-I_2,I_2)$, and satisfies $D_F^2=|m|^2I$ with eigenvalues $\pm|m|$, each twice; both by inspection in the block form. The framework's mass is therefore the almost-commutative triple's finite part and not an added ingredient.
- The finite algebra's module $\Delta$ is four-complex-dimensional and its finite triple has spectral dimension zero; a dimension-four triple requires the almost-commutative algebra and a first-order elliptic operator. The spectral dimension is the exponent of the growth and $a_{d/2}$ the coefficient of the logarithmic divergence in one and the same small-$t'$ expansion.
- The framework's metric-as-output (a signature from the level-1 form on the material sector) and the triple's distance formula (a distance from $D$) are similar in shape and different in content; the framework derives a signature, not a distance.

**Standard, and transcribed.**

- The definition of a spectral triple; the compact-resolvent and bounded-commutator conditions; the axioms of dimension, regularity, finiteness, reality, first order, orientability, and Poincaré duality.
- The KO-dimension table and its dependence on the three signs; the Euclidean frame's antisymmetric $C$ with real entries and $C^2=-1$, and $J_C=CK$ with $J_C^2=-1$ and $J_C\chi=-\chi J_C$, the quaternionic pattern.
- The spectral dimension as the heat-kernel growth; the Seeley–DeWitt expansion.
- The distance formula and the metric reconstruction theorem.
- Inner fluctuations, the gauge group from the algebra's unitaries, the spectral action, and its heat-kernel expansion.
- Almost-commutative triples and product geometries; the two fluctuation channels (gauge fields from $D_M$, the scalar from $D_F$); the oddness of $D_F$ under the chirality; the finite scale appearing in the scalar potential.

**Interpretation.**

- Reading the framework's metric-as-output and the triple's distance formula as analogous moves is the framework's presentation; the two constructions are different and the article says so.
- Regarding the biquaternion spectral triple as the algebraic interpretation of the framework's objects, rather than as a model-building tool, is this article's placement of the subject.

**Open.**

- Whether $C^\infty(M)\otimes\mathbb{B}_{\mathbb{R}}$ with the framework's Dirac operator satisfies orientability and Poincaré duality is not checked here. Orientability would require exhibiting a Hochschild cycle representing the volume form, and Poincaré duality the non-degeneracy of the $K$-theoretic intersection form — neither attempted here.
- Which algebra and which side make the triple work is not settled. The functions pass the bounded-commutator condition and the matrix factor does not, in the left reading; the right reading trades that failure for the loss of the grading, and neither reading satisfies both. The corpus's two-sided operator theory is the natural place to look for the algebra that acts on the side the Clifford coefficients do not see, and no such algebra is constructed here.
- Whether the finite geometry selected by the biquaternion algebra is physically interesting — and whether the series' gauge-group content can be recovered as inner fluctuations — is a gauge-field-category question and is not addressed.
- Whether the triple can use a positive-definite form at all. The candidate operator is not self-adjoint for the Hermitian form — $ie_t$ is anti-Hermitian and the three $i\vec e_k$ are not — while it is self-adjoint for the Dirac form, which is indefinite. A spectral triple needs a self-adjoint $D$ on a Hilbert space, so either a different frame or a different form is needed, and the algebra does not decide which.
- The exact relation between the algebra's involution $\flat$ and the module's quaternionic structure $\mathcal{J}$ is stated qualitatively (via $\mathrm{Cl}_{1,3}\cong M_2(\mathbb{H})$) and is not constructed explicitly. In particular, the sign $\epsilon'$ of $JD=\epsilon'DJ$ is not computed.

## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *Why AXF Matrices instead of Pauli and Gamma Matrices*. A gamma is an array in a chosen basis and not an object of the algebra; the arrays below are written in the basis of the four units, and no statement in this article depends on the choice.

This article needs no gamma matrix, and they are collected here only for comparison with the literature, as a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$ and not as a different algebra.

Each gamma is the array, in the basis $e_t,\vec e_x,\vec e_y,\vec e_z$ of the algebra over $\mathbb{C}$, of one two-sided action:

$$
\gamma_0:\psi\longmapsto ie_t\psi\vec e_x,\qquad
\gamma_1:\psi\longmapsto i\vec e_x\psi\vec e_y,\qquad
\gamma_2:\psi\longmapsto i\vec e_y\psi\vec e_y,\qquad
\gamma_3:\psi\longmapsto i\vec e_z\psi\vec e_y,\qquad
\gamma_5:\psi\longmapsto-ie_t\psi\vec e_z.
$$

They satisfy $\gamma_0^2=I_4$, $\gamma_k^2=-I_4$, $\gamma_5^2=I_4$, $\{\gamma_\mu,\gamma_\nu\}=2\varepsilon_\mu\delta_{\mu\nu}I_4$ with $\varepsilon=(1,-1,-1,-1)$, $\{\gamma_5,\gamma_\mu\}=0$, and $\gamma_0\gamma_1\gamma_2\gamma_3=-i\gamma_5$; $\gamma_0$ and $\gamma_5$ are Hermitian and the three vector generators anti-Hermitian, and the pattern of squares is the signature $(+,-,-,-)$ of the corpus. All of it was checked on the arrays.

$\gamma_5$ is the chiral right action written as an array. The chirality of the body is right multiplication by $-i\vec e_z$, and $\gamma_5$ multiplies by $-i\vec e_z$ as well, from the right; the factor $e_t$ in front changes nothing, $e_t$ being the identity of the algebra. The central grading is a different object, $\chi=i\tilde\Xi_{\mathrm{ad}}=e_+-e_-$, the difference of the two central idempotents of the complexified algebra, with $\chi^2=e_t$ while $\tilde\Xi_{\mathrm{ad}}$ itself is a root of $-1$.

The dictionary is complex-linear. Writing $c(M)$ for the coefficient array of $M$ in the basis of the sixteen products, a single product is a pure tensor, the products form the seven-dimensional cone $\operatorname{rank}c(M)\le1$, and a general element is a sum of at most four, with $\ell(M)=\operatorname{rank}c(M)$.

The four generators of the Euclidean frame all square to $+1$, so over $\mathbb{R}$ they generate $\mathrm{Cl}_{4,0}\cong M_2(\mathbb{H})$. The real operators of *The Majorana Equation in Biquaternionic Form* are right multiplication by $\vec e_x$ and the three maps $\psi\mapsto\vec e_k\psi\vec e_y$, one of square $-1$ and three of square $+1$, and those generate $\mathrm{Cl}_{3,1}\cong M_4(\mathbb{R})$; the Euclidean frame is that frame with the first multiplied by $i$ and the three spatial operators negated. The corpus's $\mathrm{Cl}_{1,3}$ generators are $i$ times those, with the opposite pattern of squares, and $\mathrm{Cl}_{1,3}\cong M_2(\mathbb{H})$. The gammas are the same operators with the powers of $i$ collected — $\gamma_0$ is $E_4$ and $\gamma_k$ is $-iE_k$ — so they carry the Minkowski pattern of squares: this is the frame of the body's $\chi$, not a second algebra.

## Summary

The spectral triple of the biquaternion algebra is the candidate $(\mathbb{B}_{\mathbb{R}},\mathcal{H},\mathcal{D})$, with $\mathcal{H}$ the completion of the Dirac module $\Delta=S\oplus S^{\mathrm{c}}\cong\mathbb{C}^4$ under the Hermitian form
$$
\langle\tilde\Psi,\tilde\Phi\rangle=\mathrm{Sc}\bigl(\tilde\Psi^{*}\tilde\Phi\bigr),
$$
and the operator is the framework's Dirac operator,
$$
\mathcal{D}=i\tilde\nabla+D_F,
$$
with the off-diagonal mass $D_F=m\beta+\bar m\beta^{*}$. The algebra's real-form involution is $\flat=-{}^{*}$, with
$$
\flat^2=+1,
$$
and it is antilinear, so the candidate real structure $J_{\flat}$ has $J_{\flat}^2=+1$, that is $\epsilon=+1$, the sign that four-dimensional Euclidean geometry carries.

The sign that the algebra does not carry is the quaternionic one. The Euclidean frame's own operator gives the antilinear operator $J_C=CK$ with $J_C^2=-1$ and $J_C\chi=-\chi J_C$, and that is not a four-dimensional charge conjugation but the pattern the Standard-Model finite geometry carries at $n\equiv6$. Both signs were verified explicitly, and reaching the quaternionic one requires the module's structure, $\mathrm{Cl}_{1,3}\cong M_2(\mathbb{H})$, not a central phase.

Three conditions fail, and they fail for one reason: the Clifford coefficients are elements of the algebra. The bounded-commutator condition holds for the functions and fails for the non-central matrix elements under the left action, while the right action passes it and loses the grading. The first-order condition holds for the vector-like candidate on the regular module, where the opposite action is a right action, but for the chiral triple on $\Delta$ only on the real scalars. There the opposite action is a transposition, so the gradient admits the centre $\mathbb{C}e_t$ and the mass admits $\mathbb{R}[\vec e_y]$, and the condition is their intersection. The grading itself is the finite chirality $\chi$, the right action by $-i\vec e_z$, which commutes with the gradient and anticommutes with the mass, so the finite triple is graded and odd while the whole operator on $\Delta$ is graded by nothing, and a graded triple would need $G_M\otimes\chi$.

The spectral dimension is read from the heat-kernel growth $\mathrm{Tr}\,\exp(-t'D^2)\sim {t'}^{-d/2}$ and coincides with the Seeley–DeWitt data of the determinant and anomaly articles, giving $d=4$ for the almost-commutative triple and $d=0$ for the bare finite algebra. The distance formula's metric-as-output is the spectral triple's counterpart of the framework's signature-as-output, similar in shape and different in content. Inner fluctuations, the gauge group, and the spectral action $\mathrm{Tr}f(D_A/\Lambda)$ are the standard neighbouring construction, cited and not developed here.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(\mathcal{A},\mathcal{H},D)$ | Spectral triple: algebra, Hilbert space, Dirac operator |
| $\mathbb{B}_{\mathbb{R}}$ | Biquaternion algebra as a real algebra, the candidate $\mathcal{A}$ |
| $\Delta=S\oplus S^{\mathrm{c}}\cong\mathbb{C}^4$ | Dirac module, the candidate $\mathcal{H}$ |
| $\mathcal{D}=i\tilde\nabla+D_F$ | Biquaternion Dirac operator, the candidate $D$; not self-adjoint for the Hermitian form |
| $\langle\tilde\Psi,\tilde\Phi\rangle=\mathrm{Sc}(\tilde\Psi^{*}\tilde\Phi)$ | Hermitian inner product on $\Delta$ |
| $J$ | Real structure of a spectral triple; antilinear, with $J^2=\epsilon I$ |
| $J_{\flat}$ | The framework's real structure on the module, from $\flat=-{}^{*}$; $J_{\flat}^2=+1$ |
| $J_C$ | The Euclidean frame's real structure, $J_C=CK$; $J_C^2=-1$ |
| $\epsilon,\epsilon',\epsilon''$ | Signs $J^2=\epsilon$, $JD=\epsilon'DJ$, $J\chi=\epsilon''\chi J$; they fix the KO-dimension |
| $\chi=i\tilde\Xi_{\mathrm{ad}}=e_+-e_-$; on the regular module the right action $\psi\mapsto-i\psi\vec e_z$ | Chirality operator of the triple, $\operatorname{diag}(-I_2,I_2)$ on $\Delta$; $\tilde\Xi_{\mathrm{ad}}^2=-e_t$ and $\chi^2=e_t$ |
| $P$ | Peirce index, the right action $\psi\mapsto i\psi\vec e_z$; $\chi=-P$ as maps, grading the regular module |
| $\mathbb{R}[\vec e_y]$ | The copy of $\mathbb{C}$ inside $\mathbb{B}_{\mathbb{R}}$; the fixed set of the conjugation, and the largest subalgebra on which $D_F$ commutes with the left action |
| $\flat=-{}^{*}$ | The framework's real-form involution; $\flat^2=+1$ |
| $\tilde\nabla=\sum_\mu e_\mu\,\partial/\partial Q_\mu$ | Biquaternion gradient; symbol $\sum_\mu\xi_\mu e_\mu$ of quaternion norm $\lvert\xi\rvert^2$ |
| $\beta:S^{\mathrm{c}}\to S$ | The invariant pairing $\beta(s,t)=s^{\dagger}t$ of *The Unpolarized Module of the Biquaternion Algebra*, i.e. the identity on the underlying spinors; its adjoint is the other off-diagonal block |
| $\mathrm{Cl}_{1,3}\cong M_2(\mathbb{H})$ | Quaternionic structure of the module |
| $d(\varphi,\omega)=\sup_{a\in\mathcal{A}}\{\lvert\varphi(a)-\omega(a)\rvert:\lVert[D,a]\rVert\le1\}$ | Distance formula between two states |
| $\mathrm{Tr}\,\exp(-t'D^2)\sim {t'}^{-d/2}$ | Heat-kernel growth; the spectral dimension |
| $D_A=D+\sum a_i[D,b_i]$ | Inner fluctuation; the gauge field |
| $\mathrm{Tr}\,f(D_A/\Lambda)$ | Spectral action |
| $\mathcal{A}_F,\mathcal{H}_F,D_F$ | Finite algebra $\mathbb{B}_{\mathbb{R}}$, finite Hilbert space $\Delta$, finite Dirac operator (the off-diagonal mass) |
| $D_F=m\beta+\bar m\beta^{*}$ | Mass operator; in the block basis $\left(\begin{smallmatrix}0&m\\ \bar m&0\end{smallmatrix}\right)$ |
| $D=D_M\otimes I_F+G_M\otimes D_F$ | Product geometry of an almost-commutative triple; $G_M$ the manifold chirality |
| $\Gamma=G_M\otimes\chi$ | Grading of a full triple; $D$ odd in it, while $\mathcal{D}$ alone is odd in neither factor |
| $a\cdot$, $\cdot b$ | Left action $\psi\mapsto a\psi$ and right action $\psi\mapsto\psi b$; they commute |
| $a\,\cdot\,b$ | Two-sided action $\psi\mapsto a\psi b$; the sixteen $\psi\mapsto e_\mu\psi e_\nu$ span $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ |
| $E_4:\psi\mapsto i\psi\vec e_x$, $E_k:\psi\mapsto-\vec e_k\psi\vec e_y$ | Euclidean frame, four Hermitian generators with $E_\mu^2=+1$ |
| $C:\psi\mapsto-\vec e_z\psi=E_1E_2$ | Euclidean candidate charge conjugation; real and antisymmetric, $C^2=-1$, $[C,E_1E_2E_3E_4]=0$ |
| $E_1E_2E_3E_4$, the right action by $-i\vec e_z$ | Euclidean chirality; its square is $+1$ |

## Further Reading

- [Why AXF Matrices instead of Pauli and Gamma Matrices](why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the reasons the AXF matrices replace the Pauli and gamma matrices.
- A. Connes, *Noncommutative Geometry* (Academic Press, 1994), for the founding treatment of spectral triples.
- A. Connes, "Noncommutative geometry and reality," *Journal of Mathematical Physics* **36** (1995) 6194–6231, for the real structure, the axioms, and the KO-dimension.
- A. Connes, "Gravity coupled with matter and the foundation of non-commutative geometry," *Communications in Mathematical Physics* **182** (1996) 155–176, for inner fluctuations and the spectral action.
- A. Chamseddine and A. Connes, "The spectral action principle," *Communications in Mathematical Physics* **186** (1997) 731–750, for the spectral action and its heat-kernel expansion.
- A. Connes and M. Marcolli, *Noncommutative Geometry, Quantum Fields and Motives* (American Mathematical Society, 2008), for the axiomatic treatment used here.
- J. M. Gracia-Bondía, J. C. Várilly, and H. Figueroa, *Elements of Noncommutative Geometry* (Birkhäuser, 2001), for the axioms and the distance formula.
- P. Gilkey, *Invariance Theory, the Heat Equation, and the Atiyah–Singer Index Theorem* (CRC Press, 1995), for the heat-kernel coefficients that give the spectral dimension.
- N. Berline, E. Getzler, and M. Vergne, *Heat Kernels and Dirac Operators* (Springer, 1992), for the Dirac operator's spectrum and the index-theoretic structure.
- D. V. Vassilevich, "Heat kernel expansion: user's manual," *Physics Reports* **388** (2003) 279–360, for the Seeley–DeWitt expansion shared with the determinant and anomaly articles.
- [Spectral Triples and Noncommutative Geometry](../articles_maths/spectral-triples-and-noncommutative-geometry.html), for the axioms and the KO sign table used here, and [Norm and Pairing Conventions](norm-and-pairing-conventions.html), for the Hermitian form.
- Companion articles: [The Functional Determinant in Biquaternionic Form](the-functional-determinant-in-biquaternionic-form.html), for the heat-kernel coefficients and the Seeley–DeWitt data; [The Trace Anomaly in Biquaternionic Form](the-trace-anomaly-in-biquaternionic-form.html), for the same data in its conformal interpretation; [The Feynman Propagator in Biquaternionic Form](the-feynman-propagator-in-biquaternionic-form.html), for the spinor module and the Dirac operator; [The Hermitian GNS Construction in the Biquaternion Framework](the-hermitian-gns-construction-in-the-biquaternion-framework.html), for the Hilbert-space structure the triple requires; [Conventions in the Biquaternion Universe](algebra-and-element-conventions.html), for the real-form involution $\flat$, the quaternionic isomorphism $\mathrm{Cl}_{1,3}\cong M_2(\mathbb{H})$, and the three metric levels.
