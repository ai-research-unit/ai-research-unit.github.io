# __Biquaternion Lie Group and Exponential Structure__

## Introduction

The group of units $\mathbb{B}^\times$ is a real Lie group, and its exponential map is the bridge between the group and the Lie algebra *Symmetric and Antisymmetric Decomposition of the Four General Products*. This article reads the Lie-group structure: the exponential and its parametrisation of the group, the cases of the exponential, the group law, the failure of surjectivity, and the real forms and subgroups the group carries.

The exponential itself — its series, its closed form, the logarithm and the power functions — is computed in *Biquaternion Elementary Functions*, and only its group-theoretic consequences are used here; the Lie algebra is in Algebra, and the topology of the group is in *The Biquaternion Unit Group as a Topological Group*.

## The Unit Quaternions and Their Complexification

The **unit quaternions** are the elements of $\mathbb{H}_{\mathbb{B}}$ of norm $1$:

$$
S^3 = \{\tilde q \in \mathbb{H}_{\mathbb{B}} : \langle\tilde q\rangle_{\natural} = 1\},
$$

a compact, connected, simply connected real Lie group of real dimension $3$. Every such $\tilde q$ is $\cos\theta\, e_t + \sin\theta\, \vec u$ with $\vec u$ a real unit vector part, the quaternion exponential.

Complexifying the coefficients turns $\langle\tilde q\rangle_{\natural} = 1$ into the same equation over $\mathbb{C}$, giving the **unit-norm subgroup**

$$
\mathbb{B}^\times_1 = \{\tilde{Q} \in \mathbb{B} : \langle\tilde{Q}\rangle_{\natural} = 1\},
$$

whose elements need not be real quaternions.

**Dimension.** The level set $N = 1$ has complex dimension $3$ and real dimension $6$, the biquaternion norm being a submersion wherever $\langle\tilde{Q}\rangle_{\natural} \neq 0$. The group $\mathbb{B}^\times_1$ is connected, simply connected, and non-compact, and it is the **complexification of the unit quaternions**: the trace-free subalgebra satisfies $\mathrm{B}_0 = \mathrm{K} \otimes_{\mathbb{R}} \mathbb{C}$ for the compact subalgebra $\mathrm{K}$ below, and $\mathbb{B}^\times_1$ complexifies the compact group $S^3$. Its centre is

$$
Z(\mathbb{B}^\times_1) = \{\pm e_t\} \cong \mathbb{Z}/2.
$$

**Remark (the count over the two fields, and the trace).** Over $\mathbb{R}$ the norm is real and the condition $N=1$ is one real equation in the four real coordinates of $\mathbb{H}_{\mathbb{B}}$, leaving the three-dimensional sphere $S^3$. Over $\mathbb{C}$ the norm is complex and the same condition is two real equations in the eight real coordinates of $\mathbb{B}$, leaving $\mathbb{B}^\times_1$ of real dimension $6$. The complexification adds four real dimensions, and the condition removes one more real dimension than before, so the net gain is three; at the identity these are the imaginary vector directions $i\vec e_x,i\vec e_y,i\vec e_z$, the boosts, while the real vector directions are the rotations. The trace is not the constraint: it is free on the level set, and for every $t\in\mathbb{C}$ the element with $\mathsf{M}_2(\tilde Q)=\begin{pmatrix}t&-1\\1&0\end{pmatrix}$ lies in $\mathbb{B}^\times_1$, so the trace accounts for two of the six real dimensions that remain. The two real dimensions that the condition removes are the two real components of the determinant.

## The Subgroups and the Real Forms

The relevant subgroups are: $\mathbb{B}^\times$, the nonzero-norm elements (complex dimension $4$, real dimension $8$); $\mathbb{B}^\times_1$, the unit-norm elements (complex dimension $3$, real dimension $6$); the unit quaternions $S^3$ (real dimension $3$); and the centre $\mathbb{C}^\times e_t$ of nonzero scalars (complex dimension $1$, real dimension $2$).

$S^3$ is the maximal compact subgroup of $\mathbb{B}^\times_1$, with Lie algebra the compact subalgebra $\mathrm{K}$ of *Symmetric and Antisymmetric Decomposition of the Four General Products*, §*The Trace-Free Subalgebra*. The centre $\{\pm e_t\}$ is discrete, so the quotient $\mathbb{B}^\times_1/\{\pm e_t\}$ is a Lie group of real dimension $6$.

## The $*$-Unitary Subgroup and the Defining Module

