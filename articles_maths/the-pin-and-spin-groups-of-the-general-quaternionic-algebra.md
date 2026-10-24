
# __The Pin and Spin Groups of the General Quaternionic Algebra__

## Introduction

The twisted two-sided operator $\Theta_{\tilde Q_5}(\tilde Q_1)=\tilde Q_5\tilde Q_1\tilde Q_5^{\natural}$ is an automorphism of the general quaternionic bilinear form exactly when $\langle\tilde Q_5\rangle_{\natural}=\pm1$, and it is multiplicative in the parameter, $\Theta_{\tilde Q_5}\Theta_{\tilde Q_2}=\Theta_{\tilde Q_5\tilde Q_2}$. The set of parameters with $N=\pm1$ is therefore a group that acts on the algebra by automorphisms through $\Theta$, and the assignment is two-to-one; this article reads the group, its two constituents, the versors and the sandwich they carry on the vector subspace, and the reflections of that subspace.

The two constituents are the **pin group** $\mathrm{Pin}=\{\tilde Q_5\in\mathbb{B}^\times:\langle\tilde Q_5\rangle_{\natural}=\pm1\}$ and the **spin group** $\mathrm{Spin}=\{\tilde Q_5\in\mathbb{B}^\times:\langle\tilde Q_5\rangle_{\natural}=1\}$, the latter of index two. The twisted operator is *Two-Sided Operators on the General Quaternionic Algebra*; the one-sided factors are *One-Sided Operators on the General Quaternionic Algebra*; the form and its orthogonal group are *The Four Forms and the Four Algebraic Norms*; the unit group into which both groups sit is *The Biquaternion Unit Group as a Topological Group*; the general Clifford theory of the pin and spin groups is *The Clifford, Pin and Spin Groups with Signed Inner Conjugation*, of which this is the biquaternion instance; and the vector subspace and the reflection are *Introduction to the Remarkable Subspaces* and *Biquaternion Rotations and Lorentz Transformations*.

## The Two Groups

**Definition.** The **pin group** and the **spin group** of the general quaternionic bilinear form are

$$
\mathrm{Pin}=\{\tilde Q_5\in\mathbb{B}^\times:\langle\tilde Q_5\rangle_{\natural}=\pm1\},\qquad
\mathrm{Spin}=\{\tilde Q_5\in\mathbb{B}^\times:\langle\tilde Q_5\rangle_{\natural}=1\}=\ker N .
$$

**Proposition (they are groups, and $\mathrm{Spin}$ has index two).** Both are subgroups of the unit group, closed under multiplication and inverse; $\mathrm{Spin}=\mathrm{Pin}\cap\ker N$ is normal of index two in $\mathrm{Pin}$, and the quotient is $\mathrm{Pin}/\mathrm{Spin}\cong\{\pm1\}$ through the norm.

*Proof.* The norm is multiplicative and central, so if $\langle\tilde Q_5\rangle_{\natural},\langle\tilde Q_2\rangle_{\natural}\in\{\pm1\}$ then $\langle\tilde Q_5\tilde Q_2\rangle_{\natural}\in\{\pm1\}$ and $\langle\tilde Q_5^{-1}\rangle_{\natural}=\langle\tilde Q_5\rangle_{\natural}^{-1}=\langle\tilde Q_5\rangle_{\natural}$; this makes $\mathrm{Pin}$ a group and $\mathrm{Spin}$, its norm-one part, a subgroup. The norm is a homomorphism onto $\{\pm1\}$ on $\mathrm{Pin}$, hence $\mathrm{Pin}/\mathrm{Spin}\cong\{\pm1\}$.

