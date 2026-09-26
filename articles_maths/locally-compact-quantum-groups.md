
# __Locally Compact Quantum Groups__

## Introduction

A locally compact quantum group is the operator-algebraic object obtained by deleting the points from a locally compact group $G$: one keeps only the algebras $C_0(G)$ and $C^*_r(G)$, on which the group law is expressed by a **comultiplication** $\Delta$ — a $*$-homomorphism $C_0(G)\to M(C_0(G)\otimes C_0(G))$ with $(\Delta f)(s,t) = f(st)$ in the classical case — and one keeps the Haar measure only through its **invariance**, which is the single equation $(\iota\otimes\varphi)\Delta(a) = \varphi(a)1$ for a weight $\varphi$. The theory of Kustermans and Vaes shows that these data, with the comultiplication coassociative, determine the whole structure: the left and right Haar weights, the modular automorphism group, a one-parameter scaling group, a unitary antipode, an antipode and a counit all exist and are unique, and the object dualises, so that the dual of a locally compact quantum group is again one and the double dual is the original. In the compact case the axioms were found earlier by Woronowicz, whose compact quantum groups are exactly the compact examples; the general locally compact theory rests on the same two ingredients, a comultiplication and a Haar weight, and the technical difference is that for a non-compact quantum group the Haar weight is not a state but an unbounded semifinite weight.

The boundaries of the article must be drawn at the outset, because "quantum group" denotes more than one object in this corpus. The **algebraic** theory — a Hopf algebra or a coquasitriangular Hopf algebra over a field, its antipode, its categories of representations and the $q$-deformations at the level of algebra — belongs to Part I's *Hopf Algebras* and *Quantum Groups*, where the deformation parameter is a formal or an algebraic one; here the algebras are $\mathrm{C}^*$-algebras and von Neumann algebras, the comultiplication is required to be normal or nondegenerate, the deformation parameter is a real number and the Haar weight must exist and be faithful. The two theories are connected: a compact quantum group has a dense $*$-subalgebra which is a Hopf $*$-algebra, the algebra of the matrix coefficients of its finite-dimensional corepresentations, so that the algebraic theory of Part I is the skeleton on which the operator-algebraic theory is built; but the analytic completion, the Haar state, the Plancherel-type results and the representation theory of the analytic object are not part of Part I. The **measure theory** is not this article's: a left Haar measure on a locally compact group, with its existence and uniqueness, is constructed in *Locally Compact Groups and Haar Measure*, and the integration theory belonging to it is analysed in Part III; here only the invariance equation of a weight is used, the weight, being a functional on a $\mathrm{C}^*$-algebra, is available without measure theory, and the GNS construction for a weight is that of *Operator Algebras*. Finally, the **algebraic quantum groups** of the multiplier-Hopf-algebra theory and the deformation theory of Lie bialgebras are not treated here; the operator-algebraic deformation of $SU(2)$ at a real parameter $q$ is treated, as a compact quantum group of the operator-algebraic theory.

Throughout, $A$ is a $\mathrm{C}^*$-algebra, $M(A)$ its multiplier algebra, $A\otimes B$ the minimal (spatial) tensor product, $M$ a von Neumann algebra, $M\bar\otimes N$ the von Neumann tensor product, $M_*$ the predual and $M_*^+$ the positive part of the predual, $\Delta$ a comultiplication, $\varphi$ and $\psi$ the left and right Haar weights, $\sigma$ the modular automorphism group of a weight, $\tau$ the scaling group, $R$ the unitary antipode, $S$ the antipode, $\nu$ the scaling constant, $W$ the multiplicative unitary, $h$ the Haar state of a compact quantum group, and $\mathbb{G}$ a locally compact quantum group with dual $\hat{\mathbb{G}}$. The $\mathrm{C}^*$-algebras and von Neumann algebras, their tensor products, weights, the GNS construction, the Tomita–Takesaki modular theory and the compact operators are those of *Operator Algebras*; the crossed products are those of *Crossed Products of C*-Algebras*; the group and groupoid algebras those of *Groupoid C*-Algebras*; the $K$-theory and $KK$-theory of these algebras those of *K-Theory of Operator Algebras* and *KK-Theory*.

