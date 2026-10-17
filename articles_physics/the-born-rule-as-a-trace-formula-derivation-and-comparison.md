# __The Born Rule as a Trace Formula — Derivation and Comparison__

## Introduction

The companion article *Quantum Physics in Biquaternionic Form* identifies the Hermitian subspace $\mathbb{M}_+$ of the biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ as the common home of the states and observables of a two-state system, and states the Born rule there as the trace formula

$$
\mathrm{Tr}(\tilde{P}\tilde{H})=2\,\mathrm{Sc}(\tilde{P}\tilde{H}) = 2\langle\tilde{P},\tilde{H}\rangle.
$$

Earlier articles use the formula; this article develops it and, as the title promises, separates what the framework **derives** from what it merely **restates**.

The distinction matters because $\mathbb{B}\cong M_2(\mathbb{C})$: any probability formula in the algebra is a formula about $2\times2$ matrices, and any claim that the framework "derives" the Born rule must be read against that isomorphism. What the algebra genuinely supplies is a canonical bilinear pairing — the trace pairing — a canonical family of rank-one idempotents, and the theorem that pairing a state with an idempotent (or an effect) yields a real number in $[0,1]$, that the numbers over a complete family sum to one, and that the pure-state transition probability is $\cos^2(\theta/2)$. That is algebra, and it is derived. What the algebra does not supply is the identification of those numbers with physical frequencies; that is the Born rule itself, and the framework relocates it rather than eliminating it.

The article develops the trace pairing and its naturalness; identifies the idempotents with rank-one projectors and derives $p=\mathrm{Tr}(\tilde{P}\tilde{\rho})$; treats effects and non-projective POVMs; compares the result with the standard statements $p=\mathrm{Tr}(E\rho)$ and $|\langle\psi|\phi\rangle|^2$; examines the non-uniqueness of the trace; and closes with an explicit accounting of derivation versus restatement. The standard of proof throughout is algebraic: every claim is a statement about $\mathbb{B}$ and its trace, checkable by expanding in the basis $\{e_t,i\vec e_x,i\vec e_y,i\vec e_z\}$, and no empirical input is used. Conventions are those of the companion articles: $e_t=1,\vec e_x,\vec e_y,\vec e_z$ with $\vec e_\mu^2=-e_t$; scalar imaginary $i$; $\mathbb{B}=\mathbb{M}_+\oplus\mathbb{M}_-$; and $\mathrm{Tr}(\tilde{H})=2\,\mathrm{Sc}(\tilde{H})$. Here $\mathrm{tr}$ denotes the ordinary $2\times2$ trace, related to $\mathrm{Tr}$ by $\mathrm{tr}\circ\varphi=\mathrm{Tr}$.

## The Trace Pairing on $\mathbb{M}_+$

### The Pairing and Its Naturalness

An element of $\mathbb{M}_+$ is $\tilde{H}=h_0e_t+i\vec h$, with $h_0\in\mathbb{R}$ and $\vec h=(h_1,h_2,h_3)\in\mathbb{R}^3$. The trace is

$$
\mathrm{Tr}(\tilde{H})=2\,\mathrm{Sc}(\tilde{H})=2h_0 .
$$

It is **tracial**, $\mathrm{Tr}(\tilde{Q}\tilde{Y})=\mathrm{Tr}(\tilde{Y}\tilde{Q})$, because $\mathrm{Sc}(\tilde{Q}\tilde{Y})=Q_tY_0-\sum_kQ_kY_k$ is symmetric, and **normalized** by $\mathrm{Tr}(e_t)=2$, the dimension of the algebra's representation. It defines the **trace pairing**

$$
\mathrm{Tr}(\tilde{H}\tilde{K})=2(h_0k_0+\vec h\cdot\vec k),
$$

obtained from $\tilde{H}\tilde{K}=(h_0k_0+\vec h\cdot\vec k)e_t+i(h_0\vec k+k_0\vec h)-\vec h\times\vec k$, using $(i\vec h)(i\vec k)=(\vec h\cdot\vec k)e_t-\vec h\times\vec k$. In the basis $\{e_t,i\vec e_x,i\vec e_y,i\vec e_z\}$ the Gram matrix is diagonal, with $\mathrm{Tr}(e_t e_t)=2$, $\mathrm{Tr}(e_t\,i\vec e_\mu)=0$ and $\mathrm{Tr}(i\vec e_\mu\,i\vec e_\nu)=2\delta_{\mu\nu}$. The pairing is positive-definite of signature $(4,0)$: up to the factor $2$, the Euclidean inner product on $\mathbb{R}^4$, and the restriction of the Hilbert–Schmidt form.