**Remark (the two constituents and the real shadow).** $\mathrm{Pin}$ is the disjoint union $\mathrm{Spin}\sqcup\{N=-1\}$: the norm-one shell, a complex hypersurface of complex dimension $3$, and the norm-minus-one shell, its $i$-translate, since $\langle i\tilde Q_5\rangle_{\natural}=i^{2}\langle\tilde Q_5\rangle_{\natural}=-\langle\tilde Q_5\rangle_{\natural}$ and the two shells are the same set moved by the central scalar $i$. On the real quaternion subspace $\mathbb{H}_{\mathbb{B}}$ the norm is positive definite, $\langle\tilde Q\rangle_{\natural}=\sum_\mu q_\mu^{2}\geq0$, so only the condition $\langle\cdot\rangle_{\natural}=1$ is met there, on the norm-one set $S^{3}\cong SU(2)\cong\mathrm{Spin}(3)$, and no element of $\mathbb{H}_{\mathbb{B}}$ has norm minus one; the norm-minus-one elements need the imaginary directions, the simplest being $ie_t$. On the complex algebra both shells meet the null cone.

**Proposition (the matrix identifications).** Under the isomorphism $\mathsf{M}_2:\mathbb{B}\to M_2(\mathbb{C})$ of *Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*, with $\det\mathsf{M}_2(\tilde Q_5)=\langle\tilde Q_5\rangle_{\natural}$,

$$
\boxed{\; \mathrm{Spin}\cong SL_2(\mathbb{C}),\qquad
\mathrm{Pin}\cong\{\tilde Q_5\in GL_2(\mathbb{C}):\det\mathsf{M}_2(\tilde Q_5)^{2}=1\} \;},
$$

and $\mathrm{Spin}$ is the norm-one subgroup of real dimension $6$ of *The Biquaternion Unit Group as a Topological Group*.

*Proof.* The determinant identity is the norm, so $\langle\cdot\rangle_{\natural}=1$ is $\det\mathsf{M}_2=1$; the pin condition is $\det\mathsf{M}_2=\pm1$, that is $\det^{2}=1$. The dimension and connectedness are those of the norm-one group.

## The Action and the Two-to-One Cover

**Theorem (the cover).** The assignment $\tilde Q_5\mapsto\Theta_{\tilde Q_5}$ is a group homomorphism from $\mathrm{Pin}$ to the group of automorphisms of the general quaternionic bilinear form, with kernel $\{\pm e_t\}$; it is therefore a two-to-one cover of its image,

$$
\boxed{\; \mathrm{Pin}/\{\pm e_t\}\ \cong\ \{\Theta_{\tilde Q_5}:\langle\tilde Q_5\rangle_{\natural}=\pm1\}\ \subset\ O(\mathbb{B},N) \;}.
$$

*Proof.* The composition law $\Theta_{\tilde Q_5}\Theta_{\tilde Q_2}=\Theta_{\tilde Q_5\tilde Q_2}$ makes the assignment a homomorphism; the preservation condition is $\langle\Theta_{\tilde Q_5}\tilde Q_1\rangle_{\natural}=\langle\tilde Q_5\rangle_{\natural}^{2}\langle\tilde Q_1\rangle_{\natural}$, which is preservation exactly for $\langle\tilde Q_5\rangle_{\natural}=\pm1$; and the kernel is $\{\pm e_t\}$ by the injectivity up to sign of the assignment, $\Theta_{\tilde Q_5}=\Theta_{\tilde Q_2}$ for units being $\tilde Q_2=\pm\tilde Q_5$.

**Proposition (the norm-one image is the rotation group of the vector subspace).** On $\mathrm{Spin}$ the twisted operator is the inner automorphism, $\Theta_{\tilde Q_5}=\mathrm{Ad}_{\tilde Q_5}$ for $\langle\tilde Q_5\rangle_{\natural}=1$, and the image is the group of inner automorphisms of the algebra,

$$
\boxed{\; \Theta(\mathrm{Spin})\ \cong\ \mathrm{Spin}/\{\pm e_t\}\ \cong\ \mathrm{Inn}(\mathbb{B})\ \cong\ PGL_2(\mathbb{C})\ \cong\ SO_3(\mathbb{C}) \;},
$$