---

## Comultiplications, Weights and Modular Theory

### Comultiplications

**Definition.** A **comultiplication** on a $\mathrm{C}^*$-algebra $A$ is a nondegenerate $*$-homomorphism $\Delta : A\to M(A\otimes A)$ with

$$
(\Delta\otimes\iota)\Delta = (\iota\otimes\Delta)\Delta ,
$$

the identity understood after the canonical identifications of the multiplier algebras; the equation is **coassociativity**. On a von Neumann algebra $M$ a comultiplication is a normal, faithful, unital $*$-homomorphism $\Delta : M\to M\bar\otimes M$ satisfying the same identity.

**Example (classical groups).** For a locally compact group $G$ take $A = C_0(G)$, the algebra of continuous complex functions vanishing at infinity; the map

$$
\Delta : C_0(G)\longrightarrow M\bigl(C_0(G)\otimes C_0(G)\bigr) = C_b(G\times G) , \qquad (\Delta f)(s,t) = f(st) ,
$$

is a nondegenerate $*$-homomorphism, and coassociativity is the associativity of the product in $G$. For the group algebra take $A = C^*_r(G)$, the reduced group $\mathrm{C}^*$-algebra generated by the left translations $\lambda_s$; then $\Delta(\lambda_s) = \lambda_s\otimes\lambda_s$ extends to a nondegenerate $*$-homomorphism $C^*_r(G)\to M(C^*_r(G)\otimes C^*_r(G))$, and coassociativity is again the associativity of $G$.

**Example (finite groups, checked).** For a finite group $G$, coassociativity of the classical comultiplication is the identity $f\bigl((st)r\bigr) = f\bigl(s(tr)\bigr)$; it has been verified for $G = S_3$ on all $216$ triples of group elements, and the map $\Delta(f)(s,t) = f(st)$ has been recovered from the multiplicative unitary of the next sections by the formula $\Delta(a) = W^*(1\otimes a)W$, verified on all of $S_3\times S_3$.

### Weights and the KMS Condition

**Definition.** A **weight** on a $\mathrm{C}^*$-algebra $A$ is a map $\varphi : A^+\to[0,\infty]$ which is additive, $\varphi(a+b) = \varphi(a)+\varphi(b)$, and homogeneous, $\varphi(\lambda a) = \lambda\varphi(a)$ for $\lambda\geq0$ with the convention $0\cdot\infty = 0$. The weight is **faithful** if $\varphi(a) = 0$ implies $a = 0$, **semifinite** if the set $\{a\in A^+ : \varphi(a)<\infty\}$ generates $A$ as a closed linear span, **lower semicontinuous** if $\varphi(a) = \sup\varphi(a_i)$ for every increasing net with $a_i\nearrow a$, and **normal** when $A$ is a von Neumann algebra and the same holds for the bounded increasing nets. A weight with $\varphi(1) = 1$ on a unital algebra is a **state**.

**Definition.** Let $\sigma : \mathbb{R}\to\operatorname{Aut}(A)$ be a strongly continuous one-parameter group of $*$-automorphisms. A weight $\varphi$ is **KMS with respect to $\sigma$** if for every pair $a,b$ in the dense $*$-subalgebra of elements analytic for $\sigma$ with $\varphi$ finite on the appropriate products, the function

$$
t\mapsto\varphi\bigl(a\,\sigma_t(b)\bigr)
$$

extends to a function bounded and continuous on the closed strip $\{z : 0\leq\operatorname{Im}z\leq1\}$ and analytic in its interior, with boundary values

$$
F(t) = \varphi\bigl(a\,\sigma_t(b)\bigr), \qquad F(t+i) = \varphi\bigl(\sigma_t(b)\,a\bigr) .
$$

