
# __Split-Quaternion Operator Representation__

## Introduction

A split-quaternion acts on the algebra in several ways: by left multiplication, by right multiplication, and by the **adjoint** (or sandwich) action $\tilde q \mapsto g \tilde q g^{-1}$. The first two are linear endomorphisms realizing the algebra in $\operatorname{End}(\mathbb{H}_{\mathrm{s}})$; the third is an algebra automorphism of the algebra, and its restriction to the vector subspace is the Lorentz action of signature $(2,1)$. This article treats these operators, their kernels, the double cover of the Lorentz group they produce, and their action on the distinguished subspaces.

The article owns the operator realizations: the left and right multiplication operators, the adjoint operator and its automorphism property, its kernel, the Lorentz action on $V$, the double cover of the Lorentz group by the norm-one slice, the table of the action on the distinguished subspaces, and the relation to the polar representation. It relies on *Split-Quaternion Rotations and the Lorentz Group* for the group-theoretic facts it quotes and on *Split-Quaternion Polar Representation* for the polar form.

**Conventions.** The algebra is $\mathbb{H}_{\mathrm{s}}$, with basis $1, e_1, e_2, e_3$, norm $N(\tilde q) = q_0^2 + q_1^2 - q_2^2 - q_3^2$, inverse $\tilde q^{-1} = \bar{\tilde q}/N(\tilde q)$ for $N(\tilde q) \neq 0$, and the matrix model $\Phi : \mathbb{H}_{\mathrm{s}} \to M_2(\mathbb{R})$. The vector subspace is $V = \operatorname{span}\{e_1,e_2,e_3\}$ with the restricted form $N|_V = q_1^2 - q_2^2 - q_3^2$ of signature $(2,1)$, and the distinguished subspaces $S, \mathbb{D}_2, \mathbb{D}_3$ are as in *Split-Quaternion Relations Between Subspaces*. All endomorphisms below are $\mathbb{R}$-linear.

## The Element as an Operator on the Algebra

**Definition.** For $\tilde q \in \mathbb{H}_{\mathrm{s}}$ the **left multiplication operator** and the **right multiplication operator** are

$$
L_{\tilde q} : y \mapsto \tilde q y, \qquad R_{\tilde q} : y \mapsto y\tilde q .
$$

Both are $\mathbb{R}$-linear endomorphisms of the four-dimensional space $\mathbb{H}_{\mathrm{s}}$, and the maps $\tilde q \mapsto L_{\tilde q}$ and $\tilde q \mapsto R_{\tilde q}$ are $\mathbb{R}$-algebra homomorphisms into $\operatorname{End}_{\mathbb{R}}(\mathbb{H}_{\mathrm{s}})$; the first is the **left regular representation**.

**Proposition.** Both $L_{\tilde q}$ and $R_{\tilde q}$ have trace $4 \operatorname{Sc}(\tilde q) = 4q_0$ and determinant $N(\tilde q)^2$, and $L_{\tilde q}$ is invertible if and only if $\tilde q$ is a unit, i.e. if and only if $N(\tilde q) \neq 0$.

**Proof.** Under the matrix model, left multiplication by $\tilde q$ on $\mathbb{H}_{\mathrm{s}}$ corresponds to left multiplication by the matrix $\Phi(\tilde q)$ on $M_2(\mathbb{R}) \cong \mathbb{R}^4$, whose eigenvalues are the two eigenvalues $\lambda_1, \lambda_2$ of $\Phi(\tilde q)$, each with multiplicity two. Hence $\operatorname{tr} L_{\tilde q} = 2(\lambda_1 + \lambda_2) = 2\operatorname{tr}\Phi(\tilde q) = 4q_0$ and $\det L_{\tilde q} = (\lambda_1\lambda_2)^2 = \det\Phi(\tilde q)^2 = N(\tilde q)^2$. The eigenvalues satisfy $\lambda^2 - 2q_0\lambda + N(\tilde q) = 0$, so their sum is $2q_0$ and their product is $N(\tilde q)$. Finally $L_{\tilde q}$ is invertible if and only if $\tilde q$ is not a zero divisor (since $L_{\tilde q}(y) = \tilde q y$ and the algebra has no nonzero $\tilde q$ with $\tilde q y = 0$ for all $y$), which holds if and only if $N(\tilde q) \neq 0$.

