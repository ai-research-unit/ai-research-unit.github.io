
# __Convolution on a Group__

## Introduction

Convolution is the multiplication of the group transferred to functions by integration, and read between function spaces rather than inside one it is the family of operators by which the group and its algebra act. This article develops convolution from the operator side: the left and the right convolution operators, their boundedness and their exact norms on $L^1(G)$, the approximate identities read as nets of operators converging strongly to the identity, and the Fourier transform read as an algebra homomorphism — scalar in the abelian case, operator-valued in the general one.

The article assumes the locally compact group, its Haar measure and the modular function from *Locally Compact Groups and Haar Measure*; the convolution product, the involution and the structure of the Banach $*$-algebra $L^1(G)$ from *The Convolution Algebra $L^1(G)$*; the characters, Pontryagin duality and the abelian transform from *Harmonic Analysis on Groups*; the unitary dual, the operator-valued transform and the decomposition theory from *Noncommutative Harmonic Analysis* and *The Plancherel Theorem*; and the bounded operators, the operator norm and the strong topology from *Operator Algebras*. The left and the right regular representations are *The Left and Right Regular Representation*, and the reading of $L^1(G)$ as an algebra of operators is *The Group Algebra as an Algebra of Operators*, both immediately following; the adjoint of a convolution operator belongs to the `- * Operator Theory` group of this category, and convolution by a bounded measure, with the algebra of measures, is *The Involution on the Measure Algebra*, later in this category. The Fourier transform as an operator on $L^2(G)$ is *The Fourier Operator*, written in parallel in this Part. No adjoint is used.

Throughout, $G$ is a locally compact Hausdorff group with identity $e$ and left Haar measure $dx$, $\Delta$ is the modular function and $G$ is **unimodular** when $\Delta \equiv 1$; $L^1(G)$ carries the convolution

$$
(f*g)(x) = \int_G f(y)\,g(y^{-1}x)\,dy ,
$$

the $L^1$ norm $\|f\|_1 = \int_G |f(x)|\,dx$, and the involution $f^*(x) = \overline{f(x^{-1})}\,\Delta(x)^{-1}$; $\operatorname{Irr}(G)$ is the unitary dual and $\mu_P$ the Plancherel measure. The letter $k$ is a base field real or complex when only its linear structure is used.

## Convolution as a Product and as a Bilinear Map

**Definition.** For $f, g \in L^1(G)$ the **convolution** $f*g \in L^1(G)$ is defined by the integral above; the operation is the product of the group algebra $\mathcal{A} = L^1(G)$.

**Proposition (the algebra laws).** Convolution is bilinear, associative and submultiplicative,

$$
(f*g)*h = f*(g*h), \qquad \|f*g\|_1 \leq \|f\|_1\,\|g\|_1 ,
$$

and it is commutative exactly when $G$ is abelian. The algebra $\mathcal{A}$ is unital exactly when $G$ is discrete, the unit being the point mass $\delta_e$; in general $\mathcal{A}$ has no identity.

**Proof.** Associativity is Fubini together with the associativity of the group product and the left invariance of $dx$; submultiplicativity is Fubini and $\|f\|_1\|g\|_1$; commutativity is the identity $f*g = g*f$ read through the substitution $x \mapsto x^{-1}$ and fails as soon as two elements do not commute; a unit $u$ would satisfy $u*f = f$ for all $f \in L^1(G)$, forcing $u$ to be the point mass at $e$, which is integrable exactly when $G$ is discrete. The full development is *The Convolution Algebra $L^1(G)$*; the article reads the same product as an operation between functions.

**Remark (the operator reading).** The associativity displayed above is what makes the left and the right multiplications by a fixed element into operators, and the submultiplicativity is what makes them bounded; the two readings are taken in the next section.

## The Convolution Operators

**Definition.** For $f \in L^1(G)$ the **left** and the **right convolution operators** on $L^1(G)$ are

