# __Quadratic Pairs and Semi-Traces on an Algebra with Involution__

## Introduction

An involution of a central simple algebra is classified, over a base in which two is invertible, by the dimension of its symmetric part: an **orthogonal** involution has a symmetric part of dimension $\tfrac12 n(n+1)$ and a **symplectic** one of dimension $\tfrac12 n(n-1)$, and the whole classification of *Involutions of a Central Simple Algebra* is built on that single measurement. Over a base in which two is not invertible the measurement disappears: the symmetric and the skew elements coincide, the eigenspace decomposition fails, and the two types no longer separate the involutions. The repair keeps the involution and adds one map to it, a linear functional on the symmetric part, the **semi-trace**, constrained by the reduced trace. The pair $(\sigma,f)$ is a **quadratic pair**, and the triple $(A,\sigma,f)$ is a **quadratic triple**. The notion is due to Knus, Merkurjev, Rost and Tignol, who introduced it so that the groups of type $D_n$ have a description in every characteristic; it was extended from the central simple algebras to the Azumaya algebras by Calmès and Fasel, and studied further by Gille, Neher and Ruether.

This article introduces the two submodules that the eigenspace theory does not define, the alternating and the symmetrized elements, and shows that they are the two that survive when the eigenspaces coalesce; states the semi-trace, the quadratic pair and the quadratic triple, and shows that over a base in which two is invertible the semi-trace is forced to be half the reduced trace, so that the pair adds nothing to the involution; records the criterion for a semi-trace to exist, which is that the unit be a symmetrized element, and the classification of all semi-traces by the elements of a quotient of the algebra; works three examples — the transpose of a matrix algebra, which carries no semi-trace in characteristic two, the canonical involution of a quaternion algebra, which carries one, and the orthogonal involution of a tensor product of two quaternion algebras, which is the degree-four case; and names the three cohomological obstructions of a quadratic triple, together with the extension of a Lie algebra that the third of them measures.

Throughout, $R$ is a commutative ring with $1 \neq 0$, $A$ is an **Azumaya $R$-algebra**, $\sigma$ is an involution of $A$ of the **first kind**, so that it is $R$-linear and the scalars are the centre, and $\operatorname{Trd} : A \to R$ is the **reduced trace**; when $R$ is a field the Azumaya algebras are the central simple algebras and the theory is the classical one, and the statements that need a field say so. The involution, the fixed set and the symmetric and the skew elements are from *Involutive Rings* and *The Skew Field of a Ring with Involution*; the Azumaya algebra, its centre and its reduced trace are from *Separable Algebras* and *Central Simple Algebras and the Brauer Group*; the matrix involutions are from *Matrix Rings with an Involution*, and the classification of the first-kind involutions is from *Involutions of a Central Simple Algebra*, whose eigenspace theory this article completes in the characteristic-two case; the extension groups that carry the obstructions are from *Ext and Tor*. The three obstructions are classes in the cohomology of a sheaf and exist only over a scheme: they are named and interpreted here and computed nowhere, the sheaf cohomology they need being that of *Sheaf Cohomology* and *Sheaves in Algebraic Geometry* in Part II; the obstruction section quotes the three geometric statements and their proofs from the sources, while the algebraic proofs before it use no sheaf, no scheme and no topological space. The deformations of a quadratic triple are *Deformation Theory*, and the relative question they raise is named at the close.

## The Submodules of an Algebra with an Involution

### The Symmetric and the Skew Elements

**Definition.** For an algebra $A$ with an involution $\sigma$ the **symmetric** and the **skew** elements are the kernels

$$
\mathrm{Sym}(A,\sigma) = \ker(\mathrm{id}-\sigma) = \{x : \sigma(x) = x\}, \qquad \mathrm{Skew}(A,\sigma) = \ker(\mathrm{id}+\sigma) = \{x : \sigma(x) = -x\}.
$$

**Proposition.** Both are additive subgroups of $A$ containing the central scalars fixed by $\sigma$, and

$$
\boxed{\;A = \mathrm{Sym}(A,\sigma)\oplus\mathrm{Skew}(A,\sigma)\;}
$$

when two is invertible in $R$; in characteristic two the two subgroups coincide and the decomposition fails.

