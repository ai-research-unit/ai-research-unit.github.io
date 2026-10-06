# __The Twisted Spinor Operator Representation of Biquaternions__

## Introduction

The spinor of the corpus is a module of the biquaternion algebra, and this article is about the operator that acts on it — the twisted spinor representation, the operator form of the polar word. The polar representation of a biquaternion describes an **object**: every element of non-vanishing norm is the product of four factors,

$$
\tilde{Q} = r\,e^{i\alpha}\,B\,\hat{q} ,
$$

a positive real **scale** $r$, a central **phase** $e^{i\alpha}$, a Hermitian positive **boost** $B$, and a unit real quaternion **rotor** $\hat{q}$ (*The Polar Element Representation of Biquaternions*, *The Polar Element Representation in Subspaces*). This article describes the same element as an **operator** on the simple module, and the claim that organizes the whole article is that the description is exactly the operator version of the polar description, and that it exists on exactly the same elements:

$$
\text{twisted spinor representation} \;=\; \text{operator version of the polar element representation},
\qquad\text{available only outside the null cone.}
$$

The general name for a space an operator acts on is a **module**; the name of the module is not "spinor" in general. It is a **spinor** only when the operator is restricted to the norm-one slice; kept general, the module is a **twisted spinor**, and the twist is the record of the scale and the phase. The correspondence with the polar word is one-to-one: the scale and the phase become the **twist**, that is the character by which the module is multiplied, and the boost and the rotor become the **norm-one operator**, that is the spinor representation of the Lorentz group.

The distinction is not verbal, and it is the answer to a question the corpus asks repeatedly: a biquaternion of general norm is not a Lorentz transformation, and the module it acts on is not the Lorentz module. The algebra provides two ways for an element to act: **left multiplication** on the two-dimensional complex module $S=\mathbb{C}^2$, and the **Hermitian sandwich** on the algebra itself,

$$
\tilde R\;\longmapsto\;\tilde{Q}\,\tilde R\,\tilde{Q}^{*} ,
$$

which is the action on the **material sector** $\mathbb{M}_-$, where the four-vectors live (*The Sandwich Action in Subspaces*). This article treats the first action, the one on the module, and reads it against the polar element representation. Both are operators, and they see different parts of the polar word: the module sees all four factors, while the sandwich sees three of them, and the comparison is made below.

Three claims organize the article. First, the general operator's module is the spinor module of the norm-one group **twisted** by a one-dimensional representation of the scaling: the scale and the phase do not change the module, they change its **weight**, and the four polar factors map onto the operator data term by term. Second, the correspondence fails on exactly one set — the null cone — and this is the condition of existence: the twisted spinor representation is an operator description of the polar word, so it is available precisely where the polar word is, that is, for $N(\tilde{Q})\neq0$ and nowhere else. Third, the norm-one slice, where $r=1$ and $\alpha=0$, is the Lorentz group: it is the untwisted case, and it is the only case in which the sandwich is an isometry.

**Conventions.** The conventions of *Conventions in the Biquaternion Universe* are used throughout. The quaternion basis is $e_0=1,e_1,e_2,e_3$, with $e_k^2=-e_0$ and $e_1e_2=e_3$; the scalar imaginary is $i$, commuting with the quaternion units. The algebra isomorphism is $\Phi:\mathbb{B}\to M_2(\mathbb{C})$ with $\Phi(e_k)=-i\sigma_k$ and $\Phi(i)=iI_2$, and the biquaternion norm is the determinant, $N(\tilde{Q}) = \langle\tilde{Q},\tilde{Q}\rangle_{\natural}=\tilde{Q}\tilde{Q}^{\natural}=\det\Phi(\tilde{Q})$. The **material sector** is the anti-Hermitian subspace $\mathbb{M}_-$ and the **informational sector** is the Hermitian subspace $\mathbb{M}_+$ (*The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*, *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*); the group of units is $\mathbb{B}^{\times}\cong GL(2,\mathbb{C})$ and the group of unit-norm elements is $\mathbb{B}^{\times}_1=\{N=1\}\cong SL(2,\mathbb{C})$ (*Biquaternion Norm and Invertibility*, *Biquaternion Lie Algebra*, *Biquaternion Lie Group and Exponential Structure*). The polar form and its four factors are *The Polar Element Representation of Biquaternions* and *The Polar Element Representation in Subspaces*, and are used here without repetition; the module is *The 2×2 Matrix Element Representation of Biquaternions* and *Modules over the Biquaternion Algebra*; the realizations of the algebra are *The 4×4 Regular Matrix Element Representation of Biquaternions* and *The Four-Vector Element Representation of Biquaternions*; and the operator on the algebra, with its laws and its invariants, is *Biquaternion Rotations and Lorentz Transformations* and *The Sandwich Action in Subspaces*.

## The Operator Version of the Polar Element Representation

The polar word and the operator data are the same information, cut differently, and the cut is the one the two-sided action makes.

**Theorem (the correspondence).** Let $\tilde{Q}=re^{i\alpha}B\hat{q}$ with $N(\tilde{Q})\neq0$, and let $\rho=\sqrt{N(\tilde{Q})}=re^{i\alpha}$ and $\tilde{\Lambda}=B\hat{q}$, so that $\tilde{Q}=\rho\tilde{\Lambda}$ with $N(\tilde{\Lambda})=1$. Then:

