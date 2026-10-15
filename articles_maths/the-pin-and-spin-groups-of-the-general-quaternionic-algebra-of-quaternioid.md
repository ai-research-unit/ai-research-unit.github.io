# __The Pin and Spin Groups of the General Quaternionic Algebra__

## Introduction

The pin and spin groups belong to a quadratic form, and the general quaternionic algebra of quaternions carries the **quaternionic form**

$$
N(\tilde q) = q_0^2 + q_1^2 + q_2^2 + q_3^2 ,
$$

positive definite of signature $(4,0)$ (*The Isotropic Structure of the General Quaternionic Algebra*, above this article in this category). The whole construction is short here because the form is definite and multiplicative: its shell $N = 1$ is a group, and the pin and spin groups of the block are that shell itself.

The contrast that organises the article is with the plain algebra. There the block carries **two** degree-two structures: the plain form $\mathrm B$, indefinite of signature $(1,3)$, whose shells are not groups and whose pin group therefore lives in a Clifford algebra rather than in $\mathbb{H}$; and the norm $N$, definite and multiplicative, whose shell is the unit sphere. Over the quaternion real space the quaternionic block takes $N$ itself for its form, so the definite case is the case of the block; the indefinite form keeps its own theory in the plain block, which is *The Pin and Spin Groups of the General Plain Algebra of Quaternions* in the companion reading of the plain algebra of quaternions, cited here and not repeated.

**Conventions.** The quaternionic product is $\tilde p \star \tilde q = \tilde p^{\natural}\tilde q$, with ${}^{\natural}$ the conjugation negating $e_1,e_2,e_3$; the norm is $N(\tilde q) = \tilde q\tilde q^{\natural} = \sum_\mu q_\mu^2$; the vector subspace is $V = \mathrm{Vect}(e_1,e_2,e_3)$; the shell is $\mathbb{H}^1 = \{\tilde q : N(\tilde q) = 1\}$.

## The Shells of the Form

**Theorem (the shells).** The form $N$ is positive definite and multiplicative, $N(\tilde p \star \tilde q) = N(\tilde p)N(\tilde q)$; its shells are $N = \lambda$ for $\lambda \geq 0$, the shell $N = 1$ is the unit sphere $\mathbb{H}^1$ of $\mathbb{H} \cong \mathbb{R}^4$, of real dimension three, and the shell $N = -1$ is empty.

*Proof.* The form is the sum of four squares, so it is non-negative and vanishes only at zero, and its multiplicativity under the product is the theorem of *Norm and Invertibility in the General Quaternionic Algebra*, above this article in this category; a level set of a definite form is nonempty exactly for $\lambda \geq 0$, and $N = 1$ is the unit sphere of the coordinate space.

**Theorem (the shell and the two products).** The shell $\mathbb{H}^1$ is closed under both products of the block, and it is a group under the plain product, with identity $e_0$ and inverse $\tilde q^{-1} = \tilde q^{\natural}$. Under the quaternionic product it is closed but is **not** a group, because the product has a left unit and no right unit.

*Proof.* Closure under either product is multiplicativity: $N(\tilde p \star \tilde q) = N(\tilde p\tilde q) = 1$ when both factors have norm one. The plain product is associative with the two-sided unit $e_0$, so the shell is a group for it. For the quaternionic product the shell contains $e_0$, which is a left unit alone, and no right unit exists in the whole algebra (*The Specificities of the General Quaternionic Algebra*, above this article in this category), so the shell cannot be a group for $\star$.

**Corollary.** The shell is a group and a subset invariant under the quaternionic product at the same time; the group structure it carries is the one of the plain product, and it is the structure that the pin and spin construction uses. The distinctive content of the chapter is that the form of the block is definite, and the distinctive form of the plain chapter is indefinite; the shells of an indefinite form are not groups at all.

## The Pin and Spin Groups

**Theorem (the pin and spin groups).** For the quaternionic form the pin and spin groups are the shell itself:

$$
\operatorname{Pin}(N) = \{\tilde q : N(\tilde q) = \pm1\} = \mathbb{H}^1 , \qquad \operatorname{Spin}(N) = \{\tilde q : N(\tilde q) = 1\} = \mathbb{H}^1 .
$$

*Proof.* An element of the pin group of a form is a product of vectors of norm $\pm1$; in dimension four with a multiplicative norm the products are exactly the elements of norm $\pm1$, and since the norm is never negative the two conditions coincide. Equivalently the algebra is its own Clifford algebra and the shell is its even part; the spin group is the even subgroup and equals the shell.

**Corollary (the algebraic content).** The identification $\operatorname{Spin} \cong \mathbb{H}^1$ is a statement about the quaternionic form and not about the plain form: the spin group is the unit sphere of the algebra, of real dimension three, and it is a group precisely because the norm is multiplicative. The group is the same set that the plain block calls its unit sphere; what differs between the two blocks is the form that the shell belongs to.

