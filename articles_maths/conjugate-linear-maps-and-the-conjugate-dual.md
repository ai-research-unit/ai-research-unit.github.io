# __Conjugate-Linear Maps and the Conjugate Dual__

## Introduction

Over a commutative ring $R$ with an involution $\varsigma$, the additive maps between $R$-modules come in two kinds: the $R$-linear ones and the $\varsigma$**-semilinear** ones, the maps with $f(\lambda x) = \varsigma(\lambda) f(x)$. The two kinds are not disjoint — a map may be both, as the graded-ring remark records — and the semilinear maps are exactly the maps of *Sesquialgebras* read at the level of the module, and they are what a sesquilinear structure needs: a product linear in one slot and $\varsigma$-semilinear in the other is built out of one linear slot and one semilinear slot, so the second slot must be seen by semilinear maps and not by linear ones.

This article develops the module theory of those maps and of the dual they define. The **conjugate dual** $M^{\varsigma*}$ is the module of the semilinear maps $M \to R$; it is the receiver of the pairings that are $\varsigma$-semilinear in one variable, just as the ordinary dual is the receiver of the pairings linear in both. The composition of two semilinear maps is linear, so the linear and semilinear endomorphisms together form a graded sum of the additive endomorphisms, a graded ring when the two parts meet only in $0$, and this parity is the skeleton of the whole article.

The treatment is module-theoretic: no topology, no norm and no form appear. The topological counterpart is *The Conjugate Dual of a Sesquialgebra*, and the linear theory that is imported at each step is *Modules*, *Linear Maps and Matrices* and *The Transpose of a Linear Map*. The conjugate module $M^{\varsigma}$, which is the same set with the twisted action $\lambda \cdot x = \varsigma(\lambda) x$, is defined in *Sesquialgebras* and is used throughout.

## The Conjugate-Linear Maps

### Definition and Elementary Properties

**Definition.** Let $M$ and $N$ be $R$-modules. A map $f : M \to N$ is $\varsigma$**-semilinear**, or **conjugate-linear**, when it is additive and

$$
f(\lambda x) = \varsigma(\lambda) f(x)
$$

for all $\lambda \in R$ and $x \in M$. The set of them is written $\operatorname{Hom}_{\varsigma}(M, N)$, and a semilinear map $M \to M$ is a **conjugate-linear endomorphism** of $M$.

**Proposition.** A semilinear map satisfies $f(0) = 0$ and $f(-x) = -f(x)$, and the semilinear maps $M \to N$ form an abelian group under pointwise addition.

**Proof.** Put $x = 0$ and $\lambda = 0$ for the first, $x = -x$ for the second, both as for a linear map; the sum of two additive maps is additive and satisfies the scalar rule because $\varsigma(\lambda)$ is a scalar, so the sum of two semilinear maps is semilinear, and the negative is semilinear likewise. $\square$

**Example (the involution).** The involution $\varsigma$ of $R$ is itself a $\varsigma$-semilinear map $R \to R$, since $\varsigma(\lambda\mu) = \varsigma(\mu)\varsigma(\lambda)$ with $R$ commutative gives $\varsigma(\lambda \mu) = \varsigma(\lambda)\varsigma(\mu)$; the semilinear maps therefore always exist, and $\varsigma$ is their model. Likewise the involution $x \mapsto x^{*}$ of a sesquialgebra is $\varsigma$-semilinear, and it is the semilinear map that the derived operation of *Sesquialgebras* uses in its second slot.

**Example (matrices).** On $M = N = \mathbb{C}^{n}$ with $\varsigma$ the conjugation, a semilinear map is a map of the form $z \mapsto A \bar{z}$ for a matrix $A$, where $\bar{z}$ is the coordinatewise conjugate. It is additive, and $f(\lambda z) = A \overline{\lambda z} = \bar{\lambda} A \bar{z} = \bar{\lambda} f(z)$; the semilinear maps $\mathbb{C}^{n} \to \mathbb{C}^{n}$ are therefore exactly the matrices acting on the conjugate coordinates, an $n^{2}$-dimensional family over $\mathbb{C}$.

### The Two Readings by Linear Maps