1. the module of $\tilde{Q}$ is the module of $\tilde{\Lambda}$, unchanged;
2. the scale $r$ and the phase $e^{i\alpha}$ act on that module by the single complex number $\rho$, that is, through the **twist** $\chi(\rho)=\rho$;
3. the boost $B$ and the rotor $\hat{q}$ act on that module as the norm-one element $\tilde{\Lambda}=B\hat{q}$, that is, as the **spinor representation** of the Lorentz group;
4. the sandwich, by contrast, is $r^{2}$ times the norm-one sandwich, so it keeps the scale squared, discards the phase, and doubles the boost and the rotor parameters.

**Proof.** The matrix image factorizes as $\Phi(\tilde{Q}) = \Phi(\rho\tilde{\Lambda}) = \rho\,\Phi(\tilde{\Lambda})$, with $\rho$ central and $\Phi(\tilde{\Lambda})\in SL(2,\mathbb{C})$; the action on the module is left multiplication by this product, which is (1) and (2) and (3). The sandwich statement is the factorization $\mathrm{H}_{\tilde{Q}}=r^{2}\mathrm{H}_{\tilde{\Lambda}}$ of *The Sandwich Action in Subspaces*.

| polar factor | physical name | data it becomes in the operator description | seen by the module | seen by the sandwich |
|---|---|---|---|---|
| scale $r$ | dilatation | modulus of the twist | one factor $r$ | two factors, $r^{2}$ |
| phase $e^{i\alpha}$ | central phase | argument of the twist | one factor $e^{i\alpha}$ | cancels |
| boost $B$ | rapidity $\psi$ | norm-one operator, half-rapidity $\psi/2$ | stores $\psi/2$ | produces $\psi$ |
| rotor $\hat{q}$ | angle $\theta$ | norm-one operator, half-angle $\theta/2$ | stores $\theta/2$ | produces $\theta$ |

The table is the article in miniature. **The polar representation is the object; the twisted spinor representation is the same object read as an operator on its module; the sandwich is the same object read as an operator on the algebra.** The three are not three constructions but three readings of one factorization, and that is why they share a domain: all three are statements about the polar word. The physical content is the same sentence: the scale is a length, the phase is the sector, the boost is a rapidity and the rotor is a rotation, and the operator that carries all four of them is not a Lorentz transformation but a Lorentz transformation together with a dilatation and a phase.

**The condition of existence is the same cone.** The construction above begins with an invertible element, and that is exactly the condition: the twisted spinor representation exists precisely for the biquaternions outside the null cone, $N(\tilde{Q})\neq0$, which by the determinant criterion of *Biquaternion Norm and Invertibility* are the invertible, non-zero-divisor elements. A null element still acts on the module $S$ by left multiplication, since the action of the algebra on its own simple module is defined for every element, but it is a singular operator, of rank at most one, and it carries no modulus and therefore no twist. The cone is one complex equation, hence two real equations, so it has real codimension two and the group of units $\mathbb{B}^{\times}$ has the same real dimension $8$ as the algebra $\mathbb{B}$: the domain of the twisted spinors is the algebra with a codimension-two set removed. The set is exactly the domain of the polar element representation, since the polar and the twisted descriptions exist on the same elements and fail on the same cone; the failure is a failure of the *description*, not of the action, and the action itself survives, which is what the next section records.

**Remark (the order of the four factors).** The correspondence is faithful, so the order of the factors is the order of the operations: the boost acts first in the polar word $B\hat{q}$ and the rotor second, and the same order appears in the operator $\tilde{\Lambda}=B\hat{q}$ and in the sandwich $\tilde{\Lambda}\tilde R\tilde{\Lambda}^{*}=B(\hat{q}\tilde R\hat{q}^{-1})B$. Nothing here reorders them.

## The Twisted Module of the Operator

Let $\tilde{Q}$ be invertible. Write its polar modulus and its norm-one part,

$$
\rho = \sqrt{N(\tilde{Q})} = r\,e^{i\alpha}\in\mathbb{C}^{\times},
\qquad
\tilde{\Lambda} = \frac{\tilde{Q}}{\rho},
\qquad
N(\tilde{\Lambda})=1,
\qquad
\tilde{\Lambda}=B\,\hat{q}.
$$

Under the matrix isomorphism the operator on the module is a scalar times a norm-one element,

$$
\tilde{Q}\;\longmapsto\;\Phi(\tilde{Q})=\rho\,\Phi(\tilde{\Lambda})
=\underbrace{\rho}_{\text{scalar}}\;\underbrace{\Phi(B)\,\Phi(\hat{q})}_{\text{in }SL(2,\mathbb{C})},
$$

and the action on $S=\mathbb{C}^2$ is left multiplication, $\psi\mapsto\Phi(\tilde{Q})\psi$.

**The module is the spinor module, twisted.** The factor $\Phi(\tilde{\Lambda})$ acts as the ordinary spinor representation; the scalar $\rho$ needs no module of its own. By Schur's lemma the centre acts on any simple module by a scalar, so the scale $r$ and the phase $e^{i\alpha}$ do not enlarge the module, they multiply it. What they produce is a **twist**, a one-dimensional representation $\chi$ of the scaling group, here $\chi(\rho)=\rho$. The module of the general operator is therefore the module of the norm-one group **twisted** by $\chi$, written $S\otimes\chi$, and its elements are the **twisted spinors**. Three names, in increasing generality:

| name | operator | what acts |
|---|---|---|
| spinor | norm-one element $\tilde{\Lambda}$ | the Lorentz double cover $SL(2,\mathbb{C})$ |
| twisted spinor | general unit $\tilde{Q}=\rho\tilde{\Lambda}$ | the group of units $GL(2,\mathbb{C})$ |
| module | any of the above, abstractly | the algebra |

**The twist changes the weight, not the module.** Since $\mathbb{B}$ is simple, its only simple module is $S$; the twist leaves the irreducible module $\mathbb{C}^2$ alone and only rescales it. Nothing is added to the module; something is added to the label. This is the precise sense in which "Lorentz is a particular case": the Lorentz case is the twist $\chi=1$, and the general operator is the same module with a non-trivial scalar character. The scale the twist records is exactly the scale the polar representation produces, and it is the same scale the sandwich squares.

A caution on the vocabulary. A **spinor** is a vector of the module, not the operator that acts on it, and not the rotor. The polar decomposition writes the **operator** as $\rho B\hat{q}$; the spinor is what $\rho B\hat{q}$ acts on. The two must not be conflated, since the whole content of the twist is that the operator has more factors than the module can distinguish. The domain of the construction is the complement of the light cone, as the previous section states, and the failure of the *description* on the cone does not remove the *action*: a null element still multiplies the module, it only does so singularly.

## The Four Factors as Operators

Each polar factor is an operator with its own range, and each acts differently on the module and on the algebra. The table collects them physically; the sections that follow prove the two entries that are not immediate.

| factor | physical name | operator | on the module, $\psi\mapsto\Phi(\tilde{Q})\psi$ | on the sandwich, $\tilde R\mapsto\tilde{Q}\tilde R\tilde{Q}^{*}$ |
|---|---|---|---|---|
| scale $r$ | dilatation | scaling | one factor $r$ | two factors, $r^{2}$ |
| phase $e^{i\alpha}$ | central phase | twist | one factor $e^{i\alpha}$ | cancels |
| boost $B$ | rapidity $\psi$ | boost | stores $\psi/2$ | produces $\psi$ |
| rotor $\hat{q}$ | angle $\theta$ | rotation | stores $\theta/2$ | produces $\theta$ |

The module sees **all four** factors; the sandwich sees **three** of them. The scale is counted twice by the sandwich and once by the module, because the sandwich is bilinear in the operator; the phase is counted once by the module and never by the sandwich, because the phase and its inverse appear on the two sides and are central. Physically: the phase is invisible to the material sector, and the scale is felt by the material sector twice as strongly as by the module.

## The Hermitian Sandwich and the Doubled Parameters

**The factorization.** Let $\tilde{Q}=r e^{i\alpha}B\hat{q}$. The Hermitian conjugate reverses the product and inverts each factor's conjugate type,

$$
\tilde{Q}^{*}=\hat{q}^{-1}\,B\,r\,e^{-i\alpha},
\qquad
B^{\dagger}=B,\qquad \hat{q}^{\dagger}=\hat{q}^{-1},\qquad r^{\dagger}=r,\qquad (e^{i\alpha})^{\dagger}=e^{-i\alpha},
$$

so that, the phase being central and cancelling,

$$
H_{\tilde{Q}}(\tilde R)=\tilde{Q}\,\tilde R\,\tilde{Q}^{*}
=r\,e^{i\alpha}B\hat{q}\;\tilde R\;\hat{q}^{-1}B\,r\,e^{-i\alpha}
=r^{2}\,B\bigl(\hat{q}\,\tilde R\,\hat{q}^{-1}\bigr)B
=r^{2}\,\tilde{\Lambda}\,\tilde R\,\tilde{\Lambda}^{*}.
$$

This is the central identity of the article. Everything else is a reading of it.

**Double dilatation.** The identity separates the sandwich into a scalar factor and a norm-one sandwich,

$$
H_{\tilde{Q}}=r^{2}\,H_{\tilde{\Lambda}},
\qquad\text{so}\qquad
H_{z\tilde{Q}}=\lvert z\rvert^{2}H_{\tilde{Q}}\quad (z\in\mathbb{C}^{\times}).
$$

The scale enters **twice**, once from $\tilde{Q}$ and once from $\tilde{Q}^{*}$, and the two copies multiply because the scale is central: the sandwich carries $r^{2}$ where the operator carries $r$. The effect is graded: on lengths the factor is $r^{2}$, on the biquaternion norm it is $r^{4}$, since the norm is quadratic. The polar statement is the same one read backwards,

$$
N\bigl(H_{\tilde{Q}}(\tilde R)\bigr)=\lvert N(\tilde{Q})\rvert^{2}N(\tilde R) = \langle\tilde R,\tilde R\rangle_{\natural}=\bigl(r^{2}\bigr)^{2}N(\tilde R),
$$

which is the scaling already recorded in the polar article: the interval of the material sector is dilated by the square of the scale, and the length by the scale. And the phase, which is the other central factor, does the opposite of the scale: it appears once on the module and **never** in the sandwich, since $e^{i\alpha}$ and $e^{-i\alpha}$ are inverse and commute past everything. A central phase therefore changes the module and leaves the material sector untouched.

**Doubled boost and rotation.** The norm-one part of the sandwich is the conjugation by $\tilde{\Lambda}=B\hat{q}$,

$$
\tilde R\;\longmapsto\;\tilde{\Lambda}\,\tilde R\,\tilde{\Lambda}^{*}=B\bigl(\hat{q}\,\tilde R\,\hat{q}^{-1}\bigr)B ,
$$

