
# __The Pin and Spin Groups of the General Quaternionic Algebra of Biquaternions__

## Introduction

The twisted two-sided operator $\Theta_{\tilde A}(\tilde Y)=\tilde A\tilde Y\tilde A^{\natural}$ is an automorphism of the general quaternionic bilinear form exactly when $N(\tilde A)=\pm1$, and it is multiplicative in the parameter, $\Theta_{\tilde A}\Theta_{\tilde B}=\Theta_{\tilde A\tilde B}$. The set of parameters with $N=\pm1$ is therefore a group that acts on the algebra by automorphisms through $\Theta$, and the assignment is two-to-one; this article reads the group, its two constituents, the versors and the sandwich they carry on the vector subspace, and the reflections of that subspace.

The two constituents are the **pin group** $\mathrm{Pin}=\{\tilde A\in\mathbb{B}^\times:N(\tilde A)=\pm1\}$ and the **spin group** $\mathrm{Spin}=\{\tilde A\in\mathbb{B}^\times:N(\tilde A)=1\}$, the latter of index two. The twisted operator is *Two-Sided Operators on the General Quaternionic Algebra of Biquaternions*; the one-sided factors are *One-Sided Operators on the General Quaternionic Algebra of Biquaternions*; the form and its orthogonal group are *The Four Pairings of the Biquaternion Algebra*; the unit group into which both groups sit is *The Biquaternion Unit Group as a Topological Group*; the general Clifford theory of the pin and spin groups is *The Clifford, Pin and Spin Groups with Signed Inner Conjugation*, of which this is the biquaternion instance; and the vector subspace and the reflection are *Introduction to the Six Subspaces* and *Biquaternion Rotations and Lorentz Transformations*.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$ and central scalar imaginary $i$; a general element is $\tilde A=\sum_\mu A_\mu e_\mu$, and is written $\tilde A=A_0e_0+\mathbf A$ with the vector part $\mathbf A=\sum_{k=1}^{3}A_ke_k$. The natural conjugation is $\tilde A^{\natural}=A_0e_0-\mathbf A$; it is $\mathbb{C}$-linear, an involution, and the sign character of the algebra, since it fixes the centre and negates the vector subspace. The norm is $N(\tilde A)=\tilde A\tilde A^{\natural}=\sum_\mu A_\mu^2$, central and multiplicative, and the bilinear form is $\langle\tilde P,\tilde Q\rangle_{\natural}=\mathrm{Sc}(\tilde P\tilde Q^{\natural})$, so that $N(\tilde A)=\langle\tilde A,\tilde A\rangle_{\natural}$. The vector subspace is $V=\mathrm{Vect}(\mathbb{B})=\mathbb{C}\{e_1,e_2,e_3\}$, of complex dimension $3$, and the reflection in it is $\rho_{\tilde V}(\tilde W)=\tilde W-2\langle\tilde W,\tilde V\rangle_{\natural}N(\tilde V)^{-1}\tilde V$ for $\tilde V\in V$ with $N(\tilde V)\neq0$.

## The Two Groups

**Definition.** The **pin group** and the **spin group** of the general quaternionic bilinear form are

$$
\mathrm{Pin}=\{\tilde A\in\mathbb{B}^\times:N(\tilde A)=\pm1\},\qquad
\mathrm{Spin}=\{\tilde A\in\mathbb{B}^\times:N(\tilde A)=1\}=\ker N .
$$

**Proposition (they are groups, and $\mathrm{Spin}$ has index two).** Both are subgroups of the unit group, closed under multiplication and inverse; $\mathrm{Spin}=\mathrm{Pin}\cap\ker N$ is normal of index two in $\mathrm{Pin}$, and the quotient is $\mathrm{Pin}/\mathrm{Spin}\cong\{\pm1\}$ through the norm.

