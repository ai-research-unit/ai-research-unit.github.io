# __The Born Rule from the Hermitian Form — Derivation and Comparison__

## Introduction

The companion article *Quantum Physics in Biquaternionic Form* identifies the Hermitian subspace $\mathbb{B}_{\Psi}$ of the biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ as the common home of the states and observables of a two-state system, and states the Born rule there as the normalised Hermitian form

$$
p=\frac{\langle\tilde{Ϛ}_{\Psi},\tilde R_\Psi\rangle_{*}}{\langle\tilde{Ϛ}_{\Psi},e_t\rangle_{*}}
 =\frac{\mathrm{Sc}(\tilde{Ϛ}_{\Psi}\tilde R_\Psi^{*})}{\mathrm{Sc}(\tilde{Ϛ}_{\Psi})}
 =r_t+\vec r\cdot\vec r_\Psi,
\qquad \langle\tilde{Ϛ}_{\Psi},e_t\rangle_{*}=\tfrac12,\quad \langle e_t\rangle_{*}=1.
$$

The star is not decoration. The Hermitian form $\langle\tilde Q_1,\tilde Q_2\rangle_{*}=\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})$ is the only one of the four forms whose norm is positive definite on the whole algebra, $\langle\tilde Q,\tilde Q\rangle_{*}=\sum_\mu\lvert Q_\mu\rvert^{2}$; the plain form is positive only on $\mathbb{B}_{\Psi}$ and negative on $\mathbb{B}_{\Phi}$. For a state $\tilde{Ϛ}_{\Psi}\ge0$ and an effect $0\le\tilde R_\Psi\le e_t$ the weight is $2\,\mathrm{Sc}(\tilde{Ϛ}_{\Psi}^{1/2}\tilde R_\Psi\tilde{Ϛ}_{\Psi}^{1/2})\in[0,1]$, so its non-negativity is structural and does not depend on a sign accident of the pair. On $\mathbb{B}_{\Psi}$ both arguments are Hermitian, $\tilde R_\Psi^{*}=\tilde R_\Psi$, and the Hermitian form coincides with the plain form; every formula below therefore also holds with the plain form written, and the plain form is the restriction of the Hermitian form to the sector, not a second pairing.

On $\mathbb{B}_{\Psi}$ the conjugation is the identity, so the same weight is $\mathrm{Sc}(\tilde{Ϛ}_{\Psi}\tilde R_\Psi)/\mathrm{Sc}(\tilde{Ϛ}_{\Psi})$, the plain scalar. The trace is the last reading, in the $2\times2$ image, and the weight is stated in it only at normalisation, below. This article develops the derivation and separates what the framework **derives** from what it merely **restates**.

The distinction matters because $\mathbb{B}\cong M_2(\mathbb{C})$: any probability formula in the algebra is a formula about $2\times2$ matrices, and any claim that the framework "derives" the Born rule must be read against that isomorphism. What the algebra genuinely supplies is a canonical positive pairing — the Hermitian form — a canonical family of rank-one idempotents, and the theorem that pairing a state with an idempotent (or an effect) yields a real number in $[0,1]$, that the numbers over a complete family sum to one, and that the pure-state transition probability is $\cos^2(\theta/2)$. That is algebra, and it is derived. What the algebra does not supply is the identification of those numbers with physical frequencies; that is the Born rule itself, and the framework relocates it rather than eliminating it.

The article develops the Hermitian form and its naturalness; identifies the idempotents with rank-one projectors and derives $p=\langle\tilde\Pi,\tilde{Ϛ}_{\Psi}\rangle_{*}/\langle\tilde{Ϛ}_{\Psi},e_t\rangle_{*}$; treats effects and non-projective POVMs; compares the result with the standard statements $p=\mathrm{Tr}(E\rho)$ and $|\langle\tilde{Ξ}_{\mathrm{sp}}|\xi_{\mathrm{alt}}\rangle_{*}|^2$; examines the non-uniqueness of the tracial reading; and closes with an explicit accounting of derivation versus restatement. The standard of proof throughout is algebraic: every claim is a statement about $\mathbb{B}$ and its product, checkable by expanding in the basis $\{e_t,i\vec e_x,i\vec e_y,i\vec e_z\}$, and no empirical input is used. Conventions are those of the companion articles: $e_t=1,\vec e_x,\vec e_y,\vec e_z$ with $\vec e_\mu^2=-e_t$; scalar imaginary $i$; $\mathbb{B}=\mathbb{B}_{\Psi}\oplus\mathbb{B}_{\Phi}$; $\langle\tilde Q_1,\tilde Q_2\rangle_{*}=\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})$ with $\langle\tilde Q\rangle_{*}=\langle\tilde Q,\tilde Q\rangle_{*}$ and $\langle e_t\rangle_{*}=1$; the plain form $\langle\tilde Q_1,\tilde Q_2\rangle=\mathrm{Sc}(\tilde Q_1\tilde Q_2)$ is its restriction to $\mathbb{B}_{\Psi}$; and $\mathrm{Tr}(\tilde Q)=2\langle\tilde Q,e_t\rangle_{*}$. Here $\mathrm{tr}$ denotes the ordinary $2\times2$ trace, related to $\mathrm{Tr}$ by $\mathrm{tr}\circ\iota=\mathrm{Tr}$.

## The Canonical Reading

The series states the reading in a fixed order, and the order is part of the statement. Each line is the same number read at a coarser level of structure, and the trace is the last line, used only where normalisation is stated.

$$
\boxed{\;\begin{aligned}
&\text{(1) form, with star:} && \langle\tilde Q_1,\tilde Q_2\rangle_{*}=\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*}),\\
&\text{(2) scalar, with star:} && \mathrm{Sc}(\tilde{Ϛ}_{\Psi}\tilde R_\Psi^{*}),\\
&\text{(3) scalar, without star, on } \mathbb{B}_{\Psi}: && \mathrm{Sc}(\tilde{Ϛ}_{\Psi}\tilde R_\Psi)=\mathrm{Sc}(\tilde{Ϛ}_{\Psi}\tilde R_\Psi^{*}),\\
&\text{(4) trace, at normalisation, last:} && \operatorname{Tr}(\tilde{Ϛ}_{\Psi})=2\,\mathrm{Sc}(\tilde{Ϛ}_{\Psi})=1,\qquad p=\frac{\operatorname{Tr}(\tilde{Ϛ}_{\Psi}\tilde R_\Psi^{*})}{\operatorname{Tr}(\tilde{Ϛ}_{\Psi})}=\frac{\operatorname{Tr}(\tilde{Ϛ}_{\Psi}\tilde R_\Psi)}{\operatorname{Tr}(\tilde{Ϛ}_{\Psi})}.
\end{aligned}\;}
$$