**Theorem.** For all $R$-modules $M, N$ there are natural isomorphisms of abelian groups

$$
\operatorname{Hom}_{\varsigma}(M, N) \;\cong\; \operatorname{Hom}_{R}(M^{\varsigma}, N) \;\cong\; \operatorname{Hom}_{R}(M, N^{\varsigma}).
$$

**Proof.** A semilinear $f : M \to N$ is additive, so it can be read on the same underlying set with the twisted action: $f(\lambda \cdot x) = f(\varsigma(\lambda) x) = \varsigma(\varsigma(\lambda)) f(x) = \lambda f(x)$, so $f$ is a linear map $M^{\varsigma} \to N$, and the reading is a bijection because it changes nothing but the action declared on the source. On the other side, $f(\lambda x) = \varsigma(\lambda) f(x) = \lambda \cdot f(x)$ says that the same $f$ is a linear map $M \to N^{\varsigma}$. Both readings are natural, a linear $M^{\varsigma} \to N$ being the same rule of assignment as a semilinear $M \to N$. $\square$

**Remark.** The theorem is the definitional reason the two kinds of map are not two unrelated notions: a semilinear map is a linear map with one conjugation on the source or on the target, and the choice of side is a bookkeeping convention, the two being identified by the conjugate module. It also gives the collapse: $\operatorname{Hom}_{\varsigma}(M,N) = \operatorname{Hom}_{R}(M,N)$ for $\varsigma = \mathrm{id}$, and in general a map that is both linear and semilinear satisfies $(\lambda - \varsigma(\lambda)) f = 0$ for every $\lambda$, so a **surjective** map with faithful target is both only when $\varsigma = \mathrm{id}$, which is the collapse of the entry article. Surjectivity cannot be dropped: the witness of the graded-ring remark below is a nonzero map with faithful target that is both, for a nontrivial involution.

### The Parity of a Composite

**Theorem (the parity rule).** Let $f : M \to N$ and $g : N \to P$ be $R$-linear or $\varsigma$-semilinear. Then

| $g$ | $f$ | $g \circ f$ |
|---|---|---|
| linear | linear | linear |
| linear | semilinear | semilinear |
| semilinear | linear | semilinear |
| semilinear | semilinear | linear |

**Proof.** Each case is one substitution. If $g$ and $f$ are semilinear, $(g \circ f)(\lambda x) = g(\varsigma(\lambda) f(x)) = \varsigma(\varsigma(\lambda)) g(f(x)) = \lambda (g \circ f)(x)$, using $\varsigma^{2} = \mathrm{id}$; the other three cases substitute only one $\varsigma$ and leave the other slot linear, or none at all. $\square$

**Corollary (the graded ring of endomorphisms).** On an $R$-module $M$, the linear endomorphisms form a subring $\operatorname{End}_{R}(M)$ of the additive endomorphisms, the conjugate-linear endomorphisms form the subgroup $\operatorname{End}_{\varsigma}(M)$, and the sum $\operatorname{End}_{R}(M) + \operatorname{End}_{\varsigma}(M)$ is a subring that is a $\mathbb{Z}/2$-graded ring with components $\operatorname{End}_{R}(M)$ and $\operatorname{End}_{\varsigma}(M)$ whenever the two components meet only in $0$. That happens when $\varsigma \neq \mathrm{id}$ and $R$ contains a $\lambda$ with $\varsigma(\lambda) - \lambda$ invertible — in particular when $\varsigma \neq \mathrm{id}$ and $R$ is a field — and the sum is then the direct sum $\operatorname{End}_{R}(M) \oplus \operatorname{End}_{\varsigma}(M)$.

**Proof.** The parity rule says the degree adds under composition, and by the table the sum is closed under addition and under composition, so it is a subring and the two given parts afford the grading as soon as their intersection is $0$. For the directness, a map that is both linear and semilinear satisfies $(\lambda - \varsigma(\lambda)) f = 0$ for every $\lambda$; if $\varsigma(\lambda) - \lambda$ is invertible this gives $f = 0$, so the intersection is $0$. $\square$