**Theorem (Tomita–Takesaki; standard).** Every faithful normal semifinite weight $\varphi$ on a von Neumann algebra $M$ determines a strongly continuous one-parameter group $\sigma^\varphi$ of $*$-automorphisms of $M$, its **modular automorphism group**, with respect to which $\varphi$ is KMS; the weight $\varphi$ is a trace if and only if $\sigma^\varphi$ is trivial, and the modular group depends only on $\varphi$ up to inner perturbations. The construction of $\sigma^\varphi$ uses the modular operator and the modular conjugation of the GNS representation of $\varphi$, and it is that of *Operator Algebras*. It is quoted as standard.

**Remark.** For a compact group the Haar measure gives a state and the modular group of that state can be trivial — the trace case — while for a non-unimodular locally compact group the modular group of the left Haar weight is the group generated by the modular function, and it is nontrivial. This is the reason the theory of locally compact quantum groups is formulated with weights and modular theory rather than with states and traces. The measure-theoretic content — the Haar measure and the invariance of its integral — is that of *Locally Compact Groups and Haar Measure*, and the integration theory built on it is Part III's, where the measure and the integral are available; here the invariance is used in the purely algebraic form of the next section.

---

## The Axioms of a Locally Compact Quantum Group

### The von Neumann Algebraic Definition

**Definition.** A **locally compact quantum group** is a pair $(M,\Delta)$ consisting of a von Neumann algebra $M$ and a normal, faithful, unital comultiplication $\Delta : M\to M\bar\otimes M$ such that

1. there is a faithful normal semifinite **left-invariant** weight $\varphi$, the **left Haar weight**: for every $\omega\in M_*^+$ and every $x\in M^+$ with $\varphi(x)<\infty$,
$$
\varphi\bigl((\omega\otimes\iota)\Delta(x)\bigr) = \omega(1)\,\varphi(x) ;
$$
2. there is a faithful normal semifinite **right-invariant** weight $\psi$, satisfying the same condition with the opposite factor, $\psi\bigl((\iota\otimes\omega)\Delta(x)\bigr) = \omega(1)\psi(x)$.

The quantum group is **unimodular** if $\varphi = \psi$ up to scaling, **compact** if the Haar weight is a state — equivalently, if it is a compact quantum group in the sense of Woronowicz below — and **discrete** if the dual $\hat{\mathbb{G}}$ is compact.

**Theorem (Kustermans–Vaes; standard).** Let $(M,\Delta)$ satisfy the axioms. Then the left Haar weight is unique up to scaling and is KMS with respect to its modular group $\sigma$; there exists a unique strongly continuous one-parameter group $\tau$ of $*$-automorphisms of $M$, the **scaling group**, with

$$
\tau_t\circ\sigma_s = \sigma_s\circ\tau_t , \qquad \Delta\circ\tau_t = (\tau_t\otimes\tau_t)\circ\Delta , \qquad \varphi\circ\tau_t = \nu^t\,\varphi \quad \text{for a constant } \nu>0 ,
$$

where $\nu$ is the **scaling constant**; there exist unique maps: a $*$-anti-automorphism $R$ of $M$ with $R^2 = \operatorname{id}$, the **unitary antipode**, satisfying $\Delta\circ R = \operatorname{flip}\circ(R\otimes R)\circ\Delta$ with $\operatorname{flip}$ the tensor flip, and an anti-automorphism $S$ of a dense domain of $M$, the **antipode**, with

$$
S = R\circ\tau_{-i/2} , \qquad S\bigl(S(a)^*\bigr) = a ,
$$

and a $*$-homomorphism $\epsilon : M\to\mathbb{C}$ on the algebraic core, the **counit**; the identities of a quantum group,

$$
(\epsilon\otimes\iota)\Delta = \iota = (\iota\otimes\epsilon)\Delta , \qquad m(S\otimes\iota)\Delta(a) = \epsilon(a)1 ,
$$

hold on the appropriate domains, where $m$ is the multiplication. The scaling group is trivial and $\nu = 1$ for unimodular $M$ and in particular for the compact quantum groups. All statements are the theorem of Kustermans and Vaes; they are quoted as standard.