**Remark.** The factor $N(\tilde q)^2$ and the doubled eigenvalues are the operator form of the double cover: left multiplication by $\tilde q$ and by $-\tilde q$ have the same determinant and, below, the same adjoint action on $V$.

## The Adjoint Operator

**Definition.** For a unit $g$ the **adjoint operator** is

$$
\operatorname{Ad}_g : \tilde q \mapsto g \tilde q g^{-1}.
$$

Since $g^{-1} = \bar{g}/N(g)$, the operator is $\operatorname{Ad}_g(\tilde q) = g\,\tilde q\,\bar{g}/N(g)$, and for $N(g) = 1$ it is $\operatorname{Ad}_g(\tilde q) = g \tilde q \bar{g}$.

**Theorem.** For every unit $g$, the adjoint operator $\operatorname{Ad}_g$ is an $\mathbb{R}$-**algebra automorphism** of $\mathbb{H}_{\mathrm{s}}$. The map $g \mapsto \operatorname{Ad}_g$ is a group homomorphism from the group of units $\mathbb{H}_{\mathrm{s}}^\times$ onto the inner automorphism group $\operatorname{Inn}(\mathbb{H}_{\mathrm{s}}) \cong \mathrm{PGL}_2(\mathbb{R})$.

**Proof.** It is linear (being a composite of linear maps), multiplicative, $\operatorname{Ad}_g(\tilde q y) = g \tilde q y g^{-1} = (g\tilde q g^{-1})(g y g^{-1})$, unital, and invertible with inverse $\operatorname{Ad}_{g^{-1}}$, so it is an automorphism. The homomorphism property $\operatorname{Ad}_{gh} = \operatorname{Ad}_g \operatorname{Ad}_h$ is immediate, and the image is by definition the inner automorphism group, computed under $\Phi$ as the conjugations of $M_2(\mathbb{R})$, which is $\mathrm{PGL}_2(\mathbb{R})$.

### Comparison With Left Multiplication

Left multiplication $L_g$ is **not** an algebra automorphism: it does not send $1$ to $1$ unless $g = 1$, and under it the scalar line $S$ maps to $\mathbb{R} g$, generally not to $S$. The adjoint operator, by contrast, fixes $S$ pointwise. Left multiplication realises the algebra as operators on itself and has a kernel consisting only of $0$ (the algebra is simple and not a zero divisor ring, so $L_g = 0$ only for $g = 0$); the adjoint operator realises the unit group as automorphisms and has the centre as its kernel.

## The Kernel and the Centre

**Proposition.** The kernel of the homomorphism $g \mapsto \operatorname{Ad}_g$ on the group of units is the centre $\mathbb{R}^\times \cdot 1$, consisting of the nonzero scalars.

**Proof.** $\operatorname{Ad}_g = \operatorname{id}$ means $g\tilde q = \tilde q g$ for all $\tilde q$, i.e. $g \in Z(\mathbb{H}_{\mathrm{s}}) = S = \mathbb{R}\cdot 1$. A scalar is a unit exactly when it is nonzero.

Consequently the inner automorphism group is $\mathbb{H}_{\mathrm{s}}^\times / \mathbb{R}^\times \cong \mathrm{PGL}_2(\mathbb{R})$, of dimension $3$ over $\mathbb{R}$. Two units induce the same automorphism exactly when they differ by a nonzero scalar, $g' = \lambda g$, so the automorphism sees only the class $[g] \in \mathrm{PGL}_2(\mathbb{R})$. In particular $g$ and $-g$ induce the same automorphism.

## The Action on the Vector Subspace Is the Lorentz Action

The adjoint operator preserves the vector subspace: if $\tilde q \in V$ then $g\tilde q g^{-1}$ has zero scalar part, because $\operatorname{tr}\Phi(g\tilde q g^{-1}) = \operatorname{tr}\Phi(\tilde q) = 0$. Restricting, $\operatorname{Ad}_g$ acts on $V$.