**Remark.** $\operatorname{End}_{\varsigma}(M)$ is not itself a ring: the composite of two odd elements is even, so the odd part is closed under addition and under left and right multiplication by the even part, which makes it a bimodule over $\operatorname{End}_{R}(M)$ and not a subring. The parity rule is the algebraic skeleton of every "signed" or "twisted" construction of the corpus: the graded action, the signed sandwich and the signed adjoint are all read on this $\mathbb{Z}/2$-grading of the operators, and the odd part is the part that a conjugate-linear map occupies.

**Remark (the intersection can be nonzero).** Without the invertibility the two components can meet, and the sum is then not direct. Take $R = \mathbb{Q}[\varepsilon]/(\varepsilon^{2})$ with $\varsigma(\varepsilon) = -\varepsilon$ and $M = N = R$, a faithful module. The map $f(x) = \varepsilon x$ is nonzero, and it is linear because $R$ is commutative while it is semilinear because $\varsigma(\lambda) - \lambda$ is a multiple of $\varepsilon$ and $\varepsilon^{2} = 0$; so $f$ lies in both $\operatorname{End}_{R}(M)$ and $\operatorname{End}_{\varsigma}(M)$. The failure is the same annihilator phenomenon as in *The Sesquilinear Product*: the involution is the identity only modulo the scalars that annihilate the module.

## The Module of Conjugate-Linear Maps

**Theorem.** $\operatorname{Hom}_{\varsigma}(M, N)$ is an $R$-module for the action $(\lambda \cdot f)(x) = \lambda f(x)$, the identification $\operatorname{Hom}_{\varsigma}(M, N) \cong \operatorname{Hom}_{R}(M^{\varsigma}, N)$ is an isomorphism of $R$-modules, and $\operatorname{Hom}_{\varsigma}(M, N)$ is a bimodule over $\operatorname{End}_{R}(N)$ and $\operatorname{End}_{R}(M)$ for the composition $\alpha f \beta$ with $\alpha \in \operatorname{End}_{R}(N)$ and $\beta \in \operatorname{End}_{R}(M)$.

**Proof.** The map $\lambda \cdot f$ is additive, and $(\lambda \cdot f)(\mu x) = \lambda f(\mu x) = \lambda \varsigma(\mu) f(x) = \varsigma(\mu) (\lambda \cdot f)(x)$, so it is semilinear; the module axioms are those of $N$ read pointwise, and $1 \cdot f = f$. The identification is the theorem above, and both sides carry the same pointwise action, so it is an isomorphism of modules. For the bimodule structure, $\alpha f \beta$ is linear in the outer maps and semilinear in the middle by the parity rule. $\square$

**Remark.** The action is the ordinary one on the target and the twisted one on the source: the module $\operatorname{Hom}_{\varsigma}(M,N)$ is the module $\operatorname{Hom}_{R}(M^{\varsigma},N)$ with its natural action, and reading it as $\operatorname{Hom}_{R}(M,N^{\varsigma})$ transfers the twist to the target instead. There is a single module, presented with the conjugation on whichever side is convenient, and the parity rule is what guarantees that the presentation is consistent.

## The Conjugate Dual

### Definition

**Definition.** Let $M$ be an $R$-module. The **ordinary dual** is $M^{*} = \operatorname{Hom}_{R}(M, R)$ and the **conjugate dual** is

$$
M^{\varsigma*} = \operatorname{Hom}_{\varsigma}(M, R),
$$

the semilinear maps of $M$ into the base ring read as an $R$-module.

**Theorem.** There are natural isomorphisms of $R$-modules

$$
M^{\varsigma*} \;\cong\; (M^{\varsigma})^{*}, \qquad (M^{\varsigma})^{\varsigma*} \;\cong\; M^{*},
$$

and $M^{\varsigma*} = M^{*}$ for $\varsigma = \mathrm{id}$.

**Proof.** The first is the two-readings theorem: a semilinear $M \to R$ is a linear $M^{\varsigma} \to R$. The second applies the first to the conjugate module, since $(M^{\varsigma})^{\varsigma} = M$; the third is the collapse. $\square$

