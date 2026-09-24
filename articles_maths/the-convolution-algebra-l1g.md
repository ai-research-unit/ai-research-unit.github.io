
# __The Convolution Algebra $L^1(G)$__

## Introduction

Convolution turns the integrable functions on a locally compact group into a Banach algebra, and this algebra is the correct algebraic home of harmonic analysis. On the abelian side it is the algebra whose Gelfand transform is the Fourier transform; on the non-abelian side it is a non-commutative Banach $*$-algebra whose nondegenerate representations are exactly the continuous unitary representations of the group, so that representation theory and the spectral theory of an algebra become the same subject. The present article develops the algebra $L^1(G)$: the convolution product and its inequalities, the involution carried by the modular function, approximate identities, the passage to the group $\mathrm{C}^*$-algebras and the group von Neumann algebra, and the abelian Gelfand picture as the commutative case.

The article also fixes the general (not necessarily unimodular) conventions of the harmonic-analysis block: the modular function in the involution, the two conventions for convolution on a non-unimodular group, and the relation between the left and right Haar measures. The other articles of this category use these without restatement.

The boundaries of the block. The **Haar measure**, its invariance and the modular function $\Delta$ are *Locally Compact Groups and Haar Measure*; in particular the convention $\mu(Ag) = \Delta(g)\mu(A)$, the right Haar measure $d\mu_R = \Delta^{-1}d\mu_L$, the inversion identity $\int f(x^{-1})dx = \int f(x)\Delta(x)^{-1}dx$, and the affine group with $\Delta(a,b) = a^{-1}$ are all established there and are used here. The **general integration theory**, the $L^p$ spaces, Hölder, Minkowski and Fubini, is *Measure Theory and Integration* and *Modes of Convergence*, and the **Banach- and Hilbert-space theory** — Banach algebras, spectra, the Gelfand transform, $*$-representations, the GNS construction — is standard and is quoted as it is used, with the operator-algebraic development belonging to *Operator Algebras* and the space theory to the later. The **representation theory** of the group is Part II's (*Representation Theory of Locally Compact Groups*, *Induced Representations of Locally Compact Groups*, *Mackey Theory*, *Type I Groups*), and the **abelian transform theory** is *Harmonic Analysis on Groups*; the non-abelian spectral theory isandand the operator-algebraic completions are *Operator Algebras* in the Topology on Linear Algebras slot of Part II. No physics is invoked.

Throughout, $G$ is a locally compact Hausdorff group with left Haar measure $dx = d\mu_L(x)$, modular function $\Delta$, and identity $e$; $G$ is **unimodular** when $\Delta \equiv 1$. The convolution is

$$
(f*g)(x) = \int_G f(y)\,g(y^{-1}x)\,dy ,
$$

with respect to the **left** Haar measure, and the involution is

$$
f^*(x) = \overline{f(x^{-1})}\,\Delta(x)^{-1} .
$$

The $\mathrm{C}^*$-completions are $C^*(G)$ (full) and $C^*_r(G)$ (reduced), and the group von Neumann algebra is $L(G) = \lambda(G)''$. As in *Harmonic Analysis on Groups*, the abelian dual is $G^\vee$ and the unitary dual of a general group is $\operatorname{Irr}(G)$; no use is made of the notation $\widehat{G}$.

## The Modular Function and the Spaces $L^p(G)$

### The Modular Function

Recall from *Locally Compact Groups and Haar Measure*, §The Modular Function and Unimodularity: $\Delta : G \to \mathbb{R}_{>0}$ is the continuous homomorphism defined by

$$
\mu(Ag) = \Delta(g)\,\mu(A),
$$

equivalently $d(xg) = \Delta(g)^{-1}dx$ and $\int_G f(xg)\,dx = \Delta(g)^{-1}\int_G f(x)\,dx$; the right Haar measure is $d\mu_R = \Delta^{-1}d\mu_L$, with $\mu_R(A) = \mu_L(A^{-1})$; and the inversion identity

$$
\int_G f(x^{-1})\,dx = \int_G f(x)\,\Delta(x)^{-1}\,dx
$$