a rotation followed by a boost, both with **doubled** parameters. The rotor $\hat{q}$ stores a half-angle, $e^{\mathbf{u}/2}$ with rotation angle $\lvert\mathbf{u}\rvert=\theta$, and the conjugation $\hat{q}\,\tilde R\,\hat{q}^{-1}$ is the rotation by the full angle; the same half-angle is what makes a spinor change sign under a rotation by $2\pi$. The boost factor $B$ stores a half-rapidity, $\cosh\tfrac{\psi}{2}+i\sinh\tfrac{\psi}{2}\hat{\mathbf{n}}$, and the conjugation $B\,\tilde R\,B$ is the Lorentz boost of the full rapidity. On the boost axis $e_3$ both are diagonal and exact:

$$
\Phi(B)=\mathrm{diag}\bigl(e^{\psi/2},e^{-\psi/2}\bigr),
\qquad
\Phi(B)\,X\,\Phi(B)=\mathrm{diag}\bigl(e^{\psi},e^{-\psi}\bigr)X ,
$$

so the exponent deposited by the operator is doubled by the sandwich. On a four-vector $X=t\,e_0+z\,e_3$ of the material sector this reads on the $(t,z)$ plane as

$$
t'=t\cosh\psi+z\sinh\psi, \qquad z'=t\sinh\psi+z\cosh\psi ,
$$

the standard boost with rapidity $\psi$, produced by the rotor that stores $\psi/2$. The exponent that the operator stores is doubled, and the same holds for the rotation angle: the **double rotation** and the **double dilatation** are the two faces of the single statement that the sandwich uses each non-central factor twice, and the central factors once or not at all.

**What the sandwich generates.** Combining the two readings, the map $H_{\tilde{Q}}$ is a dilatation composed with a Lorentz transformation, and as $\tilde{Q}$ runs over all invertible elements the pair $(r^{2},\tilde{\Lambda})$ runs over all positive reals and all of $\mathbb{B}^{\times}_1$. The image of the sandwich action on the material sector is therefore

$$
\{H_{\tilde{Q}}\}\cong\mathbb{R}_{>0}\times SO^{+}(1,3),
$$

the Lorentz group together with the dilatations — the **similitude** group, the Lorentz group extended by the scale — with no phase anywhere. Physically this is the statement that a general biquaternion operator is a Lorentz transformation together with a change of units, and that the unit of length is not the phase. No choice of $\tilde{Q}$ produces a phase in the sandwich, and no choice produces anything outside this group. The sandwich preserves the two Hermitian sectors and the rank of the matrix image, as the scalar factor $r^{2}$ cannot change either.

## The Special Case of Norm One: the Lorentz Group

Put $r=1$ and $\alpha=0$, so that $\tilde{Q}=\tilde{\Lambda}\in\mathbb{B}^{\times}_1\cong SL(2,\mathbb{C})$, the double cover of the proper orthochronous group $SO^{+}(1,3)$. This is the untwisted case, and it is the case the corpus treats as the Lorentz group.

**The operator.** A norm-one element is written in several equivalent ways.

| form | expression |
|---|---|
| component | $\tilde{\Lambda}=\sum_{\mu}a_{\mu}e_{\mu}$, $a_{\mu}\in\mathbb{C}$, $N(\tilde{\Lambda})=1$ |
| quaternionic | $\tilde{\Lambda}=q+ip$, $q,p\in\mathbb{H}$, $N(\tilde{\Lambda})=1$ |
| exponential | $\tilde{\Lambda}=e^{\mathbf{u}/2}e^{i\mathbf{v}/2}$, $\mathbf{u},\mathbf{v}$ real pure quaternions |
| matrix | $\Lambda_{\mathbb{C}}\in SL(2,\mathbb{C})$, $\det\Lambda_{\mathbb{C}}=1$ |
| boost | $e^{i e_1\phi/2}=\cosh\tfrac{\phi}{2}+ie_1\sinh\tfrac{\phi}{2}$ |
| rotation | $e^{e_3\theta/2}=\cos\tfrac{\theta}{2}+e_3\sin\tfrac{\theta}{2}$ |

The exponential form is the polar form with $r=1$, $\alpha=0$: the pure quaternion $\mathbf{u}$ carries the three rotation parameters and $i\mathbf{v}$ the three boosts, $3+3=6$ real dimensions, the dimension of the group. In the exponential form the half-angles are visible, $e^{\mathbf{u}/2}$ and $e^{i\mathbf{v}/2}$, and this is why the sandwich doubles them in the general case above and why this case is the untwisted one: with $\rho=1$ the modulus is $r=1$ and both the scale and the phase have disappeared. The rotation example also shows the double cover directly: $\theta\to\theta+2\pi$ sends $\tilde{\Lambda}\to-\tilde{\Lambda}$, the same element of the group with opposite sign, which is the effect seen in neutron interferometry.

**The module.** The action $\psi\mapsto\Phi(\tilde{\Lambda})\psi$ is the spinor representation proper. It is irreducible, because $\mathbb{B}$ is simple; it is faithful, because $\Phi(-e_0)=-I_2$, so the operator distinguishes $\tilde{\Lambda}$ from $-\tilde{\Lambda}$ and the representation does not descend to the quotient $\mathbb{B}^{\times}_1/\{\pm e_0\}$; and it is non-unitary, because every finite-dimensional representation of $SL(2,\mathbb{C})$ is complex-linear, so $\rho(ie_k)=i\rho(e_k)$ is Hermitian while skew-adjointness would force it to vanish, killing the boosts and the whole algebra. On the module the obstruction is the identity