**Remark (notation).** The conjugate dual is not the conjugate module. The conjugate module $M^{\varsigma}$ is the same module with the scalars twisted, and the conjugate dual $M^{\varsigma*}$ is a module of maps into $R$; they are different objects, they carry different symbols, and confusing them is the standard error of the subject. The conjugate dual of $M$ is the ordinary dual of $M^{\varsigma}$, so the two constructions are related by $M^{\varsigma*} \cong (M^{\varsigma})^{*}$; the relation is one-sided, a theorem and not a definition, and it does not say that conjugating and dualising commute: the conjugate of the ordinary dual $(M^{*})^{\varsigma}$ is a different module, identified with $(M^{\varsigma})^{*}$ only through a $\varsigma$-semilinear map and not through a linear one.

### The Pairing

**Theorem (the two pairings).** The evaluation $(f, x) \mapsto f(x)$ is an $R$-bilinear pairing $M^{\varsigma*} \times M^{\varsigma} \to R$; equivalently it is linear in the first variable and $\varsigma$-semilinear in the second, on $M^{\varsigma*} \times M$. Likewise the ordinary dual gives a pairing $M^{*} \times M \to R$ that is linear in both variables.

**Proof.** $\langle \lambda \cdot f, x \rangle = \lambda \langle f, x \rangle$ because the action on $M^{\varsigma*}$ is the pointwise one, and $\langle f, \lambda \cdot x \rangle = \langle f, \varsigma(\lambda) x \rangle = \varsigma(\varsigma(\lambda)) \langle f, x \rangle = \lambda \langle f, x \rangle$ on $M^{\varsigma}$, which is the $\varsigma$-semilinearity in the second variable when $M$ is read with its own action. The statement for the ordinary dual is the same computation with $\varsigma = \mathrm{id}$. $\square$

**Remark (why the ordinary dual does not see the second slot).** A pairing in which the second slot is $\varsigma$-semilinear cannot be built from the ordinary dual: a linear functional is linear in every variable it meets, so the pairing $M^{*} \times M \to R$ is linear in both slots and no functional of $M^{*}$ can produce the conjugated scalar that a sesquilinear product or a sesquilinear form requires in its second slot. The conjugate dual is exactly the receiver of that second kind of pairing: for every module $P$ there is a natural isomorphism between $\operatorname{Hom}_{R}(P, M^{\varsigma*})$ and the pairings $P \times M \to R$ that are linear in the first variable and $\varsigma$-semilinear in the second, sending a linear map $g$ to the pairing $(p, x) \mapsto g(p)(x)$. The asymmetry of the two slots, which the entry article records for the product, is at the level of the duals the statement that the two slots need two different duals.

### The Transpose of a Conjugate-Linear Map

**Theorem (the transpose flips the two duals).** Let $f : M \to N$ be $\varsigma$-semilinear. Then the pullback $g \mapsto g \circ f$ is a linear map

$$
f^{*} : N^{*} \to M^{\varsigma*}, \qquad f^{*} : N^{\varsigma*} \to M^{*},
$$

and the two assignments are the same rule on the two duals.

**Proof.** Take $g$ linear $N \to R$: then $(g \circ f)(\lambda x) = g(\varsigma(\lambda) f(x)) = \varsigma(\lambda) (g \circ f)(x)$, so $g \circ f$ is semilinear $M \to R$, an element of $M^{\varsigma*}$; this assignment is linear in $g$. Take $g$ semilinear $N \to R$: then $(g \circ f)(\lambda x) = g(\varsigma(\lambda) f(x)) = \varsigma(\varsigma(\lambda)) (g \circ f)(x) = \lambda (g \circ f)(x)$, so $g \circ f$ is linear, an element of $M^{*}$. $\square$

**Remark.** The transpose of a semilinear map therefore cannot stay on one dual: it exchanges the ordinary and the conjugate dual, because composing with a semilinear map flips the parity. This is the same parity flip as the transposed product of *The Sesquilinear Product*, read on the dual, and it is why the adjoint of a conjugate-linear operator in the operator theory of the category is a different construction from the adjoint of a linear one. The linear case, where the transpose of $M \to N$ is a map $N^{*} \to M^{*}$, is *The Transpose of a Linear Map*.

### The Double Conjugate Dual and the Evaluation

**Theorem (the evaluation is the evaluation of the conjugate module).** The canonical map