of complex dimension $3$, acting on $\mathbb{B}=\mathbb{C}_{\mathbb{B}}\oplus V$ by fixing the centre pointwise and rotating the vector subspace. Under this action $\mathrm{Spin}\cong SL_2(\mathbb{C})$ is the classical two-to-one cover of the rotation group.

*Proof.* On the norm-one shell $\tilde Q_5^{\natural}=\tilde Q_5^{-1}$ and the operator is $\langle\tilde Q_5\rangle_{\natural}\mathrm{Ad}_{\tilde Q_5}=\mathrm{Ad}_{\tilde Q_5}$, an algebra automorphism; a conjugation fixes the centre and preserves the trace-zero subspace $V$, and every automorphism of $\mathbb{B}\cong M_2(\mathbb{C})$ is inner by the Skolem–Noether theorem, while a scalar may be rescaled to norm one over $\mathbb{C}$, so the image is the whole inner automorphism group; $\mathrm{Inn}(M_2(\mathbb{C}))=PGL_2(\mathbb{C})$, and $PGL_2(\mathbb{C})\cong SO_3(\mathbb{C})$ is the classical isomorphism, acting on the three-dimensional traceless subspace by the rotations preserving the norm. The kernel is again $\{\pm e_t\}$, which is the classical two-to-one cover.

**Remark (what the norm-minus-one part adds).** The elements of norm minus one give operators that are multiplicative up to the sign, $\Theta_{\tilde Q_5}(\tilde Q_1)\Theta_{\tilde Q_5}(\tilde Q_3)=\langle\tilde Q_5\rangle_{\natural}\Theta_{\tilde Q_5}(\tilde Q_1\tilde Q_3)=-\Theta_{\tilde Q_5}(\tilde Q_1\tilde Q_3)$; they are automorphisms of the form all the same, and they are exactly the coset that makes the cover $\mathrm{Pin}\to\{\Theta\}$ larger than the rotation cover. The two cosets of $\mathrm{Spin}$ in $\mathrm{Pin}$ cover the automorphisms and the twisted maps.

## Versors and the Sandwich Action

The twist $\natural$ is the sign character of the algebra: it is $+1$ on the centre $\mathbb{C}_{\mathbb{B}}$ and $-1$ on the quaternion vector subspace $V$. The elements on which the twist is $-1$ play, in this algebra, the role that the vectors of a quadratic space play in the general theory of the signed inner conjugation, and the two-sided operator of such an element is the sandwich of that theory. In the grade dictionary of the Clifford algebra the elements of $V$ are the grade-two elements and the geometric grade-one vectors are the imaginary ones $i\vec e_k$; this article keeps the quaternion naming of the group, in which $\vec e_k$ is a vector, and states the dictionary once here so that the two readings are not confused.

**Definition.** A **versor** of the algebra is a product $\tilde Q_5=\tilde{Q}_{4,1}\tilde{Q}_{4,2}\cdots\tilde{Q}_{4,k}$ of elements of $V$ with $\langle\tilde{Q}_{4,j}\rangle_{\natural}\neq0$; the **Lipschitz group** is the group that the non-isotropic vectors of $V$ generate.

**Proposition (versors are units, and the norm multiplies).** Every versor is a unit, and

$$
\langle\tilde{Q}_{4,1}\tilde{Q}_{4,2}\cdots\tilde{Q}_{4,k}\rangle_{\natural}=\langle\tilde{Q}_{4,1}\rangle_{\natural}\langle\tilde{Q}_{4,2}\rangle_{\natural}\cdots \langle\tilde{Q}_{4,k}\rangle_{\natural};
$$

after division by a square root of its norm every versor lies in $\mathrm{Pin}$, and in $\mathrm{Spin}$ exactly when its norm is one.

