# __The Reflection and the Rotation in Biquaternionic Form__

## Introduction

The companion articles of the relativistic quantum series build the biquaternion Dirac algebra and use it: *Matrix Representations Conventions*, §*The Clifford Structure*, fixes the comparison between the biquaternions and the even Clifford algebra; *The Spinor Module in Biquaternionic Form and Its Lorentz Action* constructs the module on which the algebra acts; *Exercise: Chirality and the Weyl Spinors* develops the chiral projectors. This article is about a structure that all three use but none names: the **grading of the Dirac algebra by reflection parity**, and the identification of one element, the timelike frame cell $iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}$, as the hinge on which the whole structure turns. Here $L_{a}R_{b}$ is the cell that multiplies on the left by $a$ and on the right by $b$, $L_{a}R_{b}\psi=a\psi b$, and $iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}$ is the generator cell of the coordinate $x_\mu$, with $\nu(t)=x$ and $\nu(k)=y$.

The subject is one observation, made precise. The biquaternion algebra $\mathbb{B}$ is isomorphic to the **even** part of the Clifford algebra $\mathrm{Cl}_{1,3}$. Its rotors, the elements of unit norm, act on four-vectors by conjugation, and the same rotors are the points of $SL(2,\mathbb{C})$, the double cover of the restricted Lorentz group. The generators $iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}$, by contrast, are **odd**: none of them lies in the even part, whose cells are those whose right multiplier lies in $\mathrm{span}\{e_t,\vec e_z\}$, and none of them is a rotor. They act on spinors and they **exchange the two chiralities**. The odd/even split of the Clifford algebra is therefore not a bookkeeping device. It is the split between the transformations that *turn* and the transformations that *reflect*, and chirality — the property that separates the two Weyl spinors — is precisely what the odd part changes and the even part preserves.

The article is organized as follows. §*One Algebra, Read Twice* reconciles the two ways in which a single element of the algebra is used, as an object and as an operator. §*The Grading by Reflection Count* establishes the grading, by the classical theorem that every orthogonal transformation is a product of reflections. §*The Frame Cell and the Hermitian Sector* introduces the frame cell $iR_{\vec e_x}^{\mathrm{axf}}$ and shows that the Clifford metric is the biquaternion norm of the Hermitian sector, which is what makes the mostly-minus convention of the series a statement about the objects rather than a choice. §*Conjugation by $iR_{\vec e_x}^{\mathrm{axf}}$ Is the Bar* shows that conjugation by the frame cell is the conjugation of the coefficients, so that the frame, the sector swap and the reflection are one operator. §*The Spaces of Rotations and of Reflections* and §*How Many Reflections?* describe the two spaces and answer the question of how many reflections a given Lorentz transformation needs. §*Why Chirality Needs a Reflection* draws the consequence for chirality, and §*Why the Pauli Algebra Cannot Carry Chirality* shows that no chirality element exists there. A closing §*The Legacy Gamma Formulation* translates the results into the matrix notation of the literature, and it is the only section of the article that uses it; every other statement is written in cells.

The conventions are those of the series: the biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_t = 1, \vec e_x, \vec e_y, \vec e_z$, $\vec e_\mu^2 = -e_t$, $\vec e_x \vec e_y = \vec e_z$; the scalar imaginary $i$, with $i^2=-1$; the sectors $\mathbb{M}_-$, $\mathbb{M}_+$, $\mathbb{H}_{\mathbb{B}}$; the Clifford metric $g = \mathrm{diag}(+1,-1,-1,-1)$ of the generators; and the dictionary of *Matrix Representations Conventions*, §*The Clifford Structure*, which is the $\mathbb{R}$-linear comparison with the even subalgebra.

As the series writes it, the comparison is given by its values and never by a symbol,
$$
e_t\mapsto L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}},\qquad \vec e_k\mapsto L_{\vec e_k}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}},\qquad i\mapsto L_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}},
$$
so that "the image of $\tilde Q$" means the cell read off from these values and multiplicativity, and the pseudoscalar $\omega=-L_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$ is the image of $-i$. The comparison is $\mathbb{R}$-linear but not $\mathbb{C}$-linear: a factor $i$ multiplying a biquaternion becomes a right multiplication by $\vec e_z$ in the cells, not a multiplication of the cell by the scalar $i$.

Two different elements therefore carry the name $i$. The biquaternion's own imaginary is itself a cell, the image $L_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$ of $i$; the scalar imaginary of the complexified algebra multiplies a cell from outside and has no preimage. Both square to $-1$; the frame notation of the closing section uses the second. No convention is changed here.

## One Algebra, Read Twice

A single element of a matrix algebra is at once a **point** and an **operator**. This is not a peculiarity of the biquaternions; it is what a matrix algebra is. The quaternions show it most plainly: a unit quaternion is a point of the three-sphere, and it is also the rotation that acts on vectors by conjugation. The same quaternion, read two ways.

The biquaternion algebra inherits this doubling, and the series uses it constantly:

- A **Lorentz rotor** $\tilde U^{\mathrm{lor}}$ with $\langle\tilde U^{\mathrm{lor}}\rangle_{\natural} = 1$ is a point of $SL(2,\mathbb{C})$, the double cover of the restricted Lorentz group. It is also an operator: it acts on four-vectors by the rotor conjugation, and on spinors by left multiplication.
- A **generator** $iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}$ is a point of the odd part — a four-vector, one of the four legs of spacetime — and it is also an operator on the spinor module. The four are the cells $iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}$, $iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$, $iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$, $iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$.

For the rotors the doubling is familiar, since the same element is both the transformation and the operator that applies it. For the generators it is not, and the reason is the grading. The even elements act on the spinor module *preserving* its two chiral halves, because they commute with the chirality operator; the odd elements act *exchanging* them, because they anticommute with it. So an even element and an odd element, both points of the same algebra and both operators on the same module, do qualitatively different things. The remainder of this article is the elaboration of that sentence.

The two actions on a four-vector are worth naming explicitly, since both are used below. For $\tilde U^{\mathrm{lor}}$ even with $\langle\tilde U^{\mathrm{lor}}\rangle_{\natural} = 1$, the rotor conjugation
$$
\tilde{Q}_2 = \tilde U^{\mathrm{lor}}\,\tilde{Q}\,\tilde U^{\mathrm{lor}}{}^{*}
$$
implements the Lorentz transformation of the material vector $\tilde{Q}\in\mathbb{M}_-$. For a pure boost the rotor is Hermitian, $\tilde U_{\mathrm b}^{*} = \tilde U_{\mathrm b}$, and the action reduces to $\tilde{Q}_2=\tilde U_{\mathrm b}\tilde{Q}\tilde U_{\mathrm b}$; for a general element of $SL(2,\mathbb{C})$ the general form is required. Both facts are those of *The Lorentz Transformation as a Biquaternionic Rotation*. In the cells the same action is the product of four factors, the framed trivector of $\tilde Q$ standing between the image of $\bar{\tilde U}^{\,\mathrm{lor}}$ and the image of $\tilde U^{\mathrm{lor}}{}^{*}$,
$$
\bigl(\text{image of }\bar{\tilde U}^{\,\mathrm{lor}}\bigr)\;iR_{\vec e_x}^{\mathrm{axf}}\;\bigl(\text{image of }\tilde Q\bigr)\;\bigl(\text{image of }\tilde U^{\mathrm{lor}}{}^{*}\bigr)
= iR_{\vec e_x}^{\mathrm{axf}}\;\bigl(\text{image of }\tilde U^{\mathrm{lor}}\,\tilde Q\,\tilde U^{\mathrm{lor}}{}^{*}\bigr).
$$
The framed trivector of $\tilde Q$ is, for $\tilde Q\in\mathbb{M}_-$, the dual of the material vector of the section *The Frame Cell and the Hermitian Sector*, and the right-hand side is again one, because $\tilde U^{\mathrm{lor}}\tilde Q\tilde U^{\mathrm{lor}}{}^{*}$ lies in $\mathbb{M}_-$ whenever $\tilde Q$ does. The bar sits on the left factor because the frame cell passes the image of the rotor: $iR_{\vec e_x}^{\mathrm{axf}}$ times the image of $\tilde U^{\mathrm{lor}}$ is the image of $\bar{\tilde U}^{\,\mathrm{lor}}$ times $iR_{\vec e_x}^{\mathrm{axf}}$, which is the frame conjugation of the section *Conjugation by $iR_{\vec e_x}^{\mathrm{axf}}$ Is the Bar*. The bar is not optional. Sandwiching on the left by the image of $\tilde U^{\mathrm{lor}}$ instead would give the frame cell times the image of $\bar{\tilde U}^{\,\mathrm{lor}}\tilde Q\tilde U^{\mathrm{lor}}{}^{*}$, and $\bar{\tilde U}^{\,\mathrm{lor}}\tilde Q\tilde U^{\mathrm{lor}}{}^{*}$ leaves $\mathbb{M}_-$ as soon as the boost is not aligned with the vector: the product would carry a vector part beside its trivector part, and the frame cell would be applied to something that is not a vector at all.

