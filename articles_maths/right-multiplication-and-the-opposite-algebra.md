# __Right Multiplication and the Opposite Algebra__

## Introduction

The second one-sided family of a Clifford algebra is the right multiplication $R_x(y) = y\,x$. It is the mirror of the left multiplication, and it is *not* a second representation of the same algebra: because the order of the factors is reversed, the map $x \mapsto R_x$ turns products around and is a representation of the **opposite algebra** $\mathrm{Cl}(V,q)^{\mathrm{op}}$, the algebra with the same underlying vector space and the reversed product. This article treats the right family through that algebra.

The two families are then read on the same object. The vector space of the Clifford algebra is a bimodule under the left and the right multiplications at once, the two actions commute, and each is the exact commutant of the other – the double centraliser theorem on the regular bimodule. Restricting to one side gives the two regular representations; and since a Clifford algebra is isomorphic to its opposite through reversion, the right family carries nothing that the left family does not, but it carries it with the roles of the modules exchanged, and it is the family that supplies the dual of the spin representation.

The operator calculus – the definitions, the composition laws, the mutual commutants $\{L_a\}' = \{R_b\}$ and $\{R_b\}' = \{L_a\}$, and the fact that the two families generate the enveloping algebra – is *One-Sided Operators on a Clifford Algebra*. The present article adds the algebra-theoretic reading: the opposite algebra, the bimodule structure, the identification $\mathrm{End}_{\mathrm{Cl}}(\mathrm{Cl}) \cong \mathrm{Cl}^{\mathrm{op}}$ and the right modules and dual spin representation. The left regular representation and the module structure are *Left Multiplication and the Clifford Module Structure*; the one-sided action on a minimal left ideal and the spin representation are *The One-Sided Action and the Spin Representation*; the primitive idempotents and the minimal right ideals are *Spinors as Minimal Left Ideals with Inner Conjugation*; the intrinsic anti-involutions are *Clifford Algebras in Finite Dimensions*. The base is a field $F$ of characteristic not $2$ and $q$ is non-degenerate.

## The Right Regular Representation

**Definition.** The **right multiplication** by $x \in \mathrm{Cl}(V,q)$ is $R_x(y) = y\,x$. The **right regular representation** is the map $x \mapsto R_x$ into $\mathrm{End}_F(\mathrm{Cl}(V,q))$.

**Proposition (anti-multiplicativity).** For all $x, z \in \mathrm{Cl}(V,q)$,

$$
R_x R_z = R_{zx} , \qquad R_1 = \mathrm{id} .
$$

Hence $x \mapsto R_x$ is an injective homomorphism from the opposite algebra $\mathrm{Cl}(V,q)^{\mathrm{op}}$ into $\mathrm{End}_F(\mathrm{Cl}(V,q))$, equivalently an injective anti-homomorphism from $\mathrm{Cl}(V,q)$.

**Proof.** $R_x\bigl(R_z(y)\bigr) = yzx = R_{zx}(y)$; the reversal is exactly the reversed order of composition in the endomorphism ring. Injectivity is $R_x(1) = x$.

**Remark (the asymmetry with the left family).** The left multiplication is multiplicative in the written order, $L_xL_z = L_{xz}$, and the right multiplication is anti-multiplicative. It is this single reversal, and not the presence or absence of an involution, that forces the opposite algebra into the statement of the right family. With an anti-automorphism $c$ the composite $\mathrm{P}^{c}_x(y) = y\,c(x)$ recovers multiplicativity, $\mathrm{P}^{c}_x\mathrm{P}^{c}_z = \mathrm{P}^{c}_{xz}$, because the reversal inside $c$ cancels the reversal of the composition; this is the content of *One-Sided Operators on a Clifford Algebra* and is used below only for reversion and conjugation.

**Proposition (right ideals).** A subspace $J \subseteq \mathrm{Cl}(V,q)$ is a submodule of the right regular module exactly when it is a right ideal, that is when $J\cdot\mathrm{Cl}(V,q) \subseteq J$. Right multiplication by a unit preserves every right ideal, and a minimal right ideal is exactly a simple right module.

**Proof.** The two conditions are the definition of a submodule and of a right ideal; for a unit $R$, $JR = J$ because $\mathrm{Cl}R = \mathrm{Cl}$.