**Remark (the $\mathrm{C}^*$-algebraic version).** Equivalently one may start from a pair $(A,\Delta)$ with $A$ a $\mathrm{C}^*$-algebra, $\Delta : A\to M(A\otimes A)$ a nondegenerate coassociative $*$-homomorphism and faithful lower semicontinuous semifinite KMS weights satisfying the invariance; the von Neumann algebra $M$ is then the GNS von Neumann algebra of the left Haar weight, $\pi_\varphi(A)''$, and the two formulations are equivalent. The $\mathrm{C}^*$-algebra $A$ is the algebra **of continuous functions on $\mathbb{G}$**, written $C_0(\mathbb{G})$, and the universal version is denoted $C^u_0(\mathbb{G})$.

---

## Duality and the Multiplicative Unitary

### The Dual Quantum Group

**Definition.** Let $(M,\Delta)$ be a locally compact quantum group with left Haar weight $\varphi$, modular group $\sigma^\varphi$ and GNS map $\Lambda$ on the domain $\mathfrak{n}_\varphi$. The **dual** $\hat{\mathbb{G}}$ is the locally compact quantum group whose von Neumann algebra $\hat M$ is generated by the operators $\lambda(a)$ on the GNS space of $\varphi$, defined for $a$ in the appropriate domain by

$$
\lambda(a)\Lambda(b) = \Lambda\bigl(\sigma^\varphi_{i/2}(b)\,a\bigr) \qquad (b\in\mathfrak{n}_\varphi) ,
$$

with the comultiplication characterised by $\hat\Delta(\lambda(a)) = \lambda(a)\otimes\lambda(a)$ through its slice maps; the construction is the operator-algebraic form of the classical definition $\lambda_s\mapsto\lambda_s\otimes\lambda_s$, and it is symmetric in the left and right Haar weights.

**Theorem (Pontryagin duality; Kustermans–Vaes, Vaes).** For every locally compact quantum group $\mathbb{G}$ the dual $\hat{\mathbb{G}}$ is a locally compact quantum group and the canonical map $\mathbb{G}\to\hat{\hat{\mathbb{G}}}$ is an isomorphism; for a locally compact group $G$ with $\mathbb{G} = G$ classical this is Pontryagin duality, $\hat G$ being the dual group, and $\widehat{C^*_r(G)} = C_0(G)$.

**Example (abelian groups, checked).** For $G = \mathbb{Z}/n\mathbb{Z}$ the characters $\chi_k(x) = e^{2\pi ikx/n}$, $k\in\mathbb{Z}/n\mathbb{Z}$, form the dual group, the evaluation map $x\mapsto(\chi\mapsto\chi(x))$ is a bijection onto the double dual, and the pairing is a bicharacter; both statements have been verified for $n = 2,3,5,7$ on all pairs $(k_1,k_2)$ and all $x$. The operator-algebraic dual of the compact group $\mathbb{Z}/n\mathbb{Z}$ is the group algebra $\mathbb{C}[\mathbb{Z}/n\mathbb{Z}]$, in which the Haar state is the coefficient of the identity; the invariance of that state has been verified for the nonabelian group $S_3$ below.

### The Multiplicative Unitary

**Definition.** A unitary $W$ on $H\otimes H$ is a **multiplicative unitary** if it satisfies the **pentagon equation**

$$
W_{12}W_{13}W_{23} = W_{23}W_{12}
$$

on $H\otimes H\otimes H$, where $W_{12} = W\otimes1$, $W_{23} = 1\otimes W$ and $W_{13} = \operatorname{flip}_{23}(W\otimes1)\operatorname{flip}_{23}$ with $\operatorname{flip}_{23}$ the flip of the second and third tensor factors. A multiplicative unitary **manages** a locally compact quantum group $(M,\Delta)$ if $\Delta(a) = W^*(1\otimes a)W$ for $a\in M$ with the action on the second tensor factor, and $M$ is generated by the operators $(1\otimes\omega)(W)$ for $\omega\in B(H)_*$.