The odd elements are not images of biquaternions at all, so no biquaternion represents them. They lie in the odd part of $\mathrm{Cl}_{1,3}$ and act on vectors by the two-sided map of the Pin group,
$$
\rho(u): x \mapsto -\,\epsilon(u)\,u\,x\,u, \qquad u\ \text{odd},\ u^2 = \epsilon(u)\,I_4,\ \epsilon(u)=\pm1 ,
$$
which is the signed inner conjugation. A unit vector is its own inverse up to sign: $u^{2}=\epsilon(u)I_4$ makes the inverse $\epsilon(u)u$, so the formula uses only the Clifford product and the sign of the normal; no operator inverse is needed. The minus sign is what puts the hyperplane in the right place: $x\mapsto uxu^{-1}$ negates the vectors orthogonal to $u$ and fixes $u$ itself, and the reflection is its negative. The sign $\epsilon(u)$ then records whether the normal is timelike, $\epsilon=+1$, or spacelike, $\epsilon=-1$.

## The Grading by Reflection Count

The classical theorem of Cartan and Dieudonné states that every orthogonal transformation of a non-degenerate space is a product of reflections in hyperplanes. For a space of dimension $n$ at most $n$ reflections are needed, and the determinant of the transformation is $(-1)^{k}$, where $k$ is the number of reflections in any factorisation. Two remarks follow, and together they are the content of this section.

First, the **determinant classifies the transformation by the parity of the reflection count**. An even number of reflections gives a proper transformation, an odd number a reflection, or more generally an orientation-reversing transformation. In four dimensions with Lorentzian signature a single reflection is parity, time reversal, or an axis flip, and two reflections give a proper transformation whose time orientation depends on the normals: it is orthochronous when both normals are timelike or both spacelike, and it reverses time when one is timelike and the other spacelike, as $\mathrm{diag}(-1,-1,+1,+1)$ does for the normals $e_t$ and $\vec e_x$.

Second, and this is the point, the parity of the reflection count **is the grading of the Clifford algebra**:
$$
\boxed{\;\mathrm{Cl}_{1,3} = \mathrm{Cl}_{1,3}^{+} \oplus \mathrm{Cl}_{1,3}^{-}\;}.
$$
The even part is spanned by the identity, the six bivectors and the pseudoscalar; the odd part by the four vectors and the four trivectors. An even element is a product of an even number of vectors — that is, of an even number of reflections — and an odd element of an odd number. In the cells the split is carried by the right multiplier: the even part is the span of the cells whose right multiplier lies in $\mathrm{span}\{e_t,\vec e_z\}$, the odd part the span of those whose right multiplier lies in $\mathrm{span}\{\vec e_x,\vec e_y\}$. The biquaternion algebra is the even part,
$$
\mathbb{B} \cong \mathrm{Cl}_{1,3}^{+}(\mathbb{R}),
$$
as *Matrix Representations Conventions*, §*The Clifford Structure*, establishes, and the rotations therefore sit inside $\mathbb{B}$ while the reflections do not.

In the explicit representation the correspondence is exact: every even unit element acts on the four-vectors with determinant $+1$, and every odd unit element, whether a generator, a unit vector or a trivector, with determinant $-1$. It is an identity, not a counting resemblance:

| element | reflection count | determinant of the vector action | in $\mathbb{B}$? |
|---|---|---|---|
| even unit element $\Lambda$ (rotor) | even ($0$, $2$ or $4$) | $+1$ | yes |
| odd unit element $u$ (a generator $iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}$ or a trivector) | odd | $-1$ | no |

The geometric content of the even part is also known: the Lie algebra of the rotation group is generated by the bivectors, and the bivectors are precisely the products of two reflections. So the two halves of the Clifford algebra correspond to the two classes of orthogonal transformations, and the correspondence is an identity.

## The Frame Cell and the Hermitian Sector

The odd part is reached from the even part by multiplying by the time generator, and the time generator is the frame $iR_{\vec e_x}^{\mathrm{axf}}$. Every vector is
$$
x_\mu iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}} = i\bigl(x_tL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}+x_xL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}+x_yL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}+x_zL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\bigr),
$$
and the same vector is the frame cell applied to the image of an element of $\mathbb{M}_+$,
$$
w = x_t e_t + i x_x\vec e_x + i x_y\vec e_y + i x_z\vec e_z , \qquad
iR_{\vec e_x}^{\mathrm{axf}}\times(\text{image of }w) = x_\mu iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}} .
$$
Every trivector is $iR_{\vec e_x}^{\mathrm{axf}}$ times the image of an element of $\mathbb{M}_-$, up to a sign that depends on the orientation chosen for each trivector, so the table below names the trivector and not its sign. The correspondence is:

| generator cell | biquaternion direction | sector |
|---|---|---|
| $iR_{\vec e_x}^{\mathrm{axf}} = iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}$ | $e_t$ | $\mathbb{M}_+$ |
| $iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$, $iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$, $iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$ | $i\vec e_x$, $i\vec e_y$, $i\vec e_z$ | $\mathbb{M}_+$ |
| the four trivectors | $ie_t$, $\vec e_x$, $\vec e_y$, $\vec e_z$ | $\mathbb{M}_-$ |

The generators therefore *are* the Hermitian-sector basis, pushed through $iR_{\vec e_x}^{\mathrm{axf}}$: the scalar direction $e_t$ becomes the time generator, and the three imaginary-quaternion directions $i\vec e_k$ become the three spatial generators. Read backwards, the same frame carries the even algebra to the odd part. The image of $\mathbb{M}_+$ is
$$
\mathrm{span}\{L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}},\ L_{\vec e_x}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}},\ L_{\vec e_y}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}},\ L_{\vec e_z}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}\},
$$
the identity together with the **timelike bivectors**. Since the timelike bivectors generate the boosts, this says that the Hermitian sector is the boost sector — exactly the statement of *The Lorentz Transformation as a Biquaternionic Rotation*, that the pure boosts are the Hermitian elements of $SL(2,\mathbb{C})$. The real-quaternion sector plays the dual role for the other family: its image is
$$
\mathrm{span}\{L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}},\ L_{\vec e_x}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}},\ L_{\vec e_y}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}},\ L_{\vec e_z}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}\},
$$
the identity together with the spacelike bivectors, which generate the spatial rotations.

