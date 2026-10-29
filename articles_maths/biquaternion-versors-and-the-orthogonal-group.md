# __Biquaternion Versors and the Orthogonal Group__

## Introduction

The biquaternion algebra is the even part of the Clifford algebra of Lorentzian space, and that one fact decides which isometries of the norm the algebra can carry. Every operator the algebra supplies is built from one element on each side, so it is an even element of the envelope, and an even element composes an even number of reflections. The isometries it realises are therefore the proper orthochronous Lorentz transformations and no others. The reflections are odd. They lie in the odd slot of the Clifford algebra, a second copy of the algebra sitting beside it, which the algebra does not contain. The orthogonal group is an object of the biquaternion vocabulary, read on the Hermitian sector; the Pin group is not, because its elements include the odd ones, and it belongs to the Clifford envelope rather than to the algebra.

This article works the biquaternion case of the Clifford group. It fixes the two slots of the envelope and identifies the odd slot as a copy of the algebra containing the Lorentzian space; it reads the grading of the versors by the parity of their length, which is the reflection count; it tabulates the four components of $O(1,3)$ against the operations that reach them; it identifies the volume element with the central scalar imaginary up to sign and shows that it acts on Lorentzian space as minus the identity through the inner automorphism while acting as the identity through the sandwich; and it separates the two involutions in play, the Hermitian dagger of the algebra and the Clifford conjugation of the envelope, which agree on the real-quaternion slice and nowhere else.

The general theory is cited and not restated. The Clifford group, its norm, the groups Pin and Spin, the signed inner conjugation $\mathrm{Ad}^{\alpha}_{\tilde U}(\eta)=\alpha(\tilde U)\eta\tilde U^{-1}$, the reflection $\rho_\xi(\eta)=-\xi\eta\xi^{-1}$ and the Cartan–Dieudonné theorem are *The Clifford, Pin and Spin Groups with Signed Inner Conjugation*. The versor, the rotor and the sandwich action in general are *Versors, Rotors and the Sandwich Action with Signed Inner Conjugation*. The even-part identification $\mathbb{B}\cong\mathrm{Cl}^{+}_{1,3}$, the volume element and the Clifford dictionary are established in §*The Two Slots of the Envelope* and §*The Volume Element*. The sandwich, its kernel, its failure to be an automorphism and the contrast with the inner automorphism are *The Sandwich of a N-Regular, Spectrally Regular Biquaternion*, which owns the sandwich. The isometries read on the algebra itself, the rotor and the double covers, are *Biquaternion Rotations and Lorentz Transformations*; the reflections of that article are the reflections of the vector subspace $\mathrm{Vect}(\mathbb{B})$, a three-dimensional subspace of the algebra, and the reflections of this article are the Lorentz transformations of Lorentzian space, which are different maps on a different carrier. The group of units read against its matrix images is *$M_2(\mathbb{C})$ Model : The Product, the Trace and the Determinant*.

## The Form and its Isometries

**Definition.** The Hermitian sector is
$$
\mathbb{M}_+=\{\tilde{Q}:\tilde{Q}^{*}=\tilde{Q}\}=\mathrm{span}_{\mathbb{R}}\{e_t,i\vec e_x,i\vec e_y,i\vec e_z\},
$$
of real dimension four. On it the biquaternion norm restricts to a quadratic form of signature $(1,3)$: for $\tilde{Q}=te_t+i\vec u$ with $t\in\mathbb{R}$ and $\vec u\in\mathbb{R}^3$ one has $\langle \tilde{Q}\rangle_{\natural}=t^2-\lvert\vec u\rvert^2$. The anti-Hermitian sector is the mirror,
$$
\mathbb{M}_-=\{\tilde{Q}:\tilde{Q}^{*}=-\tilde{Q}\}=\mathrm{span}_{\mathbb{R}}\{ie_t,\vec e_x,\vec e_y,\vec e_z\},
$$
and the norm restricts to it with signature $(3,1)$.