$$
\tilde{\Lambda}^{*}\tilde{\Lambda}=\tilde{\Lambda}^{2}=\cosh\psi+i\sinh\psi\,\hat{\mathbf{u}}\neq e_0 ,
$$

which is the "sub-case $r=1$" of the double-dilatation statement. Physically it is the absence of an invariant probability on a finite-component object: a boost scales the two components of the spinor in opposite senses, one up and one down, and there is no finite-dimensional unitary representation of the group other than the trivial one. That is why the unitary representations are the infinite-dimensional fields.

**The two chiralities are the untwisted two-dimensional representations.** The conjugate module $\bar{S}$ carries the other handedness, and the two are inequivalent: with the two chiral Casimirs $C_{\pm}=\sum_k(N_k^{\pm})^2$ built from $N_k^{\pm}=\tfrac12(e_k\pm\mathsf{i}\,ie_k)$, one finds $C_+\mapsto0$, $C_-\mapsto-3I_2$ on $S$ and the reverse on $\bar{S}$, so $S=(\tfrac12,0)\ncong(0,\tfrac12)=\bar{S}$. Neither is a minimal left ideal, since both ideals carry $S$, and neither is obtained by right multiplication, since $S^{*}\cong S$; the handedness requires the real structure, the operation that also produces the antiparticle.

**The sandwich.** With $r=1$ the sandwich is the norm-one conjugation $\tilde R\mapsto\tilde{\Lambda}\tilde R\tilde{\Lambda}^{*}$, an isometry of the biquaternion norm, $N(H_{\tilde{\Lambda}}(\tilde R))=N(\tilde R)$. The scale is what the norm detects: the sandwich preserves the norm exactly when $r=1$, whatever the phase, and the norm-one case is the phase-free representative of the isometries. This is why the Lorentz group, and not the similitude group, is the group of the metric: the dilatation is present in the operator as soon as $r\neq1$. A general biquaternion operator therefore describes a Lorentz transformation up to a change of scale, and only the operators of scale one are the symmetries of the interval.

## Further Particular Cases

The general operator has four parameters, and every interesting case is obtained by switching one of them off. The table gives the sandwich and the module in each case, with the physical reading.

| case | condition | sandwich $H_{\tilde{Q}}$ | module twist $\chi$ |
|---|---|---|---|
| general unit | $\tilde{Q}=r e^{i\alpha}B\hat{q}$ | dilatation $r^{2}$ $\circ$ Lorentz | $\rho=r e^{i\alpha}$ |
| norm one | $r=1$, $\alpha=0$ | Lorentz transformation | trivial |
| central | $\tilde{Q}=r e^{i\alpha}$ | pure dilatation $r^{2}$, no rotation | $\rho$, no Lorentz part |
| real quaternion | $\tilde{Q}=r\hat{q}$, $N$ real $>0$ | dilated rotation of space | $r$ |
| pure boost | $\alpha=0$, $\hat{q}=1$ | boost of the doubled rapidity | $r$ |
| pure rotor | $\alpha=0$, $B=1$ | rotation of the doubled angle | $r$ |
| unitary | $\tilde{Q}=\lambda\hat{q}$, $\lvert\lambda\rvert=1$ | rotation, no dilatation | $e^{i\arg\lambda}$ |
| real norm, $N>0$ | $\alpha=0$ | no phase anywhere | $r$ |
| vanishing norm | $N(\tilde{Q})=0$ | not invertible; rank drops | undefined |

Two of the rows deserve a word. The **real quaternion** case is the one where the boost is absent and the operator is a similarity of space, a rotation composed with a dilatation, $\mathbb{R}_{>0}\times SO(3)$; it is the operator of a rigid motion with a change of units, and it is not a Lorentz transformation, since the time axis is untouched. And the **vanishing norm** case is the boundary of the whole construction: the polar representation does not exist, the operator is singular, and the sandwich drops the rank of its argument, in agreement with the zero-divisor criterion of *Biquaternion Norm and Invertibility*. The twisted-spinor description, like the polar description, is a description of the invertible elements.

## The Trace and the Two Actors

The norm-one row and the unitary row are the two the framework uses most, and what separates them is not the group each generates but the invariant each keeps. Both keep the interval, because both have scale one: the sandwich multiplies the biquaternion norm by $\lvert N(\tilde{Q})\rvert^{2} = r^{4}$, so it is an isometry exactly when $r = 1$, the central phase cancelling on the two sides. They differ in the trace.

**The unitary actor keeps the trace.** Let $\tilde{Q} = \lambda\hat{q}$ with $\lvert\lambda\rvert = 1$. Then $\Phi(\tilde{Q})$ is unitary and the sandwich fixes the unit, $\mathrm{H}_{\tilde{Q}}(e_0) = \tilde{Q}\tilde{Q}^{*} = e_0$. It is multiplicative, since $\Phi(\tilde{Q}\tilde{R}\tilde{S}) = \Phi(\tilde{Q})\Phi(\tilde{R})\Phi(\tilde{S})$ with the two outer factors regrouping, so it is an algebra automorphism, and it is the inner one $\tilde{R}\mapsto\tilde{Q}\tilde{R}\tilde{Q}^{-1}$ with $\tilde{Q}^{-1} = \tilde{Q}^{*}$. An inner automorphism preserves the trace, $\mathrm{Tr}(\mathrm{H}_{\tilde{Q}}(\tilde{R})) = \mathrm{Tr}(\tilde{R})$, so the operator carries every trace-one hyperplane into itself; on the informational sector it is the operator that permutes the states among themselves.