*Proof.* A vector $\tilde{Q}_4$ with $\langle\tilde{Q}_4\rangle_{\natural}\neq0$ is invertible, with $\tilde{Q}_4^{-1}=\tilde{Q}_4^{\natural}/\langle\tilde{Q}_4\rangle_{\natural}$, because $\tilde{Q}_4\tilde{Q}_4^{\natural}=\langle\tilde{Q}_4\rangle_{\natural}e_t$; a product of units is a unit. The norm is multiplicative on the whole algebra, so it multiplies over the factors, and the normalised element $\tilde Q_5/\langle\tilde Q_5\rangle_{\natural}^{1/2}$ has norm $\langle\tilde Q_5\rangle_{\natural}\big/\bigl(\langle\tilde Q_5\rangle_{\natural}^{1/2}\bigr)^{2}=1$, a square root of a nonzero complex number being available.

**Proposition (the sandwich on the vector subspace).** For every unit $\tilde Q_5$ the twisted operator preserves the vector subspace and acts on it by a **similarity** with multiplier $\langle\tilde Q_5\rangle_{\natural}^{2}$:

$$
\Theta_{\tilde Q_5}(V)\subseteq V,\qquad
\langle\Theta_{\tilde Q_5}\tilde W\rangle_{\natural}=\langle\tilde Q_5\rangle_{\natural}^{2}\langle\tilde W\rangle_{\natural}\qquad(\tilde W\in V).
$$

For $\tilde Q_5$ in the pin group the restriction is therefore an automorphism of the restricted form, of determinant $\langle\tilde Q_5\rangle_{\natural}^{3}$ in the basis $\vec e_x,\vec e_y,\vec e_z$.

*Proof.* The operator is $\Theta_{\tilde Q_5}=\langle\tilde Q_5\rangle_{\natural}\mathrm{Ad}_{\tilde Q_5}$, a central scalar times an inner automorphism. An automorphism of the algebra preserves the centre and the trace-zero subspace $V$, so $\Theta_{\tilde Q_5}(V)\subseteq V$; an inner automorphism preserves the determinant, hence the norm, and the scalar contributes its square, giving $\langle\Theta_{\tilde Q_5}\tilde W\rangle_{\natural}=\langle\tilde Q_5\rangle_{\natural}^{2}\langle\tilde W\rangle_{\natural}$. In the three-dimensional basis the determinant of a scalar times a map is the cube of the scalar, and the inner automorphism has determinant one on $V$; the determinant of the restriction is therefore $\langle\tilde Q_5\rangle_{\natural}^{3}$, of sign $\langle\tilde Q_5\rangle_{\natural}$.

**Corollary (the half-turn carried by a vector).** For $\tilde{Q}_4\in V$ with $\langle\tilde{Q}_4\rangle_{\natural}\neq0$ the sandwich is the half-turn about the line $\mathbb{C}\tilde{Q}_4$, composed with the homothety of ratio $\langle\tilde{Q}_4\rangle_{\natural}$: writing $\tau_{\tilde{Q}_4}$ for the half-turn,

$$
\Theta_{\tilde{Q}_4}(\tilde W)=\langle\tilde{Q}_4\rangle_{\natural}\,\tau_{\tilde{Q}_4}(\tilde W),\qquad
\tau_{\tilde{Q}_4}(\tilde W)=2\,\frac{\langle\tilde W,\tilde{Q}_4\rangle_{\natural}}{\langle\tilde{Q}_4\rangle_{\natural}}\,\tilde{Q}_4-\tilde W .
$$

Thus $\Theta_{\tilde{Q}_4}$ acts on $\tilde{Q}_4$ by $\langle\tilde{Q}_4\rangle_{\natural}$ and on its orthogonal complement by $-\langle\tilde{Q}_4\rangle_{\natural}$: for $\langle\tilde{Q}_4\rangle_{\natural}=1$ it is the half-turn, fixing the line and negating the complement, of determinant $+1$; for $\langle\tilde{Q}_4\rangle_{\natural}=-1$ the homothety and the half-turn combine into the honest reflection $\rho_{\tilde{Q}_4}$ itself, negating the line, fixing the complement, of determinant $-1$.