*Proof.* The two subgroups are kernels of additive maps; the decomposition is the eigenspace decomposition of the order-two map $\sigma$, $x = \tfrac12(x+\sigma(x))+\tfrac12(x-\sigma(x))$, and an element in both satisfies $2x = 0$; in characteristic two the conditions $\sigma(x) = x$ and $\sigma(x) = -x$ are one and the same.

The content is *The Skew Field of a Ring with Involution*, quoted here because the next two submodules are read against it.

### The Alternating and the Symmetrized Elements

**Definition.** The **alternating** and the **symmetrized** elements are the images

$$
\mathrm{Alt}(A,\sigma) = \operatorname{im}(\mathrm{id}-\sigma) = \{x-\sigma(x)\}, \qquad \mathrm{Symd}(A,\sigma) = \operatorname{im}(\mathrm{id}+\sigma) = \{x+\sigma(x)\}.
$$

**Proposition (containment).** $\mathrm{Alt}(A,\sigma)\subseteq\mathrm{Skew}(A,\sigma)$ and $\mathrm{Symd}(A,\sigma)\subseteq\mathrm{Sym}(A,\sigma)$.

*Proof.* For the first, $(\mathrm{id}+\sigma)(x-\sigma(x)) = x-\sigma(x)+\sigma(x)-x = 0$, so an alternating element is skew; the second is the computation $\sigma(x+\sigma(x)) = \sigma(x)+x$.

**Proposition (the four are two).** If two is invertible in $R$ then

$$
\boxed{\;\mathrm{Alt}(A,\sigma) = \mathrm{Skew}(A,\sigma), \qquad \mathrm{Symd}(A,\sigma) = \mathrm{Sym}(A,\sigma):\;}
$$

every skew element is alternating and every symmetric element symmetrized.

*Proof.* The containments are the previous proposition. Conversely $x \in \mathrm{Skew}$ has $x = \tfrac12(x-\sigma(x))$ and $x \in \mathrm{Sym}$ has $x = \tfrac12(x+\sigma(x))$, and the halves exist by hypothesis.

**Remark (why the images are the covariant objects).** A symmetric element is one that the involution fixes, and a symmetrized element is one of the form $x+\sigma(x)$. The two definitions agree when two is invertible, but they are different data over a general base, and the difference is exactly what the semi-trace of the next section consumes. The letters $\mathrm{Alt}$ and $\mathrm{Symd}$ name the two image submodules here; $\mathrm{Alt}$ is not the antisymmetrisation map of *The Filtration and the Associated Graded Algebra*, which carries the same letters in the Clifford theory.

### The Collapse in Characteristic Two

**Proposition.** In characteristic two the four submodules coalesce in pairs,

$$
\mathrm{Sym}(A,\sigma) = \mathrm{Skew}(A,\sigma), \qquad \mathrm{Symd}(A,\sigma) = \mathrm{Alt}(A,\sigma),
$$

so that they form the single chain $\mathrm{Alt}(A,\sigma)\subseteq\mathrm{Skew}(A,\sigma)$, whose inclusion may be proper.

*Proof.* The conditions $\sigma(x) = x$ and $\sigma(x) = -x$ are the same since $-1 = 1$; and for the images, $x+\sigma(x) = x-\sigma(x)$ for the same reason, so the two image submodules coincide as well. The containment of the alternating in the skew is the proposition above, and the properness is witnessed on a matrix algebra in the examples below.

**Proposition (the map $\xi$).** The map $\mathrm{id}+\sigma$ kills $\mathrm{Alt}(A,\sigma)$ and is onto $\mathrm{Symd}(A,\sigma)$, so it induces a surjection

$$
\xi : A/\mathrm{Alt}(A,\sigma) \twoheadrightarrow \mathrm{Symd}(A,\sigma),
$$

whose kernel is $\mathrm{Skew}(A,\sigma)/\mathrm{Alt}(A,\sigma)$; the quotient $A/\mathrm{Alt}(A,\sigma)$ is the home of the semi-traces.

*Proof.* The kernel of $\mathrm{id}+\sigma$ is $\mathrm{Skew}$ and its image is $\mathrm{Symd}$ by definition, and $\mathrm{Alt}$ lies in the kernel by the containment above, so $\xi$ is the induced map of the first isomorphism theorem.