**Definition.** Let $V$ be a real four-dimensional space with a quadratic form $q$ of signature $(1,3)$ — the abstract Lorentzian space, realised inside the algebra by the sector of the definition above — and let $O(q)=O(1,3)$ be its group of linear isometries. An isometry is **proper** when its determinant is $+1$ and **orthochronous** when it does not reverse the time orientation, that is when its $(0,0)$ entry is positive in a basis with the timelike coordinate first. The four combinations of the two signs are the four components of $O(1,3)$, and the identity component is the proper orthochronous group $SO^{+}(1,3)$.

**Remark.** Replacing $q$ by $-q$ does not change $O(q)$, and it exchanges the two sectors; $\mathbb{M}_+$ with $O(1,3)$ and $\mathbb{M}_-$ with $O(3,1)$ are the same statement in the two sign conventions, and every statement below holds for both with the roles of the timelike and spacelike directions exchanged. The corpus writes the form of $\mathbb{M}_+$ in the mostly-minus convention, and that is the one used here.

## The Two Slots of the Envelope

**Theorem (the envelope is two copies of the algebra).** Let $V$ be a real four-dimensional space with a form of signature $(1,3)$, let $\mathrm{Cl}(V)$ be its Clifford algebra, of real dimension $16$, and let $\mathrm{Cl}^{+},\mathrm{Cl}^{-}$ be its even and odd parts. Then
$$
\boxed{\;\mathrm{Cl}^{+}\cong\mathbb{B},\qquad \mathrm{Cl}(V)=\mathbb{B}\oplus\mathbb{B}\xi\;},
$$
for every non-isotropic $\xi\in V$, and the odd slot $\mathbb{B}\xi$ is a second copy of the algebra, of real dimension eight, containing the space $V$ itself.

**Proof.** The even part of the Clifford algebra of a four-dimensional space is eight-dimensional, and the identification $\mathrm{Cl}^{+}\cong\mathbb{B}$ is the Clifford structure of the algebra. For the splitting, fix $\xi\in V$ with $q(\xi)\neq0$. The element $\xi$ is odd, so $\mathbb{B}\xi\subseteq\mathrm{Cl}^{-}$; the map $Q\mapsto Q\xi$ is injective, so $\mathbb{B}\xi$ is eight-dimensional, and $\mathrm{Cl}^{-}$ is eight-dimensional as well, so $\mathbb{B}\xi=\mathrm{Cl}^{-}$. The inverse of the map is $Q\mapsto Q\xi^{-1}$, with $\xi^{-1}=\xi/q(\xi)$. The subspace $V$ is contained in the odd part, and $\mathbb{B}\xi$ is the odd part, so $V\subseteq\mathbb{B}\xi$.

**Remark (verified).** The dimensions were recomputed on the matrix model of $\mathrm{Cl}_{1,3}$, with the generators as the Dirac matrices of the mostly-minus metric: the even part has real dimension $8$ and is closed under multiplication, $\mathbb{B}\xi$ has real dimension $8$ for a unit $\xi$, the four generators lie in $\mathbb{B}\xi$, and the two together span the $16$-dimensional envelope.

**Remark (the Lorentzian space is odd, and its copy is inside the algebra).** The space on which the orthogonal group acts is $V$, and $V$ is odd: no element of the algebra is a Lorentzian vector. The algebra nevertheless contains a second copy of the same quadratic space, namely the Hermitian sector $\mathbb{M}_+$, which carries the form of signature $(1,3)$ by the definition above. The two copies are identified by the dictionary of the Clifford structure, and the identification is the reason a statement about a vector of $\mathbb{M}_+$ and a statement about a vector of $V$ can be read off one another. The identification is not the identity and is not available inside the algebra alone.

**Remark (the labelling).** The two labellings of the signature, $\mathrm{Cl}_{1,3}$ and $\mathrm{Cl}_{3,1}$, give the same even part and different ambient algebras, $\mathrm{Cl}_{1,3}\cong M_2(\mathbb{H})$ and $\mathrm{Cl}_{3,1}\cong M_4(\mathbb{R})$, as the matrix model of the envelope records. This article uses the mostly-minus labelling, which is the one in which the form on $\mathbb{M}_+$ has signature $(1,3)$ and the orthogonal group is $O(1,3)$; under the other labelling the two families of bivectors are exchanged, the quaternion units becoming products of two generators of square $+1$ instead of two of square $-1$, and nothing else in the article changes.