**Theorem.** For every unit $g$, the restriction $\operatorname{Ad}_g|_V$ preserves the restricted form $N|_V = q_1^2 - q_2^2 - q_3^2$ of signature $(2,1)$. Hence the map

$$
\operatorname{Ad} : \mathbb{H}_{\mathrm{s}}^\times \longrightarrow O(2,1), \qquad g \mapsto \operatorname{Ad}_g|_V,
$$

is a group homomorphism with kernel $\mathbb{R}^\times$ whose image is $SO(2,1)$, and it is surjective onto $SO(2,1)$; on the norm-one slice it is surjective onto the identity component $\mathrm{SO}^{+}(2,1)$.

**Proof.** The split-quaternion norm is multiplicative and $\operatorname{Ad}_g$ is an automorphism, so $N(g\tilde q g^{-1}) = N(g)N(\tilde q)N(g^{-1}) = N(\tilde q)$; since $\operatorname{Ad}_g$ preserves $V$, the restricted form is preserved, giving the map to $O(2,1)$. For a unit $g$ the inner automorphism $\operatorname{Ad}_g$ of $M_2(\mathbb{R})$ has determinant $+1$ as a transformation of $\mathrm{SL}_2(\mathbb{R})$, so the image lies in $SO(2,1)$; the group of units has two components, $\{N>0\}$ and $\{N<0\}$, and the image is the union of their images, which is all of $SO(2,1)$ because $SO(2,1)$ has exactly two components and the image meets both. Restricting to the connected norm-one group $U = \{N=1\}$ gives a connected image containing the identity, hence the identity component $\mathrm{SO}^{+}(2,1)$, as computed in *Split-Quaternion Rotations and the Lorentz Group*.

The generated transformations are the rotations and boosts computed in *Split-Quaternion Rotations and the Lorentz Group*: the elliptic subgroup from $\mathbb{R}[e_1]$ acts as rotations of the plane $\operatorname{span}\{e_2,e_3\}$ by the doubled angle, and the hyperbolic subgroups from $\mathbb{D}_2, \mathbb{D}_3$ act as boosts of the planes $\operatorname{span}\{e_1,e_3\}$ and $\operatorname{span}\{e_1,e_2\}$.

## The Kernel on the Unit-Norm Slice and the Double Cover

The whole group of units acts with kernel $\mathbb{R}^\times$; on the **unit-norm slice**

$$
\mathrm{SL}_2(\mathbb{R}) = \{\, g : N(g) = 1 \,\},
$$

which is the norm-one group of *Split-Quaternion Norm and Invertibility*, the kernel is smaller and the cover is two-to-one.

**Theorem (the double cover).** The homomorphism $\operatorname{Ad} : \mathrm{SL}_2(\mathbb{R}) \to \mathrm{SO}^{+}(2,1)$ is surjective and has kernel $\{\pm 1\}$, so

$$
\mathrm{SL}_2(\mathbb{R}) / \{\pm 1\} \cong \mathrm{PSL}_2(\mathbb{R}) \cong \mathrm{SO}^{+}(2,1)
$$

is a **double cover** of the identity component of the Lorentz group. The nontrivial deck transformation is $g \mapsto -g$.

**Proof.** On the slice the kernel is $(\mathbb{R}^\times\cdot1) \cap \mathrm{SL}_2(\mathbb{R}) = \{\lambda : \lambda^2 = 1\} = \{\pm 1\}$. Surjectivity onto $\mathrm{SO}^{+}(2,1)$ is the previous theorem restricted to the slice, which is the connected component of the identity in the group of units and maps onto the connected component $\mathrm{SO}^{+}(2,1)$ of $SO(2,1)$.

The element $-1$ is the unique nontrivial unit of norm $1$ acting trivially on $V$; it represents a full turn of the "rotor" and is the reason the parametrisation by angles is at the doubled angle. In physical language this is the spin double cover, but here it is a statement about $M_2(\mathbb{R})$.

## The Action on the Distinguished Subspaces