**Remark (what is lost in characteristic two).** The dimensions of the symmetric and the skew parts are no longer available to separate the orthogonal type from the symplectic type of *Involutions of a Central Simple Algebra*; the two parts no longer add up to the algebra; and the symmetric elements no longer carry a Jordan structure, while the skew ones still carry their Lie structure, as *Involutive Algebras* records. This is the deficiency that the semi-trace repairs, and it is the reason the pair and not the involution is the right object.

### The Four Submodules in the Two Cases

The following table collects the four submodules as the two propositions compute them.

| Submodule | two invertible | characteristic two |
|---|---|---|
| $\mathrm{Sym}(A,\sigma)$ | $\ker(\mathrm{id}-\sigma)$, the fixed elements | $=\mathrm{Skew}(A,\sigma)$ |
| $\mathrm{Skew}(A,\sigma)$ | $\ker(\mathrm{id}+\sigma)$, the anti-fixed elements | $=\mathrm{Sym}(A,\sigma)$ |
| $\mathrm{Alt}(A,\sigma)$ | $=\mathrm{Skew}(A,\sigma)$ | $=\mathrm{Symd}(A,\sigma)$ |
| $\mathrm{Symd}(A,\sigma)$ | $=\mathrm{Sym}(A,\sigma)$ | $=\mathrm{Alt}(A,\sigma)$ |
| $A$ | $\mathrm{Sym}\oplus\mathrm{Skew}$ | no decomposition |

## The Semi-Trace and the Quadratic Pair

### The Definition

**Definition.** Let $A$ be an Azumaya $R$-algebra with an involution $\sigma$. A **semi-trace** for $\sigma$ is an $R$-module map $f : \mathrm{Sym}(A,\sigma) \to R$ with

$$
f\bigl(a+\sigma(a)\bigr) = \operatorname{Trd}(a) \qquad \text{for every } a \in A .
$$

A **quadratic pair** on $A$ is an involution $\sigma$ together with a semi-trace $f$ for it, and the tuple $(A,\sigma,f)$ is a **quadratic triple**. The reduced trace used here is the one of *Central Simple Algebras and the Brauer Group*, and it satisfies $\operatorname{Trd}(\sigma(a)) = \operatorname{Trd}(a)$ for an involution of the first kind.

**Remark (the condition sits on the symmetrized elements).** The element $a+\sigma(a)$ is symmetric, so the constraint is imposed on $f$ at the symmetrized elements alone; a semi-trace is a map defined on the whole of $\mathrm{Sym}(A,\sigma)$ whose restriction to $\mathrm{Symd}(A,\sigma)$ is prescribed by the reduced trace. The definition is therefore designed for the case in which the two submodules differ, and it is then a genuine condition on $f$; when two is invertible the two submodules agree and the condition determines $f$ outright, as the next proposition shows.

### The Case of Two Invertible

**Proposition.** Let two be invertible in $R$. Then

$$
f = \tfrac12\operatorname{Trd}\big|_{\mathrm{Sym}(A,\sigma)}
$$

is a semi-trace, and it is the only one. The quadratic pairs on $A$ are therefore in bijection with the involutions of orthogonal type, and the notion adds nothing to *Involutions of a Central Simple Algebra*.

*Proof.* Since $\mathrm{Symd}(A,\sigma) = \mathrm{Sym}(A,\sigma)$, the constraint of the definition applies at every element of the domain. For an element $a+\sigma(a)$,

$$
f\bigl(a+\sigma(a)\bigr) = \tfrac12\operatorname{Trd}\bigl(a+\sigma(a)\bigr) = \tfrac12\bigl(\operatorname{Trd}(a)+\operatorname{Trd}(\sigma(a))\bigr) = \operatorname{Trd}(a),
$$

by the $R$-linearity of the reduced trace and its invariance under $\sigma$; and the constraint read at an arbitrary symmetric element $x = \tfrac12 x+\sigma(\tfrac12 x)$ forces $f(x) = \tfrac12\operatorname{Trd}(x)$, which is uniqueness.

**Remark (so the interest is characteristic two).** Whenever two is invertible the semi-trace is forced, and the theory of quadratic pairs coincides with the theory of the orthogonal involutions; the notion is a genuine refinement only over a base in which two is not invertible, where the type is unavailable and the pair carries strictly more information than the involution.

### Existence and the Classification of the Semi-Traces

**Definition.** An involution $\sigma$ is **locally quadratic** when the unit is a symmetrized element, $1_A \in \mathrm{Symd}(A,\sigma)$.