*Proof.* Insert the reflection formula of the next section, $\Theta_{\tilde{Q}_4}=-\langle\tilde{Q}_4\rangle_{\natural}\rho_{\tilde{Q}_4}$, and $\rho_{\tilde{Q}_4}(\tilde W)=\tilde W-2\langle\tilde W,\tilde{Q}_4\rangle_{\natural}\langle\tilde{Q}_4\rangle_{\natural}^{-1}\tilde{Q}_4$, writing $\tau_{\tilde{Q}_4}=-\rho_{\tilde{Q}_4}$ for the half-turn.

**Remark (why every unit preserves the vector subspace here).** In the general theory the condition $\Theta(V)\subseteq V$ defines the Clifford group, and it is not a consequence of the norm condition: over the real form of signature $(1,1)$ the unit of norm one recorded in *The Clifford, Pin and Spin Groups with Signed Inner Conjugation* has a signed inner conjugation that carries a vector outside the space of vectors. That warning does not bite in the biquaternion algebra. Here $\mathbb{B}\cong M_2(\mathbb{C})$ is a full matrix algebra over an algebraically closed field, every automorphism of it is inner by Skolem–Noether, and a central scalar times an inner automorphism preserves $V$; the Clifford group is therefore the whole unit group $\mathbb{B}^{\times}$, and inside it the pin group is exactly the norm shell, not a proper subgroup of it.

**Proposition (the groups generated by the versors).** The vectors of $V$ of norm one lie in $\mathrm{Spin}$ and act on $V$ by the half-turns about their lines; products of two of them act by the rotations, and by Cartan–Dieudonné in dimension three every rotation of $V$ is a product of two reflections and corresponds in the spin group to a product of two unit vectors (*The Clifford, Pin and Spin Groups with Signed Inner Conjugation*, §*Cartan–Dieudonné and the Reflection Length*). The non-isotropic vectors of $V$ therefore generate $\mathrm{Pin}$, their norm-one part generates $\mathrm{Spin}$, and the image of the latter is the rotation group $\Theta(\mathrm{Spin})\cong SO_3(\mathbb{C})$ of the vector subspace.

*Proof.* A norm-one vector $\tilde{Q}_4$ lies in $\mathrm{Pin}$, indeed in $\mathrm{Spin}$; by the corollary its image on $V$ fixes $\tilde{Q}_4$ and negates the orthogonal complement, which is the reflection $\rho_{\tilde{Q}_4}$ up to the sign, a half-turn. Two half-turns compose to a rotation, $\Theta_{\tilde{Q}_4}\Theta_{\tilde W}=\Theta_{\tilde{Q}_4\tilde W}$ with $\langle\tilde{Q}_4\tilde W\rangle_{\natural}=1$, and the quoted theorem of the general article supplies every rotation as such a product; the resulting group of operators has been identified with $\mathrm{Inn}(\mathbb{B})\cong SO_3(\mathbb{C})$ above.

## The Reflection

**Proposition (the reflection on the vector subspace).** For $\tilde{Q}_4\in V$ with $\langle\tilde{Q}_4\rangle_{\natural}\neq0$ the twisted operator fixes the centre up to the norm and equals the reflection up to the norm and the sign:

$$
\Theta_{\tilde{Q}_4}(e_t)=\langle\tilde{Q}_4\rangle_{\natural}e_t,\qquad
\Theta_{\tilde{Q}_4}(\tilde W)=-\langle\tilde{Q}_4\rangle_{\natural}\,\rho_{\tilde{Q}_4}(\tilde W)\qquad(\tilde W\in V).
$$