Two immediate consequences will be used repeatedly. First, the pairing is bilinear and symmetric: $\mathrm{Tr}(\tilde{H}\tilde{K})=\mathrm{Tr}(\tilde{K}\tilde{H})$, and expansion in the basis gives $\mathrm{Tr}((\alpha\tilde{H}+\beta\tilde{K})\tilde{L})=\alpha\,\mathrm{Tr}(\tilde{H}\tilde{L})+\beta\,\mathrm{Tr}(\tilde{K}\tilde{L})$. Second, it is positive definite, since $\mathrm{Tr}(\tilde{H}^2)=2(h_0^2+|\vec h|^2)\geq0$ with equality only for $\tilde{H}=0$; the trace pairing is therefore an inner product, not merely a symmetric form.

Three properties single it out. **Invariance:** under unitary conjugation $\tilde{H}\mapsto\tilde{U}\tilde{H}\tilde{U}^{*}$ the pairing is invariant; since the unit quaternions rotate $\vec h$ and fix $h_0$, an invariant symmetric bilinear form must be $\mathrm{B}=A h_0k_0+B\,\vec h\cdot\vec k$, so invariance alone leaves two parameters. **Traciality:** requiring the pairing to come from the algebra's product, $\mathrm{B}(\tilde{H},\tilde{K})=f(\tilde{H}\tilde{K})$ with $f$ tracial, forces $f$ to be a multiple of $\mathrm{Tr}$ and hence $A=B$; this is the condition that pins the form down. **Positivity:** $A,B>0$ makes the form positive-definite, capable of producing non-negative probabilities; the scale is fixed by $\mathrm{Tr}(e_t)=2$, though the scale cancels in probabilities, which are ratios. Thus the trace pairing is the unique symmetric pairing compatible with the associative product and positive — but traciality is a genuine assumption, not a consequence of symmetry.

### It Is Not the Biquaternion Norm

The other natural quadratic form on $\mathbb{M}_+$ is the **biquaternion norm**

$$
\langle\tilde{H}\rangle_{\natural} = \langle\tilde{H},\tilde{H}\rangle_{\natural}=\tilde{H}\tilde{H}^{\natural}=(h_0^2-|\vec h|^2)e_t,
$$

of signature $(1,3)$, whose future light cone is the positivity cone. The state space is the trace-one slice of that cone; the Born rule is a statement about the trace pairing. Positivity of a state is a biquaternion-norm condition, while Born probabilities are trace-pairing quantities. The Born rule therefore does not follow from the light-cone structure of $\mathbb{M}_+$; it follows from the Euclidean trace pairing, a different form on the same space.

The two forms are complementary, and the idempotents show it clearly. For $\tilde\Pi_{1,2}(\vec u)$ one has $h_0=\tfrac12$ and $|\vec h|=\tfrac12$, so the biquaternion norm vanishes,
$$
\langle\tilde\Pi_{1,2}\rangle_{\natural}=\tilde\Pi_{1,2}\tilde{P}^{\natural}_\pm=(h_0^2-|\vec h|^2)e_t=0,
$$
placing the idempotents on the boundary of the light cone, while the trace pairing gives $\mathrm{Tr}(\tilde\Pi_{1,2})=1$ and $\mathrm{Tr}(\tilde\Pi_{1,2}^2)=1$. The idempotents are null for the biquaternion norm and unit for the trace pairing; probabilities are read from the second, not the first.

## Idempotents as Projectors

The bridge to the standard formulas is the $*$-isomorphism $\varphi:\mathbb{B}\to M_2(\mathbb{C})$ with

$$
e_t\mapsto I_2,\qquad \vec e_\mu\mapsto-i\sigma_\mu\quad(\mu=1,2,3),
$$

the convention of the companion article. It gives $\varphi(\tilde{H})=h_0I_2+\vec h\cdot\boldsymbol{\sigma}$, so $\mathbb{M}_+$ maps onto the Hermitian $2\times2$ matrices, and, the Pauli matrices being traceless,

$$
\mathrm{tr}\,\varphi(\tilde{Q})=2\,\mathrm{Sc}(\tilde{Q})=\mathrm{Tr}(\tilde{Q}),
\qquad\text{hence}\qquad
\mathrm{Tr}(\tilde{H}\tilde{K})=\mathrm{tr}\bigl(\varphi(\tilde{H})\varphi(\tilde{K})\bigr).
$$

The idempotents of $\mathbb{M}_+$,

$$
\tilde\Pi_{1,2}(\vec u)=\tfrac{1}{2}(e_t\pm i\vec u),\qquad|\vec u|=1,
$$

satisfy $\varphi(\tilde\Pi_1(\vec u))=\tfrac{1}{2}(I_2+\vec u\cdot\boldsymbol{\sigma})$ because $\varphi(i\vec u)=\vec u\cdot\boldsymbol{\sigma}$. This is the standard spin-up projector; it has eigenvalues $1$ and $0$, so the biquaternion idempotent **is** a rank-one projection, and every rank-one projection arises this way. The usual identities hold: $\tilde\Pi_{1,2}^2=\tilde\Pi_{1,2}$, $\tilde\Pi_{1,2}^{*}=\tilde\Pi_{1,2}$, $\mathrm{Tr}(\tilde\Pi_{1,2})=1$, $\tilde\Pi_1+\tilde\Pi_2=e_t$, $\tilde\Pi_1\tilde\Pi_2=0$.