```text
CANONICAL READING OF THE BORN WEIGHT
====================================

1. FORM, WITH STAR
   <A,B>_* = Sc(A B*)
   The Hermitian form. Positive definite on the whole algebra, so no
   sector restriction is needed to make it an inner product.

2. SCALAR PART, WITH STAR
   Sc(Ϛ H*)
   The form read on one pair. A single complex number; on M+ it is real.

3. SCALAR PART, WITHOUT STAR (M+ only)
   Sc(Ϛ H) = Sc(Ϛ H*)
   Both arguments are Hermitian, so the star acts as the identity. The
   star is dropped only here, where it does nothing.

4. TRACE, WITH NORMALISATION (last)
   Tr(e_t) = 2,   Tr(Ϛ) = 2 Sc(Ϛ) = 1
   p = Tr(Ϛ H*) / Tr(Ϛ) = Tr(Ϛ H) / Tr(Ϛ) = 2 Sc(Ϛ H*)
   (the star is inert on M+: H* = H)

WHY THE TRACE IS LAST
---------------------
* B is four-dimensional over C. Its product defines Sc, not Tr. A trace
  of an element of B is not defined until an isomorphism B = M2(C) is
  chosen; Tr is then tr o M2, and the factor 2 is dim_C C^2.
* The factor 2 is therefore a property of the chosen image, not of the
  form. It cancels in every probability, which is a ratio.
* Sc is intrinsic: Sc(Q) = <Q,e_t>_*, the form read against the unit.
  It needs no representation and no normalisation.
* On M+ the conjugation fixes every element, so step 3 is the same number
  as step 2. Writing both makes the sector restriction explicit instead
  of hiding it inside an inert star.
* Normalisation is the only operation that needs the trace: Tr(Ϛ) = 1 is
  the matrix-image form of <Ϛ,e_t>_* = 1/2. Stating it once, last, keeps
  the trace out of the definition of the weight.

CONSEQUENCE
-----------
Every formula of the article is complete at step 2 or step 3. Step 4 is a
corollary in the 2x2 image and is never used to define the pairing.
```

The order is forced by what each level requires. The form needs only the algebra and its conjugation. The scalar part needs only the product. The plain scalar needs the sector, where the conjugation is the identity. The trace needs an isomorphism onto $M_2(\mathbb{C})$, which is additional structure, and it is used only where normalisation is stated. Reversing the order would make the weight look like a matrix formula with an algebraic afterthought, and would hide that the factor $2$ is the dimension of the image rather than a constant of the theory.

## The Hermitian Form on $\mathbb{B}_{\Psi}$

### The Pairing and Its Naturalness