## The Grading of the Versors

**Definition (cited from *The Clifford, Pin and Spin Groups with Signed Inner Conjugation*).** A **versor** is a product $\tilde U=\eta_1\cdots\eta_k$ of non-isotropic vectors of $V$. The **Clifford group** $\Gamma$ is the set of invertible elements $\tilde U$ with $\mathrm{Ad}^{\alpha}_{\tilde U}(V)\subseteq V$, and the **Clifford norm** is $\langle\tilde U\rangle_{\natural}=\tilde U\tilde U^{\natural}$, the natural sign being the Clifford conjugation of the envelope, which on the even part is the quaternion conjugation of the algebra. The groups are
$$
\mathrm{Pin}=\{\tilde U\in\Gamma : \langle\tilde U\rangle_{\natural}=\pm1\},\qquad
\mathrm{Spin}=\mathrm{Pin}\cap\mathrm{Cl}^{+},
$$
and the **signed inner conjugation** is $\mathrm{Ad}^{\alpha}_{\tilde U}(\eta)=\alpha(\tilde U)\eta\tilde U^{-1}$, with $\alpha$ the grade involution. On vectors the reflection in the hyperplane orthogonal to a non-isotropic $\xi$ is
$$
\rho_\xi(\eta)=-\xi\eta\xi^{-1}=\eta-2B(\xi,\eta)q(\xi)^{-1}\xi .
$$

**Theorem (the reflection count is the parity of the length).** A product of an odd number of vectors acts by the signed inner conjugation as an isometry of determinant $-1$; a product of an even number acts as an isometry of determinant $+1$. On the odd slot of the envelope both behaviours occur, and on the algebra, which is the even slot, only the second does.

**Proof.** The reflection $\rho_\xi$ has determinant $-1$ on a four-dimensional space, and a product of $k$ reflections has determinant $(-1)^k$; Cartan–Dieudonné writes every isometry as such a product, and the signed inner conjugation of the versor $\eta_1\cdots\eta_k$ is the composite $\rho_{\eta_1}\circ\cdots\circ\rho_{\eta_k}$. The products of even length lie in the even slot, which is the algebra; the products of odd length lie in the odd slot, which is $\mathbb{B}\xi$ by the theorem above and is not contained in the algebra.

**Remark (verified).** The signed inner conjugation was computed on the matrix model for versors of length one, two, three and four: the odd lengths gave isometries of determinant $-1$ and involutions at length one, and the even lengths gave isometries of determinant $+1$, with both time orientations occurring among them. The sandwich of a unit of the algebra, in contrast, gave determinant $+1$ in every one of the tested cases, and no element of the algebra produced a negative value in four hundred random units; the two facts are one fact, the sandwich being even in both its factors.

**Corollary (Pin is not contained in the algebra).** Every non-isotropic vector can be rescaled to a vector of square $\pm1$, and such a vector lies in $\mathrm{Pin}$ and is odd, hence is not an element of $\mathbb{B}$. Therefore
$$
\boxed{\;\mathrm{Pin}(1,3)\not\subseteq\mathbb{B},\qquad
\mathrm{Pin}(1,3)\cap\mathrm{Cl}^{+}=\mathrm{Spin}(1,3)\cong\mathbb{B}^{\times}_1\;}.
$$
The only part of the Pin group that is an object of the biquaternion algebra is the spin group, which is its even part.