The idempotent property can be checked directly, without invoking the isomorphism. For unit $\vec u$,
$$
\tilde\Pi_1^2=\tfrac14\bigl(e_t+i\vec u\bigr)^2=\tfrac14\bigl(e_t+2i\vec u+(i\vec u)(i\vec u)\bigr),
$$
and $(i\vec u)(i\vec u)=(\vec u\cdot\vec u)e_t-\vec u\times\vec u=e_t$, so $\tilde\Pi_1^2=\tfrac12(e_t+i\vec u)=\tilde\Pi_1$; similarly $\tilde\Pi_2^2=\tilde\Pi_2$ and $\tilde\Pi_1\tilde\Pi_2=\tfrac14(e_t-|\vec u|^2e_t)=0$. Conversely, every rank-one projector in $M_2(\mathbb{C})$ has the form $\tfrac12(I_2+\vec u\cdot\boldsymbol{\sigma})$, so the map $\vec u\mapsto\tilde\Pi_1(\vec u)$ is a bijection between the Bloch sphere and the rank-one projections of the algebra.

A **state** is a positive trace-one element

$$
\tilde{\rho}=\tfrac{1}{2}(e_t+i\vec r),\qquad|\vec r|\leq1,
$$

mapping to the density matrix $\tfrac{1}{2}(I_2+\vec r\cdot\boldsymbol{\sigma})$. An **effect** is an element $\tilde{E}\in\mathbb{M}_+$ with $0\leq\tilde{E}\leq e_t$ in the matrix order; effects represent measurement outcomes.

## Derivation of the Born Probability

For $\tilde{H}=h_0e_t+i\vec h$ and $\tilde{\rho}=\tfrac{1}{2}(e_t+i\vec r)$, the trace pairing gives the expectation value

$$
\langle\tilde{H}\rangle_{\tilde{\rho}}=\mathrm{Tr}(\tilde{\rho}\tilde{H})=h_0+\vec r\cdot\vec h.
$$

**The material element behind the reading.** Every Hermitian $\tilde H$ is $\tilde H=iA$ for a unique anti-Hermitian $A\in\mathbb{M}_-$, the **material element** that is observed. With this substitution the expectation is $\langle iA\rangle_{\tilde\rho}=\mathrm{Tr}(\tilde\rho\,iA)=i\,\mathrm{Tr}(\tilde\rho A)$: the trace $\mathrm{Tr}(\tilde\rho A)$ is purely imaginary, and the factor $i$ makes the reading real. The Born pairing pairs an $\mathbb{M}_+$ state with an $\mathbb{M}_-$ material element, and the two senses of "observable" are the two writings of one element, the object $A$ and its representative $iA$.

The spectral decomposition is likewise purely algebraic. Writing $\tilde{H}=h_0e_t+i|\vec h|\vec u_h$ and multiplying by $\tilde\Pi_{1,2}(\vec u_h)$, using $(i\vec u_h)(i\vec u_h)=e_t$, gives
$$
\tilde{H}\tilde\Pi_1(\vec u_h)=(h_0+|\vec h|)\tilde\Pi_1(\vec u_h),\qquad \tilde{H}\tilde\Pi_2(\vec u_h)=(h_0-|\vec h|)\tilde\Pi_2(\vec u_h),
$$
so the eigenvalues are $\lambda_\pm=h_0\pm|\vec h|$ and the spectral projectors are the idempotents. The statement that the idempotents are complete, $\tilde\Pi_1+\tilde\Pi_2=e_t$, is the algebraic form of the spectral theorem for $\tilde{H}\in\mathbb{M}_+$.

For a spectral decomposition $\tilde{H}=\lambda_+\tilde\Pi_1(\vec u_h)+\lambda_-\tilde\Pi_2(\vec u_h)$, with $\vec u_h=\vec h/|\vec h|$, $\lambda_\pm=h_0\pm|\vec h|$ and $\tilde\Pi_1+\tilde\Pi_2=e_t$, the probability of the $+$ outcome is $p_+=\mathrm{Tr}(\tilde\Pi_1(\vec u_h)\tilde{\rho})$. Directly,

$$
\tilde\Pi_1(\vec u_h)\tilde{\rho}=\tfrac{1}{4}\bigl[(1+\vec u_h\cdot\vec r)e_t+i(\vec u_h+\vec r)-\vec u_h\times\vec r\bigr],
$$

so

