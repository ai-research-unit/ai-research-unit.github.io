# __The Continuity of the Involution__

## Introduction

A sesqualgebra over the datum $(R,\varsigma)$ carries two order-two maps, the involution $\varsigma$ of the base ring and, when its product is read as a derived operation $x \star y = xy^{*}$, the involution $*$ of the algebra. The entry of the category, *Topological Sesqualgebras*, takes the datum $(R,\varsigma)$ involutive, that is $\varsigma$ continuous, and the product separately continuous, which in the derived-operation model is the continuity of $*$; the two assumptions do all the work of the layer, $\varsigma$ continuous being what makes the twisted action $\lambda \cdot x = \varsigma(\lambda)x$ continuous and the conjugate module $A^{\varsigma}$ a topological module, and $*$ continuous being what makes the derived operation inherit the continuity of the algebra product. This article separates the two maps, because they behave differently. Continuity of $\varsigma$ is a genuine restriction on the datum, and it is not free. Continuity of $*$ is free in the cases the bilinear layer has recorded, the $\mathrm{C}^*$-case first among them.

The two are not interchangeable and neither implies the other. The base involution is a map of $R$ alone, and its failure is invisible to an algebraic reading of the layer: on $\mathbb{Q}(\sqrt{2})$ with the topology inherited from $\mathbb{R}$ the conjugation is an involution of the field and it is discontinuous, so that the field, read as a module over itself with the twisted action, is a sesqualgebra algebraically whose conjugate module is not a topological module. The algebra involution is a map of $A$, and its failure is a failure of the product: on $\mathbb{R}[x]$ with the $(x)$-adic topology the substitution $f(x) \mapsto f(b-x)$ is an involution of the algebra for every $b$, it is continuous only for $b = 0$, and the derived operation $x \star y = x\sigma_b(y)$ over $(\mathbb{R},\mathrm{id})$ is therefore a sesquilinear product that is not separately continuous in its second slot for $b \neq 0$. Each failure gives a sesqualgebra which is not an object of the layer, and the two examples are the reason the hypotheses are stated rather than assumed.

The article proves that the twisted action is continuous exactly when $\varsigma$ is, under the one hypothesis that makes the converse run, that the scalar map $\lambda \mapsto \lambda x$ be a topological embedding for some $x$; it records the continuity criteria of the bilinear layer rather than reproving them; it gives the normal form by which an algebra with a continuous involution is read with an isometric one, $\lVert x\rVert_{*} = \max(\lVert x\rVert,\lVert x^{*}\rVert)$; and it reads the two continuity questions through the collapse, where they become the single question of *Involutive Topological Algebras*. The normed and complete objects are *Banach Sesqualgebras*, the spectral radius and the $\mathrm{C}^*$-identity read on the layer are *The Continuous Involution and the Spectral Radius*, the completions *The Completion of a Sesqualgebra*, the locally convex case *Fréchet and Locally Convex Sesqualgebras*, the conjugate dual *The Conjugate Dual of a Sesqualgebra*, and the base alone is *Involutive Topological Rings and Fields* and *Involutive Topological Linear Spaces*. Throughout, $R$ is a commutative topological ring with $1$, $\varsigma$ an involution of $R$, $A$ a topological $R$-module, $A^{\varsigma}$ the conjugate module of *Sesqualgebras*, §*The Conjugate Module*, and $*$ a $\varsigma$-semilinear involution of an associative $R$-algebra $A$, $(xy)^{*} = y^{*}x^{*}$, $*^2 = \mathrm{id}$, $(\lambda x)^{*} = \varsigma(\lambda)x^{*}$.

## The Two Involutions of the Layer

### The Scalar Involution

**Definition.** An **involutive topological ring** is a topological ring $R$ with a continuous involution $\varsigma$, an additive map with $\varsigma(1) = 1$, $\varsigma(ab) = \varsigma(b)\varsigma(a)$ and $\varsigma^{2} = \mathrm{id}$; the notion, the closed fixed subring $R^{\varsigma}$ and the $I$-adic criterion are *Involutive Topological Rings and Fields*, §*Continuous Involutions*. In the layer the datum is the pair $(R,\varsigma)$ with $\varsigma$ continuous, and the entry *Topological Sesqualgebras* states this as a standing hypothesis, §*The Definition*.

**Proposition (continuity at the origin).** Let $\varphi : M \to N$ be an additive map of topological groups. Then $\varphi$ is continuous if and only if it is continuous at $0$; applied to the layer, $\varsigma$ is continuous if and only if it is continuous at $0$, and the same holds for $*$.

*Proof.* If $\varphi$ is continuous at $0$ and $a \in M$, then $\varphi(a + U) \subseteq \varphi(a) + \varphi(U)$ for every neighbourhood $U$ of $0$, because $\varphi$ is additive, so continuity at $a$ follows from continuity at $0$; the converse is immediate. $\square$