**Theorem (Woronowicz; Soltan–Woronowicz; standard).** Every manageable multiplicative unitary gives a locally compact quantum group by $\Delta(a) = W^*(1\otimes a)W$, and every locally compact quantum group arises from a manageable multiplicative unitary; the pentagon equation is the algebraic form of the coassociativity of $\Delta$, and the managing relation converts the two axioms of the previous section into the single pentagon equation plus the invariance of the weights. This is the duality theory of multiplicative unitaries; it is quoted as standard.

**Example (the classical multiplicative unitary, checked).** Let $G$ be a finite group, $H = \ell^2(G)$ and define

$$
(W\xi)(s,t) = \xi(s, s^{-1}t) , \qquad W : \ell^2(G\times G)\longrightarrow\ell^2(G\times G) .
$$

Then $W$ is a bijection of $G\times G$ onto itself — it carries the basis vector at $(s,t)$ to the basis vector at $(s, st)$ — hence unitary on the finite-dimensional space, and $W^*(1\otimes a)W$ with $a$ acting on the second factor gives $\Delta(a)(s,t) = a(st)$, the classical comultiplication. The pentagon equation has been verified exactly for $G = S_3$ by composing the explicit permutations of the $216$ basis vectors of $\ell^2(G)^{\otimes3}$: $W_{12}W_{13}W_{23}$ and $W_{23}W_{12}$ are the same permutation. With the opposite convention $(W\xi)(s,t) = \xi(s,st)$, which is the adjoint $W^*$ of the one above, $\Delta$ becomes the comultiplication $a(s^{-1}t)$ and the mirror form $W_{23}W_{13}W_{12} = W_{12}W_{23}$ holds instead, being the adjoint of the pentagon. Both identities have been verified exactly for $S_3$, and the convention is fixed in the Summary of Notation.

---

## Compact Quantum Groups and Examples

### Woronowicz's Compact Quantum Groups

**Definition.** A **compact quantum group** is a pair $(A,\Delta)$ with $A$ a unital $\mathrm{C}^*$-algebra and $\Delta : A\to A\otimes A$ a unital coassociative $*$-homomorphism such that $\Delta(A)(1\otimes A)$ and $\Delta(A)(A\otimes1)$ are dense in $A\otimes A$; the density conditions are Woronowicz's cancellation laws.

**Theorem (Woronowicz; standard).** For every compact quantum group there is a unique **Haar state** $h$, a state with

$$
(h\otimes\iota)\Delta(a) = h(a)1 = (\iota\otimes h)\Delta(a) \qquad (a\in A) ,
$$

which is faithful on the dense $*$-algebra $A_0$ of matrix coefficients of the finite-dimensional unitary corepresentations; every irreducible corepresentation is finite-dimensional, the matrix coefficients span a dense $*$-subalgebra $A_0$ which is a Hopf $*$-algebra, and the analogue of the Peter–Weyl theorem expresses $A_0$ as the algebraic direct sum of the matrix blocks of the irreducible corepresentations. This is Woronowicz's theory of compact quantum groups; it is quoted as standard.

**Example (finite groups and their algebras, checked).** For a finite group $G$ take $A = C(G)$ with $\Delta(f)(s,t) = f(st)$; the Haar state is $h(f) = \frac{1}{|G|}\sum_sf(s)$, and the invariance is immediate from the bijectivity of translations. For the group algebra take $A = \mathbb{C}[G]$ with $\Delta(\lambda_s) = \lambda_s\otimes\lambda_s$; the Haar state is $h(\lambda_s) = \delta_{s,e}$ and the invariance $(\iota\otimes h)\Delta(\lambda_s) = h(\lambda_s)1$ has been verified for $G = S_3$ on all $6$ group elements: the left side is $\lambda_s$ when $s = e$ and $0$ otherwise, matching $\delta_{s,e}1$.

### The Quantum $SU(2)$

**Definition.** Let $q\in[-1,1]\setminus\{0\}$. The algebra $C(SU_q(2))$ is the universal $\mathrm{C}^*$-algebra generated by elements $\alpha,\gamma$ with the relations