$$
p_+=\tfrac{1}{2}(1+\vec u_h\cdot\vec r),\qquad p_-=\tfrac{1}{2}(1-\vec u_h\cdot\vec r).
$$

The pairing also reproduces the variance. From $\tilde{H}^2=(h_0^2+|\vec h|^2)e_t+2h_0\,i\vec h$,
$$
\langle\tilde{H}^2\rangle_{\tilde{\rho}}=\mathrm{Tr}(\tilde{\rho}\tilde{H}^2)=h_0^2+|\vec h|^2+2h_0\,\vec r\cdot\vec h,
$$
so
$$
\langle\tilde{H}^2\rangle_{\tilde{\rho}}-\langle\tilde{H}\rangle_{\tilde{\rho}}^2=|\vec h|^2-(\vec r\cdot\vec h)^2=|\vec h|^2\bigl(1-(\vec r\cdot\vec u_h)^2\bigr)\geq0,
$$
vanishing precisely when $\vec r=\pm\vec u_h$, i.e. when the state is an eigenstate of the observable. This is a nontrivial check that the statistical content is carried by the trace pairing and not by the biquaternion norm.

Three algebraic properties make the pairing a probability assignment. **Reality:** for $\tilde{H},\tilde{K}\in\mathbb{M}_+$, $\mathrm{Sc}(\tilde{H}\tilde{K})=h_0k_0+\vec h\cdot\vec k\in\mathbb{R}$, so the pairing is real without conjugation. **Positivity:** if $\tilde{P}\geq0$ and $\tilde{\rho}\geq0$ then $\mathrm{Tr}(\tilde{P}\tilde{\rho})\geq0$, since under $\varphi$ this is $A,B\geq0\Rightarrow\mathrm{tr}(AB)=\mathrm{tr}(\sqrt{A}B\sqrt{A})\geq0$; with $|\vec r|\leq1$ it also gives $p_+\leq1$. **Normalization:** by completeness and traciality,

$$
p_++p_-=\mathrm{Tr}\bigl((\tilde\Pi_1+\tilde\Pi_2)\tilde{\rho}\bigr)=\mathrm{Tr}(e_t\tilde{\rho})=\mathrm{Tr}(\tilde{\rho})=1.
$$

What is derived is the **form** of the rule: a canonical positive pairing, a complete orthogonal family of idempotents, real numbers in $[0,1]$ summing to one. With a pure state $\tilde\Pi(\vec u_y)$ in place of $\tilde{\rho}$, the same computation gives the **transition probability**

$$
\mathrm{Tr}\bigl(\tilde\Pi(\vec u_x)\tilde\Pi(\vec u_y)\bigr)=\tfrac{1}{2}(1+\vec u_x\cdot\vec u_y)=\cos^2\frac{\theta}{2},
$$

manifestly symmetric because the trace pairing is symmetric.

### What Is Derived Here

It is worth stating exactly what has been shown. The algebra fixes the pairing and the idempotents; from these, realness, positivity, and normalization of $p_+$ follow. Nothing else was used: no inner product was chosen, no Hilbert space was assumed, and no frequentist input entered. What has *not* been shown is that these numbers are observed frequencies. That identification is the Born rule, and it is an empirical postulate in the standard formalism as well. The algebraic development shows that once the pairing and the idempotents are fixed, the *structure* of the probability assignment is forced; it does not manufacture the link to experiment. The remaining sections verify that the structure is exactly the standard one and catalogue where uniqueness does and does not hold.

## General Measurements: Effects and POVMs

Writing an effect as $\tilde{E}=a\,e_t+i\vec w$, its matrix $aI_2+\vec w\cdot\boldsymbol{\sigma}$ has eigenvalues $a\pm|\vec w|$, and

$$
\tilde{E}\geq0\iff a\geq|\vec w|,\qquad \tilde{E}\leq e_t\iff 1-a\geq|\vec w|,
$$

so $\tilde{E}$ is an effect precisely when $0\leq a\leq1$ and $|\vec w|\leq\min(a,1-a)$. The two inequalities are exactly the requirement that both eigenvalues of the matrix lie in $[0,1]$. The rank-one projectors sit at $a=\tfrac12$, $|\vec w|=\tfrac12$, which are extreme points of the effect interval. A **POVM** is a finite set of effects with $\tilde{E}_i\geq0$ and $\sum_i\tilde{E}_i=e_t$. The outcome probabilities are

$$
p_i=\mathrm{Tr}(\tilde{E}_i\tilde{\rho})=2\,\mathrm{Sc}(\tilde{E}_i\tilde{\rho})=a_i+\vec w_i\cdot\vec r,
$$

where $\tilde{E}_i=a_ie_t+i\vec w_i$, and $\sum_ia_i=1$, $\sum_i\vec w_i=0$ are exactly $\sum_i\tilde{E}_i=e_t$. Reality, positivity, and normalization ($\sum_ip_i=\mathrm{Tr}(e_t\tilde{\rho})=1$) follow from the algebra; projective measurements are the case of orthogonal idempotents.

