
# __The Rotation and Reflection Groups in the Biquaternion Algebra__

## Introduction

The biquaternion algebra is an eight-dimensional real algebra with a norm form of signature $(4,4)$, and inside its unit group sit the rotation and reflection groups of the low-dimensional forms: the unit quaternions $Sp(1)$ with their double cover of $SO(3)$, the norm-one biquaternions $SL(2,\mathbb{C})$ with their double cover of the identity component of $SO(1,3)$, the two-sided action that gives $SO(4)$, the finite groups of the Lipschitz and Hurwitz units, and the Weyl groups of the small root systems that act on the algebra. This article treats these as groups: for each of them it records the generators, the order or dimension, the form preserved, and the way the group sits inside the unit group $\mathbb{B}^{\times}\cong GL(2,\mathbb{C})$, or acts on the algebra when it is the symmetry group of a lattice rather than a group of units.

The algebra, its conjugations and its norm form $N(\tilde Q)=\tilde Q\bar{\tilde Q}=\sum_\mu Q_\mu^2$ are those; the identification with $\mathrm{Cl}_{3,0}$ and the matrix model are those of *The Biquaternion Algebra as a Clifford Algebra*. The group-theoretic part of the Clifford layer — the Clifford group, the twisted adjoint action, the Pin and Spin groups and the Cartan–Dieudonné theorem — is that of *The Clifford, Pin and Spin Groups*, and the spinor module is that of *Spin Representations and Clifford Modules*, in its biquaternion formwhich owns the chiral decomposition and the action of $SL(2,\mathbb{C})=\mathrm{Spin}(1,3)$ on the module. Only the computations special to $\mathbb{B}$ are performed here.

The six real subspaces of $\mathbb{B}$ introduced — the center $\mathbb{C}_{\mathbb{B}}$, the vector subspace $\mathrm{Vect}(\mathbb{B})$, the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, the anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}$, and the Hermitian and anti-Hermitian subspaces $\mathbb{M}_\pm$ — are used throughout, and the restriction of the norm form to each is the form that the corresponding group preserves.

## The Norm Form and its Real Forms

**Definition.** On $\mathbb{B}\cong\mathbb{R}^8$ the norm form is $N(\tilde Q)=\tilde Q\bar{\tilde Q}=\sum_{\mu=0}^{3}Q_\mu^2$, with $Q_\mu\in\mathbb{C}$, and its polar form is $B(\tilde P,\tilde Q)=\tfrac12\bigl(N(\tilde P+\tilde Q)-N(\tilde P)-N(\tilde Q)\bigr)=\sum_\mu P_\mu Q_\mu$.

The form $N$ is complex-valued on $\mathbb{B}$, but its real part restricts to each of the six subspaces as a real quadratic form of fixed signature: on the four subspaces $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$ and $\mathbb{M}_{\pm}$ the form $N$ itself is real, while on the center and on $\mathrm{Vect}(\mathbb{B})$ only its real part is a real form.

**Theorem.** The restrictions of $N$ to the six subspaces have the following signatures.

| subspace | basis | signature of $N$ | dimension |
|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ (center) | $e_0,\ ie_0$ | $(1,1)$ | $2$ |
| $\mathrm{Vect}(\mathbb{B})$ (vector) | $e_1,e_2,e_3,\ ie_1,ie_2,ie_3$ | $(3,3)$ | $6$ |
| $\mathbb{H}_{\mathbb{B}}$ (quaternion) | $e_0,e_1,e_2,e_3$ | $(4,0)$ | $4$ |
| $i\mathbb{H}_{\mathbb{B}}$ (anti-quaternion) | $ie_0,ie_1,ie_2,ie_3$ | $(0,4)$ | $4$ |
| $\mathbb{M}_+$ (Hermitian) | $e_0,\ ie_1,ie_2,ie_3$ | $(1,3)$ | $4$ |
| $\mathbb{M}_-$ (anti-Hermitian) | $ie_0,\ e_1,e_2,e_3$ | $(3,1)$ | $4$ |