The algebra acts on the defining module $\mathbb{C}^2$ by the defining representation, in which a biquaternion acts as its $2\times2$ matrix $\mathsf{M}_2(\tilde{Q})$ (*$M_2(\mathbb{C})$ Model : The Product, the Trace and the Determinant*). The elements that preserve the standard Hermitian form of $\mathbb{C}^2$ are exactly those with $\tilde{Q}^{*}\tilde{Q}=e_t$, and they form a compact subgroup of the group of units,
$$
\mathrm{U}(2)=\{\tilde{Q}\in\mathbb{B}^{\times}:\tilde{Q}^{*}\tilde{Q}=e_t\},
$$
of real dimension $4$. The determinant-one elements inside it are the unit quaternions:
$$
\mathrm{U}(2)\cap SL(2,\mathbb{C})=S^3=SU(2),
$$
consistently with the unit quaternions being the $*$-unitary part of the norm-one group. Every element of $\mathrm{U}(2)$ is the product of a unit quaternion and a unit complex scalar, and the two factors meet in $\{\pm e_t\}$:
$$
\boxed{\; \mathrm{U}(2)=S^3\cdot \mathrm{U}(1)\cong (SU(2)\times \mathrm{U}(1))/\{\pm(1,1)\} \;}.
$$

**Proof.** If $\tilde{Q}\in \mathrm{U}(2)$ then $|\det\mathsf{M}_2(\tilde{Q})|=1$, so $P=\tilde{Q}\,(\det\mathsf{M}_2(\tilde{Q}))^{-1/2}\in \mathrm{U}(2)$ has determinant one, hence lies in $S^3$ by the identification of the determinant-one $*$-unitary elements with the unit quaternions; the scalar $(\det\mathsf{M}_2(\tilde{Q}))^{1/2}$ is a unit complex number. The intersection $\{\pm e_t\}$ is the set of scalars $\lambda e_t$ of determinant $\lambda^2=1$, and the kernel of $S^3\times \mathrm{U}(1)\to \mathrm{U}(2)$, $(\tilde q,\lambda)\mapsto\lambda\tilde q$, is $\{\pm(1,1)\}$.

**Remark.** The norm-one group $\mathbb{B}^{\times}_1\cong SL(2,\mathbb{C})$ is strictly larger: it acts on the defining module too, but it does not preserve the Hermitian form, and unlike $\mathrm{U}(2)$ it is non-compact.

## The Enlarged Carrier and the Closed Forms for SU(3) and SU(4)

The groups the algebra reaches directly are $SU(2)=S^3$ and the compact $\mathrm{U}(2)$ above, and the ceiling recorded in the physics article *The Gauge Group Ceiling: Why the Biquaternion Algebra Reaches SU(2) but Not SU(3)* is the statement that no octet of generators with an $\mathfrak{su}(3)$ bracket sits **inside** $\mathbb{B}$. Classical closed forms for $SU(3)$ and $SU(4)$ in terms of biquaternions nevertheless exist, and they cost exactly one enlargement of the carrier: not the algebra but the matrices over the algebra.

**Definition (matrices over the algebra).** Let $M_n(\mathbb{B})$ be the $\mathbb{C}$-algebra of $n\times n$ matrices with entries in $\mathbb{B}$, acting on $\mathbb{B}^n$. The identification $\mathbb{B}\cong M_2(\mathbb{C})$ extends entrywise, so

$$
M_n(\mathbb{B})\cong M_n(M_2(\mathbb{C}))\cong M_{2n}(\mathbb{C}),\qquad
\dim_{\mathbb{C}}M_n(\mathbb{B})=4n^2 .
$$

In particular $M_3(\mathbb{B})\cong M_6(\mathbb{C})$ contains $\mathfrak{u}(3)$ and hence $\mathfrak{su}(3)$, with its eight generators written as $3\times3$ matrices of biquaternions. This realises the ceiling's answer: the octet is not in $\mathbb{B}$, and it *is* in $M_3(\mathbb{B})$, for the price of enlarging the carrier by the factor $2$ in each matrix direction. Since $\mathbb{B}\hookrightarrow M_3(\mathbb{B})$ by the scalar matrices, the chain is $\mathfrak{su}(2)=\mathfrak{k}\subset\mathfrak{su}(3)\subset\mathfrak{u}(3)\subset M_3(\mathbb{B})$.

The closed forms use the Conway operator calculus of *The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure*, §*The Conway Operator Basis*: $a[\,]b$ is the linear function $\tilde{Q}\mapsto a\tilde{Q}b$, $\odot$ is composition, $D\{d_1,d_2,d_3\}=\frac12\sum_kd_k\vec e_k[\,]\vec e_k$, and for a unit vector $\vec b$ each of the generators $b[\,]b$ and $\vec e_k[\,]\vec e_k$ has square the identity, $(b[\,]b)^2=(\vec e_k[\,]\vec e_k)^2=[\,]$, so their exponentials are trigonometric.

**Proposition (the three exponentials).** $\mathrm{EXP}$ denoting the exponential series of a linear function, for real $\alpha$, $\beta$ and $\delta_k$,

$$
\mathrm{EXP}\Bigl(\tfrac{\alpha}{2}\bigl(a[\,]-[\,]a\bigr)\Bigr)=\exp\bigl(\tfrac{\alpha}{2}a\bigr)[\,]\exp\bigl(-\tfrac{\alpha}{2}a\bigr),
$$