**Theorem (the classification of the semi-traces).** The semi-traces for $\sigma$ are in bijection with the elements $\lambda \in A/\mathrm{Alt}(A,\sigma)$ with $\xi(\lambda) = 1_A$, the semi-trace attached to $\lambda$ being

$$
\boxed{\;f_\lambda(s) = \operatorname{Trd}(\ell\,s), \qquad s \in \mathrm{Sym}(A,\sigma)\;},
$$

for any lift $\ell$ of $\lambda$ in $A$. In particular a semi-trace exists exactly when $\sigma$ is locally quadratic.

*Proof (of the construction and of the well-definedness).* Let $\ell$ lift $\lambda$ with $\xi(\lambda) = 1_A$, that is $\ell+\sigma(\ell) = 1_A$. For $a \in A$,

$$
f_\ell\bigl(a+\sigma(a)\bigr) = \operatorname{Trd}\bigl(\ell a\bigr)+\operatorname{Trd}\bigl(\ell\,\sigma(a)\bigr) = \operatorname{Trd}\bigl((\ell+\sigma(\ell))a\bigr) = \operatorname{Trd}(a),
$$

the middle step using $\operatorname{Trd}(xy) = \operatorname{Trd}(yx)$ and the invariance of the reduced trace under $\sigma$ in the form $\operatorname{Trd}(\ell\,\sigma(a)) = \operatorname{Trd}(\sigma(\ell)\,a)$. So $f_\ell$ is a semi-trace. For the dependence on the lift, let $\ell' = \ell+y$ with $y = a-\sigma(a) \in \mathrm{Alt}(A,\sigma)$; then for $s \in \mathrm{Sym}(A,\sigma)$,

$$
\operatorname{Trd}(y s) = \operatorname{Trd}(a s)-\operatorname{Trd}(\sigma(a) s) = \operatorname{Trd}(a s)-\operatorname{Trd}(s a) = 0,
$$