**Proof.** Write $Q_\mu=a_\mu+ib_\mu$, so that $N=\sum_\mu(a_\mu^2-b_\mu^2)+2i\sum_\mu a_\mu b_\mu$. The real part is the quadratic form $\sum_\mu(a_\mu^2-b_\mu^2)$, of signature $(4,4)$ on $\mathbb{R}^8$, and the imaginary part of the polar form $B$ is the polar form of the imaginary part of $N$. On each subspace the allowed coefficients constrain the pairs $(a_\mu,b_\mu)$: on $\mathbb{H}_{\mathbb{B}}$ all $b_\mu=0$, giving four positive squares; on $i\mathbb{H}_{\mathbb{B}}$ all $a_\mu=0$, giving four negative squares; on $\mathbb{M}_+$ the coefficient of $e_0$ is real (so $b_0=0$) and those of $e_1,e_2,e_3$ are purely imaginary (so $a_1=a_2=a_3=0$), giving one positive and three negative squares; on $\mathbb{M}_-$ the signs are reversed; and on the center and the vector subspace the counts are as displayed. $\square$

**Corollary.** On the Hermitian subspace $\mathbb{M}_+$ the norm form is real and of signature $(1,3)$; this is the form whose isometry group contains $SL(2,\mathbb{C})$. On the quaternion subspace $\mathbb{H}_{\mathbb{B}}$ the norm form is the positive definite quaternion norm, whose isometry group contains $Sp(1)$. These two restrictions are the forms that organise the rotation groups of the article.

## Reflections and the Reflection Formula

**Definition.** Let $v\in\mathbb{B}$ with $N(v)=1$. The **reflection in the hyperplane $v^{\perp}$** is the linear map

$$
\rho_v(x)=-v\,x\,v^{-1}=-v\,x\,\bar v,
$$

where the second equality uses $v^{-1}=\bar v/N(v)=\bar v$. The reflection is used on a subspace on which the multiplication is Clifford – one spanned by mutually anticommuting elements whose squares are all equal to $\varepsilon e_0$ for a single sign $\varepsilon$, and containing $v$ – because on such a subspace orthogonality for $B$ and anticommutation with $v$ coincide, as the theorem below shows; the vector subspace $\mathrm{Vect}(\mathbb{B})=\mathbb{C}\{e_1,e_2,e_3\}$, where $\varepsilon=-1$, and its real form the imaginary quaternion space are the cases used here.

**Theorem.** For $v$ with $N(v)=1$ the map $\rho_v$ preserves the norm form and its polar form, satisfies $\rho_v(v)=-v$, and fixes pointwise every element that anticommutes with $v$; its square is the conjugation $\rho_v^2(x)=v^2xv^{-2}$, so it is an involution exactly when $v^2$ is a scalar, as it is for $v$ in a subspace spanned by mutually anticommuting elements of square $\pm e_0$ with no $e_0$-component. For $v$ and $x$ in $\mathrm{Vect}(\mathbb{B})=\mathbb{C}\{e_1,e_2,e_3\}$, or in its real form the imaginary quaternion space, one has $vx+xv=-2B(v,x)e_0$, so anticommutation with $v$ is orthogonality, and $\rho_v$ is the reflection in $v^{\perp}$: it fixes $v^{\perp}$ pointwise, negates the line $\mathbb{C}v$, and has determinant $-1$ as a complex-linear map.

**Proof.** Since $v$ is invertible, $\rho_v$ is a linear automorphism with $\rho_v^2(x)=v^2xv^{-2}$, which is the identity as soon as $v^2$ is a scalar; multiplicativity of $N$ gives $N(\rho_v(x))=N(v)N(x)N(v)^{-1}=N(x)$, so $\rho_v$ preserves $N$ and hence $B$; and $\rho_v(v)=-vvv^{-1}=-vN(v)=-v$. If $xv=-vx$ then $\rho_v(x)=-vxv^{-1}=-(-xv)v^{-1}=xvv^{-1}=x$, so every element anticommuting with $v$ is fixed. For $v=\sum_jv_je_j$ in $\mathrm{Vect}(\mathbb{B})$ the square is $v^2=-\bigl(\sum_jv_j^2\bigr)e_0$, a scalar, so $\rho_v$ is an involution there; and for $v,x$ in that subspace the expansion of $vx+xv$ in the basis gives $-2B(v,x)e_0$: the squared terms contribute $-2e_0\sum_jv_jx_j$ and the mixed terms cancel pairwise, so $B(x,v)=0$ and $xv=-vx$ are the same condition. There $\rho_v$ fixes the hyperplane $v^{\perp}$ pointwise and negates the complementary line $\mathbb{C}v$, so it is a reflection, of determinant $-1$ as a complex-linear map. $\square$