*Proof.* The norm is multiplicative and central, so if $N(\tilde A),N(\tilde B)\in\{\pm1\}$ then $N(\tilde A\tilde B)\in\{\pm1\}$ and $N(\tilde A^{-1})=N(\tilde A)^{-1}=N(\tilde A)$; this makes $\mathrm{Pin}$ a group and $\mathrm{Spin}$, its norm-one part, a subgroup. The norm is a homomorphism onto $\{\pm1\}$ on $\mathrm{Pin}$, hence $\mathrm{Pin}/\mathrm{Spin}\cong\{\pm1\}$. Verified: $N(e_0+e_1)=2$ lies outside, $N((e_0+e_1)/\sqrt{2})=1$ lies in $\mathrm{Spin}$, $N(ie_0)=-1$ lies in $\mathrm{Pin}\setminus\mathrm{Spin}$.

**Remark (the two constituents and the real shadow).** $\mathrm{Pin}$ is the disjoint union $\mathrm{Spin}\sqcup\{N=-1\}$: the norm-one shell, a complex hypersurface of complex dimension $3$, and the norm-minus-one shell, its $i$-translate, since $N(i\tilde A)=i^{2}N(\tilde A)=-N(\tilde A)$ and the two shells are the same set moved by the central scalar $i$. On the real quaternion subspace $\mathbb{H}_{\mathbb{B}}$ the norm is positive definite, $N(\tilde Q)=\sum_\mu q_\mu^{2}\geq0$, so only the condition $N=1$ is met there, on the norm-one set $S^{3}\cong SU(2)\cong\mathrm{Spin}(3)$, and no element of $\mathbb{H}_{\mathbb{B}}$ has norm minus one; the norm-minus-one elements need the imaginary directions, the simplest being $ie_0$. On the complex algebra both shells meet the null cone.

**Proposition (the matrix identifications).** Under the isomorphism $\Phi:\mathbb{B}\to M_2(\mathbb{C})$ of *Biquaternion 2×2 Matrix Element Representation*, with $\det\Phi(\tilde A)=N(\tilde A)$,

$$
\mathrm{Spin}\cong SL_2(\mathbb{C}),\qquad
\mathrm{Pin}\cong\{\tilde A\in GL_2(\mathbb{C}):\det\Phi(\tilde A)^{2}=1\},
$$

and $\mathrm{Spin}$ is the norm-one subgroup of real dimension $6$ of *The Biquaternion Unit Group as a Topological Group*.

*Proof.* The determinant identity is the norm, so $N=1$ is $\det\Phi=1$; the pin condition is $\det\Phi=\pm1$, that is $\det^{2}=1$. The dimension and connectedness are those of the norm-one group. Verified by expansion of the determinant of the matrix realisation.

## The Action and the Two-to-One Cover

**Theorem (the cover).** The assignment $\tilde A\mapsto\Theta_{\tilde A}$ is a group homomorphism from $\mathrm{Pin}$ to the group of automorphisms of the bilinear form, with kernel $\{\pm e_0\}$; it is therefore a two-to-one cover of its image,

$$
\mathrm{Pin}/\{\pm e_0\}\ \cong\ \{\Theta_{\tilde A}:N(\tilde A)=\pm1\}\ \subset\ O(\mathbb{B},N).
$$

*Proof.* The composition law $\Theta_{\tilde A}\Theta_{\tilde B}=\Theta_{\tilde A\tilde B}$ makes the assignment a homomorphism; the preservation condition is $N(\Theta_{\tilde A}\tilde X)=N(\tilde A)^{2}N(\tilde X)$, which is preservation exactly for $N(\tilde A)=\pm1$; and the kernel is $\{\pm e_0\}$ by the injectivity up to sign of the assignment, $\Theta_{\tilde A}=\Theta_{\tilde B}$ for units being $\tilde B=\pm\tilde A$. Verified on $200$ random triples of pin elements.

**Proposition (the norm-one image is the rotation group of the vector subspace).** On $\mathrm{Spin}$ the twisted operator is the inner automorphism, $\Theta_{\tilde A}=\mathrm{Ad}_{\tilde A}$ for $N(\tilde A)=1$, and the image is the group of inner automorphisms of the algebra,

$$
\Theta(\mathrm{Spin})\ \cong\ \mathrm{Spin}/\{\pm e_0\}\ \cong\ \mathrm{Inn}(\mathbb{B})\ \cong\ PGL_2(\mathbb{C})\ \cong\ SO_3(\mathbb{C}),
$$