$$
\mathrm{ev} : M \longrightarrow (M^{\varsigma*})^{*}, \qquad \mathrm{ev}_{x}(f) = f(x),
$$

is $\varsigma$-semilinear, and under the identification $(M^{\varsigma*})^{*} \cong (M^{\varsigma})^{**}$ it is the ordinary evaluation $\mathrm{ev} : M^{\varsigma} \to (M^{\varsigma})^{**}$ of the conjugate module.

**Proof.** $\mathrm{ev}_{\lambda x}(f) = f(\lambda x) = \varsigma(\lambda) f(x) = \varsigma(\lambda) \mathrm{ev}_{x}(f)$, so $\mathrm{ev}$ is semilinear; and each $\mathrm{ev}_{x}$ is linear in $f$, so $\mathrm{ev}_{x} \in (M^{\varsigma*})^{*} = \operatorname{Hom}_{R}(M^{\varsigma*}, R)$. By the first isomorphism of the dual theorem, $M^{\varsigma*} \cong (M^{\varsigma})^{*}$, so $(M^{\varsigma*})^{*} \cong (M^{\varsigma})^{**}$, and $\mathrm{ev}$ becomes the map $x \mapsto (\text{evaluation at } x)$ for $M^{\varsigma}$, which is the ordinary evaluation. $\square$

**Corollary (reflexivity is inherited).** If the conjugate module is reflexive, that is if the ordinary evaluation $M^{\varsigma} \to (M^{\varsigma})^{**}$ is an isomorphism, then the evaluation $\mathrm{ev} : M^{\varsigma} \to (M^{\varsigma*})^{*}$ is an isomorphism as well.

**Proof.** By the dual theorem $M^{\varsigma*} \cong (M^{\varsigma})^{*}$, so $(M^{\varsigma*})^{*} \cong (M^{\varsigma})^{**}$, and the theorem above identifies $\mathrm{ev}$ with the ordinary evaluation of $M^{\varsigma}$ under this isomorphism. The two maps are therefore the same map of the same pair of modules, and reflexivity of $M^{\varsigma}$ is exactly the statement that it is an isomorphism. $\square$

**Remark.** The evaluation lives on the conjugate module and is only semilinear on $M$: read on $M$ it is semilinear, read on $M^{\varsigma}$ it is linear, and the two readings are the same map. The bookkeeping rule is that each conjugation flips the parity and two conjugations return it, so every natural map of the theory **out of $M$ into a construction carrying one conjugation** is semilinear on $M$ and linear on the conjugate module. The plain endomorphisms of $M$ are of course still linear on $M$ — the identity is the first of them — and it is the maps that meet the conjugate dual or the conjugate module that are forced to be semilinear.

## The Transport of a Structure

### Along a Conjugate-Linear Map

**Theorem (transport preserves the parity).** Let $A$ carry a $\varsigma$-sesquilinear product $\cdot_{A}$ and let $\varphi : A \to B$ be a $\varsigma$-semilinear bijection. Then the transported product

$$
x \cdot_{B} y = \varphi\bigl( \varphi^{-1}(x) \cdot_{A} \varphi^{-1}(y) \bigr)
$$

is a $\varsigma$-sesquilinear product on $B$ of the same parity as $\cdot_{A}$, linear in the first slot and $\varsigma$-semilinear in the second.

**Proof.** In the first slot, $\varphi^{-1}$ is semilinear and $\cdot_{A}$ is linear in its first variable, so their composite is semilinear, and $\varphi$ is semilinear, so the composite is linear. In the second slot, $\varphi^{-1}$ is semilinear and $\cdot_{A}$ is semilinear in its second variable, so the composite is linear, and $\varphi$ is semilinear, so the composite is semilinear. In each slot the variable passes through two semilinear steps and the parity rule applied twice returns the parity of the slot. $\square$

**Remark.** Transport by a conjugate-linear map does **not** reverse the parity, because each slot meets one $\varphi^{-1}$ and one $\varphi$ and the two conjugations cancel. What reverses the parity is the transposition of the product, $x \cdot y \mapsto y \cdot x$, which is the bilinear map $A^{\varsigma} \times A \to A$ of *The Sesquilinear Product* and the opposite algebra of *Sesquialgebras*: there the conjugate module comes into the first slot and the parity of the first slot is reversed.