**Remark.** The reflections are those of the Clifford vector subspaces, where the elements anticommute: the vector subspace $\mathrm{Vect}(\mathbb{B})$, whose real form carries the form of signature $(3,3)$, and the imaginary quaternion space, which carries the definite form. They are not reflections of the subspaces on which the algebra acts by conjugation. On $\mathbb{H}_{\mathbb{B}}$ the norm-one element $e_0$ is central, so $\rho_{e_0}=-\mathrm{id}$ and nothing is fixed; and on the algebra as a whole $\rho_v$ has determinant $+1$ for every $v$ with $N(v)=1$, so the maps attached to the finite groups of units are rotations rather than reflections. The rotations of $\mathbb{H}_{\mathbb{B}}$ and $\mathbb{M}_+$ are the conjugation $x\mapsto qxq^{-1}$ and the action $x\mapsto\tilde Gx\tilde G^{\dagger}$; the reflections enter through the Clifford vector subspaces, as in *The Clifford, Pin and Spin Groups*.

**Theorem (Cartan–Dieudonné in $\mathbb{B}$).** On the complex three-dimensional vector subspace $\mathrm{Vect}(\mathbb{B})=\mathbb{C}\{e_1,e_2,e_3\}$ and on its real form the imaginary quaternion space $\mathbb{R}\{e_1,e_2,e_3\}$, every isometry of the restriction of $N$ is a product of at most three reflections $\rho_v$ with $v$ in the subspace and $N(v)=1$.

**Proof.** On these subspaces $N(v)=v_1^2+v_2^2+v_3^2$, a non-degenerate form, and by the theorem above the maps $\rho_v$ with $N(v)=1$ are its reflections in the hyperplanes $v^{\perp}$. The Cartan–Dieudonné theorem of *The Clifford, Pin and Spin Groups* therefore gives generation by at most $\dim W=3$ reflections. The reflections of the form $N$ on $\mathbb{M}_+$, which has signature $(1,3)$, are not of this shape; the isometries of $\mathbb{M}_+$ are generated by the reflections of that form in the Clifford layer, where the Pin and Spin groups of the signature live. $\square$

## The Clifford Group, Pin and Spin in the Biquaternion Algebra

**Definition.** The **Clifford group** is

$$
\Gamma=\{\,x\in\mathbb{B}^{\times} : \widetilde{\mathrm{Ad}}_x(W)\subseteq W\ \text{for the relevant subspace }W\,\},
$$

where $\widetilde{\mathrm{Ad}}_x(y)=\alpha(x)yx^{-1}$ is the twisted adjoint and $\alpha$ is the grade involution; the **Pin group** is the subgroup with $N(x)=\pm1$ on the subspaces where $N$ is real, and the **Spin group** is its even part $\mathrm{Spin}=\mathrm{Pin}\cap\mathrm{Cl}^0_{3,0}$.

**Theorem.** On the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, with $W$ the three-dimensional space of pure imaginary quaternions and $N$ the quaternion norm,

$$
\mathrm{Pin}(3)\longrightarrow O(3), \qquad \mathrm{Spin}(3)=Sp(1)\longrightarrow SO(3),
$$

are the double covers, and $Sp(1)$ is the group of unit quaternions $N(q)=1$. On the Hermitian subspace $\mathbb{M}_+$, with $W=\mathbb{M}_+$ and the action $x\mapsto\tilde Gx\tilde G^{\dagger}$,

$$
\mathrm{Spin}(1,3)\cong SL(2,\mathbb{C})=\{\tilde G\in\mathbb{B}:N(\tilde G)=1\}\longrightarrow SO^{+}(1,3)
$$

is the double cover of the identity component.