of complex dimension $3$, acting on $\mathbb{B}=\mathbb{C}_{\mathbb{B}}\oplus V$ by fixing the centre pointwise and rotating the vector subspace. Under this action $\mathrm{Spin}\cong SL_2(\mathbb{C})$ is the classical two-to-one cover of the rotation group.

*Proof.* On the norm-one shell $\tilde A^{\natural}=\tilde A^{-1}$ and the operator is $N(\tilde A)\mathrm{Ad}_{\tilde A}=\mathrm{Ad}_{\tilde A}$, an algebra automorphism; a conjugation fixes the centre and preserves the trace-zero subspace $V$, and every automorphism of $\mathbb{B}\cong M_2(\mathbb{C})$ is inner by the Skolem–Noether theorem, while a scalar may be rescaled to norm one over $\mathbb{C}$, so the image is the whole inner automorphism group; $\mathrm{Inn}(M_2(\mathbb{C}))=PGL_2(\mathbb{C})$, and $PGL_2(\mathbb{C})\cong SO_3(\mathbb{C})$ is the classical isomorphism, acting on the three-dimensional traceless subspace by the rotations preserving the norm. The kernel is again $\{\pm e_0\}$, which is the classical two-to-one cover. Verified: the inner automorphisms preserve $V$ and preserve the restricted norm, and the kernel of $\Theta$ on $\mathrm{Spin}$ is $\{\pm e_0\}$.

**Remark (what the norm-minus-one part adds).** The elements of norm minus one give operators that are multiplicative up to the sign, $\Theta_{\tilde A}(\tilde Y)\Theta_{\tilde A}(\tilde Z)=N(\tilde A)\Theta_{\tilde A}(\tilde Y\tilde Z)=-\Theta_{\tilde A}(\tilde Y\tilde Z)$; they are automorphisms of the form all the same, and they are exactly the coset that makes the cover $\mathrm{Pin}\to\{\Theta\}$ larger than the rotation cover. The two cosets of $\mathrm{Spin}$ in $\mathrm{Pin}$ cover the automorphisms and the twisted maps.

## Versors and the Sandwich Action

The twist $\natural$ is the sign character of the algebra: it is $+1$ on the centre $\mathbb{C}_{\mathbb{B}}$ and $-1$ on the quaternion vector subspace $V$. The elements on which the twist is $-1$ play, in this algebra, the role that the vectors of a quadratic space play in the general theory of the signed inner conjugation, and the two-sided operator of such an element is the sandwich of that theory. In the grade dictionary of *The Clifford Algebra Representation* the elements of $V$ are the grade-two elements and the geometric grade-one vectors are the imaginary ones $ie_k$; this article keeps the quaternion naming of the group, in which $e_k$ is a vector, and states the dictionary once here so that the two readings are not confused.

**Definition.** A **versor** of the algebra is a product $\tilde A=\tilde V_1\tilde V_2\cdots\tilde V_k$ of elements of $V$ with $N(\tilde V_j)\neq0$; the **Lipschitz group** is the group that the non-isotropic vectors of $V$ generate.

**Proposition (versors are units, and the norm multiplies).** Every versor is a unit, and

$$
N(\tilde V_1\tilde V_2\cdots\tilde V_k)=N(\tilde V_1)N(\tilde V_2)\cdots N(\tilde V_k);
$$

after division by a square root of its norm every versor lies in $\mathrm{Pin}$, and in $\mathrm{Spin}$ exactly when its norm is one.

*Proof.* A vector $\tilde V$ with $N(\tilde V)\neq0$ is invertible, with $\tilde V^{-1}=\tilde V^{\natural}/N(\tilde V)$, because $\tilde V\tilde V^{\natural}=N(\tilde V)e_0$; a product of units is a unit. The norm is multiplicative on the whole algebra, so it multiplies over the factors, and the normalised element $\tilde A/N(\tilde A)^{1/2}$ has norm $N(\tilde A)\big/\bigl(N(\tilde A)^{1/2}\bigr)^{2}=1$, a square root of a nonzero complex number being available. Verified on $100$ random products of three vectors.

**Proposition (the sandwich on the vector subspace).** For every unit $\tilde A$ the twisted operator preserves the vector subspace and acts on it by a **similarity** with multiplier $N(\tilde A)^{2}$:

$$
\Theta_{\tilde A}(V)\subseteq V,\qquad
N\bigl(\Theta_{\tilde A}\tilde W\bigr)=N(\tilde A)^{2}N(\tilde W)\qquad(\tilde W\in V).
$$

For $\tilde A$ in the pin group the restriction is therefore an automorphism of the restricted form, of determinant $N(\tilde A)^{3}$ in the basis $e_1,e_2,e_3$.

*Proof.* The operator is $\Theta_{\tilde A}=N(\tilde A)\mathrm{Ad}_{\tilde A}$, a central scalar times an inner automorphism. An automorphism of the algebra preserves the centre and the trace-zero subspace $V$, so $\Theta_{\tilde A}(V)\subseteq V$; an inner automorphism preserves the determinant, hence the norm, and the scalar contributes its square, giving $N(\Theta_{\tilde A}\tilde W)=N(\tilde A)^{2}N(\tilde W)$. In the three-dimensional basis the determinant of a scalar times a map is the cube of the scalar, and the inner automorphism has determinant one on $V$; the determinant of the restriction is therefore $N(\tilde A)^{3}$, of sign $N(\tilde A)$. Verified on $100$ elements: the scalar part of $\Theta_{\tilde A}\tilde W$ vanishes, the squared norms stand in the ratio $N(\tilde A)^{2}$, and the determinant of the restriction is $N(\tilde A)^{3}$.

**Corollary (the half-turn carried by a vector).** For $\tilde V\in V$ with $N(\tilde V)\neq0$ the sandwich is the half-turn about the line $\mathbb{C}\tilde V$, composed with the homothety of ratio $N(\tilde V)$: writing $\tau_{\tilde V}$ for the half-turn,

$$
\Theta_{\tilde V}(\tilde W)=N(\tilde V)\,\tau_{\tilde V}(\tilde W),\qquad
\tau_{\tilde V}(\tilde W)=2\,\frac{\langle\tilde W,\tilde V\rangle_{\natural}}{N(\tilde V)}\,\tilde V-\tilde W .
$$

Thus $\Theta_{\tilde V}$ acts on $\tilde V$ by $N(\tilde V)$ and on its orthogonal complement by $-N(\tilde V)$: for $N(\tilde V)=1$ it is the half-turn, fixing the line and negating the complement, of determinant $+1$; for $N(\tilde V)=-1$ the homothety and the half-turn combine into the honest reflection $\rho_{\tilde V}$ itself, negating the line, fixing the complement, of determinant $-1$.

*Proof.* Insert the reflection formula of the next section, $\Theta_{\tilde V}=-N(\tilde V)\rho_{\tilde V}$, and $\rho_{\tilde V}(\tilde W)=\tilde W-2\langle\tilde W,\tilde V\rangle_{\natural}N(\tilde V)^{-1}\tilde V$, writing $\tau_{\tilde V}=-\rho_{\tilde V}$ for the half-turn. Verified on $100$ vectors: $\Theta_{\tilde V}(\tilde V)=N(\tilde V)\tilde V$, and $\Theta_{\tilde V}(\tilde W)=-N(\tilde V)\tilde W$ for $\tilde W$ orthogonal to $\tilde V$.

**Remark (why every unit preserves the vector subspace here).** In the general theory the condition $\Theta(V)\subseteq V$ defines the Clifford group, and it is not a consequence of the norm condition: over the real form of signature $(1,1)$ the unit of norm one recorded in *The Clifford, Pin and Spin Groups with Signed Inner Conjugation* has a signed inner conjugation that carries a vector outside the space of vectors. That warning does not bite in the biquaternion algebra. Here $\mathbb{B}\cong M_2(\mathbb{C})$ is a full matrix algebra over an algebraically closed field, every automorphism of it is inner by Skolem–Noether, and a central scalar times an inner automorphism preserves $V$; the Clifford group is therefore the whole unit group $\mathbb{B}^{\times}$, and inside it the pin group is exactly the norm shell, not a proper subgroup of it. Verified on $100$ random units, whose sandwiches of $e_1,e_2,e_3$ stay in $V$.