**Theorem (the twisted action).** Let $A$ be a topological $R$-module and suppose $\varsigma$ continuous. Then the twisted action

$$
R \times A \longrightarrow A, \qquad (\lambda,x) \longmapsto \lambda \cdot x = \varsigma(\lambda)x,
$$

is continuous, so $A^{\varsigma}$ is a topological $R$-module; the identity map $A \to A^{\varsigma}$ is a homeomorphism of the additive topological groups, it is an isomorphism of topological $R$-modules exactly when $\varsigma = \mathrm{id}$, and in general it is a $\varsigma$-semilinear homeomorphism.

*Proof.* The twisted action is the composite of the continuous map $(\lambda,x) \mapsto (\varsigma(\lambda),x)$ of $R \times A$ with the continuous scalar action of $R$ on $A$; hence it is continuous, and the module axioms of $A^{\varsigma}$ are those of *Sesqualgebras*, §*The Conjugate Module*. The identity is a bijection carrying the additive topology of $A$ to that of $A^{\varsigma}$, the two modules sharing the underlying abelian topological group, so it is a homeomorphism; it is $R$-linear exactly when $\varsigma(\lambda)x = \lambda x$ for every $\lambda$ and $x$, which for a module with $\lambda \mapsto \lambda x$ injective for some $x$ is $\varsigma = \mathrm{id}$, and it is $\varsigma$-semilinear in general, $\lambda \cdot x = \varsigma(\lambda)x$ being the definition of the twisted action. $\square$

**Theorem (the converse).** Let $A$ be a topological $R$-module and suppose that there is $x \in A$ for which the scalar map

$$
R \longrightarrow A, \qquad \lambda \longmapsto \lambda x
$$

is a topological embedding. Then the twisted action is continuous if and only if $\varsigma$ is continuous.