**Proof.** For the quaternionic statement, a unit quaternion $q$ acts on the pure imaginary quaternions $x$ by $x\mapsto qxq^{-1}$, which preserves the norm and the orientation, giving $Sp(1)\to SO(3)$; the kernel is $\{\pm1\}$, and surjectivity is the standard Euler-angle parametrisation or follows from Cartan–Dieudonné. Adding the odd part gives $O(3)$. For the biquaternionic statement, $\tilde G\in\mathbb{B}$ with $N(\tilde G)=1$ has $\det\Phi(\tilde G)=1$, so its matrix is in $SL(2,\mathbb{C})$; the action on Hermitian $x$ by $x\mapsto\tilde Gx\tilde G^{\dagger}$ preserves the Hermitian property and the determinant, hence preserves the form $N$ of signature $(1,3)$ on $\mathbb{M}_+$, and preserves the orientation and time-orientation, giving $SO^{+}(1,3)$. The kernel is $\{\pm\tilde G_0\}$, so the cover is two-to-one, and surjectivity is the standard connectedness and dimension count $\dim_{\mathbb{R}}SL(2,\mathbb{C})=6=\dim SO(1,3)$. $\square$

**Remark.** The two statements live on different subspaces and use different actions: the quaternionic rotations are inner automorphisms $x\mapsto qxq^{-1}$, while the biquaternionic rotations are $x\mapsto\tilde Gx\tilde G^{\dagger}$, which is not an algebra automorphism but preserves the Hermitian form. This is why the first gives $SO(3)$ acting on three dimensions and the second gives $SO(1,3)$ acting on four, and it is the algebraic reason the rotation groups of the two subspaces are different even though both are built from the same algebra.

## The Two-Sided Action and $SO(4)$

**Theorem.** The group $Sp(1)\times Sp(1)$ acts on $\mathbb{H}_{\mathbb{B}}\cong\mathbb{R}^4$ by

$$
(q_1,q_2)\cdot x=q_1\,x\,q_2^{-1},
$$

and the action is an isometry of the quaternion norm, surjective onto $SO(4)$ with kernel $\{(1,1),(-1,-1)\}$.

**Proof.** For unit quaternions $q_1,q_2$ the product $q_1xq_2^{-1}$ has norm $N(q_1)N(x)N(q_2)^{-1}=N(x)$, so the action is by isometries; it is linear and orthogonal. The kernel consists of pairs acting trivially, so $q_1x=xq_2$ for all $x$, which forces $q_1=q_2=\pm1$; the two pairs give the identity, and the map is therefore injective modulo the kernel. Both groups are six-dimensional, and the image is connected, so it is all of $SO(4)$. $\square$

**Remark.** The two-sided action exhibits $SO(4)$ as the quotient $(Sp(1)\times Sp(1))/\{\pm1\}$, and the corresponding spin group is $\mathrm{Spin}(4)=Sp(1)\times Sp(1)$, in agreement with the classification. In the biquaternion algebra the same two-sided action extends complex-linearly, and its restriction to the two factors gives the two half-spin representations of *Spin Representations and Clifford Modules*.

**The unitary groups.** The group $GL(2,\mathbb{C})$ of units of $\mathbb{B}\cong M_2(\mathbb{C})$ contains $U(2)$, the group of complex-linear isometries of the positive definite Hermitian form $\tilde Q\tilde Q^\dagger$ on the defining module, and its determinant-one subgroup $SU(2)\cong Sp(1)$. These are the complex rotations of the algebra: $U(2)$ is the full unitary group of the two-dimensional module, of real dimension four, and $SU(2)$ is the unit quaternions, of dimension three, acting irreducibly on the spinor module. The chain $SU(2)\subset U(2)\subset GL(2,\mathbb{C})$ is the chain of isometry groups of the Hermitian form, the full linear group, and the unitary restrictions, and it sits inside $\mathbb{B}^{\times}$ as the stabiliser of the relevant form.

## The Norm-Form Automorphism Group

**Theorem.** The group of algebra automorphisms of $\mathbb{B}$ is the inner automorphism group

$$
\operatorname{Aut}(\mathbb{B})\cong \mathbb{B}^{\times}/\mathbb{C}^{\times}\cong PGL(2,\mathbb{C}),
$$