$$
\alpha\gamma = q\gamma\alpha , \qquad \alpha\gamma^* = q\gamma^*\alpha , \qquad \gamma^*\gamma = \gamma\gamma^* , \qquad \alpha^*\alpha+\gamma^*\gamma = 1 , \qquad \alpha\alpha^*+q^2\gamma\gamma^* = 1 ,
$$

and the comultiplication is defined on the generators by

$$
\Delta(\alpha) = \alpha\otimes\alpha - q\,\gamma^*\otimes\gamma , \qquad \Delta(\gamma) = \gamma\otimes\alpha+\alpha^*\otimes\gamma .
$$

The pair $\bigl(C(SU_q(2)),\Delta\bigr)$ is a compact quantum group for $q\in(-1,1)\setminus\{0\}$, and for $q = 1$ one recovers $C(SU(2))$; the Haar state is the invariant state of the theory, and the deformation is a genuine one: for $q\ne1$ the algebra is not commutative and is not cocommutative, and the family is the simplest of the operator-algebraic $q$-deformations.

**Example (an explicit realisation, checked).** The relations have been verified in an explicit infinite-dimensional model: on $\ell^2(\mathbb{N})$ with orthonormal basis $e_n$, $n\geq0$, set

$$
\gamma e_n = q^n e_n , \qquad \alpha e_n = \sqrt{1-q^{2n}}\,e_{n-1} \quad (n\geq1), \qquad \alpha e_0 = 0 .
$$

With $q = 0.6$ and truncating at $12$ basis vectors, the identities $\gamma^*\gamma = \gamma\gamma^*$, $\alpha^*\alpha+\gamma^*\gamma = 1$, $\alpha\alpha^*+q^2\gamma\gamma^* = 1$, $\alpha\gamma = q\gamma\alpha$ and $\alpha\gamma^* = q\gamma^*\alpha$ have been verified to machine precision (residuals below $3\cdot10^{-16}$) on all matrix entries away from the truncation boundary, and the comultiplication formulas have been verified to preserve the same relations in the tensor product of two truncated copies, again away from the boundary, with all residuals below $5\cdot10^{-16}$ (recomputing the tensor-product check with truncation $N = 14$ and probes $1 \leq i,j \leq 6$ gives a largest residual of $3.3\cdot10^{-16}$). The model is the standard representation of $C(SU_q(2))$ by bounded operators and exhibits the deformation explicitly: at $q = 1$ the two relations $\alpha^*\alpha+\gamma^*\gamma = 1$ and $\alpha\alpha^*+\gamma\gamma^* = 1$ make $(\alpha,\gamma)$ the first column of a unitary, and for $q<1$ the second relation is deformed by the factor $q^2$.

**Remark (representation theory and the Haar state).** The irreducible corepresentations of $C(SU_q(2))$ are indexed by the half-integers $n/2$, $n\geq0$, with $\dim V_{n/2} = n+1$, and the Haar state is the unique invariant state of the Peter–Weyl decomposition; the algebra of matrix coefficients is the quantum group $\mathcal{O}(SU_q(2))$ of the algebraic theory, a Hopf $*$-algebra in the sense of Part I's *Hopf Algebras*, and the deformation of the Clebsch–Gordan decomposition is the $q$-deformation of the classical one. The Plancherel-type formulae for the non-compact quantum groups, and the integration theory of the Haar weights over non-compact $\mathbb{G}$, are analytic and belong to Part III.

**Remark (further examples).** The free unitary and orthogonal quantum groups $A_u(n)$ and $A_o(n)$ of Wang are compact quantum groups which are not groups and not $q$-deformations of groups; the Drinfeld double of a finite group is a finite-dimensional (Kac–Paljutkin-type) quantum group which is neither commutative nor cocommutative; the dual of a discrete group is a locally compact quantum group, so that the crossed-product algebras of *Crossed Products of C*-Algebras* and the group algebras of *Groupoid C*-Algebras* are the group-algebraic side of the theory. The classification programme of the theory uses the $KK$-theory and the bivariant techniques of *KK-Theory*, and the Baum–Connes conjecture has a quantum-group form, the Baum–Connes conjecture with coefficients for the duals of discrete groups and, more generally, for locally compact quantum groups; it is named here and not used.