**The norm-one actor does not.** Let $\tilde{\Lambda} = B\hat{q}$ with a nontrivial boost factor. On the identity the sandwich returns the square of the element,

$$
\mathrm{H}_{\tilde{\Lambda}}(e_0) = \tilde{\Lambda}\tilde{\Lambda}^{*} = \tilde{\Lambda}^{2} = \cosh\psi + i\sinh\psi\,\hat{\mathbf{u}} , \qquad \mathrm{Tr}\left(\mathrm{H}_{\tilde{\Lambda}}(e_0)\right) = 2\cosh\psi ,
$$

which is $2$ only when the boost is absent, and on a Hermitian element $\tilde{H} = h_0e_0 + i\mathbf{h}$ it returns a boosted time,

$$
\mathrm{Tr}\left(\mathrm{H}_{\tilde{\Lambda}}(\tilde{H})\right) = 2\left(h_0\cosh\psi + \left(\hat{\mathbf{u}}\cdot\mathbf{h}\right)\sinh\psi\right) .
$$

The trace of the sandwich is therefore a time coordinate, and a boost cannot leave it alone: the trace-one hyperplane of the informational sector is carried off itself, which is the trace-side reading of the absence of an invariant probability recorded above.

**The polar word says which factor is responsible.** With $\tilde{\Lambda} = B\hat{q}$ the sandwich is

$$
\mathrm{H}_{\tilde{\Lambda}}(\tilde{H}) = B\left(\hat{q}\tilde{H}\hat{q}^{*}\right)B ,
$$

so the rotor acts by conjugation, an automorphism of the algebra, and preserves the trace; the boost factor stands on the two sides and is what changes it; and the central phase has already cancelled. Of the four factors of the polar word, therefore, exactly one moves the trace. The scale, counted twice, and the phase, cancelling, set the modulus $r^{2}$; the rotor reorients the element without touching its trace; and **the boost factor is the only factor of the polar word that leaves the trace-one slice.**

The two rows are then the two answers to the question of which group acts on which object, and the two conditions are nested rather than parallel:

| actor | condition | sandwich keeps | object |
|---|---|---|---|
| unitary | $\tilde{Q}\tilde{Q}^{*} = e_0$ | the interval and the trace; an automorphism | the trace-one slice of the informational sector, and the cone |
| norm-one rotor | $N(\tilde{Q}) = 1$ | the interval only; it moves the trace | the cone of the material sector |

The unitary condition implies the isometry, since a unitary element has $r = \lvert\lambda\rvert = 1$; the isometries that are not automorphisms are exactly the elements of scale one with a nontrivial boost factor, the norm-one row of the previous table being their phase-free representative. Their intersection is the rotor group $\mathrm{Sp}(1)$, the unitaries of norm one, and the rotor is therefore the case in which the sandwich keeps the interval, keeps the trace, and has no phase left to twist the module with.

## The Labels of the Twisted Representations

The twist is a representation-theoretic label, and it combines with the familiar ones. A character of the scaling group is

$$
\chi_{a,b}(z)=z^{a}\bar{z}^{b},
\qquad z=re^{i\theta},\quad a,b\in\mathbb{C},\quad a-b\in\mathbb{Z},
$$

the last condition being exactly what makes the character single-valued on $\mathbb{C}^{\times}$. The irreducible finite-dimensional modules of the group of units are then the twisted spinor representations

$$
(j,j')_{(a,b)}=V_j\boxtimes V_{j'}\otimes\chi_{a,b},
$$

with the labelling of the untwisted case and with one compatibility: the central element $-I$ acts on $(j,j')$ by $(-1)^{2j+2j'}$ and through the character by $(-1)^{a-b}$, so a twisted module exists exactly when

$$
a-b\equiv 2j+2j'\pmod 2 .
$$

The defining module of the group of units is the twist of the left-handed chirality by the square root of the determinant, $(\tfrac12,0)_{(1,0)}$: the scalar $z$ acts on a spinor by $z$, which is $\det^{1/2}$ since $\det(zI)=z^{2}$.

**Reality.** Complex conjugation exchanges the two factors and conjugates the character,