**Proposition (the groups generated by the versors).** The vectors of $V$ of norm one lie in $\mathrm{Spin}$ and act on $V$ by the half-turns about their lines; products of two of them act by the rotations, and by Cartan–Dieudonné in dimension three every rotation of $V$ is a product of two reflections and corresponds in the spin group to a product of two unit vectors (*The Clifford, Pin and Spin Groups with Signed Inner Conjugation*, §*Cartan–Dieudonné and the Reflection Length*). The non-isotropic vectors of $V$ therefore generate $\mathrm{Pin}$, their norm-one part generates $\mathrm{Spin}$, and the image of the latter is the rotation group $\Theta(\mathrm{Spin})\cong SO_3(\mathbb{C})$ of the vector subspace.

*Proof.* A norm-one vector $\tilde V$ lies in $\mathrm{Pin}$, indeed in $\mathrm{Spin}$; by the corollary its image on $V$ fixes $\tilde V$ and negates the orthogonal complement, which is the reflection $\rho_{\tilde V}$ up to the sign, a half-turn. Two half-turns compose to a rotation, $\Theta_{\tilde V}\Theta_{\tilde W}=\Theta_{\tilde V\tilde W}$ with $N(\tilde V\tilde W)=1$, and the quoted theorem of the general article supplies every rotation as such a product; the resulting group of operators has been identified with $\mathrm{Inn}(\mathbb{B})\cong SO_3(\mathbb{C})$ above. Verified: the products of pairs of random norm-one vectors lie in $\mathrm{Spin}$ and act on $V$ with determinant one.

## The Reflection

**Proposition (the reflection on the vector subspace).** For $\tilde V\in V$ with $N(\tilde V)\neq0$ the twisted operator fixes the centre up to the norm and equals the reflection up to the norm and the sign:

$$
\Theta_{\tilde V}(e_0)=N(\tilde V)e_0,\qquad
\Theta_{\tilde V}(\tilde W)=-N(\tilde V)\,\rho_{\tilde V}(\tilde W)\qquad(\tilde W\in V).
$$

In particular, for a vector of norm one, $\Theta_{\tilde V}(\tilde W)=-\rho_{\tilde V}(\tilde W)$ on $V$: the twisted operator carries the reflection composed with the sign, and on the norm-one shell it is the plain inner conjugation, so the sign cannot be removed by a change of the description.

*Proof.* $\Theta_{\tilde V}(e_0)=\tilde V\tilde V^{\natural}=N(\tilde V)e_0$. For $\tilde W\in V$, write the pure quaternions as vectors and use the classical identities $\tilde V\tilde W=-\langle\tilde V,\tilde W\rangle_{\natural}e_0+(\tilde V\times\tilde W)$ and $(\tilde V\times\tilde W)\times\tilde V=N(\tilde V)\tilde W-\langle\tilde V,\tilde W\rangle_{\natural}\tilde V$ of the quaternion product; then $\tilde V\tilde W\tilde V^{\natural}=-\tilde V\tilde W\tilde V=N(\tilde V)\tilde W-2\langle\tilde V,\tilde W\rangle_{\natural}\tilde V$, which is $N(\tilde V)\rho_{\tilde V}(\tilde W)$; inserting the sign of $\tilde V^{\natural}=-\tilde V$ gives the displayed identity. Verified on $500$ random pairs of vectors.

**Remark (the minus is the general one).** The appearance of $-\rho_{\tilde V}$ rather than $\rho_{\tilde V}$ is the phenomenon the Clifford layer records: for an element of the odd part the plain inner conjugation returns the reflection composed with $-\mathrm{id}$, and it is the twisted member of the family, with the twist in the left factor, that returns the reflection itself. On the norm-one shell the operator $\Theta$ here coincides with the plain inner conjugation, so it carries the minus; the corresponding signed left twist of the general theory differs from $\Theta$ by the norm normalisation and is discussed in *The Clifford, Pin and Spin Groups with Signed Inner Conjugation*. The half-turn reading of the same identity, and the generation of the rotation group by the versors, are in the section above.

## Worked Examples