## The Unit Group Acting by Inner Automorphisms

**Definition.** The **inner automorphism** or **adjoint action** of a unit $\tilde q$ is $\operatorname{Ad}_{\tilde q}(\tilde p) = \tilde q\tilde p\tilde q^{-1}$, the conjugation of the algebra by $\tilde q$; it is an algebra automorphism of $\mathbb{H}$.

**Theorem (the action).** $\operatorname{Ad}$ is a group homomorphism $\mathbb{H}^1 \to \operatorname{Aut}(\mathbb{H})$ whose kernel is $\{\pm e_0\}$; on the vector subspace $V$ the action preserves the restriction of the form and the orientation, and its image is $SO(V,N)$, so that $\mathbb{H}^1/\{\pm e_0\} \cong SO(V,N)$.

*Proof.* $\operatorname{Ad}_{\tilde p}\operatorname{Ad}_{\tilde q} = \operatorname{Ad}_{\tilde p\tilde q}$ by associativity; the kernel consists of the units with $\tilde q\tilde p\tilde q^{-1} = \tilde p$ for all $\tilde p$, that is the central units, namely $\pm e_0$, since the centre is the scalar line. On $V$ the action preserves $N$ because $N(\tilde q\tilde p\tilde q^{-1}) = N(\tilde p)$, it is the identity on the scalar line, and it preserves the orientation because it is connected; so its image lies in $SO(V,N)$. The image is all of $SO(V,N)$ by the classical identification of the unit sphere with the rotations of the three-dimensional space, quoted as standard, so $\mathbb{H}^1/\{\pm e_0\} \cong SO(V,N)$.

**Corollary.** The quaternionic form and the plain form have the same inner automorphisms, since the action $\operatorname{Ad}$ uses the plain product alone; the two blocks differ in the form attached to the action, $(4,0)$ here and $(1,3)$ in the plain reading, and not in the action itself.

## The Kernel and the Normalised Section

**Theorem (the normalised section).** The map $\operatorname{Ad}_{\tilde q} \mapsto \tilde q$ is not well defined, but the assignment sending an element of $\operatorname{Ad}(\mathbb{H}^1)$ to the unit of its fibre with $q_0 > 0$, and to the first unit with a positive coordinate on the equator $q_0 = 0$, is a set-theoretic section of the projection. The two cosets are $\pm\tilde q$, and they give the same inner automorphism.

*Proof.* The fibres of $\operatorname{Ad}$ are the cosets $\{\pm\tilde q\}$ by the kernel computation. If $q_0 \neq 0$ exactly one of $\pm\tilde q$ has the positive scalar part; on the equator $q_0 = 0$ the two elements have the same scalar part, and the tie is broken by the first nonzero coordinate of $\tilde q$, of which at least one of the two is positive. The assignment is therefore well defined as a map of sets, but it is not continuous: the two hemispheres must be glued along the equator with a jump, and $\mathbb{H}^1 \to \operatorname{Ad}(\mathbb{H}^1)$ is a non-trivial double cover with no continuous section.

**Corollary (the double cover).** The homomorphism $\mathbb{H}^1 \to SO(V,N)$ has kernel $\{\pm e_0\}$ and is $2$-to-$1$ onto its image; the two preimages of a rotation are the two units $\pm\tilde q$, and the normalised section selects one of them.

## The Reflections

**Theorem (the reflections).** Let $\tilde u \in V$ with $N(\tilde u) = 1$. Then for $\tilde x \in V$,

$$
\tilde u\tilde x\tilde u = \tilde x - 2N(\tilde u,\tilde x)\tilde u , \qquad \operatorname{Ad}_{\tilde u}(\tilde x) = \tilde u\tilde x\tilde u^{-1} = 2N(\tilde u,\tilde x)\tilde u - \tilde x ,
$$

where $N(\tilde u,\tilde x)$ is the polar form restricted to $V$. The first map is the reflection in the hyperplane $\tilde u^{\perp}$, and the second is its negative, the rotation by $\pi$ about the axis $\mathbb{R}\tilde u$. On the scalar line the same operators act as the negation, $\tilde u s \tilde u = -s$ for $s \in \mathbb{R}e_0$.

*Proof.* For a pure unit $\tilde u$ one has $\tilde u^{-1} = \tilde u^{\natural} = -\tilde u$ and $\tilde u^2 = -e_0$, so $\operatorname{Ad}_{\tilde u} = -\tilde u(\ )\tilde u$; expanding $\tilde u\tilde x\tilde u$ for pure $\tilde u,\tilde x$ with the multiplication table gives $\tilde x - 2N(\tilde u,\tilde x)\tilde u$, the reflection that fixes the plane $\tilde u^{\perp}$ and negates the line $\mathbb{R}\tilde u$. The second display is its negative, which fixes the line and negates the plane. For a scalar $\tilde x = se_0$ one has $\tilde u s\tilde u = s\tilde u^2 = -s$, as displayed.