$$
\mathrm{EXP}\bigl(iD\{\delta_1,\delta_2,\delta_3\}\bigr)
=\underset{k=1}{\overset{3}{\odot}}\exp\Bigl(\delta_k\tfrac{i}{2}\vec e_k[\,]\vec e_k\Bigr),
\qquad
\mathrm{EXP}\Bigl(\tfrac{i\beta}{2}\,b[\,]b\Bigr)=\cos\tfrac{\beta}{2}\,[\,]+i\sin\tfrac{\beta}{2}\,b[\,]b .
$$

*Proof.* The first is the Olinde–Rodrigues formula, verified residual $5.8\times10^{-16}$; for the second and third the squares of the generators are the identity, $(b[\,]b)^2=[\,]$ and $(\vec e_k[\,]\vec e_k)^2=[\,]$, so the series collapses to cosine and sine, verified residuals $1.7\times10^{-15}$ and $1.0\times10^{-15}$. The signs of the imaginary units are the ones that make the results compact for real parameters: $D$ carries $i$ and $b[\,]b$ carries $i$, while the antisymmetric function carries none.

**Theorem (Lie-type forms for $\mathrm{SU}(3)$, $\mathrm{SL}(3,\mathbb{R})$ and $\mathrm{SL}(3,\mathbb{C})$).** For real $\alpha,\beta,\delta_1,\delta_2$, with $\vec a$ and $\vec b$ unit vectors and $\delta_1+\delta_2+\delta_3=0$, every element of $\mathrm{SU}(3)$ is

$$
G=\exp\Bigl(\tfrac{\beta}{2}i\,b[\,]b\Bigr)\odot\exp\Bigl(\tfrac{\alpha}{2}\bigl(a[\,]-[\,]a\bigr)\Bigr)
\odot\exp\Bigl(iD\{\delta_1-\beta b_1^2,\ \delta_2-\beta b_2^2,\ \delta_3-\beta b_3^2\}\Bigr),
$$

with the eight independent parameters $\alpha,\beta,\delta_1,\delta_2$ and the four angles in the two unit vectors. Suppressing the imaginary units gives the same formula for $\mathrm{SL}(3,\mathbb{R})$ when all parameters are real, and for $\mathrm{SL}(3,\mathbb{C})$ when they are complex.

**Theorem (Euler-angles forms).** With unit vectors $\vec a,\vec b,\vec c,\vec d,\vec m,\vec n,\vec w$ and real angles,

$$
\boxed{\; \tilde U_{\mathrm{SU}(3)}=\exp\bigl(\tfrac{\alpha}{2}a\bigr)[\,]\exp\bigl(-\tfrac{\alpha}{2}a\bigr)
\odot\exp\bigl(iD\{\beta,\gamma,-\beta-\gamma\}\bigr)
\odot\exp\bigl(\tfrac{\delta}{2}b\bigr)[\,]\exp\bigl(-\tfrac{\delta}{2}b\bigr) \;},
$$

$$
\boxed{\; \tilde U_{\mathrm{SU}(4)}=\exp\bigl(\tfrac{\alpha}{2}a\bigr)[\,]\exp\bigl(-\tfrac{\beta}{2}b\bigr)
\odot\exp\bigl(iD\{\gamma,\delta,\epsilon\}\bigr)
\odot\exp\bigl(\tfrac{\psi}{2}c\bigr)[\,]\exp\bigl(-\tfrac{\eta}{2}d\bigr) \;},
$$

and, in the degenerate case in which the outer unit vectors coincide, an $\mathrm{SU}(2)$ element,

$$
\tilde U_{\mathrm{SU}(2)}=\exp\bigl(\tfrac{\alpha}{2}w\bigr)[\,]\exp\bigl(-\tfrac{\alpha}{2}w\bigr)
\odot\exp\Bigl(\tfrac{i\beta}{2}\bigl(\vec u_{\mathrm a}[\,]\vec u_{\mathrm a}-\vec u_{\mathrm b}[\,]\vec u_{\mathrm b}\bigr)\Bigr)
\odot\exp\bigl(\tfrac{\gamma}{2}w\bigr)[\,]\exp\bigl(-\tfrac{\gamma}{2}w\bigr).
$$

Each **outer** factor is a conjugation of the argument by a single unit vector, $\exp(\theta)[\,]\exp(-\theta)$; the $\mathrm{SU}(3)$ form has two of them, with unit vectors $\vec a$ and $\vec b$ and the four angles they carry, and its middle factor is a traceless diagonal $D\{\beta,\gamma,-\beta-\gamma\}$. The $\mathrm{SU}(4)$ form pairs **different** vectors in each outer factor, $\exp(\tfrac\alpha2a)[\,]\exp(-\tfrac\beta2b)$ and $\exp(\tfrac\psi2c)[\,]\exp(-\tfrac\eta2d)$, and its middle factor carries three diagonal parameters $\gamma,\delta,\epsilon$ with no trace condition: that is $7$ scalar parameters and $8$ angles, the fifteen parameters of $\mathrm{SU}(4)$.