The adjoint operator acts on the distinguished subspaces as follows.

| subspace | image under $\operatorname{Ad}_g$ | preserved? | remark |
|---|---|---|---|
| $S = \mathbb{R}\cdot 1$ | $S$ | yes, pointwise | the centre is fixed |
| $V = \operatorname{span}\{e_1,e_2,e_3\}$ | $V$ | yes | the Lorentz action of signature $(2,1)$ |
| a line $\mathbb{R} v \subset V$ | a line $\mathbb{R}\,\operatorname{Ad}_g(v)$ | yes as a class | the split-quaternion norm sign of $v$ is preserved |
| $\mathbb{D}_2 = \operatorname{span}\{1,e_2\}$ | a conjugate split-complex plane | only if $g$ normalises it | automorphisms permute the split-complex planes |
| $\mathbb{D}_3 = \operatorname{span}\{1,e_3\}$ | a conjugate split-complex plane | only if $g$ normalises it | as above |
| $\mathbb{H}_{\mathrm{s}} \tilde\pi_\pm$ | a minimal left ideal | only if $g$ normalises it | idempotents map to idempotents |

The first two rows are the content of the previous section. The remaining rows record that an automorphism sends a subalgebra to a subalgebra of the same isomorphism type: the split-complex planes are permuted among themselves (as all split Cartan subalgebras of $M_2(\mathbb{R})$ are conjugate), and a unit normalizes a given plane exactly when it preserves the pair of isotropic lines of that plane. The idempotents of the algebra form an orbit-like set under the automorphism group, and the minimal left ideals are permuted accordingly; this is developed alongside the idempotent theory in *Split-Quaternion Ideals and Peirce Decomposition*.

## Orbits and Invariants

The adjoint action on $V$ has the invariants of the Lorentz action: the split-quaternion norm $N|_V$ itself, and no others in general position. The adjoint action of the group of units has image the full Lorentz group $\mathrm{SO}(2,1)$, not only its identity component: a negative-norm unit such as $e_2$ acts on $V$ as $\operatorname{diag}(-1,1,-1)$, which has determinant $+1$ and reverses the sheets. The orbits on $V \setminus \{0\}$ are therefore the three **orbit types**

$$
\{v : N(v) > 0\}, \qquad \{v : N(v) = 0\} \setminus \{0\}, \qquad \{v : N(v) < 0\},
$$

the two-sheeted timelike hyperboloid, the light cone minus its vertex, and the spacelike one-sheeted hyperboloid; under the identity component $\mathrm{SO}^{+}(2,1)$, which preserves the sign of the time coordinate $q_1$, the first two sets split into their two sheets and their two nappes, giving five orbits. On the full algebra the invariants of $\operatorname{Ad}_g$ are the scalar part $q_0$ and the split-quaternion norm $N(\tilde q)$, since the scalar part is fixed by every adjoint operator; the adjoint action therefore acts trivially on $S$ and by the Lorentz action on $V$, with no mixing between the two, because it preserves each.

## The Relation to the Polar Representation

Every nonzero split-quaternion has a **polar representation** $\tilde q = \rho\, u$ with $\rho = \sqrt{|N(\tilde q)|} > 0$ and $u$ a unit of norm $\pm 1$, as in *Split-Quaternion Polar Representation*. In this representation the operator content of $\tilde q$ splits: the positive scalar $\rho$ contributes the scale factor $L_\rho = \rho \operatorname{id}$, and the unit part $u$ contributes the adjoint automorphism $\operatorname{Ad}_u$, which is the Lorentz transformation that the element carries. Left multiplication by $\tilde q$ is therefore the composite of a scaling and an operator whose restriction to $V$ is a Lorentz transformation of signature $(2,1)$; the explicit form of the polar factor for each of the three sign types ($N > 0$, $N < 0$, $N = 0$) is the subject of the polar article, and the operator here carries the action on $V$.

## Summary