The decisive consequence concerns the **metric**. The biquaternion norm $\langle\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural} = \sum_\mu Q_\mu^2$ — the coefficients $Q_\mu$ are complex, so a coefficient $i$ contributes $i^2=-1$ — evaluated on the two sector bases gives
$$
\langle\tilde Q\rangle_{\natural}\ \text{on}\ (e_t, i\vec e_x, i\vec e_y, i\vec e_z) = \mathrm{diag}(+1,-1,-1,-1) = g,
$$
$$
\langle\tilde Q\rangle_{\natural}\ \text{on}\ (ie_t, \vec e_x, \vec e_y, \vec e_z) = \mathrm{diag}(-1,+1,+1,+1) = \eta = -g .
$$
The minus signs of $g$ are those of $i^2$ on the three spatial directions, and nothing else. The Clifford metric of the generators is therefore not an independent convention laid on top of the algebra: **it is the biquaternion norm of the Hermitian sector**, and the $ict'$ metric of the material sector is its negative, the biquaternion norm of $\mathbb{M}_-$. This closes the loop of the series' metric conventions: the material coordinates carry $\eta = \mathrm{diag}(-1,+1,+1,+1)$, and the generators, which are Hermitian objects, carry $g = \mathrm{diag}(+1,-1,-1,-1)$. The two differ by the sign that distinguishes the two sectors, and neither could consistently be anything else.

The same fact appears in the vector square. For $w$ as above,
$$
\left(x_\mu iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}\right)^2 = \langle w\rangle_{\natural}\,L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}} = \left(x_t^2 - x_x^2 - x_y^2 - x_z^2\right)L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}} ,
$$
with no relative sign between the Clifford square and the biquaternion norm. The absence of that sign is the signature $g$ showing through.

## Conjugation by $iR_{\vec e_x}^{\mathrm{axf}}$ Is the Bar

The frame cell $iR_{\vec e_x}^{\mathrm{axf}}$ is not merely a bookkeeping element. It has a definite action on the algebra, and it is the action that defines the split $\mathbb{B}=\mathbb{H}_{\mathbb{B}}\oplus i\mathbb{H}_{\mathbb{B}}$.

For every $\tilde{Q}\in\mathbb{B}$,
$$
\boxed{\;iR_{\vec e_x}^{\mathrm{axf}}\times\bigl(\text{image of }\tilde{Q}\bigr)\times iR_{\vec e_x}^{\mathrm{axf}} = \text{image of }\bar{\tilde{Q}}\;}
$$
where $\bar{\tilde Q}$ is the conjugation of the coefficients, $i\mapsto -i$, with the units $e_t,\vec e_x,\vec e_y,\vec e_z$ fixed. Since that map is exactly the one that fixes $\mathbb{H}_{\mathbb{B}}$ and negates $i\mathbb{H}_{\mathbb{B}}$, the identity says that **conjugation by $iR_{\vec e_x}^{\mathrm{axf}}$ is the bar**: it is the spacetime-side avatar of the split $\mathbb{B}=\mathbb{H}_{\mathbb{B}}\oplus i\mathbb{H}_{\mathbb{B}}$, the rotation sector and its imaginary multiple. It preserves each of $\mathbb{M}_{\pm}$, because it commutes with the Hermitian conjugation whose eigenspaces they are; the sector exchange is multiplication by $i$, not a conjugation.

Among the four generators, $iR_{\vec e_x}^{\mathrm{axf}}$ is unique in being the bar itself. All four conjugations reverse the imaginary cell, $u\,L_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}\,u^{-1}=-L_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$ for $u$ any of the four generators, so all four carry the scalar imaginary $i$ to $-i$, and as maps of the biquaternions they are conjugate-linear rather than $\mathbb{C}$-linear; only the time one leaves the quaternion units alone.

Conjugation by $iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$ is the bar composed with a sign change of two units: it fixes $\vec e_k$ and negates the two units $\vec e_j$ with $j\neq k$. The bar then flips the imaginary multiples the other way round, so $i\vec e_t$ and $i\vec e_k$ are negated while $i\vec e_j$ is fixed for the same two $j$. The spatial generators reflect the quaternion units; the time one conjugates them without a reflection.

The frame completes the Clifford interpretation of the conjugations of $\mathbb{B}$, and the three maps fit in one display. Reversal $\mathrm{rev}$, the anti-automorphism that reverses the order of the factors in a product, acts on the biquaternions as **quaternion conjugation**; the frame acts as the bar; and the composite is the Hermitian conjugation:
$$
\text{image of }\tilde{Q}^{\natural}=\mathrm{rev}\bigl(\text{image of }\tilde{Q}\bigr),
\qquad
\text{image of }\bar{\tilde Q}=iR_{\vec e_x}^{\mathrm{axf}}\times\bigl(\text{image of }\tilde{Q}\bigr)\times iR_{\vec e_x}^{\mathrm{axf}},
$$
$$
\boxed{\;\text{image of }\tilde{Q}^{*}=iR_{\vec e_x}^{\mathrm{axf}}\times\mathrm{rev}\bigl(\text{image of }\tilde{Q}\bigr)\times iR_{\vec e_x}^{\mathrm{axf}}\;}
$$
The three elementary maps of the algebra therefore have separate Clifford interpretations, and the Hermitian conjugation $*$ is the bar composed with $\natural$: the algebra's own identity, not an accident of the frame.

There is a consequence worth recording, because it bears on the mass term. The algebra's real structure is the anti-Hermitian conjugation $\flat = -{}^{*}$, and the display above shows that $iR_{\vec e_x}^{\mathrm{axf}}$ is *inside* it: the frame, with its bar and its reflection properties, is one of the two ingredients of $\flat$. A formulation of the mass built on $\flat$ therefore carries the frame, but in the guise of a reality condition rather than of a generator; the linear and chirality-off-diagonal mass term of *The Dirac Equation in Biquaternionic Form* displays it openly instead. This is an observation about how the frame is packaged, not a derivation; it is stated here because it is the reason the frame is easy to overlook.

## The Spaces of Rotations and of Reflections

With the grading in hand, the two spaces can be described, and they are not of the same kind.

**The rotations.** The rotors are the unit-norm biquaternions,
$$
SL(2,\mathbb{C}) = \{\tilde U^{\mathrm{lor}}\in\mathbb{B} : \langle\tilde U^{\mathrm{lor}}\rangle_{\natural} = 1\},
$$
a group of real dimension $6$, the double cover of $SO^+(1,3)$. The sign of the norm is the time orientation: an even unit element with $\langle\tilde U\rangle_{\natural}=+1$ is orthochronous, and one with $\langle\tilde U\rangle_{\natural}=-1$ reverses time, which is why the group defined here is the restricted one. Its Lie algebra is the span of the six bivectors, the images of the six directions $\vec e_k$ and $i\vec e_k$, $k=1,2,3$. This is the space in which the rotors of the relativity articles live and act: on four-vectors in *Relativistic Mechanics in Biquaternionic Form* and *Exercise: Boosting a Four-Velocity and Rapidity Composition*, on spinors in *The Spinor Module in Biquaternionic Form and Its Lorentz Action*, on states in *Quantum Physics in Biquaternionic Form*, and in the composition of rotations of *Exercise: The Thomas Precession*.

Two subfamilies are worth separating, because the series uses them differently:

| subfamily | condition | biquaternion form | character |
|---|---|---|---|
| spatial rotations | $\tilde u_{\mathrm r}$ real quaternion | $\cos\frac{\theta}{2} + \sin\frac{\theta}{2}\vec u_{jk}$ | group $SU(2)$ |
| pure boosts | $\tilde U_{\mathrm b}$ Hermitian, $\tilde U_{\mathrm b}^{*} = \tilde U_{\mathrm b}$ | $\cosh\frac{\psi}{2} + i\sinh\frac{\psi}{2}\vec u$ | symmetric submanifold, not a group |

The boosts do not close under multiplication — the product of two non-collinear boosts is a boost plus a Thomas–Wigner rotation — so they form a submanifold of $SL(2,\mathbb{C})$ rather than a subgroup. The two families are exponentials of the two sector algebras: the boosts of elements of $\mathbb{M}_+$, namely the timelike bivectors $i\vec u$, and the spatial rotations of elements of $\mathbb{H}_{\mathbb{B}}$, namely the spacelike bivectors $\vec u_{jk}$.

**The reflections.** A reflection is an odd element of unit norm, and its data is its **normal**, a unit vector $u$. Writing the vectors as $iR_{\vec e_x}^{\mathrm{axf}}$ times the image of $w$ with $w\in\mathbb{M}_+$, the unit vectors are
$$
u = iR_{\vec e_x}^{\mathrm{axf}}\times(\text{image of }w), \qquad w\in\mathbb{M}_+, \quad \langle w\rangle_{\natural} = \pm 1 ,
$$
the timelike normals for $\langle w\rangle_{\natural} = +1$ and the spacelike ones for $\langle w\rangle_{\natural} = -1$. The canonical reflection is the time generator itself, $iR_{\vec e_x}^{\mathrm{axf}}=iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}$: its normal is the identity of the cell algebra, $L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$, which is the image of $e_t$ and a timelike unit vector.

The reflections do **not** form a group, and this is the sharp difference from the rotations. Multiplying two reflections gives an even element — a proper transformation — so the set is not closed under multiplication. The reflections form two cosets of the rotation group, one of timelike normals and one of spacelike normals, and a product of one of each leaves $SL(2,\mathbb{C})$ for the component that reverses time. Their dimension is $3$, the dimension of the unit quadric, against the $6$ of the rotations. The two together form the Pin group,
$$
\mathrm{Pin}(1,3) = \mathrm{Spin}(1,3) \cdot \{\text{unit vectors}\},
$$
whose even part is $\mathrm{Spin}(1,3) = SL(2,\mathbb{C})$ and whose algebra-level image is $\mathrm{Cl}_{1,3} = \mathrm{Cl}_{1,3}^{+}\oplus\mathrm{Cl}_{1,3}^{-}$. The relation between the two spaces is generation: the rotations are the products of an even number of reflections, and the bivectors that generate the Lorentz algebra are the products of two.

The reflections account for the four components of the full Lorentz group, and the timelike and the trivector normals give the two classical ones. The Pin action of the frame cell, whose normal is timelike, is time reversal,
$$
\rho(iR_{\vec e_x}^{\mathrm{axf}}) : x \mapsto -\,iR_{\vec e_x}^{\mathrm{axf}}\,x\,iR_{\vec e_x}^{\mathrm{axf}} = \mathrm{diag}(-1,+1,+1,+1).
$$
Parity is not that map but the Pin action of the trivector in the direction $ie_t$, the product of the three spatial generators,
$$
u = iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\,iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\,iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}, \qquad u^2=I_4, \qquad \rho(u) : x \mapsto -\,u\,x\,u = \mathrm{diag}(+1,-1,-1,-1).
$$
Both are reflections, with determinant $-1$; the identity component is the even part, and the discrete symmetries are the reflections.

**The anti-linear case.** The rule just stated — even elements act with determinant $+1$, odd elements with $-1$ — holds for the **linear** action of the Pin group. The discrete operations of the Dirac field are not all linear: $C$ and $T$ are **anti-linear**, and each carries an internal factor from the Clifford algebra. *The CPT Theorem in Biquaternionic Form* fixes the three,
$$
\eta_C=-L_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\qquad \eta_P=iR_{\vec e_x}^{\mathrm{axf}},\qquad \eta_T=-L_{\vec e_y}^{\mathrm{axf}} ,
$$
acting as $C[\psi]=\eta_C\psi^{*}$, $P[\psi]=\eta_P\psi(-\vec x)$ and $T[\psi]=\eta_T\psi^{*}(-t')$, with $\psi^{*}$ the Hermitian conjugate. The internal factor does not decide the determinant by itself:

| operation | internal factor | its grade | coordinates reversed | determinant | induced map |
|---|---|---|---|---|---|
| $P$ | $\eta_P=iR_{\vec e_x}^{\mathrm{axf}}$ | odd | $\vec x$ | $-1$ | reflection |
| $T$ | $\eta_T=-L_{\vec e_y}^{\mathrm{axf}}$ | even | $t'$ | $-1$ | reflection |
| $C$ | $\eta_C=-L_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$ | odd | none | $+1$ | proper |

$P$ and $T$ each reverse one coordinate and are reflections; $C$ reverses none and is proper. What the grade decides is not the determinant but the **chirality**, since that is decided by anticommutation with $-iR_{\vec e_z}^{\mathrm{axf}}$: the odd factors $\eta_C$ and $\eta_P$ anticommute with it, so $C$ and $P$ exchange the chiral halves, while the even factor $\eta_T$ commutes, so $T$ preserves them. The composite $CPT$ carries an even factor and preserves chirality, which is the chirality statement of the CPT article.

A single rule reproduces the determinant column: the grade contributes $(-1)^{k}$, with $k$ the grade of the internal factor, and the anti-linearity another $-1$,
$$
\det = (-1)^{k}\,(-1)^{\text{anti}} .
$$
It is a bookkeeping statement of an inversion, not a derivation. Its content is negative and worth stating plainly: for a **linear** map the grade is the reflection count, and for an **anti-linear** one it is not — the two columns are offset by one, and the even factor $\eta_T$ is the reflection while the odd factor $\eta_C$ is not.

## How Many Reflections?

The classical theorem gives an upper bound of four reflections in four dimensions. The sharper question — given a rotation, how many reflections does it take — has a clean answer, and it separates the simple Lorentz transformations from the generic ones.

A product of two reflections is an element $\tilde U^{\mathrm{lor}} = uv$ with $u$ and $v$ unit vectors. The criterion is algebraic. The product $u\tilde U^{\mathrm{lor}}$ has a grade-$1$ and a grade-$3$ part, and the grade-$3$ part is *linear* in $u$. So the condition that $u\tilde U^{\mathrm{lor}}$ be a pure vector — that is, that $\tilde U^{\mathrm{lor}}$ be $u$ times a vector — is a system of four linear equations in the four components of $u$, with a $4\times4$ matrix $M$ built from the bivector part of $\tilde U^{\mathrm{lor}}$:
$$
\tilde U^{\mathrm{lor}} = uv \ \text{for unit vectors}\ u,v \quad\Longleftrightarrow\quad Mu = 0 \ \text{for some}\ u\neq 0 \quad\Longleftrightarrow\quad \det M = 0 .
$$
Geometrically the criterion is that **$\tilde U^{\mathrm{lor}}$ fixes a two-dimensional subspace pointwise**, since a product of two reflections is the identity on the plane orthogonal to the span of $u$ and $v$. In the cell algebra the same determinant vanishes exactly when the bivector part of $\tilde U^{\mathrm{lor}}$ is simple, $B\wedge B=0$, since a simple bivector is a product $u\wedge v$ of two vectors and the kernel of $M$ is the plane they span; a plane in Lorentzian four-space always contains a non-null vector, so a nonzero solution can be rescaled to a unit normal. The three forms of the criterion agree: the determinant vanished exactly when the fixed subspace had dimension $2$.

| transformation | $\lvert\det M\rvert$ | fixed subspace | reflections needed |
|---|---|---|---|
| pure boost | $0$ | dimension $2$ | $2$ |
| pure spatial rotation | $0$ | dimension $2$ | $2$ |
| boost along $\vec e_x$ with a rotation in the $xy$ plane | $0$ | dimension $2$ | $2$ |
| boost along $\vec e_x$ with a rotation about $\vec e_x$ | $\neq 0$ | dimension $0$ | $4$ |

The rule the table obeys is geometric: the transformation is simple exactly when the **boost plane and the rotation plane share a direction**. A pure boost or a pure rotation carries only one plane, so the condition is empty; a boost with a rotation in the plane of the boost shares the boost direction; a boost with a rotation about the boost axis shares nothing.

The factorisations are explicit. The image of a boost is the frame cell times a unit vector,
$$
\text{image of }\tilde U_{\mathrm b} = iR_{\vec e_x}^{\mathrm{axf}}\,v ,
$$
where $v$ is the grade-one unit vector whose coordinates in the generator basis are
$$
\Bigl(\cosh\frac{\psi}{2},\ \sinh\frac{\psi}{2}u_x,\ \sinh\frac{\psi}{2}u_y,\ \sinh\frac{\psi}{2}u_z\Bigr),
$$
the time axis boosted by **half** the rapidity; the boost is the reflection in the resting time axis composed with the reflection in the moving one, and the half is what makes the two rapidities add to $\psi$.

A spatial rotation in the plane spanned by $iL_{\vec e_j}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$ and $iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$ is $iL_{\vec e_j}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\,v$ with
$$
v = -\cos\frac{\theta}{2}\,iL_{\vec e_j}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}} + \sin\frac{\theta}{2}\,iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}} , \qquad v^2 = -I_4 ,
$$
so that
$$
iL_{\vec e_j}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\,v = \cos\frac{\theta}{2}\,I_4 + \sin\frac{\theta}{2}\,iL_{\vec e_j}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\,iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}} .
$$
For the plane $(x,y)$ the right-hand side is the image of $\cos\frac{\theta}{2}e_t+\sin\frac{\theta}{2}\vec e_z$, the rotation about $\vec e_z$, and the other coordinate planes follow by relabelling. A generic Lorentz transformation fixes no plane at all, so by Cartan–Dieudonné it requires four reflections, the maximum.