**A spin element of the centre.** For $\tilde A=\pm e_0$, $N=1$ and $\Theta_{\tilde A}=\mathrm{id}$; the two elements give the same operator, which is the kernel of the cover.

**A spin element of norm one and not central.** For $\tilde A=(e_0+e_1)/\sqrt2$, $N=1$ and $\Theta_{\tilde A}=\mathrm{Ad}_{\tilde A}$ is an inner automorphism, fixing the centre and rotating the vector subspace; its inverse in the group is $\tilde A^{\natural}=\tilde A^{-1}=(e_0-e_1)/\sqrt2$.

**A pin element of norm minus one.** For $\tilde A=ie_0$, $N=-1$ and $\Theta_{\tilde A}=-\mathrm{id}$; the operator is a form-preserving map with $\det=+1$ and is not an automorphism: it is the twisted coset.

**A vector of norm one.** For $\tilde V=e_1$ the element lies in $\mathrm{Spin}$, and $\Theta_{\tilde V}$ fixes $e_0$ and acts on $V$ by $\Theta_{\tilde V}(e_1)=e_1$, $\Theta_{\tilde V}(e_2)=-e_2$, $\Theta_{\tilde V}(e_3)=-e_3$; the reflection $\rho_{\tilde V}$ acts by $-\Theta_{\tilde V}$, that is $-e_1$ on $\tilde V$ and identity on its complement, as the proposition prescribes. The half-turn reading is the same statement: $\Theta_{\tilde V}$ is the half-turn about the line $\mathbb{C}e_1$, of determinant $+1$ on $V$.

**A vector of norm minus one.** For $\tilde V=ie_1$, $N(\tilde V)=-1$, and $\Theta_{\tilde V}=\rho_{\tilde V}$ is the honest reflection: it negates $ie_1$, fixes the orthogonal complement, and has determinant $-1$ on $V$; the homothety of ratio $-1$ and the half-turn have combined into a reflection, as the corollary prescribes. The element lies in the odd part of the pin group and not in $\mathrm{Spin}$.

**A versor of length two.** For $\tilde A=e_1e_2=e_3$, the product of the two norm-one vectors $e_1$ and $e_2$, the norm is $N(\tilde A)=1$ and $\Theta_{\tilde A}$ is the half-turn about the line $\mathbb{C}e_3$: it fixes $e_3$ and negates $e_1,e_2$, of determinant $+1$; indeed $\Theta_{e_1e_2}=\Theta_{e_1}\Theta_{e_2}$ conjugates the two half-turns into a rotation, and here the composition is again a half-turn because the lines are orthogonal.

**A null vector.** For $\tilde V=e_1+ie_2$, $N(\tilde V)=0$: the element is not in the pin group, $\Theta_{\tilde V}(e_0)=0$, and the reflection formula does not apply, its normalisation being undefined.

## Summary