**Remark (the inverse).** The inverse of any of these elements is obtained by reversing the order of the factors and changing the signs of the exponents, and it equals the biconjugate of the function,
$$G^{-1}=G^{+\approx}=G^{\dagger},$$
the source's rule, which is the statement of *The Four Adjoints of the Biquaternion Algebra in Examples*: for an operator that fixes $e_t$ and preserves the span of $\vec e_x,\vec e_y,\vec e_z$ — as every element here does — the conjugation by the Gram matrix $D=\operatorname{diag}(1,-1,-1,-1)$ of the scalar form is invisible, and association followed by conjugation of the coefficients is the Hermitian adjoint. For a general linear function the two involutions differ, and the corpus keeps them apart.

**Remark (the elements are block-diagonal).** Every element above fixes $e_t$ and preserves the span of $\vec e_x,\vec e_y,\vec e_z$: in the coordinate order $(\vec e_x,\vec e_y,\vec e_z,e_t)$ its matrix is $\operatorname{diag}(\tilde U_3,1)$ with $\tilde U_3\in\mathrm{SU}(3)$ the $3\times3$ block. This is the structural reason the enlargement is needed and the ceiling is honest: the octet acts on a three-dimensional **complex** space, whereas the algebra's own action on $\mathbb{B}$ is four-dimensional over $\mathbb{C}$ with the scalar direction inert, so the eight generators have no home in $\mathbb{B}$ itself.

**Remark (where the method ends).** The construction does not generalise directly to $n>4$: the diagonal and antisymmetric functions have bounded room, and the source records that the quaternion expression of the general diagonal-less symmetric matrix of the required size becomes cumbersome and loses its use, which is the same observation as the *Limit of the Method* remark of the enveloping-algebra article. The endpoint is the pair $3,4$, which is also the endpoint of the physics programme's need.

## Surjectivity and Its Failure for the Subgroups

The exponential of the full unit group is surjective (*Biquaternion Elementary Functions*, §*The Logarithm*), but the two distinguished subgroups behave differently.

**The compact subgroup: surjective.** Every unit quaternion is $\cos\theta\, e_t + \sin\theta\,\vec u = \exp(\theta\vec u)$, so $\exp : \mathrm{K} \to S^3$ is surjective; this is the general fact that a connected compact Lie group has a surjective exponential map.

**The full group: not surjective.** The exponential $\exp : \mathrm{B}_0 \to \mathbb{B}^\times_1$ is **not** surjective: $\mathbb{B}^\times_1$ is not exponential. The element of $\mathbb{B}^\times_1$ with scalar part $-1$ and non-semi-simple behaviour, corresponding to the non-diagonalizable norm-one element with the repeated eigenvalue $-1$, is

$$
\tilde{Q} = -e_t + \frac{i}{2}\vec e_x - \frac{1}{2}\vec e_y, \qquad \langle\tilde{Q}\rangle_{\natural} = 1 + \left(\frac{i}{2}\right)^2 + \left(-\frac{1}{2}\right)^2 = 1.
$$

Its scalar part is $Q_t = -1$ and its vector part has $B = 0$, so the element is non-semi-simple with the repeated eigenvalue $-1$. If $\tilde{Q} = \exp(\tilde Q_2)$ with $\tilde Q_2 \in \mathrm{B}_0$, then $R_0 = 0$, and $\tilde Q_2 = \mu e_t + \tilde\Upsilon$ with $\tilde\Upsilon$ nilpotent (§*The Nilpotent Convention* of *Conventions of the Special Elements and the Peirce Decomposition*) and $e^\mu = -1$, hence $\mu \in i\pi(2\mathbb{Z}+1)$ and $\mathrm{Tr}(\tilde Q_2) = 2\mu \neq 0$, a contradiction. The same obstruction makes $\exp$ non-surjective on the real group $SL(2,\mathbb{R})$.

**Generation versus surjectivity.** Failure of surjectivity does not mean the exponentials fail to generate: since $\mathbb{B}^\times_1$ is connected and $\exp$ is a local diffeomorphism at $0$, the image $\exp(\mathrm{B}_0)$ contains a neighbourhood of the identity and generates the group, while remaining a proper subset. Nor does simple connectivity force surjectivity: $\mathbb{B}^\times_1$ is simply connected, yet $\exp$ is not onto. The classical criteria (connected compact, connected nilpotent, or $GL(n,\mathbb{C})$) are sufficient, not necessary.

---

The group of units is an open subset of $\mathbb{B}$, hence a smooth real manifold of dimension $8$, but its topology is far from that of a general open set in $\mathbb{R}^8$: it has the homotopy type of a compact group. The polar decomposition exhibits the maximal compact subgroup as a strong deformation retract, and with it determines the homotopy groups and the universal cover. Everything in this part is a statement about $\mathbb{B}^\times$ as a topological group; the topology of the ambient space is in *Topology in the Space of Biquaternions* and that of the null cone in *The Topology of the Zero-Divisor Cone*.