Two examples make the non-projective case concrete. The **unsharp measurement** with $0\leq\eta\leq1$ and unit $\vec u$ is $\tilde{E}_\pm=\tfrac12(e_t\pm i\eta\vec u)$, a POVM since $a=\tfrac12$ and $|\vec w|=\eta/2\leq\tfrac12$, with $p_\pm=\tfrac12(1\pm\eta\vec u\cdot\vec r)$; it is projective only at $\eta=1$, because

$$
\tilde{E}_+^2-\tilde{E}_+=\tfrac14(\eta^2-1)e_t .
$$

The **trine measurement**, with three unit vectors $\vec u_k$ at $120^\circ$ (so $\sum_k\vec u_k=0$), is

$$
\tilde{E}_k=\tfrac13(e_t+i\vec u_k)=\tfrac23\tilde\Pi_1(\vec u_k),\qquad k=0,1,2 .
$$

Each is an effect, they sum to $e_t$, and no two are orthogonal; the probabilities are $p_k=\tfrac13(1+\vec u_k\cdot\vec r)$ with $\sum_kp_k=1$. The trace formula thus covers general measurement statistics unchanged. Non-projective measurements are not exotic: they are needed for tasks such as unambiguous discrimination of non-orthogonal states, and the effect formalism is the algebraic home of that possibility.

The trace formula gives measurement **statistics**, not the post-measurement state; the update requires Kraus operators $\tilde{K}_i$ with $\sum_i\tilde{K}_i^{*}\tilde{K}_i=e_t$, treated in the companion article on quantum channels, and every POVM with $k$ outcomes has a Neumark dilation to a projective measurement on $\mathbb{B}\otimes_\mathbb{C}M_k(\mathbb{C})\cong M_{2k}(\mathbb{C})$, the article's two- and three-outcome examples living inside $\mathbb{B}\otimes_\mathbb{C}\mathbb{B}\cong M_4(\mathbb{C})$.

## Comparison with the Hilbert-Space Statement

In standard quantum physics a state is a density operator $\rho$, an observable is $A=\sum_aaP_a$, and $p(a)=\mathrm{Tr}(P_a\rho)$; for a pure state and a rank-one outcome projector this is $p=|\langle\phi|\psi\rangle|^2$. This is a **postulate**, motivateable by Gleason's theorem, decision theory, or envariance, but not derived from the other postulates. Because $\varphi$ is a $*$-isomorphism with $\mathrm{tr}\circ\varphi=\mathrm{Tr}$, the two formulations agree **exactly**:

$$
\mathrm{Tr}(\tilde{P}\tilde{\rho})=\mathrm{tr}\bigl(\varphi(\tilde{P})\varphi(\tilde{\rho})\bigr),\qquad
\mathrm{Tr}\bigl(\tilde\Pi(\vec u_x)\tilde\Pi(\vec u_y)\bigr)=\tfrac12(1+\vec u_x\cdot\vec u_y)=\cos^2\frac{\theta}{2}=\bigl|\langle\vec u_x+|\vec u_y+\rangle\bigr|^2,
$$

and the general Hilbert-space statement $p=\mathrm{Tr}(E\rho)$ coincides with the POVM form above. Concretely, the correspondences are: (i) idempotent $\leftrightarrow$ rank-one projector; (ii) state $\leftrightarrow$ density matrix; (iii) trace pairing $\leftrightarrow$ Hilbert–Schmidt inner product; (iv) $\mathrm{Tr}(\tilde\Pi(\vec u_x)\tilde\Pi(\vec u_y))=\cos^2(\theta/2)$ $\leftrightarrow$ $|\langle\vec u_x+|\vec u_y+\rangle|^2$; (v) POVM in effects $\leftrightarrow$ POVM in operators. Each is an identity under $\varphi$, not an approximation. The agreement is not a coincidence to be tested but an identity of notations, because $\mathbb{B}$ and $M_2(\mathbb{C})$ are the same algebra; any derivation in $\mathbb{B}$ is a derivation about $2\times2$ matrices.

The formulations differ in what they take as primitive. In the standard formalism a state is a vector and an observable an operator on vectors — different kinds of object; here both are elements of the single four-dimensional real space $\mathbb{M}_+$, paired symmetrically. The statement $|\langle\phi|\psi\rangle|^2$ is quadratic in amplitudes, while $\mathrm{Tr}(\tilde{P}\tilde{Q})$ is bilinear in projectors, so the symmetry of the transition probability is manifest rather than implicit. Writing $|\langle\phi|\psi\rangle|^2$ requires choosing a Hilbert space and an inner product; the biquaternion pairing is supplied by the algebra's own product — it is the trace, singled out by traciality. This is the substance of the claim that the Born rule is a consequence of the algebra: the form of the pairing is not chosen, it is read off. The vector statement covers only pure states, whereas the trace formula covers pure and mixed states and POVMs alike; it is a generalization of the vector statement, though a restatement of the general statement $p=\mathrm{Tr}(E\rho)$.