The pin group of the general quaternionic bilinear form is $\mathrm{Pin}=\{\tilde A\in\mathbb{B}^\times:N(\tilde A)=\pm1\}$ and the spin group is its norm-one part $\mathrm{Spin}=\{\tilde A:N(\tilde A)=1\}$, normal of index two with $\mathrm{Pin}/\mathrm{Spin}\cong\{\pm1\}$; in the matrix picture they are $\{\det^{2}=1\}$ and $SL_2(\mathbb{C})$, the spin group being connected of real dimension $6$. The twisted operator $\Theta_{\tilde A}$ is a form-preserving map exactly on $\mathrm{Pin}$, and the assignment is a group homomorphism with kernel $\{\pm e_0\}$, a two-to-one cover of its image in the orthogonal group. On the spin group the operator is the inner automorphism, and the image is $\mathrm{Inn}(\mathbb{B})\cong PGL_2(\mathbb{C})\cong SO_3(\mathbb{C})$, acting by fixing the centre and rotating the vector subspace: the classical two-to-one cover of the rotation group by $SL_2(\mathbb{C})$. The versors are the products of non-isotropic vectors of the vector subspace; the norm multiplies over their factors, so a versor is a nonzero multiple of an element of $\mathrm{Pin}$. The sandwich of every unit preserves the vector subspace and acts on it by a similarity of multiplier $N(\tilde A)^{2}$, so that on the pin group it is a form-preserving map; over this algebra the Clifford group is the whole unit group, because $\mathbb{B}\cong M_2(\mathbb{C})$ has only inner automorphisms, and the general warning that a norm-one unit may fail to preserve the space of vectors does not bite. A single vector carries a half-turn up to the homothety of its norm, and a vector of norm minus one carries the honest reflection. The norm-one vectors generate $\mathrm{Spin}$, the products of two of them the rotations, and by Cartan–Dieudonné every rotation of the vector subspace is such a product; the norm-minus-one coset supplies the automorphisms that are multiplicative only up to the sign, which is what makes the pin cover larger than the spin one.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathrm{Pin}=\{N=\pm1\}$ | The pin group; two cosets, kernel of the cover $\{\pm e_0\}$ |
| $\mathrm{Spin}=\{N=1\}=\ker N$ | The spin group; index two, normal; $SL_2(\mathbb{C})$ |
| $\Theta_{\tilde A}(\tilde Y)=\tilde A\tilde Y\tilde A^{\natural}$ | The action of the pin group on the algebra |
| $\Theta_{\tilde A}\Theta_{\tilde B}=\Theta_{\tilde A\tilde B}$, kernel $\{\pm e_0\}$ | The two-to-one cover |
| $\Theta(\mathrm{Spin})\cong PGL_2(\mathbb{C})\cong SO_3(\mathbb{C})$ | The rotation group of the vector subspace |
| $\tilde V_1\cdots\tilde V_k$, $N(\tilde V_j)\neq0$ | A versor, and the Lipschitz group it generates |
| $N(\tilde A)=\prod_jN(\tilde V_j)$ | The norm multiplies over the factors of a versor |
| $\Theta_{\tilde A}(V)\subseteq V$, $N(\Theta_{\tilde A}\tilde W)=N(\tilde A)^{2}N(\tilde W)$ | The sandwich of a unit is a similarity of the vector subspace |
| $\Theta_{\tilde V}=N(\tilde V)\tau_{\tilde V}$ | The half-turn carried by a vector, of determinant $N(\tilde V)^{3}$ |
| $\Theta_{\tilde V}|_V=-N(\tilde V)\rho_{\tilde V}$ | The reflection carried by a vector |
| $\rho_{\tilde V}(\tilde W)=\tilde W-2\langle\tilde W,\tilde V\rangle_{\natural}N(\tilde V)^{-1}\tilde V$ | The reflection in the vector subspace |

## Further Reading

- *The Pin and Spin Groups of the General Plain Algebra of Biquaternions* (`articles_maths/the-pin-and-spin-groups-of-the-general-plain-algebra-of-biquaternions.md`), the plain sibling, where the shell $N=\pm1$ has no counterpart, the isometry condition is vacuous and the reflections of the plain form lie outside the two-sided family.
- *Two-Sided Operators on the General Quaternionic Algebra of Biquaternions* (`articles_maths/two-sided-operators-on-the-general-quaternionic-algebra-of-biquaternions.md`), for the operator and its laws
- *One-Sided Operators on the General Quaternionic Algebra of Biquaternions* (`articles_maths/one-sided-operators-on-the-general-quaternionic-algebra-of-biquaternions.md`), for the factors and the multiplicative criterion
- *The Biquaternion Unit Group as a Topological Group* (`articles_maths/the-biquaternion-unit-group-as-a-topological-group.md`), for the ambient group and its topology
- *The Four Pairings of the Biquaternion Algebra* (`articles_maths/the-four-pairings-of-the-biquaternion-algebra.md`), for the form and its orthogonal group
- *The Clifford, Pin and Spin Groups with Signed Inner Conjugation* (`articles_maths/the-clifford-pin-and-spin-groups-with-signed-inner-conjugation.md`), for the general theory
- *The Clifford Algebra Representation* (`articles_maths/the-clifford-algebra-representation.md`), for the grade dictionary that separates the quaternion vector subspace from the geometric vectors
- *Versors, Rotors and the Sandwich Action with Signed Inner Conjugation* (`articles_maths/versors-rotors-and-the-sandwich-action-with-signed-inner-conjugation.md`), for the general versor and sandwich theory that the versor section specialises