**Remark (why the right family is needed for spinors).** A minimal left ideal is not preserved by right multiplication, as *The One-Sided Action and the Spin Representation* shows; a minimal *right* ideal is preserved by right multiplication by construction, and the action of the spin group on it by right multiplication is the dual of the spin representation.

## The Opposite Algebra

**Definition.** The **opposite algebra** $\mathrm{Cl}(V,q)^{\mathrm{op}}$ has the same underlying vector space and the same $F$-linear structure as $\mathrm{Cl}(V,q)$, with the product reversed: $x \cdot^{\mathrm{op}} z = z\,x$. It is associative, unital with unit $1$, and $F$-linear.

**Proposition (the opposite of a Clifford algebra is a Clifford algebra).** In $\mathrm{Cl}(V,q)^{\mathrm{op}}$ the generators satisfy $e_i \cdot^{\mathrm{op}} e_j + e_j \cdot^{\mathrm{op}} e_i = e_je_i + e_ie_j = 2B(e_i,e_j)$ and $e_i \cdot^{\mathrm{op}} e_i = e_i^{2} = q(e_i)$, the same relations as in $\mathrm{Cl}(V,q)$. So the identity of $V$ is a Clifford map into $\mathrm{Cl}(V,q)^{\mathrm{op}}$, it extends to a unital algebra homomorphism $\mathrm{Cl}(V,q) \to \mathrm{Cl}(V,q)^{\mathrm{op}}$ by the universal property, and that homomorphism is an isomorphism because the two algebras have the same finite dimension.

**Proof.** The relations are displayed; the universal property of the Clifford algebra applies to the linear map $V \hookrightarrow \mathrm{Cl}(V,q)^{\mathrm{op}}$ because a vector satisfies $v \cdot^{\mathrm{op}} v = v^{2} = q(v)$. Injectivity of the resulting homomorphism follows from its surjectivity and equal dimensions, or directly because it is an algebra map with $x \neq 0$ having $x\cdot^{\mathrm{op}}1 \neq 0$.

**Theorem (a Clifford algebra is isomorphic to its opposite).** Let $r$ be the reversion, $r(x_1\cdots x_k) = x_k\cdots x_1$ for vectors $x_i$, extended linearly, and let $\natural$ be the Clifford conjugation, $\natural = \alpha \circ r$ with $\alpha$ the grade involution. Then $r$ and $\natural$ are anti-automorphisms of $\mathrm{Cl}(V,q)$, and each is an isomorphism of algebras

$$
\mathrm{Cl}(V,q) \longrightarrow \mathrm{Cl}(V,q)^{\mathrm{op}}, \qquad x \longmapsto x^{r} \quad \text{or} \quad x \longmapsto x^{\natural}.
$$

**Proof.** Reversion is $F$-linear, fixes the generators and reverses products, so it is an anti-automorphism; a composition of the automorphism $\alpha$ with the anti-automorphism $r$ is again an anti-automorphism, and both fix $1$. An anti-automorphism is by definition a unital algebra isomorphism onto the opposite algebra. Both are bijective, with inverses of the same kind.

**Corollary (right modules are left modules).** Pulling back along an isomorphism $\mathrm{Cl} \to \mathrm{Cl}^{\mathrm{op}}$ turns right modules into left modules and right ideals into left ideals. So the representation theory of the right regular module is the representation theory of the left regular module read through reversion, and the two simple-module counts agree.

**Proof.** An isomorphism of algebras $f : A \to B$ carries $B$-modules to $A$-modules by $a\cdot m = f(a)m$; apply it with $B = \mathrm{Cl}^{\mathrm{op}}$.

## The Bimodule and the Commutant

**Proposition (the regular bimodule).** The Clifford algebra is a bimodule over itself, with the left action $L$ and the right action $R$; the two actions commute,

$$
L_a R_b = R_b L_a \qquad \text{for all } a, b \in \mathrm{Cl}(V,q),
$$

because $L_aR_b(y) = ayb = R_bL_a(y)$.

**Proof.** Associativity, with the two factors $a$ and $b$ on opposite sides of $y$.

**Theorem (the commutant of the regular representation).** The algebra of module endomorphisms of the regular left module is the opposite algebra, realised by the right multiplications,

$$
\mathrm{End}_{\mathrm{Cl}(V,q)}\bigl(\mathrm{Cl}(V,q)\bigr) \cong \mathrm{Cl}(V,q)^{\mathrm{op}}, \qquad T \longmapsto T(1),
$$