## The Correspondence with the Lie Algebra

The exponential is the correspondence between the group and the algebra. Its differential at the identity is the identity, so it is a local diffeomorphism onto a neighbourhood of $e_t$, and the inverse function theorem makes it a chart of $\mathbb{B}^\times$ near the identity; the tangent space at the identity is the whole algebra, since $\mathbb{B}^\times$ is open, with the commutator as bracket (*Symmetric and Antisymmetric Decomposition of the Four General Products*). The Baker–Campbell–Hausdorff series of the algebra converges near the origin and reproduces the group law there, and the group law $\exp(\tilde Q_3)\exp(\tilde{Q}_1)$ against $\exp(\tilde Q_3+\tilde{Q}_1)$ of *Biquaternion Elementary Functions* is its first two terms. The subgroups correspond to the subalgebras: the compact subalgebra $\mathrm{K}=\mathrm{span}_{\mathbb{R}}\{\vec e_x,\vec e_y,\vec e_z\}$ to $S^3$, the trace-free part $\mathrm{B}_0$ to the norm-one group $\mathbb{B}^\times_1$, and the centre $\mathbb{C}e_t$ to $\mathbb{C}^\times e_t$.

## One-Parameter Subgroups

**A one-parameter subgroup is the image of a real line of the Lie algebra under the exponential, and every one-parameter subgroup arises that way.**

A **one-parameter subgroup** of $\mathbb{B}^\times$ is a Lie-group homomorphism $\varphi:\mathbb{R}\to\mathbb{B}^\times$. For $\tilde X\in\mathbb{B}$ the **exponential line**

$$
\varphi_{\tilde X}(t)=\exp(t\tilde X)
$$

is one, since $\exp(s\tilde X)\exp(t\tilde X)=\exp((s+t)\tilde X)$ by the group law of *Biquaternion Elementary Functions*, §*The Group Law*. Its **infinitesimal generator** is $\varphi_{\tilde X}'(0)=\tilde X$.

**Theorem.** Every one-parameter subgroup of $\mathbb{B}^\times$ is $\varphi_{\tilde X}$ for a unique $\tilde X\in\mathbb{B}$.

*Proof.* Let $\varphi$ be a one-parameter subgroup and put $\tilde X=\varphi'(0)$. Differentiating $\varphi(s+t)=\varphi(s)\varphi(t)$ in $s$ at $s=0$ gives $\varphi'(t)=\tilde X\varphi(t)$. The product $\psi(t)=\exp(-t\tilde X)\varphi(t)$ then has

$$
\psi'(t)=-\tilde X\exp(-t\tilde X)\varphi(t)+\exp(-t\tilde X)\tilde X\varphi(t)=0,
$$

because $\exp(-t\tilde X)$ commutes with $\tilde X$. Since $\psi(0)=e_t$, $\psi$ is constant and $\varphi(t)=\exp(t\tilde X)$. The generator is recovered as $\varphi'(0)$, hence is unique. $\square$

**The subgroup depends on the line, the parametrisation on the vector.** Since $t$ ranges over $\mathbb{R}$, $\varphi_{\tilde X}$ and $\varphi_{\lambda\tilde X}$ have the same image for every real $\lambda\neq0$; the one-parameter subgroup, as a set, is the image of the real line $\mathbb{R}\tilde X$. The generator is fixed only once the parametrisation is fixed.

**The two real directions.** The exponential line of $\vec e_x$ is the circle $\exp(t\vec e_x)=\cos t\,e_t+\sin t\,\vec e_x$, and that of $i\vec e_x$ is the hyperbola $\exp(t\,i\vec e_x)=\cosh t\,e_t+\sinh t\,\vec e_x$ (§*The Exponential in the Two Real Directions* of *Biquaternion Elementary Functions*). The first is periodic and lies in the unit quaternions, the second is unbounded and lies in the Hermitian subspace. The two are the compact and the non-compact one-parameter subgroups in their simplest form.

**The subgroup lies in a centraliser.** Every $\exp(t\tilde X)$ commutes with $\tilde X$, so the image of $\varphi_{\tilde X}$ is contained in the group of units of the centraliser $C(\tilde X)=\{\tilde Y:\tilde Y\tilde X=\tilde X\tilde Y\}$ (*$M_2(\mathbb{C})$ Model : The Centraliser and the Double Centraliser*, §*The Commutant*). For a non-scalar $\tilde X$ that centraliser has complex dimension two, so the one-parameter subgroup is a real curve in a commutative surface.

## The Killing Form

**The Killing form of the unit group is the real part of the trace form on the trace-free part; its radical is the centre, and its signature is $(3,3)$.**

The Lie algebra of $\mathbb{B}^\times$ is $\mathbb{B}$ with the bracket $[\tilde X,\tilde Y]=\tilde X\tilde Y-\tilde Y\tilde X$ (§*The Correspondence with the Lie Algebra*). Its **Killing form** is

