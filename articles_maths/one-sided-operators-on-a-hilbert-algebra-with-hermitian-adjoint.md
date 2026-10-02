
# __One-Sided Operators on a Hilbert Algebra with Hermitian Adjoint__

## Introduction

Every two-sided operator of *Two-Sided Operators on a Clifford Algebra* is a product of two factors, one multiplying on the left and one on the right. This article treats the factors themselves. A **one-sided operator** is a left multiplication $y\mapsto a\,y$ or a right multiplication $y\mapsto y\,b$, together with the variants in which the multiplying element is replaced by its image under the grade involution or by its image under an anti-involution. The one-sided operators are the elementary operators out of which the two-sided family is built, and they are the operators for which the Hermitian adjoint has the cleanest form.

Two facts organise the theory. The first is that the two one-sided families are separately multiplicative, with the same order of composition, even though the right factor carries an anti-automorphism; this is why a product of two elements gives the composites in both families and why the homogeneity of a two-sided operator follows from its two factors. The second is that the **adjoint of a one-sided operator is the one-sided operator of the dagger**: $L_a^{*} = L_{a^{\dagger}}$ and $R_b^{*} = R_{b^{\dagger}}$. From that identity the whole Hermitian theory of the one-sided operators follows in three lines: an operator is self-adjoint when its element is, it is skew-adjoint when its element is, and it is unitary exactly when its element lies in the unitary slice. The left and the right multiplications are mutual commutants, and the algebra they generate is the image of the enveloping algebra $\mathrm{Cl}(V,q)\otimes_F\mathrm{Cl}(V,q)^{\mathrm{op}}$, which is the whole endomorphism algebra exactly when the Clifford algebra is central simple over the base and a proper subalgebra otherwise; this is the double centraliser theorem read in this setting, and the failure of generation is worked out in *One-Sided Operators on a Clifford Algebra*.

The algebra and the dagger are *Hilbert Algebras*; the two-sided family and the composition law are *Two-Sided Operators on a Clifford Algebra*; the scalar forms and the adjoints of left and right multiplication are *The Blade Form and the Hilbert Structure with Hermitian Adjoint*, from which the identity $L_x^{*} = L_{x^{\dagger}}$ is taken; the Hermitian structures on modules are *Hermitian Modules over a Hilbert Algebra with Hermitian Adjoint*; the unitary slice is *The Unitary Slice and the Compact Real Form with Hermitian Adjoint*; the left ideals and the spinor module are *Spinors as Minimal Left Ideals with Inner Conjugation*; and the adjoint of the one-sided action on a module is *The Adjoint of the One-Sided Action with Hermitian Adjoint*.

## The Two One-Sided Families

### Definitions

**Definition.** Let $\theta$ be an automorphism of $\mathrm{Cl}(V,q)$ and let $c$ be an anti-automorphism, with $c(xz) = c(z)c(x)$ and $c(1) = 1$. For $x \in \mathrm{Cl}(V,q)$ the **left one-sided operator** and the **right one-sided operator** attached to $x$ are

$$
\Lambda^{\theta}_x(y) = \theta(x)\,y, \qquad \qquad \mathrm P^{c}_x(y) = y\,c(x).
$$

With $\theta = \mathrm{id}$ and $\theta = \alpha$ this gives the left multiplications $L_x$ and the signed left multiplication $L_{\alpha(x)}$; with $c = \mathrm{id}$, $c = r$, $c = \bar\cdot$ and $c = {}^{\dagger}$ it gives the right multiplications $R_x$, $R_{x^{r}}$, $R_{x^{\natural}}$ and $R_{x^{\dagger}}$. The inverse variants $y\mapsto y\,x^{-1}$ are defined on the units.

**Proposition (composition laws).** Both families are multiplicative with the same order:

$$
\Lambda^{\theta}_{xz} = \Lambda^{\theta}_x\circ\Lambda^{\theta}_z, \qquad \qquad \mathrm P^{c}_{xz} = \mathrm P^{c}_x\circ\mathrm P^{c}_z .
$$