with inverse $b \mapsto R_b$. Consequently $\{L_a\}' = \{R_b\}$ and $\{R_b\}' = \{L_a\}$, the two families are mutual commutants.

**Proof.** For a module endomorphism $T$ one has $T(y) = T(y\cdot1) = y\,T(1)$, so $T = R_{T(1)}$; conversely every $R_b$ is a module endomorphism because $R_b(ay) = ayb = aR_b(y)$. The mutual-commutant form is the computation of *One-Sided Operators on a Clifford Algebra*.

**Corollary (the centre).** An element $x$ lies in the centre of the Clifford algebra exactly when $L_x = R_x$. So the centre is the set of elements on which the two regular representations agree, and the left and right regular representations are equal on an element if and only if that element is central.

**Proof.** $L_x = R_x$ says $xy = yx$ for every $y$.

**Corollary (the enveloping algebra).** The algebra generated by the left and the right families together is the image of $\mathrm{Cl}\otimes_F\mathrm{Cl}^{\mathrm{op}}$ in $\mathrm{End}_F(\mathrm{Cl})$, and it is all of $\mathrm{End}_F(\mathrm{Cl})$ exactly when $\mathrm{Cl}$ is central simple over $F$. For a Clifford algebra this holds in even dimension; in odd dimension the centre is larger and the image is a proper subalgebra. This is the statement of *One-Sided Operators on a Clifford Algebra*, quoted here for completeness.

## The Right Spin Action and the Dual Representation

**Definition.** Let $J = \pi'\mathrm{Cl}(V,q)$ be a minimal right ideal, so that $J$ is a simple right module. The **right spin action** is the restriction to $\mathrm{Spin}(V,q)$ of the right action of the algebra, $\psi \mapsto \psi\,x$.