### Conjugation as the Model

**Remark.** The identity map $M \to M^{\varsigma}$ is the universal semilinear map: it is the one that renames the scalars, every other semilinear map factoring through it by the two-readings theorem, and it is the reason the conjugate module is a functor and not merely a set. A **conjugate morphism** of sesquialgebras, in the sense of *Sesquialgebras*, is then exactly a morphism $A \to B^{\varsigma}$: the semilinear maps of this article are the underlying maps of the conjugate morphisms, and the parity rule is the statement that the composite of two conjugate morphisms is a morphism.

## Summary

Over a commutative ring $R$ with an involution $\varsigma$, the $\varsigma$-semilinear maps are the additive maps with $f(\lambda x) = \varsigma(\lambda) f(x)$; they are the linear maps of the conjugate module, $\operatorname{Hom}_{\varsigma}(M,N) \cong \operatorname{Hom}_{R}(M^{\varsigma},N) \cong \operatorname{Hom}_{R}(M,N^{\varsigma})$, and they form an $R$-module. Composition adds a parity: two linear maps give a linear map, one of each gives a semilinear map, and two semilinear maps give a linear map, so the linear and semilinear endomorphisms of $M$ together form a $\mathbb{Z}/2$-graded ring with the linear part even and the semilinear part odd, a direct sum when the two parts meet only in $0$ and not otherwise. The conjugate dual $M^{\varsigma*} = \operatorname{Hom}_{\varsigma}(M,R)$ is the ordinary dual of the conjugate module, $M^{\varsigma*} \cong (M^{\varsigma})^{*}$, and it is the receiver of the pairings linear in one variable and $\varsigma$-semilinear in the other, which the ordinary dual cannot see. The transpose of a semilinear map exchanges the two duals, because composing with it flips the parity, and the canonical map into the double conjugate dual is the ordinary evaluation of the conjugate module, semilinear on $M$ and linear on $M^{\varsigma}$. The parity is preserved by transporting a product along a conjugate-linear bijection and reversed by transposing it, so conjugation, duality and transposition are three distinct operations on the same parity bookkeeping.

## Summary of Notation

| symbol | meaning |
|---|---|
| $R$, $\varsigma$ | a commutative ring with $1$, and an involution of it |
| $f(\lambda x) = \varsigma(\lambda) f(x)$ | a $\varsigma$-semilinear, or conjugate-linear, map |
| $\operatorname{Hom}_{\varsigma}(M, N)$ | the $R$-module of the semilinear maps $M \to N$ |
| $M^{\varsigma}$ | the conjugate module, the same set with $\lambda \cdot x = \varsigma(\lambda) x$ |
| $M^{*}$ | the ordinary dual $\operatorname{Hom}_{R}(M, R)$ |
| $M^{\varsigma*}$ | the conjugate dual $\operatorname{Hom}_{\varsigma}(M, R) \cong (M^{\varsigma})^{*}$ |
| $\operatorname{End}_{R}(M) + \operatorname{End}_{\varsigma}(M)$ | the $\mathbb{Z}/2$-graded ring of the linear and semilinear endomorphisms (direct when the two parts meet only in $0$) |
| $f^{*}$ | the transpose, carrying $N^{*} \to M^{\varsigma*}$ and $N^{\varsigma*} \to M^{*}$ |
| $\mathrm{ev}_{x}(f) = f(x)$ | the evaluation into the double conjugate dual |

## Further Reading

- N. Bourbaki, *Algebra I: Chapters 1–3* (Springer, 1989), for the semilinear maps of a module over a ring with an involution, and the reading of a semilinear map as a linear map on one side or the other.
- Nathan Jacobson, *Structure of Rings* (American Mathematical Society, 1956), for the involution of a ring and the conjugate-linear maps and duals that it produces over such a ring.
- Sterling K. Berberian, *Baer \*-Rings* (Springer, 1972), for the module theory of an involution ring, the Hermitian and the sesquilinear forms read on the conjugate module, and the conjugate dual as the receiver of a semilinear pairing.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the semilinear maps of an algebra with involution and the transport of a structure along a conjugate-linear isomorphism.