An element of $\mathbb{B}_{\Psi}$ is $\tilde R_\Psi=r_t\,e_t+i\vec r_\Psi$, with $r_t\in\mathbb{R}$ and $\vec r_\Psi=(r'_x,r'_y,r'_z)\in\mathbb{R}^3$. The Hermitian form is

$$
\langle\tilde{R}_{\Psi,1},\tilde{R}_{\Psi,2}\rangle_{*}=\mathrm{Sc}(\tilde{R}_{\Psi,1}\tilde{R}_{\Psi,2}^{*})
=r_{t,1}r_{t,2}+\vec r_{\Psi,1}\cdot\vec r_{\Psi,2},
$$

obtained from $\tilde{R}_{\Psi,1}\tilde{R}_{\Psi,2}=(r_{t,1}r_{t,2}+\vec r_{\Psi,1}\cdot\vec r_{\Psi,2})e_t+i(c r_{t,1}\vec r_{\Psi,2}+c r_{t,2}\vec r_{\Psi,1})-\vec r_{\Psi,1}\times\vec r_{\Psi,2}$ together with $\tilde{R}_{\Psi,1}^{*}=\tilde{R}_{\Psi,1}$ and $\tilde{R}_{\Psi,2}^{*}=\tilde{R}_{\Psi,2}$, and its diagonal is the Hermitian norm,

$$
\langle\tilde R_\Psi\rangle_{*}=\langle\tilde R_\Psi,\tilde R_\Psi\rangle_{*}=r_t^2+|\vec r_\Psi|^2 .
$$

The unit is normalised by $\langle e_t\rangle_{*}=1$. In the basis $\{e_t,i\vec e_x,i\vec e_y,i\vec e_z\}$ the Gram matrix is the identity, so on $\mathbb{B}_{\Psi}$ the form is positive definite of signature $(4,0)$, the Euclidean inner product on $\mathbb{R}^4$; on the whole algebra it is positive definite of signature $(8,0)$.

Two immediate consequences will be used repeatedly. First, for Hermitian arguments the form is real and symmetric: $\langle\tilde{R}_{\Psi,1},\tilde{R}_{\Psi,2}\rangle_{*}=\langle\tilde{R}_{\Psi,2},\tilde{R}_{\Psi,1}\rangle_{*}=r_{t,1}r_{t,2}+\vec r_{\Psi,1}\cdot\vec r_{\Psi,2}$. As a sesquilinear form it is $\mathbb{C}$-linear in the first argument and $\mathbb{C}$-antilinear in the second; on $\mathbb{B}_{\Psi}$ only real combinations of Hermitian elements occur, so the antilinearity is inert and the pairing is symmetric. Second, it is positive definite, since $\langle\tilde{R}_{\Psi,1}\rangle_{*}=c r_{t,1}^2+|\vec r_{\Psi,1}|^2\geq0$ with equality only for $\tilde{R}_{\Psi,1}=0$; the Hermitian form is therefore an inner product on the whole algebra, not merely a symmetric form on a sector.

Three properties single it out. **Invariance:** under $*$-unitary conjugation $\tilde{R}_{\Psi,1}\mapsto\tilde{U}\tilde{R}_{\Psi,1}\tilde{U}^{*}$ the form is invariant; since the unit quaternions rotate $\vec r_{\Psi,1}$ and fix $c r_{t,1}$, an invariant symmetric bilinear form on $\mathbb{B}_{\Psi}$ must be $\mathcal{B}=\alpha r_{t,1}r_{t,2}+\beta\,\vec r_{\Psi,1}\cdot\vec r_{\Psi,2}$, so invariance alone leaves two parameters. **Product form:** requiring the form on $\mathbb{B}_{\Psi}$ to be the scalar part of the algebra's product, $\mathcal{B}(\tilde{R}_{\Psi,1},\tilde{R}_{\Psi,2})=f(\tilde{R}_{\Psi,1}\tilde{R}_{\Psi,2})$ with $f$ central and $f(e_t)=1$, forces $f=\mathrm{Sc}$ and hence $\alpha=\beta$; the Hermitian form agrees with that pairing on $\mathbb{B}_{\Psi}$ and extends it to $\mathbb{B}$ without losing positivity. **Positivity:** $\alpha,\beta>0$ makes the form on the sector positive definite; the Hermitian form is positive definite on the whole algebra, so no sector restriction is needed. The scale is fixed by $\langle e_t\rangle_{*}=1$, though the scale cancels in probabilities, which are ratios. Thus the pairing is unique once the associative product, positivity on the whole algebra and the unit normalisation are required — the product condition is a genuine assumption, not a consequence of symmetry.

### It Is Not the Biquaternion Norm

The other quadratic form on $\mathbb{B}_{\Psi}$ is the **biquaternion norm**

$$
\langle\tilde R_\Psi\rangle_{\natural} = \langle\tilde R_\Psi,\tilde R_\Psi\rangle_{\natural}=\tilde R_\Psi\tilde R_\Psi^{\natural}=(r_t^2-|\vec r_\Psi|^2)e_t,
$$

of signature $(1,3)$, whose future light cone is the positivity cone. The state space is the state slice of that cone, normalised by $\langle\tilde{Ϛ}_{\Psi},e_t\rangle_{*}=\tfrac12\langle e_t\rangle_{*}$; the Born rule is a statement about the Hermitian form. Positivity of a state is a biquaternion-norm condition, while Born probabilities are Hermitian-form quantities. The Born rule therefore does not follow from the light-cone structure of $\mathbb{B}_{\Psi}$; it follows from the Euclidean form, a different form on the same space.

The two forms are complementary, and the idempotents show it clearly. For $\tilde\Pi_{1,2}(\vec u)$ one has $r_t=\tfrac12$ and $|\vec r_\Psi|=\tfrac12$, so the biquaternion norm vanishes,
$$
\langle\tilde\Pi_{1,2}\rangle_{\natural}=\tilde\Pi_{1,2}\tilde\Pi_{1,2}^{\natural}=(r_t^2-|\vec r_\Psi|^2)e_t=0,
$$
placing the idempotents on the boundary of the light cone, while the Hermitian form gives $\langle\tilde\Pi_{1,2},e_t\rangle_{*}=\tfrac12\langle e_t\rangle_{*}$ and $\langle\tilde\Pi_{1,2}\rangle_{*}=\tfrac12$. The idempotents are null for the biquaternion norm and normalised for the Hermitian form; probabilities are read from the second, not the first.

## Idempotents and Rank-One Projections

The bridge to the standard formulas is the $*$-isomorphism $\iota:\mathbb{B}\to M_2(\mathbb{C})$ with

$$
e_t\mapsto I_2,\qquad \vec e_\mu\mapsto-i\sigma_\mu\quad(\mu=1,2,3),
$$

the convention of the companion article. It gives $\iota(\tilde R_\Psi)=r_t\,I_2+\vec r_\Psi\cdot\boldsymbol{\sigma}$, so $\mathbb{B}_{\Psi}$ maps onto the Hermitian $2\times2$ matrices, and, the Pauli matrices being traceless,

$$
\mathrm{tr}\,\iota(\tilde{Q})=2\,\mathrm{Sc}(\tilde{Q})=\mathrm{Tr}(\tilde{Q}),
\qquad\text{hence}\qquad
\mathrm{Tr}(\tilde{R}_{\Psi,1}\tilde{R}_{\Psi,2})=\mathrm{tr}\bigl(\iota(\tilde{R}_{\Psi,1})\iota(\tilde{R}_{\Psi,2})\bigr).
$$

The idempotents of $\mathbb{B}_{\Psi}$,

$$
\tilde\Pi_{1,2}(\vec u)=\tfrac{1}{2}(e_t\pm i\vec u),\qquad|\vec u|=1,
$$

satisfy $\iota(\tilde\Pi_1(\vec u))=\tfrac{1}{2}(I_2+\vec u\cdot\boldsymbol{\sigma})$ because $\iota(i\vec u)=\vec u\cdot\boldsymbol{\sigma}$. This is the standard spin-up projector; it has eigenvalues $1$ and $0$, so the biquaternion idempotent **is** a rank-one projection, and every rank-one projection arises this way. The usual identities hold: $\tilde\Pi_{1,2}^2=\tilde\Pi_{1,2}$, $\tilde\Pi_{1,2}^{*}=\tilde\Pi_{1,2}$, $\mathrm{Tr}(\tilde\Pi_{1,2})=1$, $\tilde\Pi_1+\tilde\Pi_2=e_t$, $\tilde\Pi_1\tilde\Pi_2=0$.

The idempotent property can be checked directly, without invoking the isomorphism. For unit $\vec u$,
$$
\tilde\Pi_1^2=\tfrac14\bigl(e_t+i\vec u\bigr)^2=\tfrac14\bigl(e_t+2i\vec u+(i\vec u)(i\vec u)\bigr),
$$
and $(i\vec u)(i\vec u)=(\vec u\cdot\vec u)e_t-\vec u\times\vec u=e_t$, so $\tilde\Pi_1^2=\tfrac12(e_t+i\vec u)=\tilde\Pi_1$; similarly $\tilde\Pi_2^2=\tilde\Pi_2$ and $\tilde\Pi_1\tilde\Pi_2=\tfrac14(e_t-|\vec u|^2e_t)=0$. Conversely, every rank-one projector in $M_2(\mathbb{C})$ has the form $\tfrac12(I_2+\vec u\cdot\boldsymbol{\sigma})$, so the map $\vec u\mapsto\tilde\Pi_1(\vec u)$ is a bijection between the Bloch sphere and the rank-one idempotents of the algebra.

A **state** is a positive element normalised by $\langle\tilde{Ϛ}_{\Psi},e_t\rangle_{*}=\tfrac12\langle e_t\rangle_{*}$,

$$
\tilde{Ϛ}_{\Psi}=\tfrac{1}{2}(e_t+i\vec r),\qquad|\vec r|\leq1,
$$

mapping to the density matrix $\tfrac{1}{2}(I_2+\vec r\cdot\boldsymbol{\sigma})$. An **effect** is an element $\tilde{E}_{\Psi}\in\mathbb{B}_{\Psi}$ with $0\leq\tilde{E}_{\Psi}\leq e_t$ in the matrix order; effects represent measurement outcomes.

## Derivation of the Born Probability

For $\tilde R_\Psi=r_t\,e_t+i\vec r_\Psi$ and $\tilde{Ϛ}_{\Psi}=\tfrac{1}{2}(e_t+i\vec r)$, the state is normalised against the unit, $\langle\tilde{Ϛ}_{\Psi},e_t\rangle_{*}=\tfrac12\langle e_t\rangle_{*}$, and the expectation value is the Born weight

$$
\langle\tilde R_\Psi\rangle_{\tilde{Ϛ}_{\Psi},*}=\frac{\langle\tilde{Ϛ}_{\Psi},\tilde R_\Psi\rangle_{*}}{\langle\tilde{Ϛ}_{\Psi},e_t\rangle_{*}}
=\frac{\mathrm{Sc}(\tilde{Ϛ}_{\Psi}\tilde R_\Psi^{*})}{\mathrm{Sc}(\tilde{Ϛ}_{\Psi})}
=r_t+\vec r\cdot\vec r_\Psi.
$$

**The material element behind the reading.** Every Hermitian $\tilde R_\Psi$ is $\tilde R_\Psi=iA$ for a unique anti-Hermitian $A\in\mathbb{B}_{\Phi}$, the **material element** that is observed. Since $(iA)^{*}=iA$, the expectation is

$$
\langle iA\rangle_{\tilde{Ϛ}_{\Psi},*}=\frac{\mathrm{Sc}(\tilde{Ϛ}_{\Psi}(iA)^{*})}{\mathrm{Sc}(\tilde{Ϛ}_{\Psi})}
=\frac{i\,\mathrm{Sc}(\tilde{Ϛ}_{\Psi}A)}{\mathrm{Sc}(\tilde{Ϛ}_{\Psi})},
$$

and $\mathrm{Sc}(\tilde{Ϛ}_{\Psi}A)$ is purely imaginary, so the factor $i$ makes the reading real. The Born pairing thus pairs an $\mathbb{B}_{\Psi}$ state with an $\mathbb{B}_{\Phi}$ material element; the two senses of "observable" are the object $A$ and its representative $iA$.

The spectral decomposition is likewise purely algebraic. Writing $\tilde R_\Psi=r_t\,e_t+i|\vec r_\Psi|\vec u_\Psi$ and multiplying by $\tilde\Pi_{1,2}(\vec u_\Psi)$, using $(i\vec u_\Psi)(i\vec u_\Psi)=e_t$, gives
$$
\tilde R_\Psi\tilde\Pi_1(\vec u_\Psi)=(r_t+|\vec r_\Psi|)\tilde\Pi_1(\vec u_\Psi),\qquad \tilde R_\Psi\tilde\Pi_2(\vec u_\Psi)=(r_t-|\vec r_\Psi|)\tilde\Pi_2(\vec u_\Psi),
$$
so the eigenvalues are $\lambda_\pm=r_t\pm|\vec r_\Psi|$ and the spectral projectors are the idempotents. The statement that the idempotents are complete, $\tilde\Pi_1+\tilde\Pi_2=e_t$, is the algebraic form of the spectral theorem for $\tilde R_\Psi\in\mathbb{B}_{\Psi}$.

For a spectral decomposition $\tilde R_\Psi=\lambda_+\tilde\Pi_1(\vec u_\Psi)+\lambda_-\tilde\Pi_2(\vec u_\Psi)$, with $\vec u_\Psi=\vec r_\Psi/|\vec r_\Psi|$, $\lambda_\pm=r_t\pm|\vec r_\Psi|$ and $\tilde\Pi_1+\tilde\Pi_2=e_t$, the probability of the $+$ outcome is $p_+=\langle\tilde\Pi_1(\vec u_\Psi),\tilde{Ϛ}_{\Psi}\rangle_{*}/\langle\tilde{Ϛ}_{\Psi},e_t\rangle_{*}$. Directly,

$$
\tilde\Pi_1(\vec u_\Psi)\tilde{Ϛ}_{\Psi}=\tfrac{1}{4}\bigl[(1+\vec u_\Psi\cdot\vec r)e_t+i(\vec u_\Psi+\vec r)-\vec u_\Psi\times\vec r\bigr],
$$

so $\langle\tilde\Pi_1(\vec u_\Psi),\tilde{Ϛ}_{\Psi}\rangle_{*}=\tfrac14(1+\vec u_\Psi\cdot\vec r)$ and, dividing by $\langle\tilde{Ϛ}_{\Psi},e_t\rangle_{*}=\tfrac12$,

$$
\boxed{\;p_+=\tfrac{1}{2}(1+\vec u_\Psi\cdot\vec r),\qquad p_-=\tfrac{1}{2}(1-\vec u_\Psi\cdot\vec r)\;}.
$$

The pairing also reproduces the variance. From $\tilde{R}_\Psi^2=(r_t^2+|\vec r_\Psi|^2)e_t+2c r_t\,i\vec r_\Psi$,
$$
\langle\tilde{R}_\Psi^2\rangle_{\tilde{Ϛ}_{\Psi},*}=\frac{\langle\tilde{Ϛ}_{\Psi},\tilde{R}_\Psi^2\rangle_{*}}{\langle\tilde{Ϛ}_{\Psi},e_t\rangle_{*}}=r_t^2+|\vec r_\Psi|^2+2c r_t\,\vec r\cdot\vec r_\Psi,
$$
so
$$
\langle\tilde{R}_\Psi^2\rangle_{\tilde{Ϛ}_{\Psi},*}-\langle\tilde R_\Psi\rangle_{\tilde{Ϛ}_{\Psi},*}^2=|\vec r_\Psi|^2-(\vec r\cdot\vec r_\Psi)^2=|\vec r_\Psi|^2\bigl(1-(\vec r\cdot\vec u_\Psi)^2\bigr)\geq0,
$$
vanishing precisely when $\vec r=\pm\vec u_\Psi$, i.e. when the state is an eigenstate of the observable. This is a nontrivial check that the statistical content is carried by the Hermitian form and not by the biquaternion norm.

Three algebraic properties make the pairing a probability assignment. **Reality:** for Hermitian $\tilde{R}_{\Psi,1},\tilde{R}_{\Psi,2}$, $\tilde{R}_{\Psi,2}^{*}=\tilde{R}_{\Psi,2}$, so $\langle\tilde{R}_{\Psi,1},\tilde{R}_{\Psi,2}\rangle_{*}=\mathrm{Sc}(\tilde{R}_{\Psi,1}\tilde{R}_{\Psi,2}^{*})=\mathrm{Sc}(\tilde{R}_{\Psi,1}\tilde{R}_{\Psi,2})=r_{t,1}r_{t,2}+\vec r_{\Psi,1}\cdot\vec r_{\Psi,2}\in\mathbb{R}$; the conjugation acts as the identity but the star is written. **Positivity:** for $\tilde{Q}_1\geq0$ and $\tilde{Ϛ}_{\Psi}\geq0$, $\langle\tilde{Q}_1,\tilde{Ϛ}_{\Psi}\rangle_{*}\geq0$, since under $\iota$, with $A=\iota(\tilde{Q}_1)$ and $B=\iota(\tilde{Ϛ}_{\Psi})$, this is $A,B\geq0\Rightarrow\mathrm{tr}(AB)=\mathrm{tr}(\sqrt{A}B\sqrt{A})\geq0$; with $|\vec r|\leq1$ it also gives $p_+\leq1$. Positivity is thus guaranteed twice: the form is positive definite on $\mathbb{B}$, and the pair is positive. **Normalization:** by completeness and symmetry,

$$
p_++p_-=\frac{\langle\tilde\Pi_1+\tilde\Pi_2,\tilde{Ϛ}_{\Psi}\rangle_{*}}{\langle\tilde{Ϛ}_{\Psi},e_t\rangle_{*}}=\frac{\langle e_t,\tilde{Ϛ}_{\Psi}\rangle_{*}}{\langle\tilde{Ϛ}_{\Psi},e_t\rangle_{*}}=1.
$$

### The Trace Reading and Normalisation

The derivation above uses no trace. The trace is the final reading, taken in the $2\times2$ image, where $\operatorname{Tr}=2\,\mathrm{Sc}$ and the normalised state has $\operatorname{Tr}(\tilde{Ϛ}_{\Psi})=1$. On $\mathbb{B}_{\Psi}$ both factors are Hermitian, so the scalar part is unchanged by the star, $2\,\mathrm{Sc}(\tilde{Ϛ}_{\Psi}\tilde R_\Psi^{*})=2\,\mathrm{Sc}(\tilde{Ϛ}_{\Psi}\tilde R_\Psi)$.

**The star in the numerator is inert on $\mathbb{B}_{\Psi}$.** Both factors are Hermitian, $\tilde{Ϛ}_{\Psi}^{*}=\tilde{Ϛ}_{\Psi}$ and $\tilde R_\Psi^{*}=\tilde R_\Psi$, so the star may be dropped inside the trace and $\operatorname{Tr}(\tilde{Ϛ}_{\Psi}\tilde R_\Psi^{*})=\operatorname{Tr}(\tilde{Ϛ}_{\Psi}\tilde R_\Psi)$. Intrinsically this is $\mathrm{Sc}(\tilde{Ϛ}_{\Psi}\tilde R_\Psi^{*})=\mathrm{Sc}(\tilde{Ϛ}_{\Psi}\tilde R_\Psi)$; the trace statement is its $2\times2$ reading. The unstarred trace is real: for Hermitian matrices $A,B$, $(AB)^{\dagger}=BA$, hence $\overline{\mathrm{tr}(AB)}=\mathrm{tr}((AB)^{\dagger})=\mathrm{tr}(BA)=\mathrm{tr}(AB)$. It is non-negative for $A,B\ge0$ by the positivity argument above. The weight therefore needs no star on the sector, and it is

$$
\boxed{\;p=\frac{\operatorname{Tr}(\tilde{Ϛ}_{\Psi}\tilde R_\Psi^{*})}{\operatorname{Tr}(\tilde{Ϛ}_{\Psi})}
=\frac{\operatorname{Tr}(\tilde{Ϛ}_{\Psi}\tilde R_\Psi)}{\operatorname{Tr}(\tilde{Ϛ}_{\Psi})}\in[0,1]\;},
$$

which is the standard formula. The factor $2$ is the dimension of the image and cancels in the ratio; it is not a normalisation constant of the form. Traciality, $\operatorname{Tr}(\tilde Q\tilde Q_1)=\operatorname{Tr}(\tilde Q_1\tilde Q)$, is the symmetry of the form on Hermitian arguments, $\mathrm{Sc}(\tilde Q\tilde Q_1)=Q_tQ_{1t}-\sum_kQ_kQ_{1k}$. The star is retained because it names the pairing that is positive definite on the whole algebra, and because it cannot be dropped when one factor is not Hermitian, as in the Kraus form.

### What Is Derived Here

It is worth stating exactly what has been shown. The algebra fixes the pairing and the idempotents; from these, realness, positivity, and normalization of $p_+$ follow. Nothing else was used: no inner product was chosen, no Hilbert space was assumed, and no frequentist input entered. What has *not* been shown is that these numbers are observed frequencies. That identification is the Born rule, and it is an empirical postulate in the standard formalism as well. The algebraic development shows that once the pairing and the idempotents are fixed, the *structure* of the probability assignment is forced; it does not manufacture the link to experiment. The remaining sections verify that the structure is exactly the standard one and catalogue where uniqueness does and does not hold.

## General Measurements: Effects and POVMs

Writing an effect as $\tilde{E}_{\Psi}=a\,e_t+i\vec w$, its matrix $aI_2+\vec w\cdot\boldsymbol{\sigma}$ has eigenvalues $a\pm|\vec w|$, and

$$
\tilde{E}_{\Psi}\geq0\iff a\geq|\vec w|,\qquad \tilde{E}_{\Psi}\leq e_t\iff 1-a\geq|\vec w|,
$$

so $\tilde{E}_{\Psi}$ is an effect precisely when $0\leq a\leq1$ and $|\vec w|\leq\min(a,1-a)$. The two inequalities are exactly the requirement that both eigenvalues of the matrix lie in $[0,1]$. The rank-one projectors sit at $a=\tfrac12$, $|\vec w|=\tfrac12$, which are extreme points of the effect interval. A **POVM** is a finite set of effects with $\tilde{E}_{\Psi}_i\geq0$ and $\sum_i\tilde{E}_{\Psi}_i=e_t$. The outcome probabilities are

$$
p_i=\frac{\langle\tilde{E}_{\Psi}_i,\tilde{Ϛ}_{\Psi}\rangle_{*}}{\langle\tilde{Ϛ}_{\Psi},e_t\rangle_{*}}
=2\,\mathrm{Sc}(\tilde{E}_{\Psi}_i\tilde{Ϛ}_{\Psi}^{*})
=2\,\mathrm{Sc}(\tilde{E}_{\Psi}_i\tilde{Ϛ}_{\Psi})
=\frac{\operatorname{Tr}(\tilde{E}_{\Psi}_i\tilde{Ϛ}_{\Psi}^{*})}{\operatorname{Tr}(\tilde{Ϛ}_{\Psi})}
=\frac{\operatorname{Tr}(\tilde{E}_{\Psi}_i\tilde{Ϛ}_{\Psi})}{\operatorname{Tr}(\tilde{Ϛ}_{\Psi})}
=a_i+\vec w_i\cdot\vec r,
$$

where $\tilde{E}_{\Psi}_i=a_ie_t+i\vec w_i$, and $\sum_ia_i=1$, $\sum_i\vec w_i=0$ are exactly $\sum_i\tilde{E}_{\Psi}_i=e_t$. Reality, positivity, and normalization ($\sum_ip_i=\langle e_t,\tilde{Ϛ}_{\Psi}\rangle_{*}/\langle\tilde{Ϛ}_{\Psi},e_t\rangle_{*}=1$) follow from the algebra; projective measurements are the case of orthogonal idempotents.

Two examples make the non-projective case concrete. The **unsharp measurement** with $0\leq\eta\leq1$ and unit $\vec u$ is $\tilde{E}_{\Psi}_\pm=\tfrac12(e_t\pm i\eta\vec u)$, a POVM since $a=\tfrac12$ and $|\vec w|=\eta/2\leq\tfrac12$, with $p_\pm=\tfrac12(1\pm\eta\vec u\cdot\vec r)$; it is projective only at $\eta=1$, because

$$
\tilde{E}_{\Psi}_+^2-\tilde{E}_{\Psi}_+=\tfrac14(\eta^2-1)e_t .
$$

The **trine measurement**, with three unit vectors $\vec u_k$ at $120^\circ$ (so $\sum_k\vec u_k=0$), is

$$
\tilde{E}_{\Psi}_k=\tfrac13(e_t+i\vec u_k)=\tfrac23\tilde\Pi_1(\vec u_k),\qquad k=0,1,2 .
$$

Each is an effect, they sum to $e_t$, and no two are orthogonal; the probabilities are $p_k=\tfrac13(1+\vec u_k\cdot\vec r)$ with $\sum_kp_k=1$. The normalised Hermitian form thus covers general measurement statistics unchanged. Non-projective measurements are not exotic: they are needed for tasks such as unambiguous discrimination of non-orthogonal states, and the effect formalism is the algebraic home of that possibility.

The normalised Hermitian form gives measurement **statistics**, not the post-measurement state; the update requires Kraus operators $\tilde M_{\mathrm{kraus},i}$ with $\sum_i\tilde M_{\mathrm{kraus},i}^{*}\tilde M_{\mathrm{kraus},i}=e_t$, treated in the companion article on quantum channels, and every POVM with $k$ outcomes has a Neumark dilation to a projective measurement on $\mathbb{B}\otimes_\mathbb{C}M_k(\mathbb{C})\cong M_{2k}(\mathbb{C})$, the article's two- and three-outcome examples living inside $\mathbb{B}\otimes_\mathbb{C}\mathbb{B}\cong M_4(\mathbb{C})$.

## Comparison with the Hilbert-Space Statement

In standard quantum physics a state is a density operator $\rho$, an observable is $A=\sum_aaP_a$, and $p(a)=\mathrm{Tr}(P_a\rho)$; for a pure state and a rank-one outcome projector this is $p=|\langle\xi_{\mathrm{alt}}|\tilde{Ξ}_{\mathrm{sp}}\rangle|^2$. This is a **postulate**, motivateable by Gleason's theorem, decision theory, or envariance, but not derived from the other postulates. Because $\iota$ is a $*$-isomorphism with $\mathrm{tr}\circ\iota=\mathrm{Tr}$, the two formulations agree **exactly**:

$$
\mathrm{Tr}(\tilde\Pi\tilde{Ϛ}_{\Psi}^{*})=\mathrm{tr}\bigl(\iota(\tilde\Pi)\iota(\tilde{Ϛ}_{\Psi})\bigr),\qquad
\mathrm{Tr}\bigl(\tilde\Pi(\vec u_x)\tilde\Pi(\vec u_y)^{*}\bigr)=\tfrac12(1+\vec u_x\cdot\vec u_y)=\cos^2\frac{\theta}{2}=\bigl|\langle\vec u_x+|\vec u_y+\rangle\bigr|^2,
$$

and the general Hilbert-space statement $p=\mathrm{Tr}(E\rho)$ coincides with the POVM form above. Concretely, the correspondences are: (i) idempotent $\leftrightarrow$ rank-one projector; (ii) state $\leftrightarrow$ density matrix; (iii) Hermitian form $\leftrightarrow$ Hilbert–Schmidt inner product, with the trace as its $2\times2$ reading; (iv) $\mathrm{Tr}(\tilde\Pi(\vec u_x)\tilde\Pi(\vec u_y)^{*})=\cos^2(\theta/2)$ $\leftrightarrow$ $|\langle\vec u_x+|\vec u_y+\rangle|^2$; (v) POVM in effects $\leftrightarrow$ POVM in operators. Each is an identity under $\iota$, not an approximation. The agreement is not a coincidence to be tested but an identity of notations, because $\mathbb{B}$ and $M_2(\mathbb{C})$ are the same algebra; any derivation in $\mathbb{B}$ is a derivation about $2\times2$ matrices.

The formulations differ in what they take as primitive. In the standard formalism a state is a vector and an observable an operator on vectors — different kinds of object; here both are elements of the single four-dimensional real space $\mathbb{B}_{\Psi}$, paired symmetrically. The statement $|\langle\xi_{\mathrm{alt}}|\tilde{Ξ}_{\mathrm{sp}}\rangle|^2$ is quadratic in amplitudes, while $\mathrm{Tr}(\tilde\Pi\tilde\Pi_{\mathrm{p}}^{*})$ is bilinear in the idempotents, so the symmetry of the transition probability is manifest rather than implicit. Writing $|\langle\xi_{\mathrm{alt}}|\tilde{Ξ}_{\mathrm{sp}}\rangle|^2$ requires choosing a Hilbert space and an inner product; the biquaternion pairing is supplied by the algebra's own product — it is the Hermitian form, $\mathrm{Sc}$ of the product with the second factor conjugated, positive definite on the whole algebra, and the trace is its $2\times2$ reading. This is the substance of the claim that the Born rule is a consequence of the algebra: the form of the pairing is not chosen, it is read off. The vector statement covers only pure states, whereas the normalised Hermitian form covers pure and mixed states and POVMs alike; it is a generalization of the vector statement, though a restatement of the general statement $p=\mathrm{Tr}(E\rho)$.

The comparison is for a single qubit, $\mathbb{B}\cong M_2(\mathbb{C})$. The extension to $n$ qubits uses $\mathbb{B}^{\otimes_\mathbb{C}n}\cong M_{2^n}(\mathbb{C})$ with $\mathrm{Tr}(x\otimes y)=\mathrm{Tr}(x)\mathrm{Tr}(y)$, and the normalised Hermitian form reproduces the standard Born rule there. The split $\mathbb{B}=\mathbb{B}_{\Psi}\oplus\mathbb{B}_{\Phi}$ exists for every $M_n(\mathbb{C})$, so "states and observables in one space" is not special to $n=2$; what is special is the identification with the biquaternion units and the factor $2$ in $\mathrm{Tr}=2\,\mathrm{Sc}$.

## Non-Uniqueness of the Tracial Reading

The tracial reading of the weight uses the functional $f=\mathrm{Sc}$, normalised by $f(e_t)=1$; its $2\times2$ reading is $\tfrac12\operatorname{Tr}$. The probability itself is the Hermitian form, $f(\tilde E_{\Psi}_i\tilde{Ϛ}_{\Psi}^{*})$, which coincides with $f(\tilde E_{\Psi}_i\tilde{Ϛ}_{\Psi})$ on $\mathbb{B}_{\Psi}$. On $M_n(\mathbb{C})$ the functionals satisfying $f(XY)=f(YX)$ form a one-dimensional space spanned by the trace. Hence on $\mathbb{B}$ every tracial functional is $f=\lambda\mathrm{Sc}$, and every symmetric pairing $\mathcal{B}(\tilde{R}_{\Psi,1},\tilde{R}_{\Psi,2})=f(\tilde{R}_{\Psi,1}\tilde{R}_{\Psi,2})$ with $f$ tracial is a multiple of the plain form. The normalisation $\mathrm{Sc}(e_t)=1$ fixes $\lambda=1$; the matrix reading is $\mathrm{Tr}=2\,\mathrm{Sc}$. Either gives the same probabilities, since the scale cancels in $p_i=\langle\tilde{E}_{\Psi}_i,\tilde{Ϛ}_{\Psi}\rangle_{*}/\langle\tilde{Ϛ}_{\Psi},e_t\rangle_{*}$ with $\langle\tilde{Ϛ}_{\Psi},e_t\rangle_{*}=\tfrac12$.

Uniqueness fails as soon as traciality is dropped. Keeping symmetry, invariance, and positivity leaves

$$
\mathcal{B}(\tilde{R}_{\Psi,1},\tilde{R}_{\Psi,2})=\alpha\,r_{t,1}r_{t,2}+\beta\,\vec r_{\Psi,1}\cdot\vec r_{\Psi,2},\qquad \alpha,\beta>0,
$$

a genuine two-parameter family; traciality is the extra condition $\alpha=\beta$. Keeping positivity and normalization but dropping traciality, the normalized positive functionals on $\mathbb{B}_{\Psi}$ are exactly the states: for every $\vec q\in\mathbb{R}^3$ with $|\vec q|\leq1$,

$$
f_{\vec q}(\tilde R_\Psi)=r_t+\vec q\cdot\vec r_\Psi
$$

is positive on the positive cone, being the pairing with the state $\tilde{Ϛ}_{\Psi,\vec q}=\tfrac12(e_t+i\vec q)$. Why is positivity restricted to $|\vec q|\leq1$? Under $\iota$ the functional is $f_{\vec q}(\tilde R_\Psi)=\mathrm{tr}(\rho_{\vec q}A)$ with $A=\iota(\tilde R_\Psi)$ and $\rho_{\vec q}=\tfrac12(I+\vec q\cdot\boldsymbol{\sigma})$; positivity of the functional is positivity of the density matrix, which holds exactly when $\vec q$ lies in the Bloch ball. The trace corresponds to $\vec q=0$, the maximally mixed state, which is the only point at which the functional is tracial. The trace is not the unique functional "chosen by nature"; it is the unique *tracial* functional. Concretely, extending $f_{\vec q}$ to $\mathbb{B}$ by $f_{\vec q}(\tilde{Q})=\mathrm{Re}(Q_t)+\vec q\cdot\vec v_i(\tilde{Q})$, where $\vec v_i$ is the coefficient of the imaginary vector part, one finds for $\tilde{Q}=\vec e_x$, $\tilde Q_y=i\vec e_y$ that $f_{\vec q}(\tilde{Q}\tilde Q_y)=+q_z$ while $f_{\vec q}(\tilde Q_y\tilde{Q})=-q_z$; the extension of $f_{\vec q}$ to $\mathbb{B}$ is not tracial unless $\vec q=0$.

There is a further uniqueness question: is the trace form the only probability measure on the projection lattice? In dimension at least three, **Gleason's theorem** says yes. In dimension two it **fails**: the projection lattice of $\mathbb{C}^2$ is the Bloch sphere with $P$ and $I-P$ complementary, and assignments in $[0,1]$ with complementary projectors summing to one need not be of trace form — non-trace frame functions exist. Uniqueness is restored if the domain is enlarged from projections to all effects and additivity is required there: by **Busch's** effect-based version of Gleason's theorem, a normalized additive assignment on the full effect algebra is of trace form in every dimension, including two. For a qubit, then, uniqueness of the probability measure is not a consequence of the algebra alone; it requires the effect structure, i.e. the POVM framework. It is significant that the trace formula extends cleanly to effects, since that is precisely the statement whose uniqueness is a theorem.

**Open question — the pairing at the other sector.** The weight is the Hermitian form $\langle\tilde{Ϛ}_{\Psi},\tilde R_\Psi\rangle_{*}$, positive definite on $\mathbb{B}$. On the material sector the physically relevant pairing is the indefinite Krein form $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}$, of signature $(3,1)$ up to the $i r'_t$ convention. **Whether the fundamental pairing of the framework is the Hermitian form at the informational sector or the Krein form at the material sector is open**, and the corpus's position is stated, not derived: the states are the informational ones and the pairing is the Hermitian form, with the trace as its $2\times2$ reading, and the material pairing is a calibration. The other side of the question is *The Physical Interpretation of the 12 Products*.