$$
L_f : L^1(G) \to L^1(G), \quad L_f(h) = f*h ; \qquad R_f : L^1(G) \to L^1(G), \quad R_f(h) = h*f .
$$

Equivalently $L_f = \lambda(f)$ and $R_f = \rho(f)$ are the integrated left and right regular representations, obtained from the translations $\lambda(x)h = \delta_x*h$ and $\rho(x)h = h*\delta_x$ when the group elements are integrable.

**Theorem (boundedness and the composition laws).** For all $f, g \in L^1(G)$ the operators $L_f, R_f$ are bounded with

$$
\|L_f\| \leq \|f\|_1 , \qquad \|R_f\| \leq \|f\|_1 ,
$$

and they satisfy

$$
L_f L_g = L_{f*g}, \qquad R_f R_g = R_{g*f}, \qquad L_f R_g = R_g L_f .
$$

Thus $f \mapsto L_f$ is an algebra homomorphism, $f \mapsto R_f$ an algebra anti-homomorphism, and every left convolution commutes with every right convolution.

**Proof.** The bound is submultiplicativity, $\|L_f h\|_1 = \|f*h\|_1 \leq \|f\|_1\|h\|_1$. The first two composition laws are associativity read on the two sides; the third is the associativity $(f*h)*g = f*(h*g)$, which says $L_fR_g = R_gL_f$. An anti-homomorphism reverses the order of the product, which is exactly $R_fR_g = R_{g*f}$. $\square$

**Theorem (the norm is attained).** The left regular representation is isometric,

$$
\|L_f\| = \|f\|_1 , \qquad \|R_f\| = \|f\|_1 ,
$$

so $\mathcal{C}_L = \{L_f : f \in L^1(G)\}$ and $\mathcal{C}_R = \{R_f : f \in L^1(G)\}$ are closed subalgebras of $B(L^1(G))$ isometrically isomorphic to $L^1(G)$ and to its opposite algebra.

**Proof.** The upper bound is the theorem above. For the lower bound let $\{u_i\}$ be a contractive approximate identity as in the next section, so that $\|u_i\|_1 = 1$ and $f*u_i \to f$ in $L^1(G)$. Then $\|f\|_1 = \lim_i \|f*u_i\|_1 = \lim_i\|L_fu_i\|_1 \leq \|L_f\|$. The same argument with $u_i*f$ gives the statement for $R_f$. The map $f\mapsto L_f$ is an injective homomorphism (for $L_f = 0$ gives $f*u_i\to0$ and $f = 0$) that is isometric, hence isometric onto its image, which is complete hence closed. $\square$

**Proposition (commutation with the translations).** For all $f \in L^1(G)$ and all $x \in G$,

$$
L_f\,\rho(x) = \rho(x)\,L_f , \qquad R_f\,\lambda(x) = \lambda(x)\,R_f ,
$$

where $\lambda(x)h = \delta_x*h$ and $\rho(x)h = h*\delta_x$; that is, a left convolution commutes with the right translations and a right convolution commutes with the left translations.

**Proof.** $L_f\rho(x)h = f*(h*\delta_x) = (f*h)*\delta_x = \rho(x)L_fh$, and the second identity is the mirror image. $\square$

**Remark (the two families and the commutant).** The two families commute with each other by the composition law, and each commutes with the translations on the opposite side; the identification of the full commutant of the translations as the convolution operators of bounded measures is *The Involution on the Measure Algebra*, later in this category, where the measure algebra is available. On $L^1(G)$ the operators $L_f$ and $R_f$ alone do not exhaust the commutant in general.

## Approximate Identities

**Definition.** A **bounded approximate identity** of $L^1(G)$ is a net $\{u_i\}$ in $L^1(G)$ with $\sup_i\|u_i\|_1 < \infty$ and

$$
u_i*f \to f, \qquad f*u_i \to f \qquad (f \in L^1(G)),
$$