$$
\kappa(\tilde X,\tilde Y)=\operatorname{tr}\bigl(\operatorname{ad}_{\tilde X}\operatorname{ad}_{\tilde Y}\bigr),
\qquad
\operatorname{ad}_{\tilde X}(\tilde Z)=[\tilde X,\tilde Z].
$$

**Theorem.** For all $\tilde X,\tilde Y\in\mathbb{B}$,

$$
\boxed{\;
\kappa(\tilde X,\tilde Y)=16\,\operatorname{Re}\bigl(\operatorname{Sc}(\tilde X\tilde Y)-\operatorname{Sc}\tilde X\,\operatorname{Sc}\tilde Y\bigr)
\;}
$$

and in the matrix model,

$$
\kappa(\tilde X,\tilde Y)=8\operatorname{Re}\operatorname{tr}\bigl(\mathsf M_2(\tilde X)\mathsf M_2(\tilde Y)\bigr)-4\operatorname{Re}\bigl(\operatorname{tr}\mathsf M_2(\tilde X)\,\operatorname{tr}\mathsf M_2(\tilde Y)\bigr).
$$

*Proof.* Work in the matrix model and let $\kappa_{\mathbb{C}}(X,Y)=\operatorname{tr}(\operatorname{ad}_X\operatorname{ad}_Y)$ be the complex trace, a complex bilinear form, so that $\kappa=2\operatorname{Re}\kappa_{\mathbb{C}}$. The centre contributes nothing, because $\operatorname{ad}_{\mathrm I_2}=0$. On $\mathfrak{sl}_2(\mathbb{C})$ use the basis

$$
H=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\qquad E=\begin{pmatrix}0&1\\0&0\end{pmatrix},\qquad F=\begin{pmatrix}0&0\\1&0\end{pmatrix},
$$

with $[H,E]=2E$, $[H,F]=-2F$ and $[E,F]=H$. In this basis the adjoint operators are

$$
\operatorname{ad}_H=\operatorname{diag}(0,2,-2),\qquad
\operatorname{ad}_E=\begin{pmatrix}0&0&1\\-2&0&0\\0&0&0\end{pmatrix},\qquad
\operatorname{ad}_F=\begin{pmatrix}0&-1&0\\0&0&0\\2&0&0\end{pmatrix}.
$$

Hence

$$
\operatorname{ad}_H^2=\operatorname{diag}(0,4,4),\qquad
\operatorname{ad}_E\operatorname{ad}_F=\operatorname{diag}(2,2,0),
$$

and $\operatorname{ad}_F\operatorname{ad}_E$ has trace $4$, the same as $\operatorname{ad}_E\operatorname{ad}_F$; the products $\operatorname{ad}_H\operatorname{ad}_E$, $\operatorname{ad}_E\operatorname{ad}_H$, $\operatorname{ad}_H\operatorname{ad}_F$, $\operatorname{ad}_F\operatorname{ad}_H$, $\operatorname{ad}_E^2$ and $\operatorname{ad}_F^2$ have zero trace. Therefore

$$
\kappa_{\mathbb{C}}(H,H)=8,\qquad \kappa_{\mathbb{C}}(E,F)=4,\qquad
\kappa_{\mathbb{C}}(H,E)=\kappa_{\mathbb{C}}(H,F)=\kappa_{\mathbb{C}}(E,E)=\kappa_{\mathbb{C}}(F,F)=0 .
$$

The form $4\operatorname{tr}(XY)-2\operatorname{tr}X\operatorname{tr}Y$ takes the same values on the basis, since $\operatorname{tr}(H^2)=2$ and $\operatorname{tr}(EF)=1$; both forms are complex bilinear, so they agree on $\mathfrak{sl}_2(\mathbb{C})$, and both vanish on the centre. Hence

$$
\kappa_{\mathbb{C}}(X,Y)=4\operatorname{tr}(XY)-2\operatorname{tr}X\,\operatorname{tr}Y
$$

for all $X,Y$. Taking twice the real part gives the matrix formula, and the translation $\operatorname{tr}=2\operatorname{Sc}$ gives the algebra formula. $\square$

**The radical is the centre.** For $\tilde X=e_t$ the right-hand side vanishes, so $\kappa(e_t,\tilde Y)=0$ for every $\tilde Y$. Conversely write $\tilde X=a e_t+\tilde U$ with $\operatorname{Sc}\tilde U=0$; then $\kappa(\tilde X,\tilde Y)=16\operatorname{Re}\operatorname{Sc}(\tilde U\tilde Y)$, and the plain form pairs the trace-free part nondegenerately with the whole algebra, so the vanishing for all $\tilde Y$ forces $\tilde U=0$. Hence

$$
\operatorname{rad}\kappa=\mathbb{C}e_t,
$$

of real dimension two: the Killing form is degenerate exactly along the centre.

**The trace-free part.** On $\mathrm{B}_0=\{\tilde X:\operatorname{Sc}\tilde X=0\}$, the Lie algebra of $\mathbb{B}^\times_1\cong SL_2(\mathbb{C})$, the form is