since $\operatorname{Trd}(\sigma(a)s) = \operatorname{Trd}(\sigma(sa)) = \operatorname{Trd}(sa)$; hence $f_{\ell'} = f_\ell$ and the semi-trace depends only on $\lambda$. The existence of a lift is the definition of $\mathrm{Symd}(A,\sigma)$ as the image of $\mathrm{id}+\sigma$, so a locally quadratic involution carries at least one semi-trace.

**Remark (the converse and its proof).** That the correspondence is a bijection — every semi-trace is of the displayed form, and distinct classes give distinct semi-traces — is the theorem of Gille, Neher and Ruether, and it is what makes the count of the classes in $A/\mathrm{Alt}(A,\sigma)$ the count of the semi-traces. It is proved by splitting the algebra, where the symmetric elements are read on the matrix model and the semi-trace is computed by the reduced trace of a single element; over a general base the splitting is local and the statement is the corresponding local statement.

## Examples

### The Transpose of a Matrix Algebra

Let $R$ be a commutative ring, $A = M_n(R)$ and $\sigma$ the transpose, $X \mapsto X^{\mathrm{t}}$, an involution of the first kind and of orthogonal type when two is invertible. Then $\operatorname{Trd} = \operatorname{tr}$, and the proposition of the previous section gives the semi-trace $f = \tfrac12\operatorname{tr}$ and the quadratic triple $(M_n(R),\mathrm{t},\tfrac12\operatorname{tr})$. Over a field with two invertible this is the standard quadratic pair of a matrix algebra, and it is the only one for that involution.

In characteristic two the same involution behaves differently, and the difference is visible on one element. Take $A = M_2(\mathbb{F}_2)$ and let $\sigma$ be the transpose. The symmetrized elements are spanned by the single matrix

$$
\mathrm{Symd}(A,\sigma) = \{0, E_{12}+E_{21}\},
$$

which does not contain the identity. A semi-trace is then impossible: with $a = E_{11}$ one has $a+\sigma(a) = 2E_{11} = 0$, while $\operatorname{Trd}(a) = 1$, so the defining constraint would demand $f(0) = 1$, which the $R$-linearity of $f$ forbids. The transpose of $M_2$ in characteristic two is therefore **not locally quadratic**: it carries no quadratic pair at all. This is the smallest witness that the orthogonal type alone does not survive into characteristic two.

### The Canonical Involution of a Quaternion Algebra

**Definition.** For a degree-two Azumaya $R$-algebra $A$ and an element $a \in A$, set

$$
\psi(a) = \operatorname{Trd}(a)\,1_A-a .
$$

**Proposition.** $\psi$ is an involution of $A$, it fixes the scalars and negates the traceless part; over a field with two invertible it is the conjugation of the quaternion algebra, and it is of symplectic type, with $\mathrm{Sym}(A,\psi)$ the scalars of dimension one.

*Proof.* Squaring, $\psi(\psi(a)) = \operatorname{Trd}(\psi(a))1_A-\psi(a)$, and $\operatorname{Trd}(\psi(a)) = \operatorname{Trd}(a)$, since $\operatorname{Trd}(1_A) = 2$ for a degree-two algebra; hence $\psi(\psi(a)) = a$. For the anti-multiplicativity, an element of a degree-two algebra satisfies the reduced characteristic identity

$$
a^2-\operatorname{Trd}(a)\,a+\operatorname{Nrd}(a)\,1_A = 0,
$$

whose linearisation is

$$
ab+ba = \operatorname{Trd}(a)\,b+\operatorname{Trd}(b)\,a+\operatorname{Trd}(ab)\,1_A-\operatorname{Trd}(a)\operatorname{Trd}(b)\,1_A .
$$

Expanding $\psi(a)\psi(b) = (\operatorname{Trd}(a)1_A-a)(\operatorname{Trd}(b)1_A-b)$ and substituting the linearisation gives $\psi(a)\psi(b) = \operatorname{Trd}(ab)1_A-ba = \psi(ba)$, so $\psi$ is an anti-automorphism. A scalar $\lambda$ gives $\psi(\lambda) = 2\lambda-\lambda = \lambda$, and a traceless element is negated. Over a field with two invertible, $\psi(a) = a$ forces $2a = \operatorname{Trd}(a)1_A$, hence $a$ scalar, so $\mathrm{Sym}(A,\psi)$ has dimension one, which is $\tfrac12\cdot 2\cdot(2-1)$ and therefore the symplectic type.

**Remark (the characteristic-two case).** In characteristic two the formula is still an involution and an anti-automorphism, and the symmetrized elements are the image of the map $a \mapsto \operatorname{Trd}(a)1_A$, which is the scalar line and contains the unit; the involution **is** locally quadratic. Its semi-traces are the maps $f(s) = \operatorname{Trd}(\ell s)$ with $\operatorname{Trd}(\ell) = 1$, which exist because the reduced trace of a degree-two algebra is not identically zero in characteristic two, even though $\operatorname{Trd}(1_A) = 2 = 0$ there. On $M_2(\mathbb{F}_2)$ with the involution $\psi(X) = \operatorname{tr}(X)I-X$ one may take $\ell = E_{11}$, and $f(s) = \operatorname{tr}(E_{11}s)$ is a semi-trace. The pair therefore exists, whereas the transpose's does not.

### The Degree-Four Case: Two Quaternion Algebras

Let $F$ be a field with two invertible, let $Q_1$, $Q_2$ be quaternion $F$-algebras with their canonical involutions $\psi_1$, $\psi_2$ of the previous example, and let

$$
A = Q_1\otimes_F Q_2, \qquad \sigma = \psi_1\otimes\psi_2 .
$$

The algebra $A$ is the **biquaternion algebra** of *Division Algebras*, sixteen-dimensional over $F$ and of degree four, and $\sigma$ is an involution of it. The symmetric elements of a tensor product of involutions are computed parity by parity, a pair of even elements and a pair of odd ones contributing a symmetric product and a mixed pair a skew one, so that

$$
\mathrm{Sym}(A,\sigma) = \mathrm{Sym}(Q_1,\psi_1)\otimes\mathrm{Sym}(Q_2,\psi_2)\oplus\mathrm{Skew}(Q_1,\psi_1)\otimes\mathrm{Skew}(Q_2,\psi_2),
$$

of dimension $1\cdot 1+3\cdot 3 = 10$, which is $\tfrac12\cdot 4\cdot 5$: the involution $\sigma$ is of **orthogonal type**, and $(A,\sigma,\tfrac12\operatorname{Trd})$ is a quadratic triple of degree four. The pair is the one carried by the biquaternion algebra in the relative deformation theorem of the closing section.

**Remark (the two senses of biquaternion).** The algebra of this example is the biquaternion algebra of the arithmetic literature, the tensor product of two quaternion algebras over one field, of degree four; it is not the algebra $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ of the Biquaternions category, which has degree two over $\mathbb{C}$ and carries the involution of the preceding example. The collision of the two names is recorded in *Division Algebras*, and the two algebras share only the factor $\mathbb{H}$ over $\mathbb{R}$.

## The Three Obstructions

The submodules of the first section are read through three short exact sequences, and the image of the unit under the connecting map of each is an invariant of the pair. The first two are those of Gille, Neher and Ruether; the third is the intermediate obstruction of Mackall and Ruether, and it exists only in characteristic two.

### The Strong and the Weak Obstruction

The map $\mathrm{id}+\sigma$ has kernel $\mathrm{Skew}(A,\sigma)$ and image $\mathrm{Symd}(A,\sigma)$, and it kills $\mathrm{Alt}(A,\sigma)$, so there are exact sequences

$$
0 \to \mathrm{Skew}(A,\sigma) \to A \xrightarrow{\ \mathrm{id}+\sigma\ } \mathrm{Symd}(A,\sigma) \to 0,
$$

$$
0 \to \mathrm{Skew}(A,\sigma)/\mathrm{Alt}(A,\sigma) \to A/\mathrm{Alt}(A,\sigma) \xrightarrow{\ \xi\ } \mathrm{Symd}(A,\sigma) \to 0 .
$$

The image of the unit $1_A \in \mathrm{Symd}(A,\sigma)$ under the connecting map of the first sequence is the **strong obstruction** $\Omega(A,\sigma)$, and under that of the second the **weak obstruction** $\omega(A,\sigma)$. The strong obstruction vanishes exactly when there is a linear map $A \to \mathcal{O}_X$ whose restriction to the symmetric elements is a semi-trace, and the weak obstruction vanishes exactly when $\sigma$ can be equipped with a semi-trace, that is, exactly when $\sigma$ is locally quadratic. The strong obstruction therefore controls whether a semi-trace extends to the whole algebra and the weak one whether a semi-trace exists at all.

### The Intermediate Obstruction

In characteristic two the submodules collapse, and between the two sequences above there sits a third. The map $\mathrm{id}+\sigma$ also kills the scalars, so that

$$
0 \to \mathrm{Skew}(A,\sigma)/\mathcal{O}_X \to A/\mathcal{O}_X \xrightarrow{\ \mathrm{id}+\sigma\ } \mathrm{Symd}(A,\sigma) \to 0
$$

is exact, and the image of the unit under its connecting map is the **intermediate obstruction** $\Omega'(A,\sigma)$. It is intermediate in name and in fact: the surjections

$$
\mathrm{Skew}(A,\sigma) \twoheadrightarrow \mathrm{Skew}(A,\sigma)/\mathcal{O}_X \twoheadrightarrow \mathrm{Skew}(A,\sigma)/\mathrm{Alt}(A,\sigma)
$$

carry $\Omega(A,\sigma)$ to $\Omega'(A,\sigma)$ and $\Omega'(A,\sigma)$ to $\omega(A,\sigma)$, so that in characteristic two the three obstructions form a chain, and the vanishing of the weak one is necessary for the other two to be defined with their ordinary meaning. The intermediate obstruction is the genuinely new invariant: it exists in no other characteristic, and it is not a consequence of the other two.

### The Extension of the Lie Algebra

Let $\omega(A,\sigma) = 0$, so that a semi-trace $f$ exists and $(A,\sigma,f)$ is a quadratic triple. The automorphism group of the triple has a Lie algebra $\mathfrak{pgo}_{(A,\sigma,f)}$, which sits inside $A/\mathcal{O}_X$ and is itself an extension

$$
0 \to \mathrm{Alt}(A,\sigma)/\mathcal{O}_X \to \mathfrak{pgo}_{(A,\sigma,f)} \to \mathcal{O}_X \to 0 .
$$

**Theorem.** In characteristic two the intermediate obstruction $\Omega'(A,\sigma)$ vanishes if and only if there is a semi-trace $f$ making $(A,\sigma,f)$ a quadratic triple for which this extension of Lie algebras is split exact.

*Proof (in outline).* One direction is immediate: a splitting of the extension exhibits the class of the extension as zero, and that class is the image of $\Omega'(A,\sigma)$ under the natural map $\operatorname{Ext}^1(\mathcal{O}_X,\mathrm{Alt}/\mathcal{O}_X)\to \operatorname{Ext}^1(\mathcal{O}_X,\mathrm{Skew}/\mathcal{O}_X)$; conversely a section of $\mathrm{Symd}(A,\sigma)$ lifting the unit produces a semi-trace $f$ by the classification theorem above, and the lift of the unit is exactly a splitting of the extension. The fibre-product description of $\mathfrak{pgo}_{(A,\sigma,f)}$ inside $A/\mathcal{O}_X$, which is what makes the proof run, is the content of the source.

**Remark (where the classes live).** Each of the three is a class in the cohomology of a sheaf of $\mathcal{O}_X$-modules, and over a field or a single local ring those cohomology groups vanish, so that in the algebraic theory above there is no obstruction at all: a locally quadratic involution over a field carries a semi-trace, and that semi-trace extends to a linear map on the whole algebra, since a linear functional on a subspace of a vector space always extends. The classes acquire content only over a scheme, where the algebra varies with the base, which is why the phenomenon is a geometric one and why the sheaf cohomology that carries it belongs to Part II.

## Forgetting the Quadratic Pair

The counterpoint of the whole construction is the question of what happens when the pair is forgotten. Let $A$ be an Azumaya algebra over a scheme and let $(A,\sigma,f)$ be a quadratic triple on it; one compares the deformations of the triple with those of the underlying Azumaya algebra $A$, and the triple is **relatively unobstructed** when it deforms as soon as the algebra does. The answer of Mackall and Ruether is two-sided. If two is a global unit, or if the degree of $A$ is two, then the triple is relatively unobstructed: every deformation of $A$ extends to one of $(A,\sigma,f)$, so that in the two exceptional cases of the theorem the semi-trace adds no obstruction to the deformation theory. In characteristic two, with neither hypothesis, the two behaviours separate: on an **Igusa surface**, a surface in characteristic two whose Picard scheme is not reduced, there is a biquaternion algebra $Q'\otimes P'$ with a quadratic pair such that the underlying Azumaya algebra deforms and the quadratic triple does not. The example is the one constructed in the degree-four case above, and its obstruction is inherited from a line bundle on the surface whose deformations are obstructed.

**Remark (the boundary).** The deformation functors, the tangent-obstruction theory and the comparison of the deformations of the triple with those of the algebra are the subject of *Deformation Theory*; the Igusa surface, its Picard scheme and the cohomology of its sheaves are Part II, where they are *Sheaves in Algebraic Geometry* and the geometry of surfaces; and the algebra construction of the example is the degree-four case of the examples above. Nothing of the scheme-theoretic theory is used in the algebraic part of this article.

## Summary

Over a base in which two is invertible the involutions of a central simple algebra are classified by the dimension of the symmetric part, and the alternating elements are the skew ones and the symmetrized elements the symmetric ones; in characteristic two the symmetric and the skew elements coincide, the alternating and the symmetrized ones coincide, and the two collapses destroy the type and the eigenspace decomposition at once. The repair is the **semi-trace**, an $R$-module map $f : \mathrm{Sym}(A,\sigma) \to R$ with $f(a+\sigma(a)) = \operatorname{Trd}(a)$, and the resulting **quadratic pair** $(\sigma,f)$ and **quadratic triple** $(A,\sigma,f)$. When two is invertible the semi-trace is forced to be $\tfrac12\operatorname{Trd}$ and the pair is the involution; over a general base the semi-traces are classified by the elements $\lambda \in A/\mathrm{Alt}(A,\sigma)$ with $\xi(\lambda) = 1_A$, they exist exactly when the unit is a symmetrized element, and the involution is then called locally quadratic. The matrix transpose is orthogonal over a field with two invertible but carries no semi-trace over $\mathbb{F}_2$, since its symmetrized elements miss the unit; the canonical involution $a \mapsto \operatorname{Trd}(a)1_A-a$ of a quaternion algebra is symplectic over a field with two invertible and locally quadratic in characteristic two, where its semi-traces are the maps $s \mapsto \operatorname{Trd}(\ell s)$ with $\operatorname{Trd}(\ell) = 1$; and the involution $\psi_1\otimes\psi_2$ of a tensor product of two quaternion algebras is orthogonal of degree four, with a symmetric part of dimension ten, which is the degree-four case of the theory. The submodules carry three cohomological obstructions, the strong, the intermediate and the weak, chained in characteristic two and living in the cohomology of sheaves; the intermediate one is new and vanishes exactly when the extension of the Lie algebra $\mathfrak{pgo}_{(A,\sigma,f)}$ by the scalars splits. Finally, a quadratic triple is relatively unobstructed when two is a unit or the degree is two, and in characteristic two the relative obstruction exists, on the biquaternion algebra of an Igusa surface.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$, $A$, $\sigma$ | Commutative ring, Azumaya $R$-algebra, involution of the first kind |
| $\operatorname{Trd} : A \to R$ | The reduced trace, invariant under $\sigma$ |
| $\mathrm{Sym}(A,\sigma)$ | Fixed elements, $\ker(\mathrm{id}-\sigma)$ |
| $\mathrm{Skew}(A,\sigma)$ | Anti-fixed elements, $\ker(\mathrm{id}+\sigma)$ |
| $\mathrm{Alt}(A,\sigma)$ | Alternating elements, $\operatorname{im}(\mathrm{id}-\sigma)$ |
| $\mathrm{Symd}(A,\sigma)$ | Symmetrized elements, $\operatorname{im}(\mathrm{id}+\sigma)$ |
| $\mathrm{Alt}\subseteq\mathrm{Skew}$, $\mathrm{Symd}\subseteq\mathrm{Sym}$ | The containments, over any base |
| $\mathrm{Alt}=\mathrm{Skew}$, $\mathrm{Symd}=\mathrm{Sym}$ | The equalities, two invertible |
| $\mathrm{Sym}=\mathrm{Skew}$, $\mathrm{Symd}=\mathrm{Alt}$ | The collapses, characteristic two |
| $f : \mathrm{Sym}(A,\sigma) \to R$ | A semi-trace, $f(a+\sigma(a)) = \operatorname{Trd}(a)$ |
| $(A,\sigma,f)$ | A quadratic triple; $(\sigma,f)$ a quadratic pair |
| $\xi : A/\mathrm{Alt}\to\mathrm{Symd}$ | The surjection induced by $\mathrm{id}+\sigma$ |
| $\lambda$, $\ell$ | A class with $\xi(\lambda) = 1_A$, and a lift of it |
| $f_\lambda(s) = \operatorname{Trd}(\ell s)$ | The semi-trace attached to $\lambda$ |
| $1_A \in \mathrm{Symd}(A,\sigma)$ | The locally quadratic condition |
| $a \mapsto \operatorname{Trd}(a)1_A-a$ | The canonical involution of a degree-two algebra |
| $\psi_1\otimes\psi_2$ | The orthogonal involution of $Q_1\otimes_F Q_2$ |
| $\Omega,\Omega',\omega$ | The strong, intermediate and weak obstruction |
| $\mathfrak{pgo}_{(A,\sigma,f)}$ | The Lie algebra of the automorphism group of the triple |

## Further Reading

- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, American Mathematical Society Colloquium Publications 44 (1998), for quadratic pairs, semi-traces, and the orthogonal and symplectic types of an involution.
- Max-Albert Knus, *Quadratic and Hermitian Forms over Rings*, Grundlehren der mathematischen Wissenschaften 294 (Springer, 1991), for Azumaya algebras with involution, the reduced trace and the semi-trace over a ring.
- Baptiste Calmès and Jean Fasel, *Classical groups*, in *Autour des schémas en groupes*, Volume II, Société Mathématique de France (2015), for the extension of the quadratic pairs from the central simple algebras to the Azumaya algebras.
- Asher Auel, Uriya A. First and Ben Williams, "Azumaya algebras without involution", *Journal of the European Mathematical Society* 21 (2019), for the Azumaya algebras that carry no involution, against which the locally quadratic condition is read.
- Philippe Gille, Erhard Neher and Cameron Ruether, "Azumaya algebras and obstructions to quadratic pairs over a scheme", arXiv:2209.07107 (2025), for the strong and the weak obstruction and the classification of the semi-traces.
- Eoin Mackall and Cameron Ruether, "On deformations of Azumaya algebras with quadratic pair", arXiv:2504.02728 (2025), for the intermediate obstruction, the extension of the Lie algebra, and the relative deformation theorems.