the convergence being in the norm of $L^1(G)$. It is **contractive** when $\|u_i\|_1 = 1$ for all $i$.

**Theorem (existence and operator form).** Every locally compact group carries a contractive approximate identity. One is obtained by fixing nonnegative $u_i \in L^1(G)$ with $\int_G u_i(x)\,dx = 1$ and supports shrinking to $\{e\}$; for it

$$
\|L_{u_i} - \mathrm{id}\| \to 0 \ \text{strongly}, \qquad \|R_{u_i} - \mathrm{id}\| \to 0 \ \text{strongly},
$$

that is $L_{u_i} \to \mathrm{id}$ and $R_{u_i} \to \mathrm{id}$ in the strong operator topology of $B(L^1(G))$, while $\|L_{u_i}\| = \|R_{u_i}\| = 1$ for every $i$. Hence the strong limit of the operators $L_{u_i}$ is the identity although $\mathcal{A}$ has no identity element unless $G$ is discrete.

**Proof.** For $f \in C_c(G)$ the continuity of translation gives $\|u_i*f - f\|_1 \to 0$ and $\|f*u_i - f\|_1 \to 0$, and $C_c(G)$ is dense in $L^1(G)$; the isometry $\|L_{u_i}\| = \|u_i\|_1 = 1$ is the theorem of the previous section. The strong convergence is the definition of the approximate identity, and the last sentence records that a strong limit of isometries need not be attained. $\square$

**Corollary (the identity in the discrete case).** If $G$ is discrete the net may be taken constant, $u_i = \delta_e$, and $L_{\delta_e} = R_{\delta_e} = \mathrm{id}$; the strong convergence is attained and $\mathcal{A} = \ell^1(G)$ is unital.

**Proof.** $\delta_e$ is the unit of $\ell^1(G)$ by the proposition on the algebra laws, and $L_{\delta_e} = \mathrm{id}$ by definition. $\square$

## The Fourier Transform

**Definition.** For a character $\chi$ of a locally compact abelian group $G$ the **Gelfand transform** is

$$
\hat f(\chi) = \int_G f(x)\,\chi(x)\,dx \qquad (f \in L^1(G)),
$$

and for a general locally compact group the **operator-valued transform** is

$$
\hat f(\pi) = \int_G f(x)\,\pi(x)\,dx \in B(\mathcal{H}_\pi) \qquad (\pi \in \operatorname{Irr}(G)).
$$

**Theorem (the convolution theorem).** The two transforms are algebra homomorphisms: for $f, g \in L^1(G)$,

$$
\widehat{f*g}(\chi) = \hat f(\chi)\,\hat g(\chi), \qquad \widehat{f*g}(\pi) = \hat f(\pi)\,\hat g(\pi),
$$

the first for abelian $G$, the second in general; both are continuous, with $|\hat f(\chi)| \leq \|f\|_1$ in the abelian case and $\|\hat f(\pi)\| \leq \|f\|_1$ in general.

**Proof.** The abelian identity is Fubini and the multiplicativity of $\chi$: $\widehat{f*g}(\chi) = \iint f(y)g(y^{-1}x)\chi(x)\,dy\,dx = \int f(y)\chi(y)\,dy\int g(z)\chi(z)\,dz$. The general identity is the same computation with the operator product in place of the scalar product, the integrals converging in the operator norm. Continuity is the triangle inequality for the vector-valued integral. $\square$

**Proposition (the transform diagonalises convolution).** On a unimodular group of type I the Plancherel transform $\mathcal{F} : L^2(G) \to \int^\oplus (\mathcal{H}_\pi\otimes\mathcal{H}_\pi^*)\,d\mu_P(\pi)$ intertwines left convolution with the field of its transforms,

$$
\mathcal{F}\,L_f\,\mathcal{F}^{-1} = \int^\oplus \hat f(\pi)\,d\mu_P(\pi) ,
$$