So the answer to the question is: **pure boosts and pure spatial rotations are products of two reflections, and so is a boost with a rotation in the plane of the boost; a generic Lorentz transformation is not, and needs four.** The two-reflection class is a proper submanifold of $SL(2,\mathbb{C})$, cut out by the single condition $\det M=0$. The product of two non-collinear boosts stays inside it — the Thomas–Wigner rotation of a composed boost lies in the plane of the two boosts — so what leaves the class is a boost combined with a rotation about the boost axis, that is, a boost and a rotation in orthogonal planes.

In these factorisations $u$ and $v$ are unit vectors in the Clifford sense, $u^2=\pm I_4$; the three spatial generators, the images of $i\vec e_k$, have $\langle\cdot\rangle_{\natural}=-1$ and are not rotors, the rotors being their exponentials.

## Why Chirality Needs a Reflection

The chirality operator of the series is
$$
-iR_{\vec e_z}^{\mathrm{axf}} = i\,\omega , \qquad \omega = iR_{\vec e_x}^{\mathrm{axf}}\,iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\,iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\,iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}} ,
$$
where the four scalar factors $i$ of $\omega$ multiply to $i^4=1$, so that $\omega$ is a pure product of cells. That product is the pseudoscalar,
$$
\omega = -L_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}, \qquad \omega^2 = -I_4, \qquad (-iR_{\vec e_z}^{\mathrm{axf}})^2 = I_4 .
$$
Its projectors are the two idempotents
$$
P_{L,R} = \tfrac12\bigl(I_4 \pm iR_{\vec e_z}^{\mathrm{axf}}\bigr),
$$
of rank $2$ each. The sign is the one of the series, for which $P_L$ carries the left-handed half. The relation to the odd part is the anticommutation
$$
\bigl\{\,iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}},\ -iR_{\vec e_z}^{\mathrm{axf}}\,\bigr\} = 0 ,
$$
from which the whole chirality behaviour follows. Every **even** element commutes with $-iR_{\vec e_z}^{\mathrm{axf}}$, so an even element maps each chiral half into itself; every **odd** element anticommutes with it — vectors and trivectors alike, hence every odd element — so an odd element exchanges the halves:
$$
\boxed{\;iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}\,P_R = P_L\,iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}\;}.
$$
Combine this with the grading established above and the statement is: **rotations preserve chirality, reflections reverse it.** A rotation cannot change which chiral half a spinor belongs to, and a reflection always does. Chirality is not an extra label attached to the spinor; it is the eigenvalue of the operator that tells the two halves of the algebra apart, and only the odd half moves it.