and every algebra automorphism preserves the norm form: $N(\varphi(\tilde Q))=N(\tilde Q)$.

**Proof.** The algebra $\mathbb{B}$ is central simple over $\mathbb{C}$ and is $M_2(\mathbb{C})$; by the Skolem–Noether theorem every automorphism of a central simple algebra is inner, $\varphi(x)=\tilde Gx\tilde G^{-1}$ for some unit $\tilde G$, defined up to the center $\mathbb{C}^{\times}$. Such an automorphism preserves the determinant $N$ because $\det(\tilde Gx\tilde G^{-1})=\det x$. $\square$

**Corollary.** There is an exact sequence

$$
1\longrightarrow \mathbb{C}^{\times}\longrightarrow \mathbb{B}^{\times}\xrightarrow{\ \operatorname{Ad}\ }\operatorname{Aut}(\mathbb{B})\longrightarrow 1,
$$

and $\operatorname{Aut}(\mathbb{B})\cong PGL(2,\mathbb{C})$ is a proper subgroup of the full isometry group $O(N)$ of the real norm form. The norm-form automorphisms are the inner ones, and the additional isometries are the outer orthogonal transformations of the $(4,4)$ form that are not algebra automorphisms.

**Remark.** The relation between the unit group and the isometry groups is the reason the biquaternion algebra is a convenient home for rotations. The unit group $\mathbb{B}^{\times}\cong GL(2,\mathbb{C})$ acts on the spinor module and through it on the Hermitian and quaternionic subspaces; the isometry groups of the several forms are the images of the relevant subgroups of the units, with the kernels $\{\pm1\}$ or $\mathbb{C}^{\times}$ recording the double cover and the scalar ambiguity.

## The Finite Groups of Units

The integral structures inside $\mathbb{B}$ produce finite groups of units, and they are the finite subgroups of the rotation groups.

**Definition.** The **Lipschitz units** are the eight quaternions

$$
\{\pm e_0,\ \pm e_1,\ \pm e_2,\ \pm e_3\},
$$

and the **Hurwitz units** are the Lipschitz units together with the sixteen elements

$$
\tfrac12(\pm e_0\pm e_1\pm e_2\pm e_3).
$$

**Theorem.** The Lipschitz units form a group of order $8$ isomorphic to the quaternion group $Q_8$, and the Hurwitz units form a group of order $24$ isomorphic to the binary tetrahedral group $2T$. Both lie in the unit sphere $N=1$ of $\mathbb{H}_{\mathbb{B}}$, so both are subgroups of $Sp(1)=\mathrm{Spin}(3)$.

**Proof.** The Lipschitz units are closed under multiplication because the products of the quaternion units are again units up to sign; they are the usual quaternion group of order eight. For the Hurwitz units, closure is checked by multiplying the half-integer elements: the product of two of them has integer or half-integer coordinates and norm one, and the list of norm-one half-integer quaternions is exactly the twenty-four displayed (eight with integer coordinates and sixteen with all coordinates $\pm\tfrac12$); this is the binary tetrahedral group, the preimage in $Sp(1)$ of the rotation group of the regular tetrahedron. $\square$

**Corollary.** The Hurwitz units are the vertices of the regular $24$-cell in $\mathbb{H}_{\mathbb{B}}\cong\mathbb{R}^4$. The binary octahedral group $2O$ of order $48$ and the binary icosahedral group $2I$ of order $120$ are the further finite subgroups of $Sp(1)$ obtained by adjoining the appropriate units: $2O$ contains the Hurwitz units together with the elements $\tfrac{1}{\sqrt2}(\pm1\pm e_k)$ and their products, and $2I$ requires the golden-ratio coordinates. Each of them double-covers the corresponding rotation group of the regular polyhedron, and each is a finite subgroup of the unit quaternions.

**Remark.** The finite subgroups of $Sp(1)=SU(2)$ are classified: the cyclic groups, the binary dihedral groups, and the three binary polyhedral groups $2T$, $2O$, $2I$ of orders $24,48,120$. The Hurwitz units realise $2T$ integrally, and the $24$-cell is its convex hull; the other two groups require the appropriate integral structures, and their realisation is standard. The corresponding rotation groups are the tetrahedral, octahedral and icosahedral groups in $SO(3)$.