## What Is Derivation and What Is Restatement

**Derived.** From the algebra and its Hermitian subspace: (1) a canonical positive pairing on the whole algebra, fixed up to scale by the product condition on $\mathbb{B}_{\Psi}$, positivity and the normalisation $\langle e_t\rangle_{*}=1$; (2) a canonical family of rank-one idempotents, exactly the rank-one projectors under the isomorphism; (3) reality, positivity, and normalization of the state–idempotent pairing, hence a probability distribution for a projective measurement; (4) the expectation value $\langle\tilde{Ϛ}_{\Psi},\tilde R_\Psi\rangle_{*}/\langle\tilde{Ϛ}_{\Psi},e_t\rangle_{*}=r_t+\vec r\cdot\vec r_\Psi$ and the transition probability $\langle\tilde\Pi,\tilde\Pi_{\mathrm{p}}\rangle_{*}/\langle\tilde\Pi,e_t\rangle_{*}=\cos^2(\theta/2)$, with manifest symmetry; (5) the extension to effects and POVMs, with explicit non-projective examples; (6) exact agreement with the Hilbert-space formulas under $\mathbb{B}\cong M_2(\mathbb{C})$, a theorem about the algebra rather than an empirical coincidence.

**Restated.** Not derived from the algebra: (1) the identification of the pairing with **empirical frequency** — the algebra produces a canonical number in $[0,1]$, and reading it as a probability is the Born rule's empirical content, which no algebraic manipulation removes; (2) the choices of normalization and of the factor $2$, which are conventions, since the scale cancels in probabilities; (3) the general Hilbert-space statement $p=\mathrm{Tr}(E\rho)$, of which the biquaternion formula is a restatement for $n=2$, generalizing only the pure-vector statement $|\langle\xi_{\mathrm{alt}}|\tilde{Ξ}_{\mathrm{sp}}\rangle_{*}|^2$.