holds for every $f \in L^1(G)$. The affine group $G = \{(a,b) : a > 0\}$ with $(a,b)(a',b') = (aa', ab'+b)$ has $\mu_L = a^{-2}da\,db$, $\mu_R = a^{-1}da\,db$ and $\Delta(a,b) = a^{-1}$, and is the standard non-unimodular example; the groups that are abelian, compact, discrete, nilpotent, perfect or semisimple are unimodular.

**Example (the modular function of a product).** If $G = G_1 \times G_2$ then $\Delta_G(g_1,g_2) = \Delta_{G_1}(g_1)\Delta_{G_2}(g_2)$ and $G$ is unimodular iff both factors are. The product inherits no new phenomenon; the failure of unimodularity is an obstruction of solvable groups such as the affine group.

### The Spaces $L^p(G)$

For $1 \leq p \leq \infty$ the space $L^p(G)$ is taken with respect to $dx$; since $dx$ is a Radon measure, $C_c(G)$ is dense in $L^p(G)$ for $p < \infty$, and for $1 \leq p < \infty$ the dual of $L^p(G)$ is $L^q(G)$ with $q$ conjugate to $p$. Hölder's inequality reads $\|fg\|_1 \leq \|f\|_p\|g\|_q$ and Minkowski's $\|f+g\|_p \leq \|f\|_p+\|g\|_p$.

**Theorem (continuity of translation).** For $1 \leq p < \infty$ and $f \in L^p(G)$, the maps $x \mapsto L_x f$ and $x \mapsto R_x f$ of $G$ into $L^p(G)$ are continuous, where $(L_xf)(y) = f(x^{-1}y)$ and $(R_xf)(y) = f(yx)$. Both are continuous unitary representations of $G$ on $L^2(G)$, the left and right regular representations.

**Proof.** For $f \in C_c(G)$ the statements are uniform continuity of a compactly supported continuous function together with the compactness of its support; for general $f$ they follow by density of $C_c(G)$ in $L^p(G)$ and the isometry $\|L_xf\|_p = \|f\|_p$, $\|R_xf\|_p = \|f\|_p\Delta(x)^{-1/p}$ for the right translation. Unitarity of $L$ on $L^2(G)$ is the left invariance of $dx$, and unitarity of $R$ follows from the right invariance of $d\mu_R = \Delta^{-1}dx$, equivalently from the computation $\|R_x f\|_2^2 = \int|f(yx)|^2dy = \Delta(x)^{-1}\|f\|_2^2$ compensated by the weight in the inner product of the right regular representation; on a unimodular group both are directly unitary. $\square$

**Remark (the two regular representations).** The left regular representation $\lambda = L$ and the right regular representation $\rho = R$ commute, and on $L^2(G)$ they generate the regular representation of $G \times G$; this is the operator-algebraic frame of the Plancherel theory.

## The Convolution Product

### Definition and the $L^1$ Bound

**Definition.** For measurable $f, g$ on $G$ the **convolution** is $f*g$ defined by

$$
(f*g)(x) = \int_G f(y)\,g(y^{-1}x)\,dy
$$

whenever the integral exists for almost every $x$.

With the left Haar measure, this is the standard choice: for abelian $G$ it reduces to $f*g(x) = \int f(y)g(x-y)dy$, and the substitution $y \mapsto x-y$ gives $f*g = g*f$. On a non-unimodular group the analogous right convolution, built from $g(xy^{-1})$, differs from $f*g$ by a modular factor in the variable of integration; the choice between the two conventions is dictated by the requirement that the convolution theorem hold with the operator product in the order $\hat f\hat g$, and the convention above is the one held throughout this corpus.