**Proof.** For the left family, $\Lambda^{\theta}_x(\Lambda^{\theta}_z(y)) = \theta(x)\theta(z)y = \theta(xz)y$, using that $\theta$ is an automorphism. For the right family, $\mathrm P^{c}_x(\mathrm P^{c}_z(y)) = \mathrm P^{c}_x(y\,c(z)) = y\,c(z)c(x) = y\,c(xz)$, using that $c$ is an anti-automorphism; the reversal in $c$ is compensated by the reversal of the order of composition, which is the reason both families compose in the same order.

**Proposition (commutation, and the two-sided operator).** Left and right one-sided operators commute,

$$
\Lambda^{\theta}_x\circ\mathrm P^{c}_z = \mathrm P^{c}_z\circ\Lambda^{\theta}_x ,
$$

and the two-sided operator of *Two-Sided Operators on a Clifford Algebra* is their product,

$$
\Phi^{\theta,c}_x = \Lambda^{\theta}_x\circ\mathrm P^{c}_x = L_{\theta(x)}\,R_{c(x)} .
$$

**Proof.** $(\theta(x)y)c(z) = \theta(x)(yc(z))$ by associativity, and the two-sided operator is the product by its definition.

**Corollary (composition of two-sided operators, again).** The composition law $\Phi^{\theta,c}_{xz} = \Phi^{\theta,c}_x\circ\Phi^{\theta,c}_z$ follows from the two composition laws above and the commutation: $\Phi_x\Phi_z = \Lambda^{\theta}_x\mathrm P^{c}_x\Lambda^{\theta}_z\mathrm P^{c}_z = \Lambda^{\theta}_{xz}\mathrm P^{c}_{xz} = \Phi_{xz}$. So the multiplicativity of the two-sided family is a consequence of the multiplicativity of its two one-sided factors, and the order of the factors in the composite is immaterial.

## The Hermitian Adjoint of a One-Sided Operator

### The Adjoint

**Theorem.** With respect to the form $(x,y) = \mathrm{Sc}(x^{\dagger}y)$ of the regular module, the adjoint of a one-sided operator is the one-sided operator of the dagger:

$$
\bigl(\Lambda^{\theta}_x\bigr)^{*} = \Lambda^{\theta}_{x^{\dagger}} , \qquad \qquad \bigl(\mathrm P^{c}_x\bigr)^{*} = \mathrm P^{c}_{x^{\dagger}} .
$$

In particular $L_a^{*} = L_{a^{\dagger}}$ and $R_b^{*} = R_{b^{\dagger}}$.

**Proof.** For the left multiplication,

$$
(L_ax, y) = \mathrm{Sc}\bigl((ax)^{\dagger}y\bigr) = \mathrm{Sc}\bigl(x^{\dagger}a^{\dagger}y\bigr) = (x, a^{\dagger}y) = (x, L_{a^{\dagger}}y),
$$

using that the dagger is an anti-involution and that $\mathrm{Sc}(uv) = \mathrm{Sc}(vu)$. For the right multiplication,

$$
(R_bx, y) = \mathrm{Sc}\bigl((xb)^{\dagger}y\bigr) = \mathrm{Sc}\bigl(b^{\dagger}x^{\dagger}y\bigr) = \mathrm{Sc}\bigl(x^{\dagger}\,y\,b^{\dagger}\bigr) = (x, R_{b^{\dagger}}y),
$$

where the middle equality moves the factor $b^{\dagger}$ past the product by two applications of cyclicity of the scalar part. The statements for $\Lambda^{\theta}$ and $\mathrm P^{c}$ follow by substituting $a = \theta(x)$ and $b = c(x)$.

**Remark (why the dagger and not the conjugate element).** The adjoint is the one-sided operator of the **dagger** of the element, not of the element itself and not of the other anti-involution: reversion gives the adjoint for the blade form, the dagger gives the adjoint for the form of the dagger, and the two differ by the parity sign as in *The Blade Form and the Hilbert Structure with Hermitian Adjoint*. A sibling must use the dagger for the form $\mathrm{Sc}(x^{\dagger}y)$ and reversion for the form $\mathrm{Sc}(x^{r}y)$.

### Self-Adjoint, Skew and Unitary One-Sided Operators