**Remark (which reflections).** The reflections of this article are the Lorentz reflections, that is the maps $\rho_\xi$ of the Lorentzian space. The reflections of *Biquaternion Rotations and Lorentz Transformations* are the maps $\rho_\eta(\tilde U)=-\eta\tilde U\eta^{-1}$ for $\langle \eta\rangle_{\natural}=1$ acting on the three-dimensional subspace $\mathrm{Vect}(\mathbb{B})$ of the algebra, where orthogonality and anticommutation coincide; those maps are realised by elements of the algebra, whereas the Lorentz reflections are not, which is the distinction that article records in the sentence that the Lorentz reflections live in the Clifford layer.

## What the Algebra Reaches on the Hermitian Sector

**Theorem (the sandwich of a unit is proper orthochronous).** Let $\tilde{Q}\in\mathbb{B}$ with $\lvert \langle \tilde{Q}\rangle_{\natural}\rvert=1$, and let
$$
\mathrm{H}_{\tilde{Q}}(\tilde{Q}_2)=\tilde{Q}\tilde{Q}_2\tilde{Q}^{*}
$$
be the bilinear sandwich of *Biquaternion Rotations and Lorentz Transformations*. Then the restriction of $\mathrm{H}_{\tilde{Q}}$ to $\mathbb{M}_+$ is a linear isometry of signature $(1,3)$ of determinant $+1$ and of positive time orientation. Conversely every proper orthochronous Lorentz transformation is the restriction of a sandwich of this kind, and the map from the norm-one group $\mathbb{B}^{\times}_1$ to $SO^{+}(1,3)$ is two-to-one with kernel $\{\pm e_t\}$.

**Proof.** Under $\mathsf{M}_2$ the sandwich is $X\mapsto M X M^{\dagger}$ with $M=\mathsf{M}_2(\tilde{Q})$, which is the standard action of $SL(2,\mathbb{C})$ on the Hermitian matrices and is a linear isometry of signature $(1,3)$. The condition $\lvert \langle \tilde{Q}\rangle_{\natural}\rvert=1$ is $\lvert\det M\rvert=1$, and an invertible $M$ with $\lvert\det M\rvert=1$ differs from an element of $SL(2,\mathbb{C})$ by a phase, $M=e^{i\theta}M_0$ with $\det M_0=1$; the phase cancels in the sandwich because $MM^{\dagger}=M_0M_0^{\dagger}$, so the map is that of $M_0$ and is proper orthochronous. The converse and the kernel are the double cover $SL(2,\mathbb{C})\to SO^{+}(1,3)$ of *Biquaternion Rotations and Lorentz Transformations*.

**Remark (the isometry condition is exactly the unit norm).** The sandwich multiplies the norm by $\lvert \langle \tilde{Q}\rangle_{\natural}\rvert^{2}$, since $\tilde{Q}^{*}$ has norm $(\langle \tilde{Q}\rangle_{\natural})^{\natural}$ and the norm is multiplicative; so $\lvert \langle \tilde{Q}\rangle_{\natural}\rvert=1$ is what makes it an isometry, and a zero divisor generates nothing, having no inverse. The corpus works on the norm-one slice $\langle\tilde Q\rangle_{\natural}=1$, which parametrises the same operators because $\langle i\tilde{Q}\rangle_{\natural}=-\langle \tilde{Q}\rangle_{\natural}$ and the operator is blind to the scalar imaginary.

**Theorem (the four components, and the two discrete operations).** On $\mathbb{M}_+$ the following operations are isometries, and they fall in the four components of $O(1,3)$:

| operation on $\mathbb{M}_+$ | determinant | time orientation | component |
|---|---|---|---|
| $\tilde U\mapsto \tilde{Q}\tilde U\tilde{Q}^{*}$, with $\lvert \langle \tilde{Q}\rangle_{\natural}\rvert=1$ | $+1$ | $+$ | the identity component $SO^{+}(1,3)$ |
| $\tilde U\mapsto \tilde{Q}\tilde U^{\natural}\tilde{Q}^{*}$, the argument quaternion-conjugated | $-1$ | $+$ | the improper orthochronous coset |
| $\tilde U\mapsto -\tilde{Q}\tilde U\tilde{Q}^{*}$, the result negated | $+1$ | $-$ | the proper anti-orthochronous coset |
| $\tilde U\mapsto -\tilde{Q}\tilde U^{\natural}\tilde{Q}^{*}$, both at once | $-1$ | $-$ | the improper anti-orthochronous coset |