The comparison is for a single qubit, $\mathbb{B}\cong M_2(\mathbb{C})$. The extension to $n$ qubits uses $\mathbb{B}^{\otimes_\mathbb{C}n}\cong M_{2^n}(\mathbb{C})$ with $\mathrm{Tr}(x\otimes y)=\mathrm{Tr}(x)\mathrm{Tr}(y)$, and the trace formula reproduces the standard Born rule there. The split $\mathbb{B}=\mathbb{M}_+\oplus\mathbb{M}_-$ exists for every $M_n(\mathbb{C})$, so "states and observables in one space" is not special to $n=2$; what is special is the identification with the biquaternion units and the factor $2$ in $\mathrm{Tr}=2\,\mathrm{Sc}$.

## Non-Uniqueness of the Trace

On $M_n(\mathbb{C})$ the functionals satisfying $f(XY)=f(YX)$ form a one-dimensional space spanned by the trace. Hence on $\mathbb{B}\cong M_2(\mathbb{C})$ every tracial functional is $f=\lambda\mathrm{Tr}$, and every symmetric pairing $\mathrm{B}(\tilde{H},\tilde{K})=f(\tilde{H}\tilde{K})$ with $f$ tracial is a multiple of the trace pairing. The normalization $\mathrm{Tr}(e_t)=2$ fixes $\lambda=1$; the normalized alternative $\tfrac12\mathrm{Tr}=\mathrm{Sc}$ sends $e_t\mapsto1$. Either gives the same probabilities, since the scale cancels in $p_i=\mathrm{Tr}(\tilde{E}_i\tilde{\rho})/\mathrm{Tr}(\tilde{\rho})$ with $\mathrm{Tr}(\tilde{\rho})=1$.

Uniqueness fails as soon as traciality is dropped. Keeping symmetry, invariance, and positivity leaves

$$
\mathrm{B}(\tilde{H},\tilde{K})=A\,h_0k_0+B\,\vec h\cdot\vec k,\qquad A,B>0,
$$

a genuine two-parameter family; traciality is the extra condition $A=B$. Keeping positivity and normalization but dropping traciality, the normalized positive functionals on $\mathbb{M}_+$ are exactly the states: for every $\vec q\in\mathbb{R}^3$ with $|\vec q|\leq1$,

$$
f_{\vec q}(\tilde{H})=h_0+\vec q\cdot\vec h
$$

is positive on the positive cone, being the pairing with the state $\tilde{\rho}_{\vec q}=\tfrac12(e_t+i\vec q)$. Why is positivity restricted to $|\vec q|\leq1$? Under $\varphi$ the functional is $f_{\vec q}(\tilde{H})=\mathrm{tr}(\rho_{\vec q}A)$ with $A=\varphi(\tilde{H})$ and $\rho_{\vec q}=\tfrac12(I+\vec q\cdot\boldsymbol{\sigma})$; positivity of the functional is positivity of the density matrix, which holds exactly when $\vec q$ lies in the Bloch ball. The trace corresponds to $\vec q=0$, the maximally mixed state, which is the only point at which the functional is tracial. The trace is not the unique functional "chosen by nature"; it is the unique *tracial* functional. Concretely, extending $f_{\vec q}$ to $\mathbb{B}$ by $f_{\vec q}(\tilde{Q})=\mathrm{Re}(Q_t)+\vec q\cdot\vec v_i(\tilde{Q})$, where $\vec v_i$ is the coefficient of the imaginary vector part, one finds for $\tilde{Q}=\vec e_x$, $\tilde{Y}=i\vec e_y$ that $f_{\vec q}(\tilde{Q}\tilde{Y})=+u_z$ while $f_{\vec q}(\tilde{Y}\tilde{Q})=-u_z$; the extension of $f_{\vec q}$ to $\mathbb{B}$ is not tracial unless $\vec q=0$.

There is a further uniqueness question: is the trace form the only probability measure on the projection lattice? In dimension at least three, **Gleason's theorem** says yes. In dimension two it **fails**: the projection lattice of $\mathbb{C}^2$ is the Bloch sphere with $P$ and $I-P$ complementary, and assignments in $[0,1]$ with complementary projectors summing to one need not be of trace form — non-trace frame functions exist. Uniqueness is restored if the domain is enlarged from projections to all effects and additivity is required there: by **Busch's** effect-based version of Gleason's theorem, a normalized additive assignment on the full effect algebra is of trace form in every dimension, including two. For a qubit, then, uniqueness of the probability measure is not a consequence of the algebra alone; it requires the effect structure, i.e. the POVM framework. It is significant that the trace formula extends cleanly to effects, since that is precisely the statement whose uniqueness is a theorem.