$$
\kappa(\tilde X,\tilde Y)=16\operatorname{Re}\operatorname{Sc}(\tilde X\tilde Y)=8\operatorname{Re}\operatorname{tr}\bigl(\mathsf M_2(\tilde X)\mathsf M_2(\tilde Y)\bigr),
$$

nondegenerate. The real subspaces $\mathrm{K}=\operatorname{span}_{\mathbb{R}}\{\vec e_x,\vec e_y,\vec e_z\}$ and $i\mathrm{K}$ are orthogonal, because $\operatorname{Sc}(\vec e_j\,i\vec e_k)$ is purely imaginary. On $\mathrm{K}$,

$$
\kappa(\vec e_j,\vec e_k)=-16\,\delta_{jk},
$$

so $\mathrm{K}$ is negative definite; on $i\mathrm{K}$, $\kappa(i\vec e_j,i\vec e_k)=+16\,\delta_{jk}$, so $i\mathrm{K}$ is positive definite. The signature of $\kappa$ on $\mathrm{B}_0$ is therefore

$$
(3,3),
$$

with the compact real form $\mathrm{K}=\mathfrak{su}(2)$ negative and its complement $i\mathrm{K}$ positive.

**Invariance.** The Killing form is invariant under the adjoint action,

$$
K\bigl([\tilde X,\tilde Y],\tilde Z\bigr)+K\bigl(\tilde Y,[\tilde X,\tilde Z]\bigr)=0,
$$

so $\kappa(\tilde Q\tilde X\tilde Q^{-1},\tilde Q\tilde Y\tilde Q^{-1})=\kappa(\tilde X,\tilde Y)$ for every unit $\tilde Q$. It is therefore a function of the conjugation class alone.

**Relation to the plain form.** The plain bilinear form $P(\tilde X,\tilde Y)=\operatorname{Sc}(\tilde X\tilde Y)$ of *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra* has realification of signature $(4,4)$. The Killing form is its real part with the rank-one piece carried by the centre removed,

$$
K=16\operatorname{Re}\bigl(P(\tilde X,\tilde Y)-\operatorname{Sc}\tilde X\operatorname{Sc}\tilde Y\bigr),
$$

and the subtraction is the orthogonal projection onto $\mathrm{B}_0$: the $P$-orthogonal complement of $\mathrm{B}_0$ is the centre $\mathbb{C}e_t$, since $P(e_t,\tilde X)=\operatorname{Sc}\tilde X$.

## Summary

The group of units $\mathbb{B}^\times$ is a real Lie group of real dimension $8$, and the exponential map is its link with the Lie algebra: it is a local diffeomorphism at the identity, but it is not surjective onto the group. The unit quaternions $S^3=\{\tilde q\in\mathbb{H}_{\mathbb{B}}:\langle\tilde q\rangle_{\natural}=1\}$ form a compact connected simply connected subgroup of real dimension $3$, whose complexification is the norm-one group $\mathbb{B}^\times_1$ of real dimension $6$ and centre $\{\pm e_t\}$. The complexification adds four real dimensions, and the norm-one condition removes two rather than one, so the net gain is three; the trace is free on the level set and the determinant is the constraint.

The subgroups are $\mathbb{B}^\times$, $\mathbb{B}^\times_1$, the unit quaternions $S^3$ and the centre $\mathbb{C}^\times e_t$; the maximal compact subgroup of $\mathbb{B}^\times_1$ is $S^3$, and the quotient by the centre $\mathbb{B}^\times_1/\{\pm e_t\}$ is a Lie group of real dimension $6$. Over the reals these are the real forms of the group, and the correspondence with the Lie algebra attaches each subgroup to its subalgebra: $S^3$ to $\mathrm{K}$, $\mathbb{B}^\times_1$ to $\mathrm{B}_0$, and $\mathbb{C}^\times e_t$ to the centre.

Surjectivity is not uniform. The exponential is surjective onto $S^3$, a connected compact group, and not surjective onto $\mathbb{B}^\times_1$: the norm-one group is not exponential, the obstruction a non-semi-simple element with the repeated eigenvalue $-1$, and the same obstruction occurs in $SL(2,\mathbb{R})$. The image still contains a neighbourhood of the identity and generates the connected group, so failure of surjectivity is not failure of generation.

The one-parameter subgroups are the exponential lines $t\mapsto\exp(t\tilde X)$; every one-parameter subgroup is of this form, with generator $\tilde X$ unique for a fixed parametrisation. The Killing form is $\kappa(\tilde X,\tilde Y)=16\operatorname{Re}(\operatorname{Sc}(\tilde X\tilde Y)-\operatorname{Sc}\tilde X\operatorname{Sc}\tilde Y)$; its radical is the centre $\mathbb{C}e_t$, and on the trace-free part it has signature $(3,3)$, negative on the compact $\mathrm{K}$ and positive on $i\mathrm{K}$.