The two operations beyond the sandwich are quaternion conjugation of the argument and the negation; they are the discrete parity and the product of parity with time reversal, and with the sandwich they generate the whole of $O(1,3)$.

**Proof.** The first row is the theorem above. Quaternion conjugation fixes $e_t$ and negates $\vec e_x,\vec e_y,\vec e_z$, so on $\mathbb{M}_+$ it sends $te_t+i\vec u$ to $te_t-i\vec u$, which is the parity $\mathrm{diag}(1,-1,-1,-1)$, of determinant $-1$ and orthochronous; a determinant $-1$ isometry followed by a proper orthochronous one is improper orthochronous, and the determinant multiplies. The negation sends $te_t+i\vec u$ to $-te_t-i\vec u$, of determinant $+1$ and anti-orthochronous. The four signs are distinct, and the table is complete because $O(1,3)$ has exactly four components.

**Remark (verified).**

**Remark (parity and time reversal).** The parity $P$ is the quaternion conjugation of the argument, and the product $PT$ is the negation; the time reversal alone is therefore the composite $P\circ(PT)$, which is the quaternion conjugation followed by the negation. Neither $P$ nor $PT$ is a sandwich, since every sandwich with $\lvert\langle\tilde Q\rangle_{\natural}\rvert=1$ is proper orthochronous, and neither is the square of the other.

## The Volume Element

**Definition.** Let $\gamma^{0},\gamma^{1},\gamma^{2},\gamma^{3}$ generate the envelope in the mostly-minus convention, with $(\gamma^{0})^2=+1$ and $(\gamma^{k})^2=-1$, and let
$$
\Omega=\gamma^{0}\gamma^{1}\gamma^{2}\gamma^{3}
$$
be the volume element of $\mathrm{Cl}_{1,3}$. Then $\Omega^2=-1$, and $\Omega$ commutes with the even slot and anticommutes with every vector. In the biquaternion dictionary the quaternion units are the spatial bivectors, $\vec e_x\mapsto\gamma^{2}\gamma^{3}$, $\vec e_y\mapsto\gamma^{3}\gamma^{1}$, $\vec e_z\mapsto\gamma^{1}\gamma^{2}$, and the central scalar imaginary is $i\mapsto-\Omega$.

**Theorem (the volume element is minus the identity on Lorentzian space).** On the odd slot the signed inner conjugation of the volume element negates every vector,
$$ \mathrm{Ad}^{\alpha}_{\Omega}(\eta)=\Omega \eta\Omega^{-1}=-\eta, $$
so that $\Omega$ acts on the Lorentzian space as $-\mathrm{id}$, the product of parity with time reversal, of determinant $+1$ and anti-orthochronous. On the Hermitian copy of the same space the sandwich of the corresponding element, the central scalar imaginary, is the identity, since $i$ is central and $i^{\dagger}=-i$.

**Proof.** The volume element of an even-dimensional Clifford algebra anticommutes with every vector: moving $\gamma^{j}$ past the monomial $\Omega$, in which it occurs, costs the sign $(-1)^{3}$, so $\gamma^{j}\Omega=-\Omega\gamma^{j}$, and the same for every generator. Hence $\Omega \eta\Omega^{-1}=-\Omega\Omega^{-1}\eta=-\eta$. For the second statement, $i$ commutes with everything, so $\mathrm{H}_{i}(\tilde U)=iUi^{\dagger}=iU(-i)=-i^2\tilde U=\tilde U$.

**Remark (verified).** Both statements were recomputed on the matrix model: the signed inner conjugation of $\Omega$ gave $-\eta$ on all four generators, and the sandwich of $\mathsf{M}_2(\pm i)=\pm iI$ gave the identity on the Hermitian sector.