The mass is where the two halves are coupled, and the series writes the coupling twice, in the two forms the grading distinguishes. The **algebra** equation is the one-sided chiral pair of *The Dirac Equation in Biquaternionic Form*,
$$
\tilde\nabla\tilde\Psi_R = m\tilde\Psi_L , \qquad \tilde\nabla^{\natural}\tilde\Psi_L = m\tilde\Psi_R ,
$$
in which every derivative acts by left multiplication. Left multiplication commutes with every right multiplication, hence with $-iR_{\vec e_z}^{\mathrm{axf}}$, so this equation is **chirality-blind**: its halves are named for the two members of the pair, not by an eigenvalue of the chirality cell. Chirality enters with the **module** equation, the single four-component equation
$$
(\mathbb{D}-m)\psi = 0 , \qquad \mathbb{D} = -R_{\vec e_x}^{\mathrm{axf}}\frac{\partial}{\partial t'} - \sum_k L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\frac{\partial}{\partial x_k} ,
$$
whose cells multiply on both sides. Every term of $\mathbb{D}$ anticommutes with $-iR_{\vec e_z}^{\mathrm{axf}}$, so $\mathbb{D}$ is odd, and it carries one chiral half into the other. The opposite signs in the square come from the cells, not from the display: $(R_{\vec e_x}^{\mathrm{axf}})^2=-I_4$ while $\bigl(L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\bigr)^2=+I_4$, so
$$
\mathbb{D}^2=-\frac{\partial^2}{\partial t'^2}+\sum_k\frac{\partial^2}{\partial x_k^2},
$$
and $(\mathbb{D}-m)(\mathbb{D}+m)$ is the Klein–Gordon operator up to an overall sign. The mass is a multiple of the identity — central and even — and flips nothing by itself.

The consequence is immediate. Were $\psi=\psi_L$ a single chirality, the equation would read $\mathbb{D}\psi_L=m\psi_L$ with the left side in the other half, so $\psi_L=0$: a massive field carries both halves, and chirality is not conserved. At $m=0$ the equation splits into $\mathbb{D}\psi_L=0$ and $\mathbb{D}\psi_R=0$, because $\mathbb{D}$ carries each half into the other and the sum vanishes half by half: the two halves decouple, and a field of one chirality alone is now allowed. That decoupling is the operator-level content of the statement that chirality and helicity agree only in the massless limit.

The representation-theoretic form of the same fact is the split of the complexified Lorentz algebra into two copies of $\mathfrak{sl}(2,\mathbb{C})$, each of them the complexification of an $\mathfrak{su}(2)$,
$$
\mathfrak{so}(1,3)_{\mathbb{C}} \cong \mathfrak{sl}(2,\mathbb{C})\oplus\mathfrak{sl}(2,\mathbb{C}),
$$
under which a finite-dimensional representation is labelled by a pair $(j_1,j_2)$. The rotations and boosts act within each factor, and chirality is *which* factor:

| object | label | chirality |
|---|---|---|
| scalar | $(0,0)$ | in neither factor; no chirality label exists |
| left Weyl spinor | $(\tfrac12,0)$ | in the first factor alone |
| right Weyl spinor | $(0,\tfrac12)$ | in the second factor alone |
| vector | $(\tfrac12,\tfrac12)$ | in both factors equally |

This is the precise sense in which chirality is tied to spin $\tfrac12$: the two Weyl spinors are the two smallest nontrivial modules of the two factors, and "left-handed" *means* "$(\tfrac12,0)$". A scalar carries no chirality because it sits in neither factor, and a vector is chirality-blind because it sits in both equally. The link between spin $\tfrac12$ and chirality is not a coincidence to be explained: each chiral half is a minimal module of one factor, and the cell is what tells the two factors apart.

The exchange of the two factors is an orientation-reversing operation, which is why it takes a reflection. **Parity is exactly that reflection.** It fixes the time direction and reverses the three spatial ones, and it exchanges the two spinor modules,
$$
\mathsf{P} : (\tfrac12,0) \longleftrightarrow (0,\tfrac12).
$$
It is odd in both readings — the trivector $iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\,iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\,iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$ for the geometric reflection, the internal factor $\eta_P=iR_{\vec e_x}^{\mathrm{axf}}$ for the parity of the Dirac field — and every odd element carries $P_R$ to $P_L$, so the exchange of the modules is the projector identity
$$
\eta_P P_R = P_L \eta_P .
$$

Parity violation — the statement that the weak interaction couples to one chirality and not the other — is therefore not an accidental property of the Standard Model but the statement that the interaction distinguishes the two factors of the complexified Lorentz algebra. This is what *Chiral Fermions in the Biquaternion Framework* and *The Neutrino and Majorana Fermions in Biquaternionic Form* develop on the physical side.

## Why the Pauli Algebra Cannot Carry Chirality

The non-relativistic limit of the Dirac equation is governed by the Pauli matrices, and it is natural to ask whether chirality could have been discussed there. It could not, and the reason is algebraic and exact.

The Pauli matrices generate $\mathrm{Cl}_{3}$, whose complexification is $M_2(\mathbb{C})$ and whose volume element is
$$
\sigma_1\sigma_2\sigma_3 = i\,I_2 ,
$$
a **central** element of the algebra that squares to $-1$. A chirality needs an element $\Gamma$ with $\Gamma^2 = +1$ that *anticommutes* with every generator, so that its two eigenspaces are exchanged by the generators and can be called the two chiralities; conjugation by $\Gamma$ then implements the parity map of the algebra. In $\mathrm{Cl}_{3}(\mathbb{C})=M_2(\mathbb{C})$ there is no such element at all: the only matrix anticommuting with all three Pauli matrices is zero. The natural candidate, the volume element, fails twice over — it is central, so it commutes rather than anticommutes, and it squares to $-1$ rather than $+1$. Its formal projectors $\frac{1}{2}(1\pm iI_2)$ would in any case be scalar matrices and not idempotent.

The obstruction is not the absence of a grading, since every Clifford algebra carries the even/odd grading and $\mathrm{Cl}_{3}$ has its even part of dimension $4$. What fails is that no element of the algebra implements that grading. A chiral projector would have to commute with every generator, and $M_2(\mathbb{C})$ acts irreducibly on the two-component module, so the only such elements are the scalars, which give the trivial projectors $0$ and $I_2$. Equivalently, no invertible matrix conjugates all three Pauli matrices to their negatives: it would have to anticommute with all three, and the only such matrix is zero. There is nowhere to put a chirality, and the obstruction is not a matter of ingenuity.

The Dirac algebra escapes it because it has **one more generator**, and that generator is timelike. The chirality cell is the product of all four generators, as the section *Why Chirality Needs a Reflection* records,
$$
-iR_{\vec e_z}^{\mathrm{axf}} = i\,\bigl(iR_{\vec e_x}^{\mathrm{axf}}\bigr)\bigl(iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\bigr)\bigl(iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\bigr)\bigl(iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\bigr) = -iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}} ,
$$
and there is no way to form it from three: a product of three generators is a trivector, odd, while the chirality cell is even. The timelike direction is not an optional extra; it is the ingredient that makes the chirality element exist. Chirality is therefore intrinsically relativistic: the Dirac algebra carries it, the Pauli algebra cannot, and the non-relativistic limit keeps only the spin. The same conclusion follows from the label table above, since the two-factor split is a property of the complexified *Lorentz* algebra, which the spatial rotation algebra does not possess.

## The Legacy Gamma Formulation

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra.

Here $L_a$ and $R_b$ are the left and right multiplications, $L_a\psi=a\psi$ and $R_b\psi=\psi b$.
$$
\gamma_0=iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}},\quad \gamma_1=iL_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_2=iL_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_3=iL_{\vec e_z}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_5=-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}} .
$$

The same in the axis-free display:

$$
\gamma_0=iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}},\quad \gamma_1=iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad \gamma_2=iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad \gamma_3=iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad \gamma_5=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}} .
$$

Each generator is a single cell product, and every element of the cell algebra is a sum of at most four cell products, one for each term of the rank decomposition of its coefficient matrix in the cell basis.

$\gamma_5=-iR_{\vec e_z}^{\mathrm{pau}}$ is the chirality cell itself. The central grading $\chi$ — the difference of the two central idempotents of the complexified algebra, so $\chi^2=e_t$ — is a different object, represented by $\gamma_5$ on the Dirac module.

The $\gamma$'s are a complex frame, not a real one: they generate $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$ over $\mathbb{C}$, whereas the cells with real coefficients generate the real algebra $\mathrm{Cl}_{3,1}(\mathbb{R})=M_4(\mathbb{R})$. It is the complexification that makes the scalar $i$ central, and that is why each generator is written as $i$ times a real cell.