## The Integral Lattice and the Weyl Groups

**Definition.** The **Lipschitz order** is the lattice

$$
\mathcal{L}=\mathbb{Z}e_0\oplus\mathbb{Z}e_1\oplus\mathbb{Z}e_2\oplus\mathbb{Z}e_3\subseteq\mathbb{H}_{\mathbb{B}},
$$

and the **Hurwitz order** is the larger lattice obtained by adjoining the half-integer elements of norm one. An **integral biquaternion** is an element of $\mathbb{B}$ whose coordinates lie in an integral lattice of $\mathbb{C}$, for instance $\mathbb{Z}[i]$.

**Theorem.** The Lipschitz order is an order in $\mathbb{H}$ but not maximal, and its group of units is the group of Lipschitz units of order $8$. The Hurwitz order is a maximal order in $\mathbb{H}$, and its group of units is the Hurwitz group of order $24$, the binary tetrahedral group $2T$.

**Proof.** That the Lipschitz order is not maximal is shown by the half-integer elements of the Hurwitz order, which cannot be written with integer coordinates; the Hurwitz order contains it with index and is maximal. The unit computations are as in the previous section. $\square$

**Remark.** The Hurwitz units are the vertices of the regular $24$-cell in $\mathbb{H}\cong\mathbb{R}^4$. Its full symmetry group is the Weyl group $F_4$ of order $1152$, and the subgroup of signed permutations of the four coordinates is the Weyl group $B_4$ of order $2^4\cdot4!=384$, the symmetry group of the regular $16$-cell and of the hypercube. The reflection formula enters as follows: the twenty-four Hurwitz units give twelve distinct maps $\rho_v(x)=-vxv^{-1}$, each of determinant $+1$ on the algebra and therefore a rotation of it rather than a reflection, and together they generate the group of order $24$ consisting of the conjugation action of $2T$, which is $2T/\{\pm1\}\cong A_4$, together with its negative, the antipodal map. The Weyl groups are larger; they are the orthogonal symmetries of the lattices, acting on the algebra, and they are not contained in its unit group, which is finite of order $24$. The root system $A_1$ is already present at the level of one generator: on the line $\mathbb{R}e_1$ the reflection $\rho_{e_1}$ acts as $-1$ and on its orthogonal complement as the identity, so the Weyl group $W(A_1)=\mathbb{Z}/2$ of order $2$ is realised on a one-dimensional Clifford subspace. This is the arithmetic side of the rotation groups of the biquaternion algebra, and it links the Clifford structure to the theory of lattices and root systems.

## Summary

The biquaternion algebra carries a norm form $N$ of signature $(4,4)$ whose restrictions to its six real subspaces have signatures $(1,1)$, $(3,3)$, $(4,0)$, $(0,4)$, $(1,3)$ and $(3,1)$. For $N(v)=1$ the map $\rho_v(x)=-vxv^{-1}=-vx\bar v$ preserves the norm form, negates $v$, is an involution, and is the reflection in $v^{\perp}$ on a Clifford vector subspace, where it has determinant $-1$ as a complex-linear map; on the algebra as a whole it has determinant $+1$ and is a rotation. On the Clifford vector subspaces Cartan–Dieudonné gives every isometry as a product of at most $\dim W$ reflections. The Clifford group $\Gamma$, the Pin group and the Spin group are defined by the twisted adjoint action and the norm condition as in the Clifford layer.

The rotation groups sit in the unit sphere $N=1$ of the algebra. On the quaternion subspace, the unit quaternions form $Sp(1)=\mathrm{Spin}(3)$ and double-cover $SO(3)$, while $\mathrm{Pin}(3)$ double-covers $O(3)$. On the Hermitian subspace, the norm-one biquaternions form $SL(2,\mathbb{C})=\mathrm{Spin}(1,3)$ and double-cover the identity component of $SO(1,3)$ through the action $x\mapsto\tilde Gx\tilde G^{\dagger}$. The two-sided action of $Sp(1)\times Sp(1)$ gives $SO(4)$ with $\mathrm{Spin}(4)=Sp(1)\times Sp(1)$, the unitary groups $U(2)$ and $SU(2)$ are the complex rotations of the defining module, and the unit group $\mathbb{B}^{\times}\cong GL(2,\mathbb{C})$ has automorphism group $PGL(2,\mathbb{C})$, which preserves the norm form and is a proper subgroup of its full isometry group.