$$
\overline{(j,j')_{(a,b)}}=(j',j)_{(b,a)},
$$

so a twisted module is self-conjugate exactly when $j=j'$ and $b=a$; in that case the twist is the real pairing of the scale with itself, and the module is of real type, as $(\tfrac12,\tfrac12)_{(1,1)}$ is.

**Unitarity.** A twisted spinor is unitarizable only if the twist is unitary and the norm-one part is trivial. The twist is unitary exactly when the scale exponent is purely imaginary, $\mathrm{Re}(a+b)=0$, since $\lvert\chi_{a,b}(z)\rvert=r^{a+b}$; and the norm-one part admits no non-trivial finite-dimensional unitary representation. So the twisted spinor representations retain the non-unitarity of the untwisted ones, and the twist never repairs it: a general biquaternion operator cannot be made into a symmetry of a finite-dimensional probability.

## What the Algebra Carries

The algebra $\mathbb{B}$ is four-dimensional over $\mathbb{C}$, and its natural self-actions carry a short list of twisted representations.

**Left multiplication.** $\mathbb{B}\cong S\oplus S$ as a left module, so left multiplication carries two copies of the defining twisted module, $2\times(\tfrac12,0)_{\chi}$ with $\chi(\rho)=\rho$; the twist is the same on both copies, since the centre acts by the same scalar.

**Right multiplication.** $\mathbb{B}\cong S^{*}\oplus S^{*}$ with $S^{*}\cong S$, so right multiplication carries two copies of the **same** chirality, twisted the same way. Neither one-sided action produces the opposite handedness.

**Conjugation.** The sandwich is irreducible on the algebra and carries the twisted four-vector, $(\tfrac12,\tfrac12)$ scaled by $r^{2}$. This is the action on the material sector, and it is the operator that builds the four-vectors of the theory from the module. Combined with the previous paragraph, the algebra carries the twisted spinor and the twisted four-vector and nothing else.

**What the algebra does not carry.** The higher modules $(1,0)$, $(1,1)$, $(\tfrac32,0)$ are not modules over $\mathbb{B}$, twisted or not: the modules of $M_2(\mathbb{C})$ are the direct sums of copies of $S$, of even dimension, while $\operatorname{Sym}^{2}(S)$ has dimension $3$ and $\operatorname{Sym}^{3}(S)$ has dimension $4$ with a different action. The tower is generated by symmetric powers of the twisted spinor, $\operatorname{Sym}^{2j}(S)\otimes\operatorname{Sym}^{2j'}(\bar{S})$, but each member must be built from tensor powers of the spinor rather than found inside the algebra. This is the boundary of the biquaternion description of operators, and the twist does not move it: a field of higher spin has to be constructed, not discovered in the algebra.

## Summary

The polar representation writes a biquaternion as an object, $\tilde{Q}=r e^{i\alpha}B\hat{q}$; this article writes it as an operator, and the two descriptions are the same information on the same elements. Acting on the module $S=\mathbb{C}^2$ by left multiplication, its matrix image is $\Phi(\tilde{Q})=\rho\Phi(\tilde{\Lambda})$ with $\rho=\sqrt{N(\tilde{Q})}=re^{i\alpha}$ and $\tilde{\Lambda}=B\hat{q}$ of norm one, so the module is the spinor module of the Lorentz double cover **twisted** by the character $\chi(\rho)=\rho$. The twist does not enlarge the module — by Schur the module stays $\mathbb{C}^2$, irreducible — it changes the weight, and it is the record of the scale and the phase that the polar form carries. The correspondence is one-to-one: scale and phase become the twist, boost and rotor become the norm-one operator, and the order of the factors is preserved. Because it is the operator version of the polar word, the description exists exactly where the polar word does, on the complement of the light cone; the action on the module survives on the cone, but the twist and the modulus do not, and there is nothing to read.

Acting on the material sector by the Hermitian sandwich, $H_{\tilde{Q}}(\tilde R)=\tilde{Q}\tilde R\tilde{Q}^{*}$, the operator factors as $r^{2}\tilde{\Lambda}\tilde R\tilde{\Lambda}^{*}$. The scale is counted **twice**, once per side, giving $r^{2}$ on lengths and $r^{4}$ on the interval; the phase cancels, since it and its inverse appear on the two sides and are central, so the phase is invisible to the material sector. The norm-one part, a rotation by the doubled angle followed by a boost of the doubled rapidity, has its stored half-angles doubled by the sandwich: the boost rotor stores $\psi/2$ and produces the rapidity $\psi$, as the diagonal example $\mathrm{diag}(e^{\psi/2},e^{-\psi/2})\mapsto\mathrm{diag}(e^{\psi},e^{-\psi})$ shows exactly. The image of the sandwich is the Lorentz group together with the dilatations, the similitude group $\mathbb{R}_{>0}\times SO^{+}(1,3)$, with no phase anywhere. A general biquaternion operator is therefore a Lorentz transformation together with a change of units, and the unit of length is not the phase.

The norm-one case, $r=1$ and $\alpha=0$, is the Lorentz group, the untwisted case, and the phase-free isometry — the sandwich preserves the norm exactly when the scale is one — and it is where the spinor is the module, the double cover is visible as $-e_0\mapsto-I_2$ and as the sign change under a rotation by $2\pi$, and the two chiralities $(\tfrac12,0)$ and $(0,\tfrac12)$ are inequivalent, separated by the chiral Casimirs. The other particular cases are read off by switching off one parameter: a central operator gives a pure double dilatation, a real quaternion gives a dilated rotation of space, a pure boost gives the doubled rapidity, and a vanishing norm removes the operator entirely. The two rows of the case table that lie closest to each other, the norm-one row and the unitary row, are separated by the invariant each keeps rather than by the group each generates: the sandwich scales the biquaternion norm by $r^{4}$, so both are isometries of the interval, but only the unitary elements fix the unit and hence preserve the trace, and among the four factors of the polar word it is the boost factor alone that moves the trace-one slice.

The twisted labels are $(j,j')_{(a,b)}$, with the character $\chi_{a,b}(z)=z^{a}\bar{z}^{b}$, $a-b\in\mathbb{Z}$, and the parity compatibility $a-b\equiv 2j+2j'\pmod 2$. Conjugation sends $(j,j')_{(a,b)}$ to $(j',j)_{(b,a)}$, and unitarity requires a purely imaginary scale exponent and is then still destroyed by the norm-one part. The algebra carries the twisted spinor and the twisted four-vector and no higher module: the rest of the tower is generated by symmetric powers of the twisted spinor, and lives in the tensor category rather than in the algebra.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra |
| $\tilde{Q}=r e^{i\alpha}B\hat{q}$ | Polar form: scale, phase, boost, rotor |
| $N(\tilde{Q}) = \langle\tilde{Q},\tilde{Q}\rangle_{\natural}=\tilde{Q}\tilde{Q}^{\natural}=\det\Phi(\tilde{Q})$ | Biquaternion norm |
| $r$, $e^{i\alpha}$ | Scale and central phase, both central |
| $B$, $\hat{q}$ | Hermitian positive boost, unit real quaternion rotor |
| $\rho=\sqrt{N(\tilde{Q})}=re^{i\alpha}$ | Complex modulus; the twist parameter |
| $\tilde{\Lambda}=\tilde{Q}/\rho=B\hat{q}$ | Norm-one part; the Lorentz transformation |
| $\mathbb{B}^{\times}\cong GL(2,\mathbb{C})$ | Group of units; the general operator group |
| $\mathbb{B}^{\times}_1\cong SL(2,\mathbb{C})$ | Lorentz double cover; norm-one group |
| $S=\mathbb{C}^2$ | Module; the spinor module when untwisted |
| $S\otimes\chi$ | Twisted spinor module; the general module |
| $\chi(\rho)=\rho$ | Twist character of the defining module ($\det^{1/2}$) |
| $\chi_{a,b}(z)=z^{a}\bar{z}^{b}$, $a-b\in\mathbb{Z}$ | General character of the scaling group |
| $(j,j')_{(a,b)}$ | Twisted label; exists when $a-b\equiv 2j+2j'\pmod 2$ |
| $H_{\tilde{Q}}(\tilde R)=\tilde{Q}\tilde R\tilde{Q}^{*}$ | Hermitian sandwich, the operator on the material sector |
| $H_{\tilde{Q}}=r^{2}\tilde{\Lambda}\tilde R\tilde{\Lambda}^{*}$ | Factorization: dilatation times Lorentz |
| $\mathrm{H}_{\tilde{Q}}(e_0)=\tilde{Q}\tilde{Q}^{*}$ | Image of the unit: $e_0$ for a unitary, $\tilde{\Lambda}^{2}$ for a norm-one rotor |
| $\operatorname{Tr}\left(\mathrm{H}_{\tilde{Q}}(\tilde{R})\right)$ | Trace of the sandwich; preserved exactly for the unitary $\tilde{Q}$, and moved by the boost factor alone |
| $N(H_{\tilde{Q}}(\tilde R))=\lvert N(\tilde{Q})\rvert^{2}N(\tilde R) = \langle\tilde R,\tilde R\rangle_{\natural}=r^{4}N(\tilde R)$ | Interval dilated by the square of the scale |
| $\mathrm{diag}(e^{\psi/2},e^{-\psi/2})\mapsto\mathrm{diag}(e^{\psi},e^{-\psi})$ | The doubled rapidity on the boost axis |
| $\mathbb{R}_{>0}\times SO^{+}(1,3)$ | Image of the sandwich: dilatations and Lorentz |
| $\mathbb{M}_-$, $\mathbb{M}_+$ | Material sector (anti-Hermitian) and informational sector (Hermitian) |
| $C_{\pm}=\sum_k(N_k^{\pm})^2$ | Chiral Casimirs, $(0,-3)$ vs $(-3,0)$ |
| $\operatorname{Sym}^{2j}(S)\otimes\operatorname{Sym}^{2j'}(\bar{S})$ | Carrier of the higher twisted modules |
| $\langle\tilde{P},\tilde{Q}\rangle_{*}$ | the complex sesquilinear form, $\mathrm{Sc}(\tilde{P}\tilde{Q}^{*})$; on the diagonal $\langle\tilde{Q},\tilde{Q}\rangle_{*}=\sum_\mu\lvert Q_\mu\rvert^{2}$ |
| $\langle\tilde{P},\tilde{Q}\rangle$ | the complex bilinear form, the scalar part of the complex bilinear product, $\mathrm{Sc}(\tilde{P}\tilde{Q})$ |

## Further Reading

- Steven Weinberg, *The Quantum Theory of Fields*, Vol. 1 (Cambridge, 1995), for the Lorentz representations built from Weyl spinors, the non-unitarity of the finite-dimensional ones, and the reason the physical representations are infinite-dimensional.
- Wu-Ki Tung, *Group Theory in Physics* (World Scientific, 1985), for the $(j,j')$ labelling, the two $\mathrm{SU}(2)$ halves, and the reality classification.
- I. M. Gel'fand, R. A. Minlos, and Z. Ya. Shapiro, *Representations of the Rotation and Lorentz Groups and Their Applications* (Pergamon, 1963), for the finite- and infinite-dimensional theory.
- William Fulton and Joe Harris, *Representation Theory: A First Course* (Springer, 1991), for symmetric powers, highest weights, and the Clebsch–Gordan rule.
- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations* (Springer, 2015), for complexification, real forms, and the classification of unitary representations.
- Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time*, Vol. 1 (Cambridge, 1984), for the two-component spinor calculus, self-duality, and the chiral projectors.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for spinors as minimal left ideals and the Clifford origin of chirality.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the rotor picture of the Lorentz group and the spinor–four-vector correspondence.