the field acting by multiplication on the fibre $\mathcal{H}_\pi\otimes\mathcal{H}_\pi^*$; in the abelian case this is the statement that $L_f$ on $L^2(G)$ is unitarily equivalent to multiplication by the bounded continuous function $\hat f$ on $G^\vee$.

**Proof.** The convolution theorem gives $\widehat{f*h}(\pi) = \hat f(\pi)\hat h(\pi)$, and the Plancherel transform carries $h$ to the field $\hat h(\pi)$; hence it carries $L_fh$ to $\hat f(\pi)\hat h(\pi)$. The abelian case is the specialisation $\mathcal{H}_\pi = \mathbb{C}$ and $\mathcal{H}_\pi\otimes\mathcal{H}_\pi^* = \mathbb{C}$, where the field is multiplication by $\hat f(\chi)$. $\square$

**Remark (norm realised on the spectrum).** The transform of the previous proposition realises the operator norm of $L_f$ on $L^2(G)$ as an essential supremum in the abelian case, $\|L_f\|_{B(L^2)} = \|\hat f\|_\infty$, and in general as the essential supremum of $\pi \mapsto \|\hat f(\pi)\|$ against $\mu_P$; the $L^1$ norm of the theorem on $L_f$ is the norm of the same operator on $L^1(G)$, and the two need not agree. The $L^2$ norms belong to *The Plancherel Operator* and *Noncommutative Harmonic Analysis*.

## The Algebra of Convolution Operators

**Theorem (the convolution operators form the group algebra).** The assignment $f \mapsto L_f$ is an isometric algebra isomorphism of $L^1(G)$ onto the closed subalgebra $\mathcal{C}_L \subseteq B(L^1(G))$; the algebra $\mathcal{C}_L$ is commutative exactly when $G$ is abelian, unital exactly when $G$ is discrete, and its strong closure contains the identity of $B(L^1(G))$ while containing no identity of itself when $G$ is non-discrete.

**Proof.** The map is an isometric homomorphism by the theorems above; the algebra properties are transferred from $\mathcal{A}$ along it; the strong closure contains the strong limit of the approximate identity, which is the identity operator, and the last statement is that of the section on approximate identities. $\square$

**Proposition (the action on $L^p$).** For $1 \leq p \leq \infty$ and $f \in L^1(G)$ the formula $L_fh = f*h$ defines a bounded operator on $L^p(G)$ with

$$
\|L_f\|_{B(L^p)} \leq \|f\|_1 ,
$$

and on $L^\infty(G)$ the operator is weak-$*$ continuous; the left convolution operators on the several $L^p$ are the several integrated regular representations of the same element.

**Proof.** Young's inequality $\|f*h\|_p \leq \|f\|_1\|h\|_p$ is Minkowski's integral inequality, and the weak-$*$ continuity is duality with the $L^q$ action for $q$ conjugate to $p$, $1 < p < \infty$; the endpoint cases are the usual ones. The identification with the integrated regular representation is the definition. $\square$

**Remark (what the article does not do).** The article has used no involution and no adjoint: the anti-linear structure of $L^1(G)$ and the adjoint of $L_f$ on $L^2(G)$ are the `- * Theory` and `- * Operator Theory` groups of this category, and the group $C^*$-algebras $C^*(G)$ and $C^*_r(G)$, together with the von Neumann algebra $L(G)$, are treated where their operator-algebraic foundations are available. The measure algebra and convolution by a bounded measure, which complete the commutant of the translations, are *The Involution on the Measure Algebra*, later in this category.

## Summary