The finite integral structures give the Lipschitz units of order $8$ and the Hurwitz units of order $24$, the latter being the binary tetrahedral group, together with the binary octahedral and icosahedral groups of orders $48$ and $120$; and the Lipschitz and Hurwitz orders are respectively a non-maximal and a maximal order in $\mathbb{H}$, with unit groups of orders $8$ and $24$, the Hurwitz units being the vertices of the $24$-cell, whose symmetry group is the Weyl group $F_4$ of order $1152$, containing the Weyl group $B_4$ of order $384$ of the signed permutations.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_k^2=-e_0$ |
| $N(\tilde Q)=\tilde Q\bar{\tilde Q}=\sum_\mu Q_\mu^2$ | Norm form, signature $(4,4)$ on $\mathbb{B}$ |
| $B(\tilde P,\tilde Q)=\sum_\mu P_\mu Q_\mu$ | Polar form of $N$ |
| $\mathbb{C}_{\mathbb{B}},\mathrm{Vect}(\mathbb{B}),\mathbb{H}_{\mathbb{B}},i\mathbb{H}_{\mathbb{B}},\mathbb{M}_\pm$ | The six real subspaces |
| $\rho_v(x)=-vxv^{-1}=-vx\bar v$ | Reflection on a Clifford vector subspace, $N(v)=1$ |
| $\Gamma,\mathrm{Pin},\mathrm{Spin}$ | Clifford, Pin and Spin groups inside $\mathbb{B}$ |
| $\widetilde{\mathrm{Ad}}_x(y)=\alpha(x)yx^{-1}$ | Twisted adjoint action |
| $Sp(1)=\mathrm{Spin}(3)$ | Unit quaternions, double cover of $SO(3)$ |
| $\mathrm{Pin}(3)$ | Double cover of $O(3)$ |
| $SL(2,\mathbb{C})=\mathrm{Spin}(1,3)=\{N=1\}$ | Norm-one biquaternions, double cover of $SO^+(1,3)$ |
| $x\mapsto\tilde Gx\tilde G^{\dagger}$ | Action of $SL(2,\mathbb{C})$ on $\mathbb{M}_+$ |
| $Sp(1)\times Sp(1)\to SO(4)$ | Two-sided action, kernel $\{\pm(1,1)\}$ |
| $U(2),SU(2)$ | Complex rotations of the defining module; $SU(2)\cong Sp(1)$ |
| $\mathbb{B}^{\times}\cong GL(2,\mathbb{C})$, $\operatorname{Aut}(\mathbb{B})\cong PGL(2,\mathbb{C})$ | Unit and automorphism groups |
| Lipschitz units, Hurwitz units | Groups of orders $8$ and $24$, $Q_8$ and $2T$ |
| $2O,2I$ | Binary octahedral and icosahedral groups, orders $48$ and $120$ |
| $\mathcal{L}=\mathbb{Z}e_0\oplus\cdots\oplus\mathbb{Z}e_3$ | Lipschitz order; Hurwitz order its maximal extension |
| $A_1,B_4,F_4$ | Weyl groups of the root systems realised on a one-dimensional Clifford subspace and on the Lipschitz and Hurwitz lattices; orders $2$, $384$ and $1152$ |



## Further Reading

- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A. K. Peters, 2003), for the finite groups of unit quaternions, the $24$-cell and the Weyl groups.
- John H. Conway and Neil J. A. Sloane, *Sphere Packings, Lattices and Groups* (Springer, 3rd ed. 1999), for the integral quaternion orders and the root systems realised in them.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the reflection formula and the Pin and Spin groups in low dimensions.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the two-sided quaternionic actions and the classical group isomorphisms.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for the double covers and the Cartan–Dieudonné theorem.