In particular, for a vector of norm one, $\Theta_{\tilde{Q}_4}(\tilde W)=-\rho_{\tilde{Q}_4}(\tilde W)$ on $V$: the twisted operator carries the reflection composed with the sign, and on the norm-one shell it is the plain inner conjugation, so the sign cannot be removed by a change of the description.

*Proof.* $\Theta_{\tilde{Q}_4}(e_t)=\tilde{Q}_4\tilde{Q}_4^{\natural}=\langle\tilde{Q}_4\rangle_{\natural}e_t$. For $\tilde W\in V$, write the pure quaternions as vectors and use the classical identities $\tilde{Q}_4\tilde W=-\langle\tilde{Q}_4,\tilde W\rangle_{\natural}e_t+(\tilde{Q}_4\times\tilde W)$ and $(\tilde{Q}_4\times\tilde W)\times\tilde{Q}_4=\langle\tilde{Q}_4\rangle_{\natural}\tilde W-\langle\tilde{Q}_4,\tilde W\rangle_{\natural}\tilde{Q}_4$ of the quaternion product; then $\tilde{Q}_4\tilde W\tilde{Q}_4^{\natural}=-\tilde{Q}_4\tilde W\tilde{Q}_4=\langle\tilde{Q}_4\rangle_{\natural}\tilde W-2\langle\tilde{Q}_4,\tilde W\rangle_{\natural}\tilde{Q}_4$, which is $\langle\tilde{Q}_4\rangle_{\natural}\rho_{\tilde{Q}_4}(\tilde W)$; inserting the sign of $\tilde{Q}_4^{\natural}=-\tilde{Q}_4$ gives the displayed identity.

**Remark (the minus is the general one).** The appearance of $-\rho_{\tilde{Q}_4}$ rather than $\rho_{\tilde{Q}_4}$ is the phenomenon the Clifford layer records: for an element of the odd part the plain inner conjugation returns the reflection composed with $-\mathrm{id}$, and it is the twisted member of the family, with the twist in the left factor, that returns the reflection itself. On the norm-one shell the operator $\Theta$ here coincides with the plain inner conjugation, so it carries the minus; the corresponding signed left twist of the general theory differs from $\Theta$ by the norm normalisation and is discussed in *The Clifford, Pin and Spin Groups with Signed Inner Conjugation*. The half-turn reading of the same identity, and the generation of the rotation group by the versors, are in the section above.

## Worked Examples

**A spin element of the centre.** For $\tilde Q_5=\pm e_t$, $N=1$ and $\Theta_{\tilde Q_5}=\mathrm{id}$; the two elements give the same operator, which is the kernel of the cover.

**A spin element of norm one and not central.** For $\tilde Q_5=(e_t+\vec e_x)/\sqrt2$, $\langle\cdot\rangle_{\natural}=1$ and $\Theta_{\tilde Q_5}=\mathrm{Ad}_{\tilde Q_5}$ is an inner automorphism, fixing the centre and rotating the vector subspace; its inverse in the group is $\tilde Q_5^{\natural}=\tilde Q_5^{-1}=(e_t-\vec e_x)/\sqrt2$.

**A pin element of norm minus one.** For $\tilde Q_5=ie_t$, $\langle\cdot\rangle_{\natural}=-1$ and $\Theta_{\tilde Q_5}=-\mathrm{id}$; the operator is a form-preserving map with $\det=+1$ and is not an automorphism: it is the twisted coset.

**A vector of norm one.** For $\tilde{Q}_4=\vec e_x$ the element lies in $\mathrm{Spin}$, and $\Theta_{\tilde{Q}_4}$ fixes $e_t$ and acts on $V$ by $\Theta_{\tilde{Q}_4}(\vec e_x)=\vec e_x$, $\Theta_{\tilde{Q}_4}(\vec e_y)=-\vec e_y$, $\Theta_{\tilde{Q}_4}(\vec e_z)=-\vec e_z$; the reflection $\rho_{\tilde{Q}_4}$ acts by $-\Theta_{\tilde{Q}_4}$, that is $-\vec e_x$ on $\tilde{Q}_4$ and identity on its complement, as the proposition prescribes. The half-turn reading is the same statement: $\Theta_{\tilde{Q}_4}$ is the half-turn about the line $\mathbb{C}\vec e_x$, of determinant $+1$ on $V$.