A split-quaternion $\tilde q$ acts on the algebra by left multiplication $L_{\tilde q}$ and right multiplication $R_{\tilde q}$, both linear endomorphisms of trace $4q_0$ and determinant $N(\tilde q)^2$, and by the adjoint operator $\operatorname{Ad}_g : \tilde q \mapsto g\tilde q g^{-1}$ for a unit $g$. The adjoint operator is an algebra automorphism; the map $g \mapsto \operatorname{Ad}_g$ has kernel the centre $\mathbb{R}^\times$ and image $\operatorname{Inn}(\mathbb{H}_{\mathrm{s}}) \cong \mathrm{PGL}_2(\mathbb{R})$, so it depends only on the class of $g$ modulo scalars and in particular $\operatorname{Ad}_g = \operatorname{Ad}_{-g}$.

The adjoint operator preserves the vector subspace $V$ and the restricted form $N|_V = q_1^2-q_2^2-q_3^2$ of signature $(2,1)$, so it realises the Lorentz group; on the unit-norm slice $\mathrm{SL}_2(\mathbb{R})$ the kernel shrinks to $\{\pm 1\}$ and the map is a double cover $\mathrm{SL}_2(\mathbb{R}) \to \mathrm{SO}^{+}(2,1)$, with deck transformation $g \mapsto -g$ and the angle doubling of the rotor. On the distinguished subspaces, $S$ is fixed pointwise and $V$ is preserved and acted on by Lorentz transformations, while the split-complex planes and the minimal left ideals are permuted among their conjugates and are preserved only by units that normalize them. The orbits on $V \setminus \{0\}$ under the adjoint action of the unit group are the two-sheeted timelike hyperboloid, the light cone minus its vertex and the spacelike one-sheeted hyperboloid; under the identity component $\mathrm{SO}^{+}(2,1)$, which is the image of the norm-one group, the first two split into two orbits each. The scale of a nonzero element is carried by its polar modulus and the Lorentz transformation it generates by its unit part.

## Summary of Notation

| Symbol | Meaning | Article |
|---|---|---|
| $\mathbb{H}_{\mathrm{s}}$ | the split-quaternion algebra | *Split-Quaternion Algebra* |
| $L_{\tilde q}, R_{\tilde q}$ | left and right multiplication operators | this article |
| $\operatorname{Ad}_g(\tilde q) = g\tilde q g^{-1}$ | the adjoint (sandwich) operator | this article |
| $g$ | a unit, $N(g) \neq 0$ | *Split-Quaternion Norm and Invertibility* |
| $\operatorname{Inn}(\mathbb{H}_{\mathrm{s}}) \cong \mathrm{PGL}_2(\mathbb{R})$ | the inner automorphism group | this article |
| $Z(\mathbb{H}_{\mathrm{s}}) = S = \mathbb{R}\cdot 1$ | the kernel of $g \mapsto \operatorname{Ad}_g$ | *Split-Quaternion Scalar and Vector Subspaces* |
| $V$ | the vector subspace, preserved, with form $(2,1)$ | *Split-Quaternion Scalar and Vector Subspaces* |
| $\mathrm{SL}_2(\mathbb{R})$ | the norm-one slice $\{g : N(g)=1\}$ | *Split-Quaternion Norm and Invertibility* |
| $\mathrm{SO}^{+}(2,1)$ | the identity component of the Lorentz group | *Split-Quaternion Rotations and the Lorentz Group* |
| $\mathbb{D}_2, \mathbb{D}_3$ | the split-complex planes, permuted by automorphisms | *Split-Quaternion Split-Complex Subspaces* |
| $\rho u$ | the polar representation of a nonzero element | *Split-Quaternion Polar Representation* |

## Further Reading

- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the adjoint action of the units of a Clifford algebra on its Lie algebra and the Lorentz group.
- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd ed. (Cambridge University Press, 2001), for the regular and adjoint representations and the double cover of the Lorentz group.
- Robert Gilmore, *Lie Groups, Lie Algebras, and Some of Their Applications* (Wiley, 1974), for $\mathrm{PSL}_2(\mathbb{R}) \cong \mathrm{SO}^{+}(2,1)$ and the orbit classification of the Minkowski form.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the action of the coquaternion units on the split vector space.