**Corollary.** The unit quaternion $\tilde u$ is the versor of the reflection $\tilde x \mapsto \tilde u\tilde x\tilde u$, and the two units $\pm\tilde u$ realise the same inner automorphism; every element of the image of $\operatorname{Ad}$ on $V$ is a product of such rotations, hence a rotation, and the reflection in the hyperplane perpendicular to a vector of the three-dimensional space is the map the pure unit realises.

## The Comparison with the Plain Algebra

**Proposition.** The plain algebra of the same space carries the indefinite form $\mathrm B(\tilde q) = q_0^2 - \vec q \cdot \vec q$ of signature $(1,3)$ and the same norm $N$; the shells of $\mathrm B$ are not groups, so the pin group of $\mathrm B$ lives in the Clifford algebra of $\mathrm B$ and not in $\mathbb{H}$, whereas the shells of $N$ are groups and their pin group is the unit sphere. The quaternionic block takes $N$ for its form, so in this block the definite case is the case of the block and the shell is the pin and spin group without a passage to a Clifford algebra.

*Proof.* Multiplicativity fails for an indefinite form on a division algebra of dimension four, with the witness of the plain article; the shell statements are the theorems above.

| | plain block | quaternionic block |
|---|---|---|
| form | $\mathrm B$, signature $(1,3)$, indefinite | $N$, signature $(4,0)$, definite |
| shells | not groups | groups, the unit sphere |
| pin group | in the Clifford algebra of $\mathrm B$ | the shell $\mathbb{H}^1$ itself |
| spin group | the even part of that Clifford algebra | the shell $\mathbb{H}^1$ itself |
| inner automorphisms | $\mathbb{H}^1/\{\pm e_0\} \cong SO(V,N)$ | the same |

**Corollary.** The two blocks share the inner automorphisms and the unit sphere and differ in the form: the quaternionic form is the definite one, so its pin and spin groups are the shell; the plain form is the indefinite one, so its pin group leaves the algebra. The definiteness of the quaternionic form is therefore the reason the chapter has a pin and spin group inside the algebra.

## Summary

The form of the general quaternionic algebra of quaternions is the definite quaternionic form $N$, multiplicative under the product. Its shells are the levels $N = \lambda \geq 0$; the shell $N = 1$ is the unit sphere $\mathbb{H}^1$, of real dimension three, it is closed under both products of the block and is a group under the plain one, the quaternionic product having a left unit alone. The pin and spin groups of the form are the shell itself, $\operatorname{Pin}(N) = \operatorname{Spin}(N) = \mathbb{H}^1$, the spin group being a group precisely because the norm is multiplicative; the chapter therefore has its pin and spin groups inside the algebra, where the plain chapter has them inside a Clifford algebra. The unit group acts by the inner automorphisms $\operatorname{Ad}_{\tilde q}(\tilde p) = \tilde q\tilde p\tilde q^{-1}$, with kernel $\{\pm e_0\}$ and $2$-to-$1$ image $SO(V,N)$ on the vector subspace; the normalised section selects one of the two units, by the sign of $q_0$ with a tie-break on the equator. A pure unit $\tilde u$ realises the reflection $\tilde x \mapsto \tilde u\tilde x\tilde u$ in the hyperplane perpendicular to it and the rotation by $\pi$ through its inner automorphism. Over $\mathbb{C}$ the form becomes isotropic, the shell becomes a non-compact quadric, and the compactness of the sphere is a property of the real member alone.

## Summary of Notation

| symbol | meaning |
|---|---|
| $N(\tilde q) = \sum_\mu q_\mu^2$ | the quaternionic form of the block, definite of signature $(4,0)$ |
| $\mathbb{H}^1 = \{\tilde q : N(\tilde q) = 1\}$ | the unit sphere, $\operatorname{Pin}(N) = \operatorname{Spin}(N)$ |
| $\operatorname{Ad}_{\tilde q}(\tilde p) = \tilde q\tilde p\tilde q^{-1}$ | the inner automorphism of a unit |
| $\{\pm e_0\}$ | the kernel of the inner action on the algebra |
| $q_0 > 0$, with a tie-break on the equator | the normalisation of the section |
| $\tilde u\tilde x\tilde u = \tilde x - 2N(\tilde u,\tilde x)\tilde u$ | the reflection by a pure unit, for $\tilde x \in V$ |
| $\mathrm B(\tilde q) = q_0^2 - \vec q \cdot \vec q$ | the plain form of the sibling block, indefinite of signature $(1,3)$ |

## Further Reading

- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the pin and spin groups of a quadratic form and their relation to the quaternions.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the pin group of an indefinite form and the twisted adjoint action.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the versors, the unit sphere and the double cover of the rotation group.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for the algebraic construction of the pin and spin groups from the Clifford algebra.