**A vector of norm minus one.** For $\tilde{Q}_4=i\vec e_x$, $\langle\tilde{Q}_4\rangle_{\natural}=-1$, and $\Theta_{\tilde{Q}_4}=\rho_{\tilde{Q}_4}$ is the honest reflection: it negates $i\vec e_x$, fixes the orthogonal complement, and has determinant $-1$ on $V$; the homothety of ratio $-1$ and the half-turn have combined into a reflection, as the corollary prescribes. The element lies in the odd part of the pin group and not in $\mathrm{Spin}$.

**A versor of length two.** For $\tilde Q_5=\vec e_x\vec e_y=\vec e_z$, the product of the two norm-one vectors $\vec e_x$ and $\vec e_y$, the norm is $\langle\tilde Q_5\rangle_{\natural}=1$ and $\Theta_{\tilde Q_5}$ is the half-turn about the line $\mathbb{C}\vec e_z$: it fixes $\vec e_z$ and negates $\vec e_x,\vec e_y$, of determinant $+1$; indeed $\Theta_{\vec e_x\vec e_y}=\Theta_{\vec e_x}\Theta_{\vec e_y}$ conjugates the two half-turns into a rotation, and here the composition is again a half-turn because the lines are orthogonal.

**A null vector.** For $\tilde{Q}_4=\vec e_x+i\vec e_y$, $\langle\tilde{Q}_4\rangle_{\natural}=0$: the element is not in the pin group, $\Theta_{\tilde{Q}_4}(e_t)=0$, and the reflection formula does not apply, its normalisation being undefined.

## Summary