**The identities the series uses.** In the $\gamma$ reading, with $\epsilon_{0123}=+1$,
$$
\{\gamma_\mu,\gamma_\nu\}=2g_{\mu\nu}I_4,\qquad
(\gamma_k)^2=-I_4,\qquad
\gamma_5^2=I_4,\qquad
\{\gamma_\mu,\gamma_5\}=0,
$$
$$
[\gamma_\mu,\gamma_\nu]=2\gamma_\mu\gamma_\nu\quad(\mu\ne\nu),\qquad
[\gamma_a,S_{cd}]=g_{ac}\gamma_d-g_{ad}\gamma_c,\qquad
S_{cd}=\tfrac14[\gamma_c,\gamma_d],
$$
$$
\mathrm{tr}(\gamma_\mu\gamma_\nu)=4g_{\mu\nu},\qquad
\mathrm{tr}(\gamma_5\gamma_\mu\gamma_\nu\gamma_\rho\gamma_\sigma)=-4i\,\epsilon_{\mu\nu\rho\sigma},
$$
$$
\mathrm{tr}(\gamma_\mu\gamma_\nu\gamma_\rho\gamma_\sigma)
=4\bigl(g_{\mu\nu}g_{\rho\sigma}-g_{\mu\rho}g_{\nu\sigma}+g_{\mu\sigma}g_{\nu\rho}\bigr).
$$
Four contraction sums accompany them. The four that hold in every frame are the ones with one index raised, $\gamma^\mu=\varepsilon_\mu\gamma_\mu$ and $\varepsilon=(+1,-1,-1,-1)$:
$$
\sum_\mu\gamma^\mu\gamma_\mu=4I_4,\qquad
\sum_\mu\gamma^\mu\gamma_\alpha\gamma_\mu=-2\gamma_\alpha,\qquad
\sum_\mu\gamma^\mu\gamma_\alpha\gamma_\beta\gamma_\mu=4g_{\alpha\beta}I_4,
$$
$$
\sum_\mu\gamma^\mu\gamma_\alpha\gamma_\beta\gamma_\gamma\gamma_\mu=-2\,\gamma_\gamma\gamma_\beta\gamma_\alpha .
$$
Written with every index down, they are frame statements instead, because a cell's square changes with the frame. In a Euclidean frame, where every cell squares to $+I_4$, the same four sums read
$$
\sum_\mu\gamma_\mu\gamma_\mu=4I_4,\qquad
\sum_\mu\gamma_\mu\gamma_\alpha\gamma_\mu=-2\gamma_\alpha,\qquad
\sum_\mu\gamma_\mu\gamma_\alpha\gamma_\beta\gamma_\mu=4\delta_{\alpha\beta}I_4,
$$
$$
\sum_\mu\gamma_\mu\gamma_\alpha\gamma_\beta\gamma_\gamma\gamma_\mu=-2\,\gamma_\gamma\gamma_\beta\gamma_\alpha ,
$$
and in the frame of the series the metric enters term by term. Writing $\gamma_\mu^2=\varepsilon_\mu I_4$,
$$
\sum_\mu\gamma_\mu\gamma_\mu=\Bigl(\sum_\mu\varepsilon_\mu\Bigr)I_4=-2I_4,\qquad
\sum_\mu\gamma_\mu\gamma_\alpha\gamma_\mu=\Bigl(2\varepsilon_\alpha-\sum_\mu\varepsilon_\mu\Bigr)\gamma_\alpha ,
$$
so the second sum is $4\gamma_0$ for $\alpha=0$ and vanishes identically for spacelike $\alpha$. The third is not the substitution $\delta_{\alpha\beta}\to g_{\alpha\beta}$; it is
$$
\sum_\mu\gamma_\mu\gamma_\alpha\gamma_\beta\gamma_\mu
=2\varepsilon_\alpha\,\gamma_\beta\gamma_\alpha-\bigl(2\varepsilon_\beta+2\bigr)\gamma_\alpha\gamma_\beta ,
$$
which is $-2\gamma_0\gamma_k$ for one timelike and one spacelike index, $+2\gamma_j\gamma_k$ for two spacelike ones, and $-2\varepsilon_\alpha I_4$ for $\alpha=\beta$. The raised-index display is the one to compute with, and the lowered one the one to read in the Euclidean literature.

**The display.** Every array printed in this section is given twice: in the Peirce display first, labelled $\mathrm{pau}$, whose arrays are the ones the literature prints, and in the axis-free display after it, labelled $\mathrm{axf}$, which is the display of the body and of the corpus. The two are carried into one another by $L_{e_\mu}^{\mathrm{axf}}=C_{\Pi}L_{e_\mu}^{\mathrm{pau}}C_{\Pi}^{-1}$, and a conjugation by $C_{\Pi}$ changes no product, no anticommutator, no trace and no determinant, so every identity of the section holds in both. An array is a statement about one display; a cell named in the running text keeps the Peirce label, and its axis-free array is the conjugate. The label names the array and not the operator.

## Summary

The claims of this article, in order.

1. **One algebra, two interpretations.** The biquaternion algebra is a matrix algebra, so each element is at once a point of a transformation group and an operator. The rotors are the even instances; the generators $iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}$ are the odd ones, and the even and odd instances act on the spinor module in opposite ways.

2. **The grading is the reflection count.** By Cartan–Dieudonné, an orthogonal transformation is a product of reflections and its determinant is $(-1)^{\text{count}}$. The split $\mathrm{Cl}_{1,3} = \mathrm{Cl}_{1,3}^{+}\oplus\mathrm{Cl}_{1,3}^{-}$ is that parity.

3. **The frame and the metric.** Every vector is $iR_{\vec e_x}^{\mathrm{axf}}$ times the image of $w\in\mathbb{M}_+$, and the image of $\mathbb{M}_+$ is the identity together with the timelike bivectors — the boost sector. The biquaternion norm on the Hermitian basis is $g = \mathrm{diag}(+1,-1,-1,-1)$, its minus signs being those of $i^2$, and on the material basis $\eta = -g$. The Clifford metric is the biquaternion norm of the objects the generators represent, so the mostly-minus convention is forced rather than chosen.

4. **Conjugation by $iR_{\vec e_x}^{\mathrm{axf}}$ is the bar.** Conjugating the image of $\tilde{Q}$ by $iR_{\vec e_x}^{\mathrm{axf}}$ gives the image of $\bar{\tilde{Q}}$: it fixes $\mathbb{H}_{\mathbb{B}}$ and negates $i\mathbb{H}_{\mathbb{B}}$, hence preserves each of $\mathbb{M}_{\pm}$. Together with reversal, which is quaternion conjugation, it composes into the Hermitian conjugation ${}^{*}$. The real structure $\flat = -{}^{*}$ therefore carries the frame within it.

5. **Rotations and reflections have different spaces.** The rotations are the unit-norm biquaternions, a group of dimension $6$ with the bivectors as Lie algebra. The reflections are the odd unit elements, two cosets of dimension $3$ organised by their $\mathbb{M}_+$ normals, not a group. Together they are $\mathrm{Pin}(1,3)$. **Anti-linear maps shift the correspondence by one:** the grade and the determinant are offset by a sign, so an even internal factor belongs to a reflection and an odd one to a proper transformation — which is how $T$ (even) is a reflection while $C$ (odd) is not.

6. **Two reflections, or four.** A rotation is a product of two reflections exactly when it fixes a plane — equivalently, when a certain $4\times 4$ determinant vanishes. Pure boosts, pure spatial rotations, and boosts with a rotation in the plane of the boost qualify; a boost with a rotation about the boost axis does not, and needs four.

7. **Chirality is what the reflection changes.** Even elements commute with $-iR_{\vec e_z}^{\mathrm{axf}}$, odd ones anticommute, so rotations preserve chirality and reflections reverse it. The mass is even and central, a multiple of the identity on the module: it couples the two chiral equations without flipping a chirality itself, and the odd module operator $\mathbb{D}$ performs the flip. In the split $\mathfrak{so}(1,3)_{\mathbb{C}}\cong\mathfrak{sl}(2,\mathbb{C})\oplus\mathfrak{sl}(2,\mathbb{C})$, chirality is which factor, and the exchange of the factors is parity.