**Remark (what this says about the determinant-one components).** The volume element is an element of the algebra, and it is even, so the anti-orthochronous part of $SO(1,3)$ is reached by an element of the algebra after all; but it is reached by the inner automorphism and not by the sandwich, and the sandwich of the same element is the identity. The algebra's elements therefore supply more of the orthogonal group than the algebra's sandwich does, and the difference is exactly the replacement of the dagger by the inverse.

## The Two Involutions

**Theorem (the dagger is not the Clifford conjugation).** Let $\mathrm{rev}$ be the reversion of $\mathrm{Cl}_{1,3}$, the anti-automorphism fixing every vector; on the even slot it is the Clifford conjugation. Restricted to $\mathbb{B}$ the two involutions ${}^{*}$ and $\mathrm{rev}$ are different: $\mathrm{rev}$ fixes $e_t$, negates $\vec e_x,\vec e_y,\vec e_z$, fixes $i$ and $\Omega$, and negates the boosts $i\vec e_k$, while ${}^{*}$ fixes $e_t$, negates $\vec e_x,\vec e_y,\vec e_z$, negates $i$, and fixes the boosts $i\vec e_k$. Their composite is the real-structure automorphism $\sigma$ of the algebra, the map $A\otimes h\mapsto\bar{A}\otimes h$ that conjugates the coefficients and fixes the quaternion units,
$$
\mathrm{rev}={}^{*}\circ\sigma .
$$

**Proof.** The dictionary sends $\vec e_k$ to a spatial bivector and $i$ to $-\Omega$. Reversion negates every bivector, so it negates $\vec e_k$ and $i\vec e_k$, and it fixes the identity and the degree-four volume element. The Hermitian dagger negates the coefficients of $\vec e_x,\vec e_y,\vec e_z$ and of $i$, and fixes $i$ times a quaternion unit. The two agree on $e_t$ and on $\vec e_k$, and differ on $i$ and on $i\vec e_k$; the composite therefore fixes the quaternion units and negates $i$, which is the automorphism $A\otimes h\mapsto\bar{A}\otimes h$.

**Remark (verified).** The composite was recomputed: the reversion of the volume element is the volume element, the reversion of $i\vec e_x$ is $-i\vec e_x$, the dagger of $i$ is $-i$, and the identity $\mathrm{rev}={}^{*}\circ\sigma$ held on random elements of the algebra to machine precision. The equality $\mathrm{rev}(\tilde{Q})=\tilde{Q}^{*}$ holds exactly on the real-quaternion slice, since it is equivalent to $\sigma$ fixing the element and $\sigma$ conjugates the four coefficients.

**Corollary (they agree on the real-quaternion slice).** On $\mathbb{H}_{\mathbb{B}}$, the elements with four real coefficients, the coefficient conjugation is the identity and the two involutions coincide. Consequently on that slice the sandwich is the inner automorphism scaled by the norm,
$$
\boxed{\;\mathrm{H}_{\tilde{Q}}=\langle \tilde{Q}\rangle_{\natural}\cdot\mathrm{Ad}_{\tilde{Q}},\qquad
\mathrm{Ad}_{\tilde{Q}}(\tilde{Q}_2)=\tilde{Q}\tilde{Q}_2\tilde{Q}^{-1}\;},
$$
and off the slice the two differ.

**Proof.** The inverse is $\tilde{Q}^{-1}=\tilde{Q}^{\natural}/\langle \tilde{Q}\rangle_{\natural}$, so $\langle \tilde{Q}\rangle_{\natural}\mathrm{Ad}_{\tilde{Q}}(\tilde U)=\tilde{Q}\tilde U\tilde{Q}^{\natural}$, which is the sandwich for every $\tilde{Q}$ with $\tilde{Q}^{\natural}=\tilde{Q}^{*}$, that is on the real-quaternion slice and only there.

**Remark (the shear is the coefficient conjugation).** The sandwich and the inner automorphism agree on the real-quaternion slice and differ everywhere else, the difference being the coefficient conjugation of the right factor; the sandwich is the inner automorphism read through the Hermitian dagger rather than through the algebra inverse.