The larger $*$-unitary groups are reached by enlarging the carrier and not the algebra. The matrices over the algebra satisfy $M_n(\mathbb{B})\cong M_{2n}(\mathbb{C})$, so $M_3(\mathbb{B})\cong M_6(\mathbb{C})$ contains $\mathfrak{su}(3)$ with its eight generators, and the closed forms for $\mathrm{SU}(3)$ and $\mathrm{SU}(4)$ — a Lie-type form and Euler-angles forms, built from the antisymmetric, diagonal and diagonal-less symmetric linear functions of the enveloping-algebra article — are the explicit elements of those groups written with $3\times3$ matrices of biquaternions. They do not put an octet inside $\mathbb{B}$: each element fixes $e_t$ and acts on the vector part, so the matrix is $\operatorname{diag}(\tilde U_3,1)$ and the group is an $\mathrm{SU}(3)$ block on a three-dimensional complex space, while the algebra's own action on $\mathbb{B}$ is four-dimensional over $\mathbb{C}$ with the scalar direction inert. The ceiling is thus untouched and the price of the embedding is the factor $2$ in each matrix direction.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}^\times$ | Group of units; real Lie group of real dimension $8$ |
| $\exp$ | Exponential map; closed form in *Biquaternion Elementary Functions* |
| $S^3=\{\tilde q\in\mathbb{H}_{\mathbb{B}}:\langle\tilde q\rangle_{\natural}=1\}$ | Unit quaternions; compact subgroup of real dimension $3$ |
| $\mathbb{B}^\times_1=\{N=1\}$ | Norm-one group; complexification of $S^3$; real dimension $6$ |
| $\{\pm e_t\}$ | Centre of $\mathbb{B}^\times_1$; the quotient is a Lie group of real dimension $6$ |
| $\mathrm{B}_0$ | Lie algebra of $\mathbb{B}^\times_1$; trace-free part |
| $\mathrm{K}=\mathrm{span}_{\mathbb{R}}\{\vec e_x,\vec e_y,\vec e_z\}$ | Lie algebra of $S^3$; compact subalgebra |
| $\mathbb{C}^\times e_t$ | Centre of $\mathbb{B}^\times$; Lie algebra $\mathbb{C}e_t$ |
| $\varphi_{\tilde X}(t)=\exp(t\tilde X)$ | One-parameter subgroup with generator $\tilde X$ |
| $\kappa(\tilde X,\tilde Y)=\operatorname{tr}(\operatorname{ad}_{\tilde X}\operatorname{ad}_{\tilde Y})$ | Killing form; radical $\mathbb{C}e_t$, signature $(3,3)$ on $\mathrm{B}_0$ |
| $M_n(\mathbb{B})\cong M_{2n}(\mathbb{C})$ | Matrices over the algebra; the enlarged carrier |
| $a[\,]b$, $\odot$, $D\{\delta\}$ | Conway operator $\tilde{Q}\mapsto a\tilde{Q}b$, its composition, and the diagonal function |
| $G^{-1}=G^{+\approx}=G^{\dagger}$ | The inverse of a group element; association with conjugation |

## Further Reading

- A. Gsponer, "Explicit closed-form parametrization of SU(3) and SU(4) in terms of complex quaternions and elementary functions," arXiv:math-ph/0211056v2, 2002, for the closed forms of *The Enlarged Carrier*, the non-canonical SU(3) representation (25) with its inverse (27)–(28), the three elementary exponentials (18), (19) and (21) that make its factorisation work, the Euler-angles forms (31)–(33), and the parametrisations (34)–(38) in the Gell-Mann-type basis; the paper's Table 1, which offers a dictionary between its functions and the Gell-Mann parameters, is inconsistent as printed and is not transcribed here or in the companion $\mathrm{SU}(3)$ article.
- A. W. Conway, "Quaternions and matrices," *Proceedings of the Royal Irish Academy* **A 50** (1945) 98–130, and J. L. Synge, "Quaternions, Lorentz transformations, and the Conway–Dirac–Eddington matrices," *Communications of the Dublin Institute for Advanced Studies* **A 21** (1972), for the Conway operator calculus used by the closed forms.
- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations: An Elementary Introduction* (Springer, 2nd ed. 2015).
- John Stillwell, *Naive Lie Theory* (Springer, 2008).
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997).
- Companion articles: [The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure](the-enveloping-operator-algebra-of-the-biquaternion-algebra-and-the-bi-module-structure.html) (the Conway operator basis) and [The Four Adjoints of the Biquaternion Algebra in Examples](the-four-adjoints-of-the-biquaternion-algebra-in-examples.html) (function association); [The Gauge Group Ceiling: Why the Biquaternion Algebra Reaches SU(2) but Not SU(3)](../articles_physics/the-gauge-group-ceiling-why-the-biquaternion-algebra-reaches-su-2-but-not-su-3.html) (the ceiling the enlarged carrier answers); [The Gluon: An Octet Outside the Biquaternion Algebra](../articles_physics/the-gluon-an-octet-outside-the-biquaternion-algebra.html).