**Proposition ($L^1$ bound and Young's inequality).** Let $f \in L^p(G)$ and $g \in L^q(G)$ with $1 \leq p, q, r \leq \infty$ and $1/p + 1/q = 1 + 1/r$. Then $f*g$ is defined almost everywhere, belongs to $L^r(G)$, and

$$
\|f*g\|_r \leq \|f\|_p\,\|g\|_q .
$$

In particular, taking $p = q = r = 1$, $L^1(G)$ is closed under convolution and $\|f*g\|_1 \leq \|f\|_1\|g\|_1$. The inequality holds for all locally compact $G$ when $p = q = r = 1$, and for unimodular $G$ in general.

**Proof.** The case $p = q = r = 1$: Tonelli's theorem and the left invariance of $dy$ give

$$
\|f*g\|_1 \leq \int_G\int_G |f(y)||g(y^{-1}x)|\,dy\,dx = \int_G|f(y)|\Bigl(\int_G|g(y^{-1}x)|\,dx\Bigr)dy = \|f\|_1\|g\|_1 .
$$

The general case is the Riesz–Thorin interpolation of the three elementary cases $(p,q,r) = (1,1,1)$, $(1,\infty,\infty)$ and $(\infty,\infty,\infty)$ with a change of variables; on a unimodular group the middle estimate is $\|f*g\|_\infty \leq \|f\|_1\|g\|_\infty$, which is immediate, and the interpolation is the standard Young inequality. The details are in the references. $\square$

### Associativity, Involution and the Banach Algebra Structure

**Theorem.** The convolution on $L^1(G)$ is associative, bilinear and satisfies the norm inequality; the map $(f,g) \mapsto f*g$ is continuous and $L^1(G)$ is a Banach algebra with $\|f*g\|_1 \leq \|f\|_1\|g\|_1$. It has no identity when $G$ is not discrete and has an identity only in the discrete case, where the identity is $\delta_e$.

**Proof.** Associativity is Fubini's theorem applied to the triple integral defining $(f*g)*h$ and $f*(g*h)$ and the change of variable that moves the compositional structure to the middle variable; the argument is the same as in the compact case of *Analysis on Compact Groups*, §Convolution and the Banach Algebra $L^1(K)$. If $u$ is a two-sided identity then $u*f = f$ for $f \in C_c(G)$; testing at points and using approximate identity arguments forces $u$ to be the point mass $\delta_e$, which is in $L^1(G)$ only when $G$ is discrete. $\square$

**Theorem (adjoint of a convolution).** For $f, g \in L^1(G)$ the adjoints of the operators of convolution are

$$
(f*g)^*(x) = (g^* * f^*)(x), \qquad (f^*)^* = f ,
$$

and the involution $f \mapsto f^*$ is an isometric anti-automorphism of the Banach algebra $L^1(G)$: $(f*g)^* = g^* * f^*$, $(\lambda f + \mu g)^* = \bar\lambda f^* + \bar\mu g^*$ and $\|f^*\|_1 = \|f\|_1$.

**Proof.** The adjoint-producing involution is isometric: by the inversion identity applied with $g(x) = |f(x^{-1})|$,

$$
\|f^*\|_1 = \int_G |f(x^{-1})|\,\Delta(x)^{-1}\,dx = \int_G |f(x)|\,dx = \|f\|_1 ,
$$

and $f^{**} = f$ follows from the multiplicativity of $\Delta$ and $\Delta(x)^{-1}\Delta(x^{-1})^{-1} = 1$. For the anti-automorphism identity, substitute $y = x^{-1}z$ in the defining integral; the substitution is a left translation, so $dy = dz$, and $(x^{-1}z)^{-1}x^{-1} = z^{-1}$, whence

$$
(f*g)^*(x) = \Delta(x)^{-1}\int_G \overline{f(x^{-1}z)}\,\overline{g(z^{-1})}\,dz .
$$

On the other hand, using $\Delta(z^{-1}x)^{-1} = \Delta(z)\Delta(x)^{-1}$,

$$
(g^* * f^*)(x) = \int_G \Delta(z)^{-1}\overline{g(z^{-1})}\,\Delta(z^{-1}x)^{-1}\overline{f(x^{-1}z)}\,dz = \Delta(x)^{-1}\int_G \overline{f(x^{-1}z)}\,\overline{g(z^{-1})}\,dz ,
$$

the two modular factors cancelling to $\Delta(x)^{-1}$. The two expressions agree, which is the identity. The computation is standard and is in the references. $\square$

**Remark (why the modular function cannot be avoided).** On a non-unimodular group the naive involution $f \mapsto \overline{f(x^{-1})}$ fails to be isometric: on the affine group it changes the norm by the factor $\Delta$, since $\int|f(x^{-1})|dx = \int|f(x)|\Delta(x)^{-1}dx$ by the inversion identity. The factor $\Delta(x)^{-1}$ in $f^*$ is exactly what restores the $L^1$ norm, and it is the reason the convolution algebra of a non-unimodular group is a Banach $*$-algebra rather than a symmetric one in the naive sense. For abelian and compact groups $\Delta \equiv 1$ and the formula reduces to the familiar ones of *Harmonic Analysis on Groups* and *Analysis on Compact Groups*.

**Corollary (the Banach $*$-algebra).** $L^1(G)$ is a Banach $*$-algebra with isometric involution, and it is commutative if and only if $G$ is abelian; it is unital if and only if $G$ is discrete.

## Approximate Identities and Amenability

### Existence of a Bounded Approximate Identity

**Definition.** A **left (two-sided) approximate identity** for a Banach algebra $A$ is a net $(u_\alpha) \subseteq A$ with $\|u_\alpha f - f\| \to 0$ (respectively $\|u_\alpha f - f\| \to 0$ and $\|f u_\alpha - f\| \to 0$) for every $f \in A$. It is **bounded** with bound $M$ if $\|u_\alpha\| \leq M$ for all $\alpha$.

**Theorem.** For every locally compact group $G$, $L^1(G)$ has a two-sided approximate identity $(u_\alpha)$ with $u_\alpha \geq 0$, $\int_G u_\alpha = 1$ and $\|u_\alpha\|_1 = 1$. It can be chosen to consist of continuous compactly supported functions supported in any prescribed base of neighbourhoods of $e$.

**Proof.** Let $(U_\alpha)$ be a base of neighbourhoods of $e$ and choose $u_\alpha \in C_c(G)$ with $u_\alpha \geq 0$, $\operatorname{supp} u_\alpha \subseteq U_\alpha$ and $\int u_\alpha = 1$. Then

$$
(u_\alpha * f)(x) - f(x) = \int_{U_\alpha} u_\alpha(y)\bigl(f(y^{-1}x) - f(x)\bigr)\,dy
$$

so $\|u_\alpha * f - f\|_1 \leq \int_{U_\alpha}u_\alpha(y)\|L_yf - f\|_1\,dy \leq \sup_{y \in U_\alpha}\|L_yf - f\|_1$, which tends to $0$ by the continuity of translation. The right-handed statement follows by writing $f * u_\alpha = (u_\alpha^* * f^*)^*$ with $u_\alpha^*$ supported in $U_\alpha^{-1}$, or by the same argument with the right regular representation; taking symmetric neighbourhoods and symmetric $u_\alpha$ handles both at once. The bound $\|u_\alpha\|_1 = 1$ is the normalisation. $\square$

### Reiter's Property and Amenability

**Definition (Reiter's property $P_1$).** A locally compact group $G$ has **Reiter's property $P_1$** if there is a net $(u_\alpha) \subseteq L^1(G)$ with $u_\alpha \geq 0$, $\int_G u_\alpha = 1$ and

$$
\|L_g u_\alpha - u_\alpha\|_1 \longrightarrow 0
$$

uniformly for $g$ in compact subsets of $G$, where $L_g u_\alpha(x) = u_\alpha(g^{-1}x)$.

**Theorem (Reiter).** A locally compact group $G$ is amenable if and only if it has property $P_1$; equivalently, if and only if $L^1(G)$ has an approximate identity that is approximately invariant under left translation.

**Proof sketch.** Amenability is the existence of an invariant mean on $L^\infty(G)$, the existence of Følner sets for the discrete case and the equivalent formulations of *Amenable Groups*, which states the group-theoretic criteria and defers the analytic ones to this article. If $(u_\alpha)$ satisfies $P_1$, the functionals $f \mapsto \int f\,u_\alpha\,dx$ on $L^\infty(G)$ are means whose limits along a subnet are invariant, giving amenability; conversely, an invariant mean is approximated weakly by absolutely continuous means, and a convexity argument (the mean is a fixed point of the action on the convex set of means, and the absolutely continuous means are weak-$*$ dense) produces a net satisfying $P_1$. The proof is Reiter's and is quoted from the literature. $\square$

**Remark (the invariant approximate identity as the analytic form of amenability).** The contrast with the always-existing approximate identity of the previous theorem is the point: every $L^1(G)$ has a *normalised* approximate identity, but only for an amenable $G$ can it be chosen approximately **invariant** under left translation. The convolution algebra is thus the analytic locus of amenability, and the weak-containment statement "the trivial representation is weakly contained in the regular representation" is its representation-theoretic form; that statement belongs.

## Representations and Completions

### Nondegenerate $*$-Representations and Unitary Representations

A **$*$-representation** of $L^1(G)$ on a Hilbert space $H$ is a homomorphism $\pi$ into the bounded operators with $\pi(f^*) = \pi(f)^*$. It is **nondegenerate** if $\pi(L^1(G))H$ is dense in $H$.

**Theorem (the correspondence).** There is a bijection between nondegenerate $*$-representations $\pi$ of $L^1(G)$ on a Hilbert space $H$ and continuous unitary representations $U$ of $G$ on $H$, given by

$$
\pi(f) = \int_G f(g)\,U(g)\,dg ,
$$

the integral converging in the strong operator topology. The bijection respects direct sums, subrepresentations, irreducibility and unitary equivalence, and it satisfies $\|\pi(f)\| \leq \|f\|_1$ and $\pi(L_x f) = U(x)\pi(f)$, $\pi(R_x f) = \pi(f)U(x)^{-1}$.

**Proof sketch.** For $f \in L^1(G)$ the map $f \mapsto \int f(g)U(g)dg$ is a bounded linear map into the bounded operators, with the norm bound by $\|f\|_1$, and the multiplicativity is the convolution theorem in integrated form; the *-property uses the modular factor in $f^*$ and the unitarity of $U$. Conversely, given a nondegenerate representation, the operators $U(x)$ are recovered as the strong limits of $\pi(f)$ for $f$ an approximate identity concentrated near $x$, or equivalently by the formula $U(x)\pi(f) = \pi(L_xf)$ extended to $H$ by nondegeneracy; continuity of $x \mapsto U(x)$ and the representation identities follow from the continuity of translation in $L^1(G)$. The details are standard. $\square$

**Corollary (the representation theory is algebra).** The unitary representation theory of $G$ is recovered from the Banach $*$-algebra $L^1(G)$ alone, and the irreducible unitary representations of $G$ correspond to the nondegenerate irreducible $*$-representations of $L^1(G)$. This is the sense in which harmonic analysis is the representation theory of the convolution algebra, and it is the reason the articles of this block can pass freely between the two languages. The algebraic objects are Part II's; the analytic passage is here.

### The Reduced and Full Group $\mathrm{C}^*$-Algebras

**Definition.** The **left regular representation** of $L^1(G)$ is $\lambda(f)h = f*h$ on $L^2(G)$; it is a nondegenerate $*$-representation. The **reduced group $\mathrm{C}^*$-algebra** is the norm closure

$$
C^*_r(G) = \overline{\lambda(L^1(G))}^{\ \|\cdot\|} \subseteq B(L^2(G)),
$$

and the **full group $\mathrm{C}^*$-algebra** $C^*(G)$ is the completion of $L^1(G)$ in the enveloping norm $\|f\|_{C^*} = \sup_\pi\|\pi(f)\|$, the supremum over all nondegenerate $*$-representations.

**Theorem.** (a) The map $L^1(G) \to C^*_r(G)$ is a surjective $*$-homomorphism with dense image, so $C^*_r(G)$ is the smallest $\mathrm{C}^*$-algebra generated by the regular representation. (b) The supremum defining the enveloping norm is finite, since $\|\pi(f)\| \leq \|f\|_1$, and $C^*(G)$ is a $\mathrm{C}^*$-algebra; there is a canonical surjection $C^*(G) \to C^*_r(G)$. (c) $\pi$ is a representation of $C^*(G)$ restricted to $L^1(G)$; the reduced representation is the composition with the quotient map precisely when the group is amenable, and otherwise the map is not injective. (d) For abelian $G$, $C^*(G) \cong C_0(G^\vee)$.

**Pro.** (a) and (b) are the properties of the enveloping $\mathrm{C}^*$-norm and the density of $L^1(G)$; (c) is the statement that the regular representation is faithful on $C^*(G)$ exactly in the amenable case (the weak containment of the trivial representation in the regular representation), treated; (d) is the Gelfand–Naimark theorem for the commutative $\mathrm{C}^*$-algebra $L^1(G)$ of *Harmonic Analysis on Groups*, §The Algebra of the Transform. $\square$

### The Group von Neumann Algebra

**Definition.** The **group von Neumann algebra** is $L(G) = \lambda(G)'' = \lambda(L^1(G))''$, the weak (or strong) operator closure of the image of $L^1(G)$ in $B(L^2(G))$.

**Theorem.** $L(G)$ is a von Neumann algebra containing the image of $L^1(G)$; it is the double commutant of the image of the group, $L(G) = \lambda(G)''$, and it equals the commutant of the right regular representation, $L(G) = \rho(G)'$. When $G$ is discrete, $L(G)$ is finite, with faithful normal tracial weight $\tau(a) = \langle a\delta_e,\delta_e\rangle$, and it is a factor exactly when every nontrivial conjugacy class of $G$ is infinite (the **icc** condition); for $G$ discrete non-abelian free the factor is of type $\mathrm{II}_1$. For compact $G$, $L(G)\cong\bigoplus_{\pi\in\operatorname{Irr}(G)}\operatorname{End}(\mathcal{H}_\pi)$, a direct sum of type I factors, by *The Peter–Weyl Theorem*, §Consequences.

**Proof.** The double-commutant theorem identifies the weak closure with the double commutant; $\rho(G)'$ contains $\lambda(G)$ and is the commutant of the right representation, and the two coincide for the regular representation by the standard computation of the commutant of a direct sum of type I factors or, in the general case, by the von Neumann algebra theory of *Operator Algebras*. The discrete statements are in *Operator Algebras*, §Examples from Matrix and Group Algebras. $\square$

## The Abelian Case

### The Gelfand Transform

Let $G$ be locally compact abelian, so that $\Delta \equiv 1$ and $f^*(x) = \overline{f(-x)}$. Then $L^1(G)$ is a commutative Banach $*$-algebra and its Gelfand transform is the Fourier transform: the spectrum of $L^1(G)$ is $G^\vee$, and for $\chi \in G^\vee$ the corresponding character is $f \mapsto \hat f(\chi) = \int f(x)\overline{\chi(x)}dx$. The convolution theorem $\widehat{f*g} = \hat f\hat g$ is the homomorphism property of the Gelfand transform, and the involution satisfies $\widehat{f^*}(\chi) = \overline{\hat f(\chi)}$. The completion of $L^1(G)$ in the $\mathrm{C}^*$-norm is $C^*(G) \cong C_0(G^\vee)$, with the Gelfand transform as the isomorphism. This is *Harmonic Analysis on Groups*, §The Algebra of the Transform, and it is the exact commutative case of the correspondence between the algebra and the group.

### The Center and the Central Characters

**Theorem.** For a unimodular group $G$, the center of $L^1(G)$ is

$$
Z(L^1(G)) = \{f \in L^1(G) : f(xy) = f(yx) \text{ for almost all } x,y \in G\},
$$

the closed subspace of functions invariant under conjugation; for abelian $G$, $Z(L^1(G)) = L^1(G)$. The nonzero complex homomorphisms of the center are the **central characters**, and for a compact or a type I group they are in bijection with the unitary dual.

**Proof.** $f$ is central iff $f*g = g*f$ for every $g \in L^1(G)$. Testing against a $g$ concentrated in a small neighbourhood of a point $z$ gives $f(z^{-1}x) = f(xz^{-1})$ for almost all $x$, which is the conjugation invariance $f(xy) = f(yx)$ after $z = y^{-1}$. Conversely conjugation invariance gives centrality by the same change of variable. The statement about central characters is the spectral theory of the commutative Banach algebra $Z(L^1(G))$ together with the description of its characters by irreducible representations; for compact groups the central characters are the normalised characters $\chi_\pi/d_\pi$ of *Analysis on Compact Groups*. $\square$

**Remark (the abelian side is the whole center).** For $G$ abelian the center is the whole algebra and its Gelfand spectrum is $G^\vee$; for a compact group the center is the algebra of class functions and its spectrum is the dual; for a general unimodular type I group the center is described by the Plancherel measure. The center is thus the bridge between the commutative and the non-commutative pictures.

## Examples

### Discrete Groups

For $G$ discrete with counting measure, $\Delta \equiv 1$, $L^1(G) = \ell^1(G)$, and convolution is

$$
(f*g)(x) = \sum_{y \in G} f(y)\,g(y^{-1}x) ,
$$

the multiplication of the **group algebra** $\ell^1(G)$; the involution is $f^*(x) = \overline{f(x^{-1})}$, and the identity $\delta_e$ is present, so $\ell^1(G)$ is a unital Banach $*$-algebra. For finite $G$ this is the algebraic group algebra of *Group Algebras* with the normalised counting measure, and its transform is the Wedderburn decomposition of *The Peter–Weyl Theorem*. For $G = \mathbb{Z}$ the algebra is the algebra of absolutely convergent Fourier series under multiplication, with the maximal ideal space the circle, as in *Harmonic Analysis on Groups*, §The Standard Cases. The reduced $\mathrm{C}^*$-algebra $C^*_r(G)$ of a discrete group is generated by the unitary operators $\lambda(x)$ of the regular representation.

### Compact Groups

For $G = K$ compact with normalised Haar measure, $G$ is unimodular, the involution is $f^*(k) = \overline{f(k^{-1})}$, and the algebra $L^1(K)$ has a transform into $\bigoplus_{\pi\in\operatorname{Irr}(K)}\operatorname{End}(\mathcal{H}_\pi)$ which is injective with dense image; it is commutative exactly when $K$ is abelian, in which case it is the algebra of *Analysis on Compact Groups*, §The Fourier Transform on a Compact Group. The center is the algebra of class functions, and its characters are the irreducible characters.

### The Line, the Torus and Euclidean Space

For $G = \mathbb{R}^n$, $\Delta \equiv 1$, $L^1(\mathbb{R}^n)$ is commutative, and the Gelfand transform is the Fourier transform of *Fourier Analysis on Euclidean Spaces*; the spectrum is $\mathbb{R}^n$ itself. For $G = T^n$ the algebra is the convolution algebra of integrable functions on the torus, whose Gelfand spectrum is $\mathbb{Z}^n$, and the transform is the Fourier coefficient map. Both are instances of the abelian theory of *Harmonic Analysis on Groups*.

### The Affine Group

Let $G = \{(a,b) : a > 0\}$ with the multiplication above, $\mu_L = a^{-2}da\,db$ and $\Delta(a,b) = a^{-1}$. The convolution is

$$
(f*g)(a,b) = \int_0^\infty\!\!\int_{-\infty}^{\infty} f(\alpha,\beta)\,g\bigl(\alpha^{-1}a,\ \alpha^{-1}(b-\beta)\bigr)\,\alpha^{-2}\,d\alpha\,d\beta ,
$$

and the involution is $f^*(a,b) = a\,\overline{f(a^{-1},-b/a)}$ because $\Delta(a,b)^{-1} = a$ and $(a,b)^{-1} = (a^{-1},-b/a)$. The algebra $L^1(G)$ is non-commutative and is not symmetric in the naive involution: the modular factor is essential to $\|f^*\|_1 = \|f\|_1$, and this is the simplest illustration of the non-unimodular conventions of the whole block. The group is solvable, hence not of the semisimple class, and it is not amenable since it is not unimodular; Reiter's property $P_1$ therefore fails, although the normalised approximate identity of the general theorem still exists.

## Summary

For a locally compact group $G$ with left Haar measure $dx$ and modular function $\Delta$ (the convention $\mu(Ag)=\Delta(g)\mu(A)$, $d\mu_R=\Delta^{-1}d\mu_L$, $\int f(x^{-1})dx=\int f(x)\Delta(x)^{-1}dx$ of *Locally Compact Groups and Haar Measure*), the convolution $(f*g)(x)=\int f(y)g(y^{-1}x)dy$ makes $L^1(G)$ a Banach algebra with $\|f*g\|_1\le\|f\|_1\|g\|_1$ and Young's inequality $\|f*g\|_r\le\|f\|_p\|g\|_q$ for $1/p+1/q=1+1/r$; the involution $f^*(x)=\overline{f(x^{-1})}\Delta(x)^{-1}$ makes it a Banach $*$-algebra with isometric involution, $(f*g)^*=g^* * f^*$. It is commutative iff $G$ is abelian and unital iff $G$ is discrete. Every $L^1(G)$ has a normalised two-sided approximate identity; it has an approximately invariant one if and only if $G$ is amenable (Reiter's property $P_1$). Nondegenerate $*$-representations of $L^1(G)$ are exactly the continuous unitary representations of $G$, through $\pi(f)=\int f(g)U(g)dg$, and this correspondence makes the unitary representation theory of $G$ a chapter of the spectral theory of a Banach $*$-algebra. The completions are the reduced group $\mathrm{C}^*$-algebra $C^*_r(G)$, the full $C^*(G)$ with canonical surjection onto it, and the group von Neumann algebra $L(G)=\lambda(G)''=\rho(G)'$, which for discrete $G$ is finite with trace $\langle a\delta_e,\delta_e\rangle$ and for compact $G$ is $\bigoplus_\pi\operatorname{End}(\mathcal{H}_\pi)$. In the abelian case the Gelfand transform is the Fourier transform and $C^*(G)\cong C_0(G^\vee)$; the center is the algebra of conjugation-invariant functions, whose characters are the central characters. The examples are the discrete group algebra $\ell^1(G)$, the compact case, $\mathbb{R}^n$ and $T^n$, and the affine group, which exhibits the modular factor in the involution and the failure of amenability.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $G$, $e$, $dx = d\mu_L$ | Locally compact group, identity, left Haar measure |
| $\Delta$, unimodular | Modular function, $\mu(Ag)=\Delta(g)\mu(A)$; $\Delta\equiv1$ |
| $d\mu_R = \Delta^{-1}d\mu_L$ | Right Haar measure |
| $L_x$, $R_x$ | Left and right translations on functions |
| $\lambda$, $\rho$ | Left and right regular representations on $L^2(G)$ |
| $(f*g)(x) = \int_G f(y)g(y^{-1}x)\,dy$ | Convolution (left Haar measure) |
| $f^*(x) = \overline{f(x^{-1})}\Delta(x)^{-1}$ | Isometric involution |
| $L^1(G)$ | Convolution Banach $*$-algebra |
| $(u_\alpha)$ | Approximate identity; normalised, $u_\alpha\ge0$, $\int u_\alpha = 1$ |
| $P_1$ | Reiter's property, equivalent to amenability |
| $\pi(f) = \int_G f(g)U(g)\,dg$ | Nondegenerate $*$-representation from a unitary representation |
| $C^*_r(G)$ | Reduced group $\mathrm{C}^*$-algebra, closure of $\lambda(L^1(G))$ |
| $C^*(G)$ | Full group $\mathrm{C}^*$-algebra, enveloping norm |
| $L(G) = \lambda(G)'' = \rho(G)'$ | Group von Neumann algebra |
| $Z(L^1(G))$ | Center, the conjugation-invariant functions (unimodular $G$) |
| $\hat f(\chi) = \int_G f\overline\chi\,dx$ | Gelfand transform in the abelian case |
| $\ell^1(G)$ | Group algebra of a discrete group |
| $\tau(a) = \langle a\delta_e,\delta_e\rangle$ | Trace on $L(G)$, $G$ discrete |





## Further Reading

- Gerald B. Folland, *A Course in Abstract Harmonic Analysis* (CRC Press, 2nd ed. 2015), for the convolution algebra, approximate identities, Reiter's condition and the group $\mathrm{C}^*$-algebras.
- Edwin Hewitt and Kenneth A. Ross, *Abstract Harmonic Analysis I* (Springer, 2nd ed. 1979), for the detailed theory of $L^1(G)$, its ideals and its representations.
- Lynn H. Loomis, *An Introduction to Abstract Harmonic Analysis* (Van Nostrand, 1953; reprinted Dover, 2011), for the algebra of convolution and the passage to representations.
- Hans Reiter and Jan D. Stegeman, *Classical Harmonic Analysis and Locally Compact Groups* (Oxford, 2nd ed. 2000), for Reiter's property $P_1$, amenability and the approximate identities.
- Alain Connes, *Noncommutative Geometry* (Academic Press, 1994), for the group von Neumann algebra, the trace and the type classification in the operator-algebraic setting.
- Dana P. Williams, *Crossed Products of $\mathrm{C}^*$-Algebras* (AMS, 2007), for the reduced and full group $\mathrm{C}^*$-algebras and the amenability of the canonical quotient.
- Jean Dixmier, *$\mathrm{C}^*$-Algebras* (North-Holland, 1977), for the enveloping $\mathrm{C}^*$-algebra, the spectrum of a Banach $*$-algebra and the representation theory used here.
- Walter Rudin, *Functional Analysis* (McGraw–Hill, 2nd ed. 1991), for the Hilbert-space spectral theory, the compact and Hilbert–Schmidt operators and the Banach-algebra foundations quoted as standard.