**Corollary.** For $a \in \mathrm{Cl}(V,q)$,

$$
L_a \text{ is self-adjoint} \iff a^{\dagger} = a, \qquad
L_a \text{ is skew-adjoint} \iff a^{\dagger} = -a, \qquad
L_a \text{ is unitary} \iff a^{\dagger}a = 1,
$$

and the same with $R_a$ in place of $L_a$.

**Proof.** Immediate from the theorem; unitarity means $L_a^{*}L_a = \mathrm{id}$, that is $L_{a^{\dagger}a} = \mathrm{id}$, that is $a^{\dagger}a = 1$ by the injectivity of $a\mapsto L_a$ proved below.

**Corollary (the slice and the vectors).** The left multiplications by the elements of the unitary slice are the unitary one-sided operators, so $a\mapsto L_a$ restricts to a unitary representation $U\to \mathrm U(\mathrm{Cl}(V,q),(\cdot,\cdot))$ of the slice; and **every vector acts by a skew-adjoint operator**, $L_v^{*} = L_{v^{\dagger}} = -L_v$, because the dagger negates the vectors. When the involution is positive, a vector also satisfies $v^{\dagger}v = -v^{2} = q(v)\cdot(-1)$, so $L_v$ is unitary exactly on the norm-one vectors, and the left multiplications by an orthonormal frame are the **complex structures** of the algebra: each is skew-adjoint, unitary and of square $-1$.

### The Generated $*$-Algebra

**Theorem (the commutants and the generated algebra).** The two families are mutual commutants,

$$
\{L_a : a \in A\}' = \{R_b : b \in A\}, \qquad \{R_b : b \in A\}' = \{L_a : a \in A\},
$$

so the bicommutant of each family is itself, and the $F$-algebra generated by the two is the image of the enveloping algebra

$$
\langle L_a, R_b\rangle = \mathrm{Im}\bigl(A\otimes_FA^{\mathrm{op}}\to \mathrm{End}_F(A)\bigr), \qquad a\otimes b^{\mathrm{op}}\mapsto L_aR_b .
$$

That image is all of $\mathrm{End}_F(\mathrm{Cl}(V,q))$, of dimension $(\dim_F\mathrm{Cl})^{2}$, exactly when the Clifford algebra is **central simple** over $F$; otherwise it is a proper subalgebra, the endomorphisms over the centre $\mathrm{End}_{Z(A)}(A)$ of dimension $(\dim_F A)^{2}/[Z(A):F]$. For a non-degenerate form over a field of characteristic not two this is all of $\mathrm{End}_F$ exactly for even $n$, while for odd $n$ the volume element supplies a centre of degree two and only half of $\mathrm{End}_F$ is generated: on $\mathrm{Cl}_{0,3}(\mathbb{R})\cong\mathbb{H}\oplus\mathbb{H}$ the products $L_aR_b$ span a space of dimension $32$, while $\mathrm{End}_F$ has dimension $64$. The left multiplications alone form a subalgebra isomorphic to the opposite algebra of the Clifford algebra, and the right multiplications alone its commutant.

**Proof.** The left and the right multiplications commute, and $L_aR_b(1) = ab$, so the image of $A\otimes_FA^{\mathrm{op}}$ in $\mathrm{End}_F(A)$ is exactly the algebra generated by the two families. The map is **not** injective in general: $\sum_ia_i\otimes b_i^{\mathrm{op}}$ is killed precisely when $\sum_i a_ixb_i = 0$ for every $x$, which is what the dimension count of the counterexample detects. When $A$ is central simple $A\otimes_FA^{\mathrm{op}}\cong\mathrm{End}_F(A)$, by the dimension count $\dim(A\otimes_FA^{\mathrm{op}}) = (\dim A)^{2} = \dim\mathrm{End}_F(A)$ and injectivity; the $*$-structure is $(L_aR_b)^{*} = R_{b^{\dagger}}L_{a^{\dagger}} = L_{a^{\dagger}}R_{b^{\dagger}}$ of the theorem above, so in the central simple case the generated algebra is closed under the adjoint.