The pin group of the general quaternionic bilinear form is $\mathrm{Pin}=\{\tilde Q_5\in\mathbb{B}^\times:\langle\tilde Q_5\rangle_{\natural}=\pm1\}$ and the spin group is its norm-one part $\mathrm{Spin}=\{\tilde Q_5:\langle\tilde Q_5\rangle_{\natural}=1\}$, normal of index two with $\mathrm{Pin}/\mathrm{Spin}\cong\{\pm1\}$; in the matrix picture they are $\{\det^{2}=1\}$ and $SL_2(\mathbb{C})$, the spin group being connected of real dimension $6$. The twisted operator $\Theta_{\tilde Q_5}$ is a form-preserving map exactly on $\mathrm{Pin}$, and the assignment is a group homomorphism with kernel $\{\pm e_t\}$, a two-to-one cover of its image in the orthogonal group. On the spin group the operator is the inner automorphism, and the image is $\mathrm{Inn}(\mathbb{B})\cong PGL_2(\mathbb{C})\cong SO_3(\mathbb{C})$, acting by fixing the centre and rotating the vector subspace: the classical two-to-one cover of the rotation group by $SL_2(\mathbb{C})$. The versors are the products of non-isotropic vectors of the vector subspace; the norm multiplies over their factors, so a versor is a nonzero multiple of an element of $\mathrm{Pin}$. The sandwich of every unit preserves the vector subspace and acts on it by a similarity of multiplier $\langle\tilde Q_5\rangle_{\natural}^{2}$, so that on the pin group it is a form-preserving map; over this algebra the Clifford group is the whole unit group, because $\mathbb{B}\cong M_2(\mathbb{C})$ has only inner automorphisms, and the general warning that a norm-one unit may fail to preserve the space of vectors does not bite. A single vector carries a half-turn up to the homothety of its norm, and a vector of norm minus one carries the honest reflection. The norm-one vectors generate $\mathrm{Spin}$, the products of two of them the rotations, and by Cartan–Dieudonné every rotation of the vector subspace is such a product; the norm-minus-one coset supplies the automorphisms that are multiplicative only up to the sign, which is what makes the pin cover larger than the spin one.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathrm{Pin}=\{N=\pm1\}$ | The pin group; two cosets, kernel of the cover $\{\pm e_t\}$ |
| $\mathrm{Spin}=\{N=1\}=\ker N$ | The spin group; index two, normal; $SL_2(\mathbb{C})$ |
| $\Theta_{\tilde Q_5}(\tilde Q_1)=\tilde Q_5\tilde Q_1\tilde Q_5^{\natural}$ | The action of the pin group on the algebra |
| $\Theta_{\tilde Q_5}\Theta_{\tilde Q_2}=\Theta_{\tilde Q_5\tilde Q_2}$, kernel $\{\pm e_t\}$ | The two-to-one cover |
| $\Theta(\mathrm{Spin})\cong PGL_2(\mathbb{C})\cong SO_3(\mathbb{C})$ | The rotation group of the vector subspace |
| $\tilde{Q}_{4,1}\cdots\tilde{Q}_{4,k}$, $\langle\tilde{Q}_{4,j}\rangle_{\natural}\neq0$ | A versor, and the Lipschitz group it generates |
| $\langle\tilde Q_5\rangle_{\natural}=\prod_j\langle\tilde Q_{4,j}\rangle_{\natural}$ | The norm multiplies over the factors of a versor |
| $\Theta_{\tilde Q_5}(V)\subseteq V$, $\langle\Theta_{\tilde Q_5}\tilde W\rangle_{\natural}=\langle\tilde Q_5\rangle_{\natural}^{2}\langle\tilde W\rangle_{\natural}$ | The sandwich of a unit is a similarity of the vector subspace |
| $\Theta_{\tilde{Q}_4}=\langle\tilde{Q}_4\rangle_{\natural}\tau_{\tilde{Q}_4}$ | The half-turn carried by a vector, of determinant $\langle\tilde{Q}_4\rangle_{\natural}^{3}$ |
| $\Theta_{\tilde{Q}_4}\vert_V=-\langle\tilde{Q}_4\rangle_{\natural}\rho_{\tilde{Q}_4}$ | The reflection carried by a vector |
| $\rho_{\tilde{Q}_4}(\tilde W)=\tilde W-2\langle\tilde W,\tilde{Q}_4\rangle_{\natural}\langle\tilde{Q}_4\rangle_{\natural}^{-1}\tilde{Q}_4$ | The reflection in the vector subspace |

## Further Reading

- [The Pin and Spin Groups of the Biquaternion Algebra](the-pin-and-spin-groups-of-the-biquaternion-algebra.html), the plain sibling, where the shell $N=\pm1$ has no counterpart, the isometry condition is vacuous and the reflections of the plain form lie outside the two-sided family.
- [Two-Sided Operators on the General Quaternionic Algebra](two-sided-operators-on-the-general-quaternionic-algebra.html), for the operator and its laws
- [One-Sided Operators on the General Quaternionic Algebra](one-sided-operators-on-the-general-quaternionic-algebra.html), for the factors and the multiplicative criterion
- [The Biquaternion Unit Group as a Topological Group](the-biquaternion-unit-group-as-a-topological-group.html), for the ambient group and its topology
- [The Four Forms and the Four Algebraic Norms](the-four-forms-and-the-four-algebraic-norms.html), for the form and its orthogonal group
- [The Clifford, Pin and Spin Groups with Signed Inner Conjugation](the-clifford-pin-and-spin-groups-with-signed-inner-conjugation.html), for the general theory
- [Versors, Rotors and the Sandwich Action with Signed Inner Conjugation](versors-rotors-and-the-sandwich-action-with-signed-inner-conjugation.html), for the general versor and sandwich theory that the versor section specialises