**Open question — the pairing at the other sector.** The trace pairing $\mathrm{Tr}(\tilde{\rho}\tilde{H})$ is defined through the positive form $\langle\tilde P,\tilde Q\rangle_{*}$ of the probability row. On the material sector the positive form is $\langle\tilde P,\tilde Q\rangle_{*}$ read as the Euclidean square and the physical pairing of that row is the indefinite $\langle\tilde P,\tilde Q\rangle_{\natural*}$. **Whether the fundamental pairing of the framework is the trace at the informational sector with $\langle\tilde P,\tilde Q\rangle_{*}$ or a pairing at the material sector with $\langle\tilde P,\tilde Q\rangle_{\natural*}$ is open**, and the corpus's position is stated, not derived: the states are the informational ones and the pairing is the trace, and the material pairing is a calibration. The other side of the question is *The Biquaternioid General Quaternionic Sesqualgebra (GQS) over $\mathbb{C}$*.

## What Is Derivation and What Is Restatement

**Derived.** From the algebra and its Hermitian subspace: (1) a canonical symmetric pairing, fixed up to scale by traciality and positivity and normalized by $\mathrm{Tr}(e_t)=2$; (2) a canonical family of rank-one idempotents, exactly the rank-one projectors under the isomorphism; (3) reality, positivity, and normalization of the state–idempotent pairing, hence a probability distribution for a projective measurement; (4) the expectation value $\mathrm{Tr}(\tilde{\rho}\tilde{H})=h_0+\vec r\cdot\vec h$ and the transition probability $\mathrm{Tr}(\tilde{P}\tilde{Q})=\cos^2(\theta/2)$, with manifest symmetry; (5) the extension to effects and POVMs, with explicit non-projective examples; (6) exact agreement with the Hilbert-space formulas under $\mathbb{B}\cong M_2(\mathbb{C})$, a theorem about the algebra rather than an empirical coincidence.

**Restated.** Not derived from the algebra: (1) the identification of the pairing with **empirical frequency** — the algebra produces a canonical number in $[0,1]$, and reading it as a probability is the Born rule's empirical content, which no algebraic manipulation removes; (2) the choices of normalization and of the factor $2$, which are conventions, since the scale cancels in probabilities; (3) the general Hilbert-space statement $p=\mathrm{Tr}(E\rho)$, of which the biquaternion formula is a restatement for $n=2$, generalizing only the pure-vector statement $|\langle\phi|\psi\rangle|^2$.