8. **Chirality is relativistic.** In the complexified Pauli algebra $\mathrm{Cl}_{3}(\mathbb{C})\cong M_2(\mathbb{C})$ the volume element is central and squares to $-1$, no element implements the parity map, and the module $\mathbb{C}^2$ is irreducible: there is no chiral projector. The chirality cell is the product of all four generators, and it exists only because one of them is timelike.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $\mathrm{Cl}_{1,3}$, $\mathrm{Cl}_{1,3}^{\pm}$ | Clifford algebra and its even/odd parts |
| $g = \mathrm{diag}(+1,-1,-1,-1)$ | Clifford metric of the generators |
| $\eta = \mathrm{diag}(-1,+1,+1,+1) = -g$ | $ict'$ metric of the material coordinates |
| $L_{a}R_{b}$ | Left multiplication $L_a$ and right multiplication $R_b$: $L_{a}R_{b}\psi = a\psi b$, $L_{a}R_{b}L_{c}R_{d} = L_{ac}R_{db}$ |
| image of $\tilde Q$ | The $\mathbb{R}$-linear comparison with the even subalgebra, by its values $e_t\mapsto L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$, $\vec e_k\mapsto L_{\vec e_k}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$, $i\mapsto L_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$; written by its values, never by a symbol |
| $iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}$ | The generator cells: $iR_{\vec e_x}^{\mathrm{axf}} = iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}$ and $iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$ for $k=1,2,3$ |
| $\omega = iR_{\vec e_x}^{\mathrm{axf}}\,iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\,iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\,iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}} = -L_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$ | Pseudoscalar, $\omega^2 = -I_4$; its four factors of $i$ multiply to $i^4=1$ |
| $-iR_{\vec e_z}^{\mathrm{axf}} = i\omega = -iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$ | Chirality cell, $(-iR_{\vec e_z}^{\mathrm{axf}})^{2} = I_4$ |
| $P_{L,R} = \tfrac12(I_4 \pm iR_{\vec e_z}^{\mathrm{axf}})$ | Chirality projectors, rank $2$ |
| $\tilde\Psi_{L,R} = P_{L,R}\tilde\Psi$ | The two chiral components of a spinor |
| $\tilde\nabla$, $\tilde\nabla^{\natural}$ | The biquaternion gradient and its quaternion conjugate; the one-sided chiral pair $\tilde\nabla\tilde\Psi_R=m\tilde\Psi_L$, $\tilde\nabla^{\natural}\tilde\Psi_L=m\tilde\Psi_R$, blind to chirality |
| $\mathbb{D} = -R_{\vec e_x}^{\mathrm{axf}}\partial/\partial t'-\sum_k L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\partial/\partial x_k$ | The module Dirac operator, built from two-sided cells; odd under the chirality cell, hence it carries one half into the other |
| $iR_{\vec e_x}^{\mathrm{axf}} = iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}$ | The frame cell; the reflection whose normal is $e_t$ |
| $\rho(u) : x\mapsto -\epsilon(u)\,u x u$ | Pin action of an odd unit element; $u^2=\epsilon(u)I_4$ |
| Reversal | Reversing the Clifford image of $\tilde{Q}$ gives the image of $\tilde{Q}^{\natural}$; Clifford reversal is quaternion conjugation |
| Frame conjugation | Conjugating the image of $\tilde{Q}$ by $iR_{\vec e_x}^{\mathrm{axf}}$ gives the image of $\bar{\tilde{Q}}$ |
| Hermitian conjugation | The image of $\tilde{Q}^{*}$ is $iR_{\vec e_x}^{\mathrm{axf}}$ times the reversed image of $\tilde{Q}$, times $iR_{\vec e_x}^{\mathrm{axf}}$; $*$ is the bar composed with $\natural$ |
| $\tilde U^{\mathrm{lor}}$, $\langle\tilde U^{\mathrm{lor}}\rangle_{\natural} = 1$ | Rotor, unit-norm biquaternion; $SL(2,\mathbb{C})$ |
| $\tilde{Q}_2 = \tilde U^{\mathrm{lor}}\tilde{Q}\tilde U^{\mathrm{lor}}{}^{*}$ | Rotor conjugation on $\mathbb{M}_-$ |
| $\mathbb{M}_+$ | Hermitian sector; its image is the identity together with the timelike bivectors (boosts) |
| $\mathbb{H}_{\mathbb{B}}$ | Real-quaternion sector; its image is the identity together with the spacelike bivectors (spatial rotations) |
| $\det M$ | Two-reflection criterion: $\det M = 0$ iff $\tilde U^{\mathrm{lor}}$ fixes a plane pointwise |
| $\det = (-1)^{k}(-1)^{\text{anti}}$ | Reflection parity of a module map, linear or anti-linear |
| $\mathsf{P}$ | Parity reflection; exchanges the two chiral halves |
| $\eta_P = iR_{\vec e_x}^{\mathrm{axf}}$ | The internal factor of the parity of the Dirac field; odd, so $\eta_P P_R = P_L\eta_P$ |

## Further Reading

- Companion articles in this series: [Matrix Representations Conventions](matrix-representations-conventions.html) (the Clifford reading, the sign conventions, and the chirality operator used throughout, §*The Clifford Structure*); [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html) (the chiral pair, the two-sided form and the mass); [The Spinor Module in Biquaternionic Form and Its Lorentz Action](the-spinor-module-in-biquaternionic-form-and-its-lorentz-action.html) (the module, the one-sided spinor action, and the two factors $\mathrm{SU}(2)\oplus\mathrm{SU}(2)$); [Exercise: Chirality and the Weyl Spinors](exercise-chirality-and-the-weyl-spinors.html) (the projectors and the two Weyl modules); [The Lorentz Transformation as a Biquaternionic Rotation](the-lorentz-transformation-as-a-biquaternionic-rotation.html) (the boost rotor, its Hermiticity, and the rotor conjugation); [The Lorentz Group in Biquaternionic Form — Structure and Representations](the-lorentz-group-in-biquaternionic-form-structure-and-representations.html); [Exercise: The Thomas Precession](exercise-the-thomas-precession.html) (the composition of non-collinear boosts); [Exercise: Boosting a Four-Velocity and Rapidity Composition](exercise-boosting-a-four-velocity-and-rapidity-composition.html).
- On the physics of chirality: [Chiral Fermions in the Biquaternion Framework](chiral-fermions-in-the-biquaternion-framework.html); [The Neutrino and Majorana Fermions in Biquaternionic Form](the-neutrino-and-majorana-fermions-in-biquaternionic-form.html); [The CPT Theorem in Biquaternionic Form](the-cpt-theorem-in-biquaternionic-form.html) (the anti-linear discrete symmetries of the last subsection); [Zitterbewegung in Biquaternionic Form](zitterbewegung-in-biquaternionic-form.html) (the mass as the coupling between the chiralities); [Exercise: The Non-Relativistic Limit and the Pauli Equation](exercise-the-non-relativistic-limit-and-the-pauli-equation.html) (the reduction to the Pauli algebra).
- Foundational articles: [Introduction to the Biquaternion Universe](introduction-to-the-biquaternion-universe.html); [The Material Sector: Four-Vectors, Interval and Lorentz Action](the-material-sector-four-vectors-interval-and-lorentz-action.html); [The Informational Sector: States, Observables and Probability](the-informational-sector-states-observables-and-probability.html); [Algebra and Element Conventions](algebra-and-element-conventions.html).
- On the Clifford structures used here: [Clifford Algebras](../articles_maths/clifford-algebras.html); [Two-Sided Operators on a Clifford Algebra](../articles_maths/two-sided-operators-on-a-clifford-algebra.html) (the cell algebra, its two closures, and the frame); *Clifford Algebras in finite dimensions*; *Spinors*; [The Spinor Representation of the Lorentz Group in Biquaternionic Form](the-spinor-representation-of-the-lorentz-group-in-biquaternionic-form.html).