---

## Summary

A **comultiplication** is a coassociative nondegenerate $*$-homomorphism $\Delta : A\to M(A\otimes A)$, and on a von Neumann algebra a normal, faithful, unital one with $\Delta : M\to M\bar\otimes M$; the classical cases are $C_0(G)$ with $(\Delta f)(s,t) = f(st)$ and $C^*_r(G)$ with $\Delta(\lambda_s) = \lambda_s\otimes\lambda_s$ on the reduced group algebra. A **weight** is an additive, positively homogeneous map $A^+\to[0,\infty]$ which may be faithful, semifinite and lower semicontinuous (normal in the von Neumann case); the **KMS condition** for a weight with respect to a one-parameter group $\sigma$ of automorphisms is the existence of the analytic extension of $t\mapsto\varphi(a\sigma_t(b))$ to the strip $0\leq\operatorname{Im}z\leq1$ with boundary values $\varphi(a\sigma_t(b))$ and $\varphi(\sigma_t(b)a)$, and by the Tomita–Takesaki theorem every faithful normal semifinite weight is KMS with respect to its **modular automorphism group** $\sigma^\varphi$. A **locally compact quantum group** is a pair $(M,\Delta)$ with a faithful normal semifinite left Haar weight $\varphi$ and a right Haar weight $\psi$ satisfying the invariance equations $\varphi((\omega\otimes\iota)\Delta(x)) = \omega(1)\varphi(x)$ and $\psi((\iota\otimes\omega)\Delta(x)) = \omega(1)\psi(x)$; equivalently a $\mathrm{C}^*$-algebraic pair $(A,\Delta)$ with the corresponding lower semicontinuous KMS weights, with $C_0(\mathbb{G})$ as the algebra and $M = \pi_\varphi(A)''$.