**Not explained.** The framework does not derive the uniqueness of the probability measure for a qubit from the algebra alone (Gleason fails in dimension two; Busch's theorem is needed); it does not explain why a particular outcome occurs (the measurement problem is unchanged); and it predicts no deviation from standard quantum physics. The claim that the Born rule is "a consequence of the algebra rather than an independent postulate" is correct about the **form** of the rule and the objects it relates, not about its empirical or interpretive content.

## Summary

The Born rule in the biquaternion framework is the normalised Hermitian form

$$
p=\frac{\langle\tilde{Ϛ}_{\Psi},\tilde R_\Psi\rangle_{*}}{\langle\tilde{Ϛ}_{\Psi},e_t\rangle_{*}}
 =\frac{\mathrm{Sc}(\tilde{Ϛ}_{\Psi}\tilde R_\Psi^{*})}{\mathrm{Sc}(\tilde{Ϛ}_{\Psi})}
 =r_t+\vec r\cdot\vec r_\Psi,
\qquad \langle\tilde{Ϛ}_{\Psi},e_t\rangle_{*}=\tfrac12\langle e_t\rangle_{*},\quad \langle e_t\rangle_{*}=1,
$$

with $\langle\tilde Q_1,\tilde Q_2\rangle_{*}=\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})$ and $\langle\tilde Q\rangle_{*}=\sum_\mu\lvert Q_\mu\rvert^{2}$. The star is the Hermitian conjugation and it carries the positivity: $\langle\tilde Q\rangle_{*}$ is positive definite on the whole algebra, and for $\tilde{Ϛ}_{\Psi}\ge0$, $0\le\tilde R_\Psi\le e_t$ the weight is $2\,\mathrm{Sc}(\tilde{Ϛ}_{\Psi}^{1/2}\tilde R_\Psi\tilde{Ϛ}_{\Psi}^{1/2})\in[0,1]$. The plain form $\langle\tilde Q_1,\tilde Q_2\rangle=\mathrm{Sc}(\tilde Q_1\tilde Q_2)$ is the restriction of the Hermitian form to $\mathbb{B}_{\Psi}$, where $\tilde R_\Psi^{*}=\tilde R_\Psi$, so the same weight is $\mathrm{Sc}(\tilde{Ϛ}_{\Psi}\tilde R_\Psi)/\mathrm{Sc}(\tilde{Ϛ}_{\Psi})$; it is positive definite of signature $(4,0)$ there and negative definite on $\mathbb{B}_{\Phi}$. The biquaternion norm $\langle\tilde R_\Psi\rangle_{\natural}=r_t^2-|\vec r_\Psi|^2$ is a third object, whose future cone cuts out the state space.