Convolution turns a locally compact group into the Banach algebra $L^1(G)$, the product $(f*g)(x) = \int_G f(y)g(y^{-1}x)dy$ being associative, submultiplicative and commutative exactly for abelian $G$, unital exactly for discrete $G$. Read as operators, the left and right multiplications $L_f h = f*h$ and $R_f h = h*f$ are the integrated regular representations, bounded on $L^1(G)$ with $\|L_f\| = \|R_f\| = \|f\|_1$, satisfying $L_fL_g = L_{f*g}$, $R_fR_g = R_{g*f}$ and $L_fR_g = R_gL_f$, and each commuting with the translations on the opposite side. A contractive approximate identity $\{u_i\}$ inside $L^1(G)$ is exactly a net with $L_{u_i} \to \mathrm{id}$ and $R_{u_i} \to \mathrm{id}$ in the strong operator topology, its strong limit being the identity although the algebra has no identity unless $G$ is discrete. The Gelfand transform $\hat f(\chi) = \int f\chi$ and the operator-valued transform $\hat f(\pi) = \int f\pi$ are algebra homomorphisms, continuous with bound $\|f\|_1$, and they diagonalise convolution: $\mathcal{F}L_f\mathcal{F}^{-1}$ is the field of operators $\hat f(\pi)$ on the Plancherel direct integral, multiplication by $\hat f$ in the abelian case. The left convolution operators form a closed subalgebra of $B(L^1(G))$ isometrically isomorphic to $L^1(G)$, and the same formula gives bounded convolution operators on every $L^p(G)$ with $\|L_f\|_{B(L^p)} \leq \|f\|_1$. No involution, adjoint, group $C^*$-algebra or measure algebra is used; these belong to the `- *` groups of the category and to *The Involution on the Measure Algebra*, later.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $G$, $e$, $dx$, $\Delta$ | Locally compact group, identity, left Haar measure, modular function |
| $\mathcal{A} = L^1(G)$ | The group algebra, $f*g$ the convolution |
| $\|f\|_1 = \int_G\lvert f(x)\rvert\,dx$ | The $L^1$ norm of the algebra |
| $f^*(x) = \overline{f(x^{-1})}\Delta(x)^{-1}$ | The involution, cited from the algebra article |
| $L_f$, $R_f$ | Left and right convolution operators, $L_fh = f*h$, $R_fh = h*f$ |
| $\|L_f\| = \|R_f\| = \|f\|_1$ | Exact operator norms on $L^1(G)$ |
| $L_fL_g = L_{f*g}$, $R_fR_g = R_{g*f}$, $L_fR_g = R_gL_f$ | Composition laws |
| $\lambda(x)$, $\rho(x)$ | Left and right translations, $h\mapsto\delta_x*h$, $h\mapsto h*\delta_x$ |
| $\{u_i\}$ | Contractive approximate identity, $\|u_i\|_1 = 1$ |
| $\hat f(\chi)$, $\hat f(\pi)$ | Gelfand transform; operator-valued transform |
| $\widehat{f*g} = \hat f\hat g$ | Convolution theorem |
| $\mathcal{C}_L$, $\mathcal{C}_R$ | Closed subalgebras of $B(L^1(G))$ isomorphic to $L^1(G)$ and its opposite |
| $\operatorname{Irr}(G)$, $\mu_P$, $\mathcal{H}_\pi$ | Unitary dual, Plancherel measure, representation space |

## Further Reading

- Edwin Hewitt and Kenneth A. Ross, *Abstract Harmonic Analysis I* (Springer, second edition, 1979), for the convolution algebra $L^1(G)$, its approximate identities and the algebra of measures.
- Lynn H. Loomis, *An Introduction to Abstract Harmonic Analysis* (Van Nostrand, 1953), for the convolution operators and the classical convolution theorem.
- Walter Rudin, *Fourier Analysis on Groups* (Wiley, 1962), for the Gelfand transform of $L^1(G)$ on an abelian group and the norm realised on the dual.
- Gerald B. Folland, *A Course in Abstract Harmonic Analysis* (CRC Press, second edition, 2015), for the operator-valued transform, the convolution theorem and the Plancherel transform.
- John B. Conway, *A Course in Functional Analysis* (Springer, second edition, 1990), for the strong operator topology, isometric representations and the bounded operators on $L^p$.