**Remark (the regular representation is a $*$-representation).** The left multiplications alone give the **regular representation** $a\mapsto L_a$ of the Clifford algebra on itself, which by the theorem above is a $*$-representation in the sense of *Hermitian Modules over a Hilbert Algebra with Hermitian Adjoint*, since $L_{a^{\dagger}} = L_a^{*}$. The right multiplications give the opposite representation, the commutant, corresponding to the bimodule structure; the two together generate the endomorphisms over the centre, the whole endomorphism algebra exactly in the central simple case.

## Images, Kernels and Ideals

**Proposition.** For every $a$,

$$
L_a(1) = a, \qquad R_a(1) = a,
$$

so $a\mapsto L_a$ and $a\mapsto R_a$ are injective $F$-linear maps; and

$$
\ker L_a = \{\, y : ay = 0 \,\}, \qquad \ker R_a = \{\, y : ya = 0 \,\}
$$

are the left and right annihilators of $a$.

**Proposition (the images are ideals).** The image of a right multiplication is a **left** ideal and the image of a left multiplication is a **right** ideal:

$$
R_a\bigl(\mathrm{Cl}\bigr) = \mathrm{Cl}\cdot a, \qquad L_a\bigl(\mathrm{Cl}\bigr) = a\cdot \mathrm{Cl} .
$$

**Proof.** $R_a(y) = ya$ and $x(ya) = (xy)a$ is again of the form $y'a$, so $\mathrm{Cl}\cdot a$ is closed under left multiplication; $L_a(y) = ay$ and $(ay)x = a(yx)$ makes $a\cdot\mathrm{Cl}$ a right ideal.

**Corollary (the spinor module as an image).** If $\pi$ is a primitive idempotent then $R_\pi$ has image the minimal left ideal $\mathrm{Cl}\,\pi$ and kernel the complementary ideal, so the spinor module of *Spinors as Minimal Left Ideals with Inner Conjugation* is the image of the one-sided operator $R_\pi$, and the one-sided operator $L_\pi$ has image the complementary minimal right ideal. This is the reason the adjoint of the one-sided action is the operator-theoretic starting point of *The Adjoint of the One-Sided Action with Hermitian Adjoint*.

## Worked Cases

### The Positive Case: the Quaternion Algebra

Let $\mathrm{Cl}_{0,2}(\mathbb{R}) = \mathbb{H}$ with $e_1^{2} = e_2^{2} = -1$ and the dagger positive, so $v^{\dagger} = -v$ for every vector. For a vector $v$, $v^{\dagger}v = -v^{2} = 1$, so the left and right multiplications $L_v$ and $R_v$ are **unitary**; and $v^{\dagger} = -v$ makes them **skew-adjoint**, while $v^{2} = -1$ makes them of **square $-1$**:

$$
L_v^{*} = -L_v, \qquad L_v^{2} = L_{-1} = -\,\mathrm{id}, \qquad (L_vx, L_vy) = (x,y).
$$

So each of $L_{e_1}, L_{e_2}, L_{e_1e_2}$ is simultaneously skew-adjoint, unitary and a complex structure on the four-dimensional real space $\mathbb{H}$, and they satisfy the quaternion relations $L_{e_1}L_{e_2} = L_{e_1e_2}$. The vectors therefore give the three almost complex structures that make the quaternion algebra a module over the quaternions, all of them one-sided operators.

### The Split Case: an Involution

Let $\mathrm{Cl}_{1,1}(\mathbb{R})$ with $e_1^{2} = 1$, $e_2^{2} = -1$ and the dagger indefinite. Then $e_1^{\dagger} = -e_1$ and $e_1^{2} = 1$, so

$$
L_{e_1}^{*} = -L_{e_1}, \qquad L_{e_1}^{2} = \mathrm{id},
$$

a skew-adjoint involution; it is not unitary, and its action on the form reverses the sign, $(L_{e_1}x, L_{e_1}y) = -(x,y)$, because $e_1^{\dagger}e_1 = -e_1^{2} = -1$. The same vector is a unit of $\Gamma(V,q)$ with norm $1$ and gives an honest reflection on $V$, so the one-sided operator and the two-sided operator divide the labour: the two-sided signed inner conjugation by $e_1$ is the reflection, while the one-sided $L_{e_1}$ is a skew-adjoint involution of the whole algebra that reverses the sign of the Hermitian form.