Under $\iota:\mathbb{B}\to M_2(\mathbb{C})$ the idempotents map to rank-one projectors, states to density matrices, and $\mathrm{tr}\circ\iota=\mathrm{Tr}$. The probability $p_+=\langle\tilde\Pi_1(\vec u_\Psi),\tilde{Ϛ}_{\Psi}\rangle_{*}/\langle\tilde{Ϛ}_{\Psi},e_t\rangle_{*}=\tfrac12(1+\vec u_\Psi\cdot\vec r)$ is real, in $[0,1]$, and normalized, all as consequences of the algebra. General measurements are effects $\tilde{E}_{\Psi}=ae_t+i\vec w$ with $|\vec w|\leq\min(a,1-a)$; POVMs are families of effects summing to $e_t$; the probabilities are $\langle\tilde E_{\Psi}_i,\tilde{Ϛ}_{\Psi}\rangle_{*}/\langle\tilde{Ϛ}_{\Psi},e_t\rangle_{*}=a_i+\vec w_i\cdot\vec r$, as the unsharp and trine examples show. Normalisation is the only place the trace is read: with $\operatorname{Tr}(e_t)=2$, the normalised state has $\operatorname{Tr}(\tilde{Ϛ}_{\Psi})=2\,\mathrm{Sc}(\tilde{Ϛ}_{\Psi})=1$, and the same weight is $p=\operatorname{Tr}(\tilde{Ϛ}_{\Psi}\tilde R_\Psi^{*})/\operatorname{Tr}(\tilde{Ϛ}_{\Psi})=\operatorname{Tr}(\tilde{Ϛ}_{\Psi}\tilde R_\Psi)/\operatorname{Tr}(\tilde{Ϛ}_{\Psi})$, the factor $2$ being the dimension of the image and the star in the numerator being inert on $\mathbb{B}_{\Psi}$.