**Not explained.** The framework does not derive the uniqueness of the probability measure for a qubit from the algebra alone (Gleason fails in dimension two; Busch's theorem is needed); it does not explain why a particular outcome occurs (the measurement problem is unchanged); and it predicts no deviation from standard quantum physics. The claim that the Born rule is "a consequence of the algebra rather than an independent postulate" is correct about the **form** of the rule and the objects it relates, not about its empirical or interpretive content.

## Summary

The Born rule in the biquaternion framework is the trace formula $\mathrm{Tr}(\tilde{P}\tilde{H})=2\,\mathrm{Sc}(\tilde{P}\tilde{H}) = 2\langle\tilde{P},\tilde{H}\rangle$. On $\mathbb{M}_+$ the trace pairing $\mathrm{Tr}(\tilde{H}\tilde{K})=2(h_0k_0+\vec h\cdot\vec k)$ is the Euclidean positive-definite pairing of signature $(4,0)$, distinct from the Lorentzian biquaternion norm $\langle\tilde{H}\rangle_{\natural}=h_0^2-|\vec h|^2$ whose future cone cuts out the state space. It is natural because it is the product's trace: among symmetric invariant positive pairings it is the tracial one.

Under $\varphi:\mathbb{B}\to M_2(\mathbb{C})$ the idempotents map to rank-one projectors, states to density matrices, and $\mathrm{tr}\circ\varphi=\mathrm{Tr}$. The probability $p_+=\mathrm{Tr}(\tilde\Pi_1(\vec u_h)\tilde{\rho})=\tfrac12(1+\vec u_h\cdot\vec r)$ is real, in $[0,1]$, and normalized, all as consequences of the algebra. General measurements are effects $\tilde{E}=ae_t+i\vec w$ with $|\vec w|\leq\min(a,1-a)$; POVMs are families of effects summing to $e_t$; the probabilities are $a_i+\vec w_i\cdot\vec r$, as the unsharp and trine examples show.

The comparison with the standard statement is exact, because $\mathbb{B}\cong M_2(\mathbb{C})$ as $*$-algebras: the biquaternion formula and $p=\mathrm{Tr}(E\rho)$ are the same equation, and the pure case is $|\langle\phi|\psi\rangle|^2=\cos^2(\theta/2)$. The formulations differ in what they take as primitive and in the manifest symmetry of the transition probability. The trace is unique up to scale among tracial functionals, but symmetry, invariance and positivity alone leave a two-parameter family, and the normalized positive non-tracial functionals are exactly the states. Uniqueness of the probability measure requires more than the algebra: Gleason fails for a qubit on projections, and Busch's effect-based theorem restores uniqueness. The framework derives the form of the Born rule and its consistency properties, restates the identification with empirical probability, and does not explain outcome selection or predict departures from standard quantum physics.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$, $\vec e_\mu^2 = -e_t$ | Quaternion basis |
| $i$ | Scalar imaginary, $i^2 = -1$ |
| $\mathbb{M}_+$ | Hermitian subspace (states, observables, effects) |
| $\mathbb{M}_-$, $\mathbb{B} = \mathbb{M}_+\oplus\mathbb{M}_-$ | Anti-Hermitian subspace (generators) |
| $\tilde{H} = h_0 e_t + i\vec h$ | General Hermitian element |
| $\mathrm{Tr}(\tilde{H}) = 2\,\mathrm{Sc}(\tilde{H}) = 2h_0$ | Trace |
| $\mathrm{Tr}(\tilde{H}\tilde{K}) = 2(h_0k_0 + \vec h\cdot\vec k)$ | Trace pairing, signature $(4,0)$ |
| $\langle\tilde{H}\rangle_{\natural} = \langle\tilde{H},\tilde{H}\rangle_{\natural} = \tilde{H}\tilde{H}^{\natural} = (h_0^2 - |\vec h|^2)e_t$ | Biquaternion norm, signature $(1,3)$ |
| $\tilde{\rho} = \tfrac{1}{2}(e_t + i\vec r)$, $|\vec r|\leq 1$ | State; Bloch vector $\vec r$ |
| $\tilde\Pi_{1,2}(\vec u) = \tfrac{1}{2}(e_t \pm i\vec u)$, $|\vec u|=1$ | Idempotent (pure state, rank-one projector) |
| $\tilde{E} = a e_t + i\vec w$, $|\vec w|\leq\min(a,1-a)$ | Effect |
| $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H}) = 2\langle\tilde{P},\tilde{H}\rangle$ | Trace formula (Born rule) |
| $\mathrm{Tr}(\tilde\Pi_1(\vec u_h)\tilde{\rho}) = \tfrac{1}{2}(1+\vec u_h\cdot\vec r)$ | Born probability, projective |
| $\mathrm{Tr}(\tilde{E}_i\tilde{\rho}) = a_i + \vec w_i\cdot\vec r$ | Born probability, POVM |
| $\mathrm{Tr}(\tilde\Pi(\vec u_x)\tilde\Pi(\vec u_y)) = \tfrac{1}{2}(1+\vec u_x\cdot\vec u_y) = \cos^2(\theta/2)$ | Transition probability |
| $\varphi: e_t\mapsto I_2$, $\vec e_\mu\mapsto -i\sigma_\mu$ | Isomorphism $\mathbb{B}\to M_2(\mathbb{C})$ |
| $\mathrm{tr}\circ\varphi = \mathrm{Tr}$ | Trace correspondence |
| $\tilde{K}_i$, $\sum_i\tilde{K}_i^{*}\tilde{K}_i = e_t$ | Kraus operators (measurement update) |
| $\langle\tilde{P},\tilde{Q}\rangle$ | the general plain bilinear form, the scalar part of the general plain bilinear product, $\mathrm{Sc}(\tilde{P}\tilde{Q})$ |
| $\langle\tilde{P},\tilde{Q}\rangle_{*}$ | the general plain sesquilinear form, $\mathrm{Sc}(\tilde{P}\tilde{Q}^{*})$; on the diagonal $\langle\tilde{Q},\tilde{Q}\rangle_{*}=\sum_\mu\lvert Q_\mu\rvert^{2}$ |

## Further Reading

- John von Neumann, *Mathematical Foundations of Quantum Mechanics* (Princeton, 1932), for the original formulation of the Born rule and the density matrix.
- Andrew M. Gleason, "Measures on the closed subspaces of a Hilbert space," *Journal of Mathematics and Mechanics* **6** (1957) 885–893, for the uniqueness of the trace form on projection lattices in dimension three and above.
- Paul Busch, "Quantum states and generalized observables: a simple proof of Gleason's theorem," *Physical Review Letters* **91** (2003) 120403, for the effect-based theorem that covers the qubit.
- Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information* (Cambridge, 2000), for the standard treatment of the Born rule, POVMs, and the Bloch ball.
- K. Kraus, *States, Effects, and Operations* (Springer, 1983), for effects, POVMs, and the structure of state and observable spaces.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the algebraic structure of $\mathrm{Cl}_{1,3}$, the idempotents, and the trace.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the geometric-algebra treatment of projectors, spinors, and the state space.