*Proof.* If $\varsigma$ is continuous the twisted action is continuous by the theorem above. Conversely, suppose the twisted action continuous; fixing the same $x$, the map $\lambda \mapsto \varsigma(\lambda)x$ is the composite of $\lambda \mapsto (\lambda,x)$ with the twisted action, hence continuous. The map $\lambda \mapsto \lambda x$ is a topological embedding, so its inverse, defined on the image $Rx$, is continuous; the two maps take their values in $Rx$ and $x$ generates it as an $R$-module, so $\varsigma(\lambda)x = \varsigma(\lambda')x$ implies $\lambda = \lambda'$ and the map $\lambda \mapsto \varsigma(\lambda)$ is the composite of the continuous map $\lambda \mapsto \varsigma(\lambda)x$ with the inverse of the embedding, hence continuous. $\square$

**Remark (the models of the hypothesis).** The embedding hypothesis holds in the cases the layer uses. If $A$ is a topological algebra over a complete valued field $\mathbb{K}$ with $1 \neq 0$, then $\lambda \mapsto \lambda \cdot 1$ is a linear isomorphism of $\mathbb{K}$ onto the one-dimensional subspace $\mathbb{K} \cdot 1$, and a finite-dimensional subspace of a Hausdorff topological vector space over a complete valued field carries the canonical topology, by *Topological Modules and Vector Spaces*, §*Topological Vector Spaces*; so the hypothesis is automatic for a unital topological algebra over $\mathbb{R}$ or $\mathbb{C}$, and in particular for every object of the layer whose base is such a field. It can fail for a base whose scalar action is degenerate, and then only the direct implication of the theorem is available.

**Remark (the commutativity of $R$ is used).** The twisted action is an action of $R$ and not of $R^{\mathrm{op}}$ because $R$ is commutative. The verification is $\lambda \cdot (\mu \cdot x) = \varsigma(\lambda)\varsigma(\mu)x = \varsigma(\mu\lambda)x = (\mu\lambda) \cdot x = (\lambda\mu) \cdot x$, the middle equality being the multiplicativity of $\varsigma$ read backwards and the last the commutativity of the ring; over a noncommutative ring the same computation produces the action of the opposite ring, since $\varsigma(\mu\lambda) \neq \varsigma(\lambda\mu)$ as soon as $\mu\lambda \neq \lambda\mu$, and the twisted action is then not an action at all in the sense of the layer. The datum of the layer is therefore a *commutative* involutive topological ring, and the word is load bearing.

### The Algebra Involution

**Definition.** A **topological involution** of a topological $R$-algebra $A$, relative to the involution $\varsigma$ of $R$, is a $\varsigma$-semilinear involution $*$ of $A$ that is continuous for the topology; the notion, its continuity criteria and the topological theory of the symmetric and skew parts are *Involutive Topological Algebras*, §*Definition and First Properties* and §*The Criterion*. The layer uses it through the derived operation of *Sesqualgebras*, §*The Derived Operation of an Involutive Algebra*.

**Proposition (the derived operation inherits the continuity).** Let $A$ be a topological $R$-algebra whose product is separately continuous and let $*$ be a continuous $\varsigma$-semilinear involution. Then the derived operation

$$
A \times A \longrightarrow A, \qquad (x,y) \longmapsto x \star y = xy^{*}
$$

is separately continuous. More precisely, the map $(x,y) \mapsto xy^{*}$ is the composite of $(\mathrm{id},*)$ with the product, it is continuous in $x$ for fixed $y$ because the product is, it is continuous in $y$ for fixed $x$ because $*$ is, and it is jointly continuous as soon as the product is.

*Proof.* The right multiplication of the derived operation is $R^{\star}_{a}(x) = x \star a = xa^{*}$, which is the right multiplication $R_{a^{*}}$ of the algebra and is continuous for fixed $a$ by the separate continuity of the product; the left multiplication is $L^{\star}_{a}(x) = a \star x = ax^{*}$, the composite of $*$ with the left multiplication $L_{a}$, hence continuous for fixed $a$ when $*$ is; joint continuity is inherited because $(\mathrm{id},*)$ is continuous and the product is. $\square$

**Proposition (the second scalar rule is the twisted action).** Let $A$ be a sesqualgebra over $(R,\varsigma)$ whose product is separately continuous and let $A^{\varsigma}$ carry the topology of $A$. Then the continuity of the product in its second slot is the continuity of the bilinear map

$$
A \times A^{\varsigma} \longrightarrow A, \qquad (x,y) \longmapsto xy,
$$

of *Topological Sesqualgebras*, §*The Two Slots*; the two statements are the same statement, because the scalar action of $A^{\varsigma}$ is the twisted action.

*Proof.* The second scalar rule reads $x(\lambda y) = \varsigma(\lambda)(xy)$; the map $(\lambda,y) \mapsto \lambda \cdot y = \varsigma(\lambda)y$ is the twisted action, and the product's continuity in the second variable is the continuity of the composite of that action with the product. The bilinear map on the pair is the product read with the conjugate module in the second factor, and the two differ only in which scalars act, so the continuity claims coincide. $\square$

**Remark.** The two propositions are the whole of what the algebra involution does for the layer. It never enters the first scalar rule, which is $R$-linear and reads on $A$ alone; it enters the definition of the product of the derived operation, where it is the second slot, and it enters the operator theory, where the left multiplications are $\varsigma$-semilinear and the right ones linear, as *Sesqualgebras*, §*The Left and the Right Multiplication*, records. The form layer and the operator theory of the category assume its continuity and state it as a hypothesis, *Topological Sesqualgebras with a Form*, §*The Definition*, and *Bounded Operators on a Sesqualgebra*.

## Continuity Criteria

### Continuity at the Origin

**Remark (what the bilinear layer proves, and what this article uses).** The continuity criteria for an involution of a topological algebra are proved once, in *Involutive Topological Algebras*: an involution of a topological algebra is continuous exactly when it is continuous at $0$; for a linear topology with the two-sided ideals $I_0 \supseteq I_1 \supseteq \cdots$ it is continuous exactly when for every $n$ there is $m$ with $\sigma(I_m) \subseteq I_n$, a cofinal family of stable ideals $J_n = I_n \cap \sigma(I_n)$ may always be used, and for the $I$-adic topology of a two-sided ideal $I$ the criterion is $\sigma(I)^{m} \subseteq I$ for some $m$, which holds with $m = 1$ when $\sigma(I) = I$. The semilinear case is the same criterion read on the $\varsigma$-semilinear map, and the finite-dimensional case is the theorem of that article's §*The Semilinear Case and the Fixed Field*: over a complete valued field a semilinear involution of a finite-dimensional algebra is continuous exactly when the involution of the scalars is. The layer adds nothing to the criterion and cites it, the base involution $\varsigma$ being the ring-level case of *Involutive Topological Rings and Fields*, §*The Criterion*.

**Corollary (the criteria read on the layer).** A sesqualgebra over $(R,\varsigma)$ whose base topology is linear with the ideals $I_n$ is an object of the layer as far as its base is concerned exactly when for every $n$ there is $m$ with $\varsigma(I_m) \subseteq I_n$; and if $R$ is the polynomial ring $\mathbb{R}[x]$ with the $(x)$-adic topology then the linear involutions $\varsigma_b$ of the example below are continuous exactly for $b = 0$.

*Proof.* The first clause is the criterion applied to the additive map $\varsigma$ of the topological ring $R$, whose topology is linear with the ideals $I_n$; the second is the computation of the example. $\square$

### The $\mathrm{C}^{*}$-Condition

**Theorem (the involution of a $\mathrm{C}^{*}$-algebra is isometric).** Let $A$ be a $\mathrm{C}^{*}$-algebra, with the $\mathrm{C}^{*}$-identity $\lVert a^{*}a\rVert = \lVert a\rVert^{2}$. Then $\lVert a^{*}\rVert = \lVert a\rVert$ for every $a$, so the involution is isometric and therefore continuous, with $\lVert *\rVert = 1$.

*Proof.* The identity gives $\lVert a\rVert^{2} = \lVert a^{*}a\rVert \leq \lVert a^{*}\rVert\lVert a\rVert$, hence $\lVert a\rVert \leq \lVert a^{*}\rVert$ for $a \neq 0$ and trivially for $a = 0$; the same inequality applied to $a^{*}$, whose adjoint is $a$, gives the reverse, so the two norms are equal. An isometry is continuous, and the norm of the involution is one by the definition of the operator norm. $\square$

**Remark (the position of the theorem in the layer).** The $\mathrm{C}^{*}$-identity is the one hypothesis that removes the continuity of the algebra involution from the list of assumptions: on a $\mathrm{C}^{*}$-algebra the involution is continuous not by hypothesis but by the identity, and the topology itself is a function of the involution, so a $\mathrm{C}^{*}$-algebra is an object of the layer with the continuity of $*$ free. The statement belongs to *Involutive Banach Algebras and the Gelfand–Naimark Theorem*, §*Involutive Banach Algebras*, and to *The Involution and the Spectral Radius*, §*The Identities*, where the norm is recovered as $\lVert a\rVert = r(a^{*}a)^{1/2}$ from the involutive algebra alone; the normed objects of this category, the submultiplicative norm of the layer and the completeness, are *Banach Sesqualgebras*, and the spectral reading of the continuity is *The Continuous Involution and the Spectral Radius*. This article uses the isometry and no more.

### The Normal Form of a Continuous Involution

**Theorem (the isometric normal form).** Let $A$ be an associative algebra with a submultiplicative norm $\lVert\cdot\rVert$ and an involution $*$, and put

$$
\lVert x\rVert_{*} = \max\bigl(\lVert x\rVert, \lVert x^{*}\rVert\bigr) .
$$

Then $\lVert\cdot\rVert_{*}$ is a norm on $A$, it is equivalent to $\lVert\cdot\rVert$ as soon as $*$ is continuous for $\lVert\cdot\rVert$, it is submultiplicative, and the involution is isometric for it, $\lVert x^{*}\rVert_{*} = \lVert x\rVert_{*}$. Consequently an algebra with a continuous involution may always be read with an isometric one, and the $\mathrm{C}^{*}$-identity is the sharp case of the construction.

*Proof.* The maximum of two norms is a norm: it is positive definite because $\lVert x\rVert_{*}=0$ gives $\lVert x\rVert = 0$, homogeneous because both terms are, and subadditive because the maximum of two subadditive functions is subadditive. If $*$ is continuous with $\lVert *\rVert = C$ then $\lVert x^{*}\rVert \leq C\lVert x\rVert$, so $\lVert x\rVert \leq \lVert x\rVert_{*} \leq \max(1,C)\lVert x\rVert$, which is the equivalence. Submultiplicativity is

$$
\lVert xy\rVert_{*} = \max\bigl(\lVert xy\rVert, \lVert (xy)^{*}\rVert\bigr)
= \max\bigl(\lVert xy\rVert, \lVert y^{*}x^{*}\rVert\bigr)
\leq \max\bigl(\lVert x\rVert\lVert y\rVert, \lVert y^{*}\rVert\lVert x^{*}\rVert\bigr)
\leq \lVert x\rVert_{*}\lVert y\rVert_{*} ,
$$

the middle equality being $(xy)^{*} = y^{*}x^{*}$ and the first inequality the submultiplicativity of the original norm; the last inequality holds because $\lVert x\rVert\lVert y\rVert \leq \lVert x\rVert_{*}\lVert y\rVert_{*}$ and $\lVert y^{*}\rVert\lVert x^{*}\rVert \leq \lVert y\rVert_{*}\lVert x\rVert_{*} = \lVert x\rVert_{*}\lVert y\rVert_{*}$, so that the larger of the two is also at most the product. The involution is isometric because $\lVert x^{*}\rVert_{*} = \max(\lVert x^{*}\rVert,\lVert x\rVert) = \lVert x\rVert_{*}$, the two entries of the maximum being exchanged. $\square$

**Remark.** The normal form is not a change of object: it is the same algebra with an equivalent topology, and it is the reason the sesquilinear layer may state its normed axioms with an isometric involution without loss of generality, which is what *Banach Sesqualgebras* does. When the involution is already isometric, as in a $\mathrm{C}^{*}$-algebra or for the transpose on the matrices with the operator norm, the two norms agree; when it is not, the normal form is strictly larger, and the matrix algebra with a norm conjugated by an invertible matrix is the cheapest witness, for a real conjugating matrix $T$ the transpose is isometric for the conjugated norm exactly when $TT^{T} = cI$ with $c > 0$, which is the same as $T$ orthogonal up to a scalar; over $\mathbb{C}$ the condition is weaker, $T = \mathrm{diag}(1,i)$ being isometric although $TT^{T} = \mathrm{diag}(1,-1)$ is not a scalar, so the real case is the one the example uses.

### Automatic Continuity and Its Failure

**Remark (what is free).** Continuity of an involution is free in the following cases, all recorded in the bilinear layer: for the identity; for every involution of a topological algebra that preserves the ideals of a linear topology, by the criterion; for every involution in finite dimension over a complete valued field; for the involution of a $\mathrm{C}^{*}$-algebra, by the isometry above; and for every map when the topology is discrete or indiscrete. It is not free in general, and the two failures below are the ones the layer displays. The statement is *Involutive Topological Algebras*, §*The Two Kinds, and What the Topology Sees* and §*What the Topology Adds*, read on the semilinear map.

**Example (a discontinuous involution of the base, verdict: the conjugate module is not a topological module).** Let $F = \mathbb{Q}(\sqrt{2})$ with the topology inherited from $\mathbb{R}$, a valued field which is not complete, and let $\varsigma$ be the conjugation $a + b\sqrt{2} \mapsto a - b\sqrt{2}$. The rationals converge to $\sqrt{2}$ in the induced topology and are fixed by $\varsigma$, so the image of the limit would have to be both $\sqrt{2}$ and $-\sqrt{2}$; hence $\varsigma$ is discontinuous, as *Involutive Topological Algebras*, §*The Semilinear Case and the Fixed Field*, records. Read on the layer with $A = F$ and the module structure of the field, the map $\lambda \mapsto \lambda \cdot 1 = \varsigma(\lambda)$ is the twisted action at $1$, and it is discontinuous: the twisted action fails, the conjugate module $F^{\varsigma}$ is not a topological $F$-module, and the product of the sesqualgebra $\mathbb{Q}(\sqrt{2})$ with the derived operation of the conjugation, whose second slot carries the twisted action, is not separately continuous in that slot. The object is a sesqualgebra algebraically and it is not an object of the topological layer; the failure is the reason the datum of the layer carries $\varsigma$ continuous.

**Example (a discontinuous involution of the algebra, verdict: the derived operation is not separately continuous).** Let $A = \mathbb{R}[x]$ with the $(x)$-adic topology, whose ideals $(x)^{n}$ are two-sided, and for $b \in \mathbb{R}$ let $\sigma_b$ be the substitution $\sigma_b(f)(x) = f(b-x)$; it is a $\varsigma$-linear involution of the algebra for $\varsigma = \mathrm{id}$, a ring homomorphism because $x \mapsto b-x$ is one, and of order two because $x \mapsto b-x$ is, the algebra being commutative so that the reversal of the product costs nothing. The substitution is continuous exactly for $b = 0$: the image of the ideal $(x)$ is the ideal $(b-x)$, whose $m$-th power $(b-x)^{m}$ has the nonzero constant term $b^{m}$ for $b \neq 0$, so $\sigma_b((x))^{m} \not\subseteq (x)$ for every $m$ and the $I$-adic criterion fails, while for $b = 0$ the ideal $(x)$ is preserved. Now read the layer over $(\mathbb{R},\mathrm{id})$, where the involution of the base is the identity and is free, and take the derived operation

$$
x \star y = x\,\sigma_b(y) .
$$

This is a $\mathbb{R}$-bilinear product, so it is a sesqualgebra over the trivial datum, and its second slot is the substitution: for $b \neq 0$ the right multiplication $x \mapsto x \star f = x\sigma_b(f)$ is not continuous, since $\sigma_b$ is not, and the product is not separately continuous. The verdict is that the algebraic sesquilinear structure is not an object of the layer although its base involution is trivial, which shows that the continuity of $*$ is not a consequence of the continuity of $\varsigma$.

**Remark (what is not claimed).** The article does not assert that the involution of a general Banach $*$-algebra is automatically continuous: the cases above are the ones in which continuity is free, and outside them the continuity of $*$ is a hypothesis of the layer, assumed in the definition of an object and verified case by case, as in *Banach Sesqualgebras*. What is unconditional is the normal form of §*The Normal Form of a Continuous Involution*, which shows that whenever the involution is continuous it may be replaced, without changing the topology, by an isometric one; equivalently, a Banach $*$-algebra with a continuous involution is a Banach $*$-algebra with an isometric involution in an equivalent norm. The spectral consequences of that replacement are *The Continuous Involution and the Spectral Radius*.

**Remark (the two failures are independent).** The first example has $\varsigma$ discontinuous with the algebra involution absent, the second has $\varsigma = \mathrm{id}$ and $*$ discontinuous, so neither continuity hypothesis implies the other, and the layer states both. A discrete or indiscrete base has both free, and there the two hypotheses are vacuous; over a finite ring with the discrete topology every map is continuous, by *Topological Algebras and Banach Algebras*, §*Topological Algebras*, so the layer's hypotheses are automatic for the finite models.

## The Conjugate Module Read Topologically

### The Topological Module

**Theorem.** Let $A$ be a topological $R$-module with a scalar map $\lambda \mapsto \lambda x$ a topological embedding for some $x$, and let $\varsigma$ be an involution of $R$. Then the conjugate module $A^{\varsigma}$ is a topological $R$-module if and only if $\varsigma$ is continuous. When it is, the additive topological groups of $A$ and $A^{\varsigma}$ coincide, the identity is a homeomorphism, and it is $R$-linear exactly when $\varsigma = \mathrm{id}$.

*Proof.* The three assertions are the two theorems of §*The Scalar Involution*, read together: the topological module structure of $A^{\varsigma}$ is the continuity of the twisted action, which is equivalent to the continuity of $\varsigma$ under the embedding hypothesis; the additive group is the same because the twisted action changes the scalars and not the addition; and the identity is $R$-linear exactly when the two actions agree. $\square$

**Remark (conjugation as an operation of the layer).** The conjugation $A \mapsto A^{\varsigma}$ is of order two on the objects, $(A^{\varsigma})^{\varsigma} = A$, and it does not change the underlying additive topological group: the two objects are the same topological space with two module structures, and the layer works with the pair $(A,A^{\varsigma})$ rather than with a single module, which is why its theorems are stated for the product on the pair. *Sesqualgebras*, §*The Conjugate Module*, records the algebraic statement; the topological reading adds that the conjugation preserves the topology, so that the two objects have the same continuous maps on their additive groups, and the two readings differ exactly by the continuity of $\varsigma$.

### The Product on the Pair

**Theorem (the product is a continuous bilinear map on the pair).** Let $A$ be a sesqualgebra over $(R,\varsigma)$ whose product is separately continuous and suppose $\varsigma$ continuous. Then the product, read as a map

$$
A \times A^{\varsigma} \longrightarrow A, \qquad (x,y) \longmapsto xy ,
$$

is $R$-bilinear and separately continuous, and it is jointly continuous as soon as the product is.

*Proof.* The bilinearity is the theorem of *Sesqualgebras*, §*The Conjugate Module*, which identifies the two scalar rules with the bilinearity of the product on the pair; the continuity in the first variable is the continuity of the product of $A$ in its first variable, and the continuity in the second is the continuity of the twisted action followed by the product, by §*The Algebra Involution* above. $\square$

**Remark.** The theorem is the reason the layer states the continuity of the product in the second slot as a hypothesis on the *action*: with $\varsigma$ continuous and the product of the algebra separately continuous, both slots are continuous and the object is a topological sesqualgebra; with $\varsigma$ discontinuous the second slot is not continuous although the product of the algebra is, and the failure is invisible from $A$ alone.

### The Morphisms

**Remark (conjugate morphisms).** A conjugate morphism $A \to B$ is a $\varsigma$-semilinear multiplicative map, and it is exactly a morphism $A \to B^{\varsigma}$ of *Sesqualgebras*, §*Morphisms*; read topologically, it is continuous exactly when its underlying additive map is, the semilinearity being carried by the twisted actions of the two modules, and its continuity criterion is that of *Involutive Topological Algebras*, §*Definition and First Properties*, applied to the map. The distinction between the morphisms and the conjugate morphisms is therefore a distinction between two objects of the layer, $B$ and $B^{\varsigma}$, and it vanishes at $\varsigma = \mathrm{id}$.

## The Collapse at the Trivial Involution

### The Reduction

**Theorem (the collapse of the two questions into one).** Let $A$ be a sesqualgebra over $(R,\varsigma)$ with $\varsigma = \mathrm{id}$. Then the twisted action is the ordinary action, $A^{\varsigma} = A$ as topological $R$-module, the identity $A \to A^{\varsigma}$ is $R$-linear, the product on the pair is the product of $A$, and the continuity of the base involution is automatic. The layer is then the layer of *Topological Algebras and Banach Algebras* with a continuous involution, and the only continuity question left is the continuity of $*$, which is the question of *Involutive Topological Algebras*. If in addition $* = \mathrm{id}$ then both maps are the identity and no continuity hypothesis is left.

*Proof.* At $\varsigma = \mathrm{id}$ the twisted action is $\lambda \cdot x = \lambda x$, so the conjugate module is the module, the twisted action is the scalar action and is continuous by the axioms of a topological module, the product on the pair is the product of $A$, and $\varsigma$ is the identity map, which is continuous. The remaining assertions are the identification of the objects with those of *Topological Algebras and Banach Algebras*, §*Topological Algebras*, and the collapse theorem of *Topological Sesqualgebras*, §*The Collapse*. $\square$

**Remark.** The theorem is the reason the article is about the nontrivial involution. At $\varsigma = \mathrm{id}$ the continuity of the base is free and there is one question; with $\varsigma$ nontrivial there are two, and the second one, the twisted action, is the genuinely new hypothesis of the sesquilinear layer. The collapse is also the check on the statements above: each of them reduces to a statement of the bilinear layer at $\varsigma = \mathrm{id}$, the normal form reducing to the trivial bound, the twisted-action theorem to the continuity of the scalar action, and the product theorem to the bilinear product of the algebra.

## Examples

### The Matrix Models

**Example (the complex matrices, verdict: two continuous involutions, the algebra one isometric).** Let $R = \mathbb{C}$ with the conjugation $\varsigma$, $A = M_n(\mathbb{C})$ with the entrywise topology, the conjugate transpose $*$ and the operator norm. The base involution is continuous, so the twisted action $\lambda \cdot X = \bar\lambda X$ is continuous and the conjugate module is a topological module; the algebra involution is continuous because the entrywise topology is finite-dimensional, and it is isometric for the operator norm, $\lVert X^{*}\rVert = \lVert X\rVert$, and satisfies the $\mathrm{C}^{*}$-identity $\lVert X^{*}X\rVert = \lVert X\rVert^{2}$, so the continuity of $*$ is free in the sharp sense. The verdict: an object of the layer with both hypotheses automatic, and the model on which the derived operation $S \star T = ST^{*}$ of *Sesqualgebras*, §*Examples*, is read.

**Example (the linear involution that is continuous and not isometric, verdict: the normal form is needed).** Let $A = M_n(\mathbb{R})$ with the involution the transpose and the norm $\lVert X\rVert_{T} = \lVert TXT^{-1}\rVert$ for the operator norm and an invertible real $T$. The norm is submultiplicative, the involution is continuous, being linear in finite dimension, and it is isometric for $\lVert\cdot\rVert_{T}$ only when $T$ is orthogonal up to a scalar. The normal form $\max(\lVert X\rVert_{T},\lVert X^{\mathsf{T}}\rVert_{T})$ is then strictly larger and the involution is isometric for it; the example is the witness that a continuous involution need not be isometric and that the construction of §*The Normal Form of a Continuous Involution* is not vacuous. Both norms define the same topology and hence the same layer, which is the content of the theorem.

### The Analytic Models

**Example (the function algebra, verdict: a continuous antilinear involution).** Let $A = C(X,\mathbb{C})$ for a compact Hausdorff space $X$, with the sup norm, the involution $\sigma(f) = \bar f$ relative to the conjugation of the scalars, and the twisted action $\lambda \cdot f = \bar\lambda f$. The involution is isometric, $\lVert\bar f\rVert_{\infty} = \lVert f\rVert_{\infty}$, and the $\mathrm{C}^{*}$-identity holds pointwise, so it is an object of the layer with $*$ free; the fixed part is $C(X,\mathbb{R})$, and the conjugate module is the same algebra with the conjugate scalar action, by the theorem of §*The Conjugate Module Read Topologically*.

**Example (the convolution algebra, verdict: isometric involution without the $\mathrm{C}^{*}$-identity).** Let $G$ be a locally compact group and let $A = L^{1}(G)$ with the convolution product, the involution $f^{*}(x) = \overline{f(x^{-1})}\Delta(x)^{-1}$ and the $L^{1}$-norm. The involution is isometric, $\lVert f^{*}\rVert_{1} = \lVert f\rVert_{1}$, hence continuous, and for $G = \mathbb{R}$ the norm is not a $\mathrm{C}^{*}$-norm, the $\mathrm{C}^{*}$-identity failing, which is the case worked in *The Involution and the Spectral Radius*, §*Examples*. The verdict: the continuity of the algebra involution may come from an isometry which is not a $\mathrm{C}^{*}$-identity, so the layer's hypothesis is strictly weaker than the $\mathrm{C}^{*}$-case; the group algebra is *Group Algebras*, and the normed objects of the layer are *Banach Sesqualgebras*.

### The Base

**Example (the discrete base, verdict: both hypotheses vacuous).** Let $R$ be a finite ring with the discrete topology and let $A$ be a finite module over it, with any involution $\varsigma$ and any involution $*$. Every map of a discrete space is continuous, so both involutions are continuous, the twisted action is continuous and the conjugate module is a topological module; the layer there is the algebraic layer with a topology that sees nothing, and it is the reason the examples above use the $(x)$-adic and the induced-$\mathbb{R}$ topologies rather than a discrete one.

## Summary

A sesqualgebra over $(R,\varsigma)$ carries two order-two maps and the layer assumes both continuous, for different reasons. Continuity of the base involution $\varsigma$ makes the twisted action $\lambda \cdot x = \varsigma(\lambda)x$ continuous, hence makes the conjugate module $A^{\varsigma}$ a topological module; the theorem is an equivalence under the one hypothesis that the scalar map $\lambda \mapsto \lambda x$ be a topological embedding, a hypothesis automatic for a unital topological algebra over a complete valued field, and the twisted action is an action of $R$ only because $R$ is commutative. Continuity of the algebra involution $*$ makes the derived operation $x \star y = xy^{*}$ inherit the continuity of the algebra product and is what the form layer and the operator theory assume; it is free for a $\mathrm{C}^{*}$-algebra, where the involution is isometric with $\lVert a^{*}\rVert = \lVert a\rVert$ by the $\mathrm{C}^{*}$-identity, free in finite dimension over a complete valued field, free for an involution preserving the ideals of a linear topology, and free over a discrete base. It fails for the substitution $f(x) \mapsto f(b-x)$ on $\mathbb{R}[x]$ with the $(x)$-adic topology when $b \neq 0$, and there the derived operation $x \star y = x\sigma_b(y)$ over $(\mathbb{R},\mathrm{id})$ is a sesquilinear structure that is not separately continuous; continuity of the base fails for the conjugation of $\mathbb{Q}(\sqrt{2})$ with the topology inherited from $\mathbb{R}$, and there the conjugate module is not a topological module; the two failures are independent. A continuous involution may always be made isometric by the normal form $\lVert x\rVert_{*} = \max(\lVert x\rVert,\lVert x^{*}\rVert)$, a norm equivalent to the original, submultiplicative and invariant under the involution, so the normed layer loses nothing by assuming the involution isometric. At $\varsigma = \mathrm{id}$ the twisted action is the ordinary action, the conjugate module is the module, the base involution is the identity, and the two continuity questions become the single question of the bilinear layer, the continuity of $*$; the collapse is the sense in which the continuity of the base is the new hypothesis of the sesquilinear layer.

## Summary of Notation

| symbol | meaning |
|---|---|
| $(R,\varsigma)$ | a commutative involutive topological ring with $1$, and its continuous involution |
| $\lambda \cdot x = \varsigma(\lambda)x$ | the twisted action, continuous exactly when $\varsigma$ is |
| $A^{\varsigma}$ | the conjugate module, a topological module when the twisted action is continuous |
| $*$, $*^{2} = \mathrm{id}$, $(xy)^{*} = y^{*}x^{*}$ | the $\varsigma$-semilinear involution of the algebra, and its two laws |
| $x \star y = xy^{*}$ | the derived operation, separately continuous when $*$ is |
| $\lVert a^{*}a\rVert = \lVert a\rVert^{2}$ | the $\mathrm{C}^{*}$-identity, which makes $*$ isometric and free |
| $\lVert x\rVert_{*} = \max(\lVert x\rVert,\lVert x^{*}\rVert)$ | the isometric normal form of a continuous involution |
| $\sigma_b(f)(x) = f(b-x)$ | the involutions of $\mathbb{R}[x]$ with the $(x)$-adic topology, continuous only for $b = 0$ |
| $\varsigma$ of $\mathbb{Q}(\sqrt{2})$ | the discontinuous conjugation, so that the conjugate module is not a topological module |
| $\varsigma = \mathrm{id}$ | the collapse: the twisted action is the ordinary action, and the two questions become one |

## Further Reading

- Seth Warner, *Topological Rings* (North-Holland, 1993), for the involutive topological rings, the continuous involutions and the topology of the base.
- Charles E. Rickart, *General Theory of Banach Algebras* (Van Nostrand, 1960), for the involutions of Banach algebras, the continuity questions and the role of the $\mathrm{C}^{*}$-identity.
- Theodore W. Palmer, *Banach Algebras and the General Theory of \*-Algebras, Volume II* (Cambridge University Press, 2001), for the general theory of involutive Banach algebras and the comparison of the Banach `*`-norms.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras, Volume I* (Academic Press, 1983), for the $\mathrm{C}^{*}$-algebras, the isometry of the involution and the uniqueness of the $\mathrm{C}^{*}$-norm.
- Nicolas Bourbaki, *Topological Vector Spaces, Chapters 1–5* (Springer, 1987), for the topological modules, the linear topologies and the finite-dimensional canonical topology.
- Gérard J. Murphy, *$\mathrm{C}^{*}$-Algebras and Operator Theory* (Academic Press, 1990), for the $\mathrm{C}^{*}$-identity and the spectral radius formula.