The comparison with the standard statement is exact, because $\mathbb{B}\cong M_2(\mathbb{C})$ as $*$-algebras: the biquaternion formula and $p=\mathrm{Tr}(E\rho)$ are the same equation, and the pure case is $|\langle\xi_{\mathrm{alt}}|\tilde{Ξ}_{\mathrm{sp}}\rangle_{*}|^2=\cos^2(\theta/2)$. The formulations differ in what they take as primitive and in the manifest symmetry of the transition probability. The trace is unique up to scale among tracial functionals, but symmetry, invariance and positivity alone leave a two-parameter family, and the normalized positive non-tracial functionals are exactly the states. Uniqueness of the probability measure requires more than the algebra: Gleason fails for a qubit on projections, and Busch's effect-based theorem restores uniqueness. The framework derives the form of the Born rule and its consistency properties, restates the identification with empirical probability, and does not explain outcome selection or predict departures from standard quantum physics.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$, $\vec e_\mu^2 = -e_t$ | Quaternion basis |
| $i$ | Scalar imaginary, $i^2 = -1$ |
| $\mathbb{B}_{\Psi}$ | Hermitian subspace (states, observables, effects) |
| $\mathbb{B}_{\Phi}$, $\mathbb{B} = \mathbb{B}_{\Psi}\oplus\mathbb{B}_{\Phi}$ | Anti-Hermitian subspace (generators) |
| $\tilde R_\Psi = r_t e_t + i\vec r_\Psi$ | General Hermitian element |
| $\langle\tilde{R}_{\Psi,1},\tilde{R}_{\Psi,2}\rangle_{*}=\mathrm{Sc}(\tilde{R}_{\Psi,1}\tilde{R}_{\Psi,2}^{*})$, $\langle\tilde R_\Psi\rangle_{*}=\langle\tilde R_\Psi,\tilde R_\Psi\rangle_{*}$ | Hermitian form and Hermitian norm; positive definite, $(8,0)$ on $\mathbb{B}$, $(4,0)$ on $\mathbb{B}_{\Psi}$ |
| $\langle\tilde{R}_{\Psi,1},\tilde{R}_{\Psi,2}\rangle=\mathrm{Sc}(\tilde{R}_{\Psi,1}\tilde{R}_{\Psi,2})$, $\langle\tilde R_\Psi\rangle=\langle\tilde R_\Psi,\tilde R_\Psi\rangle$ | Plain form and plain norm: the restriction of the Hermitian form to $\mathbb{B}_{\Psi}$ |
| $\langle e_t\rangle_{*}=1$, $\langle\tilde{Ϛ}_{\Psi},e_t\rangle_{*}=\tfrac12$ | Unit and state normalisation |
| $\langle\tilde R_\Psi\rangle_{\tilde{Ϛ}_{\Psi},*}=\langle\tilde{Ϛ}_{\Psi},\tilde R_\Psi\rangle_{*}/\langle\tilde{Ϛ}_{\Psi},e_t\rangle_{*}=\mathrm{Sc}(\tilde{Ϛ}_{\Psi}\tilde R_\Psi^{*})/\mathrm{Sc}(\tilde{Ϛ}_{\Psi})=r_t+\vec r\cdot\vec r_\Psi$ | Born weight |
| $\mathrm{Tr}(\tilde R_\Psi)=2\,\mathrm{Sc}(\tilde R_\Psi)=2c r_t$, $\mathrm{Tr}(\tilde{R}_{\Psi,1}\tilde{R}_{\Psi,2}^{*})=2\,\mathrm{Sc}(\tilde{R}_{\Psi,1}\tilde{R}_{\Psi,2}^{*})$ | Trace, the $2\times2$ reading; stated once, at normalisation |
| $\langle\tilde R_\Psi\rangle_{\natural} = \langle\tilde R_\Psi,\tilde R_\Psi\rangle_{\natural} = \tilde R_\Psi\tilde R_\Psi^{\natural} = (r_t^2 - |\vec r_\Psi|^2)e_t$ | Biquaternion norm, signature $(1,3)$ |
| $\tilde{Ϛ}_{\Psi} = \tfrac{1}{2}(e_t + i\vec r)$, $|\vec r|\leq 1$ | State, $\langle\tilde{Ϛ}_{\Psi},e_t\rangle_{*}=\tfrac12$; Bloch vector $\vec r$ |
| $\tilde\Pi_{1,2}(\vec u) = \tfrac{1}{2}(e_t \pm i\vec u)$, $|\vec u|=1$ | Idempotent (pure state) |
| $\tilde{E}_{\Psi} = a e_t + i\vec w$, $|\vec w|\leq\min(a,1-a)$ | Effect |
| $\langle\tilde\Pi_1(\vec u_\Psi),\tilde{Ϛ}_{\Psi}\rangle_{*}/\langle\tilde{Ϛ}_{\Psi},e_t\rangle_{*} = \tfrac{1}{2}(1+\vec u_\Psi\cdot\vec r)$ | Born probability, projective |
| $\langle\tilde{E}_{\Psi}_i,\tilde{Ϛ}_{\Psi}\rangle_{*}/\langle\tilde{Ϛ}_{\Psi},e_t\rangle_{*} = a_i + \vec w_i\cdot\vec r$ | Born probability, POVM |
| $\langle\tilde\Pi(\vec u_x),\tilde\Pi(\vec u_y)\rangle_{*}/\langle\tilde\Pi,e_t\rangle_{*} = \tfrac{1}{2}(1+\vec u_x\cdot\vec u_y) = \cos^2(\theta/2)$ | Transition probability; in the $2\times2$ image $\mathrm{Tr}(\tilde\Pi\tilde\Pi_{\mathrm{p}}^{*})$ |
| $\iota: e_t\mapsto I_2$, $\vec e_\mu\mapsto -i\sigma_\mu$ | Isomorphism $\mathbb{B}\to M_2(\mathbb{C})$ |
| $\mathrm{tr}\circ\iota = \mathrm{Tr}$ | Trace correspondence |
| $\tilde M_{\mathrm{kraus},i}$, $\sum_i\tilde M_{\mathrm{kraus},i}^{*}\tilde M_{\mathrm{kraus},i} = e_t$ | Kraus operators (measurement update) |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle$ | the general plain bilinear form, the scalar part of the general plain bilinear product, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2)$ |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{*}$ | the Hermitian form, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2^{*})$, the probability pairing; on the diagonal $\langle\tilde{Q}_2,\tilde{Q}_2\rangle_{*}=\sum_\mu\lvert Q_{2\mu}\rvert^{2}\ge0$ |

## Further Reading

- John von Neumann, *Mathematical Foundations of Quantum Mechanics* (Princeton, 1932), for the original formulation of the Born rule and the density matrix.
- Andrew M. Gleason, "Measures on the closed subspaces of a Hilbert space," *Journal of Mathematics and Mechanics* **6** (1957) 885–893, for the uniqueness of the trace form on projection lattices in dimension three and above.
- Paul Busch, "Quantum states and generalized observables: a simple proof of Gleason's theorem," *Physical Review Letters* **91** (2003) 120403, for the effect-based theorem that covers the qubit.
- Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information* (Cambridge, 2000), for the standard treatment of the Born rule, POVMs, and the Bloch ball.
- K. Kraus, *States, Effects, and Operations* (Springer, 1983), for effects, POVMs, and the structure of state and observable spaces.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the algebraic structure of $\mathrm{Cl}_{1,3}$, the idempotents, and the trace.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the geometric-algebra treatment of projectors, spinors, and the state space.