**Remark (the dagger is the Euclidean reversion).** The involution ${}^{*}$ is the reversion of a different Clifford structure on the same algebra: the positive definite one, $\mathbb{B}\cong\mathrm{Cl}_{3,0}$, in which the vectors are the imaginary quaternions $i\vec e_k$, and which is the structure of *The Number Systems as Clifford Algebras*. Reversion fixes vectors, so it fixes the $i\vec e_k$, and it negates the products of three of them, which is why it negates $i$; that is exactly the action of the dagger. The Lorentzian reversion is the other one, and the two disagree by the coefficient conjugation and not by a change of basis.

## What the Algebra Does Not Cover

**The orthogonal group is an object of the algebra; the Pin group is not.** $O(1,3)$ is read on the Hermitian sector, its elements are linear maps of a subspace of the algebra, and the table above exhibits each component as an operation on that subspace. The Pin group is not an object of the algebra: it contains the odd versors, which are the reflections, and the odd slot of the envelope is a second copy of the algebra rather than a part of it. A row for $\mathrm{Pin}$ would place an object of $\mathrm{Cl}_{1,3}$ inside $\mathbb{B}$, which is false, and it would give that object two owners, the Clifford articles already owning it.

**What the last cover is.** The double cover the algebra records is the even one, $\mathrm{Spin}(1,3)\to SO^{+}(1,3)$, with kernel $\{\pm e_t\}$; the odd slot records the covers of the improper components, whose reflections are the odd versors of $\mathrm{Pin}$. The two-to-one cover of the whole orthogonal group by $\mathrm{Pin}$ is a statement about the envelope, and the corresponding statement about the algebra is only about its identity component.

**Where the determinant minus one lives.** No element of the algebra gives a reflection of Lorentzian space, and no sandwich of the algebra leaves the proper orthochronous component: the determinant of a sandwich is $+1$ because the sandwich is even in both factors. The determinant minus one transformations of the space are reached either by the odd slot of the envelope or, inside the algebra, by conjugating the argument, which is the parity, and which is a reflection of the space and not a sandwich.

**What an object of the algebra can and cannot hold.** The objects of the algebra are the elements of $\mathbb{B}$ and the groups and sets built from them by multiplication, conjugation and the sandwich. The orthogonal group is such an object, read on the Hermitian sector. The Pin group is not, because it contains the odd versors, which are the reflections; the only part of it that is an object of the algebra is the even cover $\mathbb{B}^{\times}_1\cong\mathrm{Spin}(1,3)$.

## Summary