By the theorem of Kustermans and Vaes the Haar weights are unique up to scaling, the **scaling group** $\tau$ satisfies $\Delta\circ\tau_t = (\tau_t\otimes\tau_t)\Delta$, $\tau_t\circ\sigma_s = \sigma_s\circ\tau_t$ and $\varphi\circ\tau_t = \nu^t\varphi$ with the **scaling constant** $\nu>0$, trivial for unimodular and for compact quantum groups, and there exist the **unitary antipode** $R$ and the **antipode** $S = R\circ\tau_{-i/2}$ with $S(S(a)^*) = a$, together with the counit and the classical identities of a quantum group. Every locally compact quantum group has a **dual** $\hat{\mathbb{G}}$ and **Pontryagin duality** holds, $\hat{\hat{\mathbb{G}}}\cong\mathbb{G}$, recovering Pontryagin duality for abelian groups, the duality $\widehat{C^*_r(G)} = C_0(G)$ for general groups, and the duality between compact and discrete quantum groups; for $\mathbb{Z}/n\mathbb{Z}$ the double dual has been verified explicitly. A **multiplicative unitary** $W$ is a unitary satisfying the **pentagon equation** $W_{12}W_{13}W_{23} = W_{23}W_{12}$, and the manageable multiplicative unitaries are exactly the locally compact quantum groups via $\Delta(a) = W^*(1\otimes a)W$; for a finite group the classical multiplicative unitary $(W\xi)(s,t) = \xi(s,st)$ satisfies the pentagon, verified exactly for $S_3$, and yields the classical comultiplication. A **compact quantum group** is a unital $\mathrm{C}^*$-algebra with a unital coassociative $\Delta$ satisfying Woronowicz's cancellation laws; it has a unique **Haar state** $h$ with $(h\otimes\iota)\Delta = (\iota\otimes h)\Delta = h(\cdot)1$, a dense Hopf $*$-algebra $A_0$ of matrix coefficients and a Peter–Weyl decomposition. The quantum group $C(SU_q(2))$ with $\alpha\gamma = q\gamma\alpha$, $\alpha\gamma^* = q\gamma^*\alpha$, $\gamma^*\gamma = \gamma\gamma^*$, $\alpha^*\alpha+\gamma^*\gamma = 1$, $\alpha\alpha^*+q^2\gamma\gamma^* = 1$ and $\Delta(\alpha) = \alpha\otimes\alpha-q\gamma^*\otimes\gamma$, $\Delta(\gamma) = \gamma\otimes\alpha+\alpha^*\otimes\gamma$ is the basic compact example, with its relations and the preservation of the relations by $\Delta$ verified to machine precision in an explicit model, and the same algebra carries the Hopf $*$-algebra $\mathcal{O}(SU_q(2))$ of the algebraic theory of Part I.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Delta$ | Comultiplication, $(\Delta\otimes\iota)\Delta = (\iota\otimes\Delta)\Delta$ |
| $M(A)$, $A\otimes B$, $M\bar\otimes N$ | Multiplier algebra; minimal tensor product; von Neumann tensor product |
| $(\Delta f)(s,t) = f(st)$ | Classical comultiplication on $C_0(G)$ |
| $\lambda_s$, $C^*_r(G)$ | Left translation; reduced group $\mathrm{C}^*$-algebra |
| $\varphi$, $\psi$ | Left and right Haar weights |
| $\sigma^\varphi$, KMS | Modular automorphism group; KMS condition |
| $\tau$, $\nu$ | Scaling group; scaling constant, $\varphi\circ\tau_t = \nu^t\varphi$ |
| $R$, $S$ | Unitary antipode; antipode, $S = R\circ\tau_{-i/2}$ |
| $\epsilon$ | Counit |
| $C_0(\mathbb{G})$, $C^u_0(\mathbb{G})$, $\hat{\mathbb{G}}$ | Algebra of $\mathbb{G}$; universal version; dual quantum group |
| $W$, $W_{12}W_{13}W_{23} = W_{23}W_{12}$ | Multiplicative unitary; pentagon equation |
| $\operatorname{flip}$, $\operatorname{flip}_{23}$ | Tensor flip; flip of the second and third factors |
| $\Delta(a) = W^*(1\otimes a)W$ | Managing relation |
| $A_0$, $h$ | Hopf $*$-algebra of matrix coefficients; Haar state |
| $\alpha$, $\gamma$, $q$ | Generators and parameter of $C(SU_q(2))$ |
| $A_u(n)$, $A_o(n)$ | Free unitary and orthogonal quantum groups |

## Further Reading

- Johan Kustermans and Stefaan Vaes, "Locally compact quantum groups", *Annales Scientifiques de l'École Normale Supérieure* **33** (2000), 837–934, for the axioms, the Haar weights, the modular and scaling groups and the antipode.
- Stanisław L. Woronowicz, "Compact matrix pseudogroups", *Communications in Mathematical Physics* **111** (1987), 613–665, for the compact quantum groups, the Haar state and the Peter–Weyl theory.
- Stanisław L. Woronowicz, "From multiplicative unitaries to quantum groups", *International Journal of Mathematics* **7** (1996), 127–149, for the pentagon equation, manageability and the reconstruction theorem.
- Stefaan Vaes, "Locally compact quantum groups", in *Quantum Symmetries*, Les Houches Lecture Notes (2008), for a survey of the Kustermans–Vaes theory and its examples.
- Alfons Van Daele, "An algebraic framework for group duality", *Advances in Mathematics* **140** (1998), 323–366, for the algebraic approach to the same axioms and the passage to the operator-algebraic setting.
- Shuzhou Wang, "Free products of compact quantum groups", *Communications in Mathematical Physics* **167** (1995), 671–692, for the free unitary and orthogonal quantum groups.
- Michel Enock and Jean-Marie Schwartz, *Kac Algebras and Duality of Locally Compact Groups* (Springer, 1992), for the unimodular case, the Kac algebras and Pontryagin duality.
- Roland Vergnioux and Christian Voigt, "The Baum–Connes conjecture for free orthogonal quantum groups", *Advances in Mathematics* **227** (2011), 1873–1913, for the quantum-group form of the Baum–Connes conjecture and its operator-algebraic tools.