## Summary

A **one-sided operator** on a Clifford algebra is a left multiplication $\Lambda^{\theta}_x(y) = \theta(x)y$ or a right multiplication $\mathrm P^{c}_x(y) = y\,c(x)$ attached to an automorphism $\theta$ and an anti-automorphism $c$. Both families are **multiplicative with the same order**, $\Lambda^{\theta}_{xz} = \Lambda^{\theta}_x\Lambda^{\theta}_z$ and $\mathrm P^{c}_{xz} = \mathrm P^{c}_x\mathrm P^{c}_z$, because the reversal inside $c$ is cancelled by the reversal of the order of composition; left and right operators commute, and the two-sided operator is their product, $\Phi^{\theta,c}_x = \Lambda^{\theta}_x\mathrm P^{c}_x$, so the multiplicativity of the two-sided family is inherited from its factors.

With respect to the form $(x,y) = \mathrm{Sc}(x^{\dagger}y)$ the **adjoint of a one-sided operator is the one-sided operator of the dagger**, $L_a^{*} = L_{a^{\dagger}}$ and $R_b^{*} = R_{b^{\dagger}}$, whence a one-sided operator is self-adjoint, skew-adjoint or unitary exactly when its element is self-adjoint, skew-adjoint or in the unitary slice; every vector acts by a skew-adjoint operator, and in the positive case by a skew-adjoint unitary complex structure. The left multiplications give the **regular $*$-representation**, the right multiplications its commutant, and the two together generate the image of the enveloping algebra $\mathrm{Cl}\otimes_F\mathrm{Cl}^{\mathrm{op}}$, which is all of $\mathrm{End}_F(\mathrm{Cl}(V,q))$ exactly when the Clifford algebra is central simple and a proper subalgebra otherwise. Finally $L_a(1) = R_a(1) = a$, so both maps are injective; the kernel of a one-sided operator is an annihilator and its image an ideal, and the spinor module is the image of $R_\pi$ for a primitive idempotent $\pi$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Lambda^{\theta}_x(y) = \theta(x)y$ | Left one-sided operator |
| $\mathrm P^{c}_x(y) = y\,c(x)$ | Right one-sided operator |
| $L_a$, $R_b$ | Ordinary left and right multiplication |
| $\Lambda^{\theta}_{xz} = \Lambda^{\theta}_x\Lambda^{\theta}_z$, $\mathrm P^{c}_{xz} = \mathrm P^{c}_x\mathrm P^{c}_z$ | Composition laws |
| $\Phi^{\theta,c}_x = \Lambda^{\theta}_x\mathrm P^{c}_x$ | Two-sided operator as a product of one-sided ones |
| $L_a^{*} = L_{a^{\dagger}}$, $R_b^{*} = R_{b^{\dagger}}$ | Adjoints with respect to $\mathrm{Sc}(x^{\dagger}y)$ |
| $\langle L_a, R_b\rangle = \mathrm{Im}(\mathrm{Cl}\otimes\mathrm{Cl}^{\mathrm{op}})$ | Generated algebra; $=\mathrm{End}_F$ iff central simple |
| $\mathrm{Cl}\cdot a$, $a\cdot\mathrm{Cl}$ | Left and right ideals, images of $R_a$ and $L_a$ |

## Further Reading

- Ian R. Porteous, *Clifford Algebras and the Classical Groups*, Cambridge Studies in Advanced Mathematics 50 (Cambridge University Press, 1995), for the left and right multiplications and the regular representations.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for the Clifford action, its adjoint and the self-adjointness of the Dirac operator.
- Nathan Jacobson, *Structure of Rings*, American Mathematical Society Colloquium Publications 37 (American Mathematical Society, 1956), for the double centraliser theorem and the regular representations of a finite-dimensional algebra.
- Richard S. Pierce, *Associative Algebras*, Graduate Texts in Mathematics 88 (Springer, 1982), for the left and right regular representations, annihilators and the Frobenius structure.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for algebras with involution acting on themselves and the adjoint of the regular representation.