The biquaternion algebra is the even part of the Clifford algebra of Lorentzian space, and the envelope is two copies of it, $\mathrm{Cl}_{1,3}=\mathbb{B}\oplus\mathbb{B}\xi$, the odd copy containing the space on which the orthogonal group acts. The parity of the length of a versor is its reflection count, so the odd versors are the reflections and lie outside the algebra, and the only part of $\mathrm{Pin}(1,3)$ that is an object of the algebra is $\mathrm{Spin}(1,3)=\mathbb{B}^{\times}_1$. The bilinear sandwich of a unit of norm one is an isometry of the Hermitian sector of determinant $+1$ and orthochronous, and with quaternion conjugation of the argument and the negation it generates the whole orthogonal group: the four operations give the four components, of determinants $\pm1$ and of the two time orientations. The volume element, which is the central scalar imaginary up to sign, anticommutes with every vector, so it acts on Lorentzian space as $-\mathrm{id}$, the product of parity and time reversal, through the inner automorphism, while its sandwich is the identity because the scalar imaginary is central and Hermitian-conjugates to its negative. The dagger of the algebra is the reversion of the Euclidean Clifford structure and not the Clifford conjugation of the Minkowski one; the two differ by the automorphism that conjugates the coefficients, they agree exactly on the real-quaternion slice, and there the sandwich is the inner automorphism scaled by the norm.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{M}_+,\mathbb{M}_-$ | Hermitian and anti-Hermitian sectors, of signatures $(1,3)$ and $(3,1)$; the Hermitian one is the copy of Lorentzian space inside the algebra |
| $V$ | The four-dimensional space of signature $(1,3)$ whose Clifford algebra is the envelope; it is odd, and it lies in the odd slot |
| $\mathrm{Cl}_{1,3},\mathrm{Cl}^{+},\mathrm{Cl}^{-}$ | The envelope, of real dimension $16$; its even part, the algebra, of real dimension $8$; its odd part, $\mathbb{B}\xi$, a second copy of the algebra |
| $\xi$ | A non-isotropic vector of $V$; the odd slot is $\mathbb{B}\xi$ and the inverse of $Q\mapsto Q\xi$ is $Q\mapsto Q\xi^{-1}$ |
| $\tilde{Q}$ | An element of $\mathbb{B}$; the operator $\mathrm{H}_{\tilde{Q}}(\tilde{Q}_2)=\tilde{Q}\tilde{Q}_2\tilde{Q}^{*}$ |
| $\rho_\xi(\eta)=-\xi\eta\xi^{-1}$ | The reflection in the hyperplane orthogonal to $\xi$; a Lorentz transformation, realised by the odd versor $\xi$ |
| $\mathrm{Ad}^{\alpha}_{\tilde U}(\eta)=\alpha(\tilde U)\eta\tilde U^{-1}$ | The signed inner conjugation; $\mathrm{Ad}_{\tilde{Q}}(\tilde{Q}_2)=\tilde{Q}\tilde{Q}_2\tilde{Q}^{-1}$ is the inner automorphism |
| $\Gamma$, $\langle\tilde U\rangle_{\natural}=\tilde U\tilde U^{\natural}$ | The Clifford group and the Clifford norm; $\mathrm{Pin}=\{\langle\tilde U\rangle_{\natural}=\pm1\}$ and $\mathrm{Spin}=\mathrm{Pin}\cap\mathrm{Cl}^{+}\cong\mathbb{B}^{\times}_1$ |
| $\Omega=\gamma^{0}\gamma^{1}\gamma^{2}\gamma^{3}$ | The volume element of $\mathrm{Cl}_{1,3}$, $\Omega^2=-1$, central in the even part and anticommuting with every vector; the central scalar imaginary is $-\Omega$ |
| $\mathrm{rev},\sigma$ | The reversion of $\mathrm{Cl}_{1,3}$ fixing every vector; the automorphism conjugating the coefficients, $A\otimes h\mapsto\bar{A}\otimes h$; $\mathrm{rev}={}^{*}\circ\sigma$ |
| $\mathbb{H}_{\mathbb{B}}$ | The real-quaternion slice, four real coefficients; the slice on which ${}^{*}$ and $\mathrm{rev}$ coincide and $\mathrm{H}_{\tilde{Q}}=\langle \tilde{Q}\rangle_{\natural}\mathrm{Ad}_{\tilde{Q}}$ |
| $P,PT$ | Parity, the quaternion conjugation of the argument; the product of parity and time reversal, the negation; neither is a sandwich |
| $O(1,3),SO^{+}(1,3)$ | The orthogonal group of the form and its identity component; their components are indexed by the determinant and the time orientation |

## Further Reading

- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the Clifford group, its norm, the signed inner conjugation and the double cover of the orthogonal group.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the identification of the biquaternion algebra with the even part of $\mathrm{Cl}_{1,3}$ and for the matrix models of the two slots.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for the Clifford algebra as the ambient object, the volume element and the parity grading.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge University Press, 2003), for the versor product, the reflection and the Cartan–Dieudonné theorem as they are used in the physical literature.
- Within the corpus, the owner articles [The Clifford, Pin and Spin Groups with Signed Inner Conjugation](the-clifford-pin-and-spin-groups-with-signed-inner-conjugation.html), [Versors, Rotors and the Sandwich Action with Signed Inner Conjugation](versors-rotors-and-the-sandwich-action-with-signed-inner-conjugation.html), [Biquaternion Rotations and Lorentz Transformations](biquaternion-rotations-and-lorentz-transformations.html).