**Proposition (the transport by reversion).** Reversion maps a minimal right ideal to a minimal left ideal, $r(J) = \mathrm{Cl}(V,q)\,r(\pi')$, and it intertwines the right action with the left action by the reversed element:

$$
r(\psi\,x) = x^{r}\,r(\psi), \qquad \psi \in J .
$$

So the right spin action on $J$ is, on $r(J)$ and through $r$, the ordinary left action by $x^{r}$. Hence the right spin action is the spin representation composed with the algebra anti-automorphism $r$; it is the contragredient of the spin representation up to the group automorphism $\mathrm{inv}\circ r$ of the spin group, and the right simple modules give no irreducible representation that the left modules do not already give.

**Proof.** $r(\psi x) = r(x)r(\psi) = x^{r}r(\psi)$, using that $r$ is an anti-automorphism; that $r(J)$ is a minimal left ideal follows because $r$ is an algebra isomorphism $\mathrm{Cl}\to\mathrm{Cl}^{\mathrm{op}}$, so it exchanges left and right ideals. The comparison with the contragredient is the standard duality $x \mapsto (x^{-1})^{\mathrm{t}}$ of a finite-dimensional representation, applied to the transport just computed.

**Remark (the pairing between the two spinor spaces).** A minimal left ideal $I$ and a minimal right ideal $J$ built from complementary primitive idempotents pair through the algebra product $I\times J \to \mathrm{Cl}$, whose composition with the coefficient of the unit is a bilinear form; the left action on $I$ and the right action on $J$ are adjoint for it. The non-degeneracy of that form, the trace form behind it and the invariance under the spin group are the Hermitian structure, treated in *The Trace Form and the Hilbert Structure with Hermitian Adjoint* and in the Hermitian group, and the present article uses only the transport by reversion. The identification of the minimal right ideals with the opposite chiral halves, and the module-theoretic form of the two-half structure, are *Spin Representations and Clifford Modules with Inner Conjugation* and *Spinors as Minimal Left Ideals with Inner Conjugation*.

## Worked Cases

### The Quaternions

For $\mathrm{Cl}_{0,2}(\mathbb{R}) \cong \mathbb{H}$, reversion is the quaternion conjugation $a + bi + cj + dk \mapsto a - bi - cj - dk$ on the imaginary part, and it is an anti-automorphism with $x^{r}x = x^{2}$. The isomorphism $\mathbb{H} \to \mathbb{H}^{\mathrm{op}}$ is $x \mapsto x^{r}$, and the right regular module carries the same simple module as the left, since $\mathbb{H}$ is a division algebra.

### The Split Case $\mathrm{Cl}_{1,1}(\mathbb{R})$

With $e_1^{2} = 1$, $e_2^{2} = -1$ the algebra is $M_2(\mathbb{R})$; reversion sends a matrix to its transpose, and transposition is the isomorphism $M_2(\mathbb{R}) \to M_2(\mathbb{R})^{\mathrm{op}}$. The left ideals are the column spaces and the right ideals the row spaces, exchanged by transposition; the centre consists of the scalar matrices, and $L_a = R_a$ exactly for those, which is the corollary in the smallest matrix case.

### The Centre in Odd Dimension

For $\mathrm{Cl}_{0,3}(\mathbb{R}) \cong \mathbb{H}\oplus\mathbb{H}$ the volume element $\omega$ is central, so $L_\omega = R_\omega = \mathrm{id}$ on the algebra; the element $\omega$ acts by the same scalar $1$ on the left and on the right, and it is the smallest witness that the two regular representations agree on a non-scalar in odd dimension.

## Summary

The **right multiplication** $R_x(y) = yx$ is anti-multiplicative, $R_xR_z = R_{zx}$, so $x \mapsto R_x$ is a faithful representation of the **opposite algebra** $\mathrm{Cl}(V,q)^{\mathrm{op}}$, and its submodules are the right ideals. The opposite algebra of a Clifford algebra is itself a Clifford algebra of the same dimension, and reversion, or Clifford conjugation, is an explicit isomorphism $\mathrm{Cl} \cong \mathrm{Cl}^{\mathrm{op}}$; right modules are therefore left modules read through that isomorphism, and the two simple-module counts agree. The Clifford algebra is a bimodule under the left and the right actions, the two commute because they sit on opposite sides, and the double centraliser theorem on the regular module gives $\mathrm{End}_{\mathrm{Cl}}(\mathrm{Cl}) \cong \mathrm{Cl}^{\mathrm{op}}$ and the mutual commutants $\{L_a\}' = \{R_b\}$, $\{R_b\}' = \{L_a\}$. The centre is exactly the set where the two actions agree, and the enveloping algebra generated by both families is all of $\mathrm{End}_F(\mathrm{Cl})$ precisely in even dimension. On the spinors the left family gives the spin representation and the right family, on a minimal right ideal, gives the same representation transported by reversion, which is its dual direction up to the automorphism $\mathrm{inv}\circ r$; the two halves of the spin representation are this pair. The operator calculus is *One-Sided Operators on a Clifford Algebra*; the left-side module theory is *Left Multiplication and the Clifford Module Structure*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R_x(y) = y\,x$ | Right multiplication |
| $R_xR_z = R_{zx}$ | Anti-multiplicativity |
| $\mathrm{Cl}(V,q)^{\mathrm{op}}$ | Opposite algebra, reversed product |
| $r$, $\natural = \alpha\circ r$ | Reversion and Clifford conjugation, anti-automorphisms |
| ${}_{\mathrm{Cl}}\mathrm{Cl}_{\mathrm{Cl}}$ | The regular bimodule, commuting actions |
| $\mathrm{End}_{\mathrm{Cl}}(\mathrm{Cl}) \cong \mathrm{Cl}^{\mathrm{op}}$ | Commutant of the left regular representation |
| $Z(\mathrm{Cl}) = \{x : L_x = R_x\}$ | Centre |
| $J = \pi'\mathrm{Cl}(V,q)$ | Minimal right ideal, dual spinor space |
| $\psi \mapsto \psi\,x$ | Right spin action, the dual direction |

## Further Reading

- Claude Chevalley, *The Algebraic Theory of Spinors and Clifford Algebras*, Collected Works vol. 2 (Springer, 1997), for the regular bimodule and the two regular representations of a Clifford algebra.
- Richard S. Pierce, *Associative Algebras*, Graduate Texts in Mathematics 88 (Springer, 1982), for the opposite algebra, the regular bimodule and the double centraliser theorem.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups*, Cambridge Studies in Advanced Mathematics 50 (Cambridge University Press, 1995), for reversion, conjugation and the anti-automorphisms of a Clifford algebra.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for the duality between the spin representation and its contragredient.
- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd ed. (Cambridge University Press, 2001), for reversion and conjugation in the low-dimensional algebras.
