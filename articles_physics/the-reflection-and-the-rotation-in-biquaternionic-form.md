# __The Reflection and the Rotation in Biquaternionic Form__

## Introduction

The companion articles of the relativistic quantum series build the biquaternion Dirac algebra and use it: *The Dirac Algebra and Biquaternions — A Dictionary* fixes the isomorphism between the biquaternions and the even Clifford algebra; *The Spinor Module in Biquaternionic Form and Its Lorentz Action* constructs the module on which the algebra acts; *Exercise: Chirality and the Weyl Spinors* develops the chiral projectors. This article is about a structure that all three use but none names: the **grading of the Dirac algebra by reflection parity**, and the identification of one element — the timelike generator $\gamma^0$ — as the hinge on which the whole structure turns.

The subject is the following observation, made precise. The biquaternion algebra $\mathbb{B}$ is isomorphic to the **even** part of the Clifford algebra $\mathrm{Cl}_{1,3}$. Its elements include the Lorentz rotors, which act on four-vectors by conjugation; and its elements are at the same time the points of the rotation group. The generators $\gamma^\mu$, by contrast, are **odd**: they are not biquaternions at all, they lie outside the even part, and they are not rotors. They act on spinors and they **exchange the two chiralities**. The odd/even split of the Clifford algebra is therefore not a bookkeeping device. It is the split between the transformations that *turn* and the transformations that *reflect*, and chirality — the property that separates the two Weyl spinors — is precisely what the odd part changes and the even part preserves.

The article is organized as follows. The first section reconciles the two ways a single element of the algebra is used — as an object and as an operator. The second establishes the grading, by the classical theorem that every orthogonal transformation is a product of reflections. The third introduces the frame $\gamma^0$ and shows that the Clifford metric is the norm form of the Hermitian sector, which is what makes the mostly-minus convention of the series a statement about the objects rather than a choice. The fourth shows that conjugation by $\gamma^0$ is complex conjugation on $\mathbb{B}$, so that the frame, the sector swap, and the reflection are one operator. The fifth and sixth give the spaces of rotations and of reflections, and answer the question of how many reflections a given Lorentz transformation needs. The last two sections draw the consequence for chirality and explain why the Pauli algebra cannot carry it.

The conventions are those of the series: the biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0 = 1, e_1, e_2, e_3$, $e_k^2 = -e_0$, $e_1e_2 = e_3$; the scalar imaginary $i$; the sectors $\mathbb{M}_-$, $\mathbb{M}_+$, $\mathbb{H}_{\mathbb{B}}$; the Clifford metric $g = \mathrm{diag}(+1,-1,-1,-1)$ of the generators; and the isomorphism $\Phi$ of the dictionary article, under which $\Phi(e_k)$ is a spacelike bivector, $\Phi(e_0) = I_4$, and $\Phi(i) = -\omega$ with $\omega = \gamma^0\gamma^1\gamma^2\gamma^3$ the pseudoscalar. No convention is changed here.

## One Algebra, Read Twice

A single element of a matrix algebra is at once a **point** and an **operator**. This is not a peculiarity of the biquaternions; it is what a matrix algebra is. The quaternions show it most plainly: a unit quaternion is a point of the three-sphere, and it is also the rotation that acts on vectors by conjugation. The same quaternion, read two ways.

The biquaternion algebra inherits this doubling, and the series uses it constantly:

- A **rotor** $\tilde{\Lambda}$ with $N(\tilde{\Lambda}) = 1$ is a point of $SL(2,\mathbb{C})$, the double cover of the restricted Lorentz group. It is also an operator: it acts on four-vectors by the rotor conjugation, and on spinors by left multiplication.
- A **generator** $\gamma^\mu$ is a point of the odd part — a four-vector, one of the four legs of spacetime — and it is also an operator on the spinor module.

For the rotors the doubling is familiar and the two readings are both two-sided or both one-sided. For the generators it is not, and the reason is the grading. The even elements act on the spinor module *preserving* its two chiral halves, because they commute with the chirality operator; the odd elements act *exchanging* them, because they anticommute with it. So an even element and an odd element, both points of the same algebra and both operators on the same module, do qualitatively different things. The remainder of this article is the elaboration of that sentence.

The two actions on a four-vector are worth naming explicitly, since both are used below. For $\tilde{\Lambda}$ even with $N(\tilde{\Lambda}) = 1$, the rotor conjugation

$$
\tilde{X} \mapsto \tilde{\Lambda}\tilde{X}\tilde{\Lambda}^\dagger
$$

implements the Lorentz transformation of the material vector $\tilde{X}\in\mathbb{M}_-$. For a pure boost the rotor is Hermitian, $\tilde{\Lambda}^\dagger = \tilde{\Lambda}$, and the action reduces to $\tilde{X}\mapsto\tilde{\Lambda}\tilde{X}\tilde{\Lambda}$; for a general element of $SL(2,\mathbb{C})$ the general form is required. Both facts are those of *The Lorentz Transformation as a Biquaternionic Rotation*. In the Clifford representation the same action is the conjugation $x\mapsto\Lambda x\Lambda^{-1}$ by $\Phi(\tilde{\Lambda})$, which is legitimate because in that representation a unit element satisfies $\Phi(\tilde{\Lambda})^\dagger = \Phi(\tilde{\Lambda})^{-1}$.

The odd elements are not in $\mathbb{B}$, so they have no biquaternion representative. They lie in the odd part of $\mathrm{Cl}_{1,3}$ and act on vectors by the two-sided map of the Pin group,

$$
\rho(u): x \mapsto -\,u\,x\,u^{-1}, \qquad u\ \text{odd},\ u^2 = \pm I_4 ,
$$

which is the twisted adjoint. The sign in front is the only difference from the even formula, and it is what makes the odd elements reflections rather than rotations.

## The Grading by Reflection Count

The classical theorem of Cartan and Dieudonné states that every orthogonal transformation of a non-degenerate space is a product of reflections in hyperplanes. For a space of dimension $n$ at most $n$ reflections are needed, and the determinant of the transformation is $(-1)^{k}$, where $k$ is the number of reflections in any factorisation. Two remarks follow, and together they are the content of this section.

First, the **determinant classifies the transformation by the parity of the reflection count**. An even number of reflections gives a rotation, an odd number a reflection (or, more generally, an orientation-reversing transformation). In four dimensions with Lorentzian signature, a product of two reflections is a Lorentz transformation of the restricted group, and a single reflection is parity, time reversal, or an axis flip.

Second, and this is the point, the parity of the reflection count **is the grading of the Clifford algebra**:

$$
\mathrm{Cl}_{1,3} = \mathrm{Cl}_{1,3}^{+} \oplus \mathrm{Cl}_{1,3}^{-}.
$$

The even part is spanned by the identity, the six bivectors, and the pseudoscalar; the odd part by the four vectors and the four trivectors. An even element is a product of an even number of vectors — that is, of an even number of reflections — and an odd element of an odd number. The biquaternion algebra is the even part,

$$
\mathbb{B} \cong \mathrm{Cl}_{1,3}^{+}(\mathbb{R}),
$$

as the dictionary article establishes, and the rotations therefore sit inside $\mathbb{B}$ while the reflections do not.

The identification is verified directly in the explicit representation. For $40$ random even elements of unit norm, the vector action has determinant $+1$; for $40$ random odd elements of unit norm, it has determinant $-1$. The correspondence is exact and not merely a counting resemblance:

| element | reflection count | determinant of the vector action | in $\mathbb{B}$? |
|---|---|---|---|
| even unit element $\Lambda$ (rotor) | even ($0$, $2$ or $4$) | $+1$ | yes |
| odd unit element $u$ ($\gamma^\mu$ or a trivector) | odd | $-1$ | no |

The geometric content of the even part is also known: the Lie algebra of the rotation group is generated by the bivectors, and the bivectors are precisely the products of two reflections. So the two halves of the Clifford algebra correspond to the two classes of orthogonal transformations, and the correspondence is an identity.

## The Frame $\gamma^0$ and the Hermitian Sector

The odd part is reached from the even part by a frame, and the frame is the timelike generator. Every vector is

$$
x_\mu\gamma^\mu = \gamma^0\,\Phi(w), \qquad w \in \mathbb{M}_+ ,
$$

with all coefficients positive; every trivector is $\gamma^0\Phi(w')$ with $w'\in\mathbb{M}_-$. The correspondence is coefficient by coefficient:

| Clifford element | biquaternion | sector |
|---|---|---|
| $\gamma^0$ | $e_0$ | $\mathbb{M}_+$ |
| $\gamma^1, \gamma^2, \gamma^3$ | $ie_1, ie_2, ie_3$ | $\mathbb{M}_+$ |
| trivectors | combinations of $ie_0, e_1, e_2, e_3$ | $\mathbb{M}_-$ |

The generators therefore *are* the Hermitian-sector basis, pushed through $\gamma^0$: the scalar direction $e_0$ becomes the time generator, the three imaginary-quaternion directions $ie_k$ become the three spatial generators. And in the other direction, the frame maps the even algebra onto its generators:

$$
\Phi(\mathbb{M}_+) = \mathrm{span}\{I_4,\ \gamma^0\gamma^1,\ \gamma^0\gamma^2,\ \gamma^0\gamma^3\},
$$

the identity together with the **timelike bivectors**. Since the timelike bivectors generate the boosts, this says that the Hermitian sector is the boost sector — exactly the statement of *The Lorentz Transformation as a Biquaternionic Rotation*, that the pure boosts are the Hermitian elements of $SL(2,\mathbb{C})$. The real-quaternion sector plays the dual role for the other family,

$$
\Phi(\mathbb{H}_{\mathbb{B}}) = \mathrm{span}\{I_4,\ \gamma^2\gamma^3,\ \gamma^3\gamma^1,\ \gamma^1\gamma^2\},
$$

the identity together with the spacelike bivectors, which generate the spatial rotations.

The decisive consequence concerns the **metric**. The norm form $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = \sum_\mu Q_\mu^2$ evaluated on the two sector bases gives

$$
N \text{ on } (e_0, ie_1, ie_2, ie_3) = \mathrm{diag}(+1,-1,-1,-1) = g,
$$
$$
N \text{ on } (ie_0, e_1, e_2, e_3) = \mathrm{diag}(-1,+1,+1,+1) = \eta = -g .
$$

The Clifford metric of the generators is not an independent convention laid on top of the algebra. **It is the norm form of the Hermitian sector**, and the $ict$ metric of the material sector is its negative, the norm form of $\mathbb{M}_-$. This closes the loop of the series' metric conventions: level $2$ carries $\eta = \mathrm{diag}(-1,+1,+1,+1)$, the form of the material coordinates; level $3$ carries $g = \mathrm{diag}(+1,-1,-1,-1)$, the form of the objects the generators represent, which are Hermitian. The two differ by the sign that distinguishes the two sectors, and neither could consistently be anything else.

The same fact appears in the vector square. For $w = x_0e_0 + ix_1e_1 + ix_2e_2 + ix_3e_3 \in \mathbb{M}_+$,

$$
\left(x_\mu\gamma^\mu\right)^2 = N(w)\,I_4 = \left(x_0^2 - x_1^2 - x_2^2 - x_3^2\right)I_4 ,
$$

with no relative sign between the Clifford square and the biquaternion norm. The absence of that sign is the signature $g$ showing through.

## Conjugation by $\gamma^0$ Is Complex Conjugation

The frame $\gamma^0$ is not merely a bookkeeping element. It has a definite action on the algebra, and it is the action that defines the two sectors.

For every $\tilde{Q}\in\mathbb{B}$,

$$
\gamma^0\,\Phi(\tilde{Q})\,\gamma^0 = \Phi(\tilde{Q}^*),
$$

where $\tilde{Q}^*$ is the complex conjugate, $i\mapsto -i$ with the quaternion units fixed. Since complex conjugation is exactly the map that fixes $\mathbb{H}_{\mathbb{B}}$ and negates $i\mathbb{H}_{\mathbb{B}}$, this says that **conjugation by $\gamma^0$ is the sector-exchanging conjugation**: it is the spacetime-side avatar of the operation that separates the material and informational sectors.

Among the four generators, $\gamma^0$ is unique in this. The spatial generators reflect instead: $\gamma^k$ fixes $e_k$ and negates the two units $e_j$ with $j\neq k$, and it acts dually on the imaginary units, negating $ie_k$ and fixing the other two. They are linear involutions on the quaternion units, not conjugations. Only the time direction conjugates.

The frame completes the Clifford reading of the conjugations of $\mathbb{B}$. Clifford reversal $\mathrm{rev}$, the anti-automorphism that reverses the order of the factors in a product, acts on the biquaternions as **quaternion conjugation**:

$$
\mathrm{rev}\big(\Phi(\tilde{Q})\big) = \Phi(\bar{\tilde{Q}}) .
$$

Composing the reversal with the frame conjugation gives the Hermitian conjugation:

$$
\Phi(\tilde{Q}^\dagger) = \gamma^0\,\mathrm{rev}\big(\Phi(\tilde{Q})\big)\,\gamma^0 .
$$

So the two elementary conjugations of the algebra have separate Clifford readings — reversal for the quaternion conjugation, the frame for the complex one — and $\dagger$ is their composite. Verified on generic elements.

There is a consequence worth recording, because it bears on the mass term. The algebra's real structure is the anti-Hermitian conjugation $\flat = -\dagger$, and the identity above shows that $\gamma^0$ is *inside* it: the frame, with its sector-exchanging and reflection properties, is one of the two ingredients of $\flat$. A formulation of the mass built on $\flat$ therefore carries the frame, but in the guise of a reality condition rather than of a generator; the linear and chirality-off-diagonal mass term of *The Dirac Equation in Biquaternionic Form* displays it openly instead. This is an observation about how the frame is packaged, not a derivation; it is stated here because it is the reason the frame is easy to overlook.

## The Spaces of Rotations and of Reflections

With the grading in hand, the two spaces can be described, and they are not of the same kind.

**The rotations.** The rotors are the unit-norm biquaternions,

$$
SL(2,\mathbb{C}) = \{\tilde{\Lambda}\in\mathbb{B} : N(\tilde{\Lambda}) = 1\},
$$

a group of real dimension $6$, the double cover of $SO^+(1,3)$. Its Lie algebra is the span of the six bivectors, the images of $e_k$ and $ie_k$ under $\Phi$. This is the space in which the rotors of the relativity articles live and act: on four-vectors in *Relativistic Mechanics in Biquaternionic Form* and *Exercise: Boosting a Four-Velocity and Rapidity Composition*, on spinors in *The Spinor Module in Biquaternionic Form and Its Lorentz Action*, on states in *Quantum Mechanics in Biquaternionic Form*, and in the composition of rotations of *Exercise: The Thomas Precession*.

Two subfamilies are worth separating, because the series uses them differently:

| subfamily | condition | biquaternion form | character |
|---|---|---|---|
| spatial rotations | $\tilde{\Lambda}$ real quaternion | $\cos\frac{\theta}{2} + \sin\frac{\theta}{2}\hat{e}_{jk}$ | group $SU(2)$ |
| pure boosts | $\tilde{\Lambda}$ Hermitian, $\tilde{\Lambda}^\dagger = \tilde{\Lambda}$ | $\cosh\frac{\psi}{2} + i\sinh\frac{\psi}{2}\hat{\mathbf{u}}$ | symmetric submanifold, not a group |

The boosts do not close under multiplication — the product of two non-collinear boosts is a boost plus a Thomas–Wigner rotation — so they form a submanifold of $SL(2,\mathbb{C})$ rather than a subgroup. The two families are exponentials of the two sector algebras: the boosts of elements of $\mathbb{M}_+$, namely the timelike bivectors $i\hat{\mathbf{u}}$, and the spatial rotations of elements of $\mathbb{H}_{\mathbb{B}}$, namely the spacelike bivectors $\hat{e}_{jk}$.

**The reflections.** A reflection is an odd element of unit norm, and its data is its **normal**, a unit vector $u$. Writing the vectors as $\gamma^0\Phi(w)$ with $w\in\mathbb{M}_+$, the unit vectors are

$$
u = \gamma^0\Phi(w), \qquad w\in\mathbb{M}_+, \quad N(w) = \pm 1 ,
$$

the timelike normals for $N(w) = +1$ and the spacelike ones for $N(w) = -1$. The canonical reflection is the frame itself, $\gamma^0 = \gamma^0\Phi(e_0)$: its normal is the identity $e_0$ of $\mathbb{B}$.

The reflections do **not** form a group, and this is the sharp difference from the rotations. Multiplying two reflections gives an even element — a rotation — so the set of reflections is a single coset of the rotation group, not closed under multiplication. Its dimension is $3$, the dimension of the unit quadric, against the $6$ of the rotations. The two together form the Pin group,

$$
\mathrm{Pin}(1,3) = \mathrm{Spin}(1,3) \cdot \{\text{unit vectors}\},
$$

whose even part is $\mathrm{Spin}(1,3) = SL(2,\mathbb{C})$ and whose algebra-level image is $\mathrm{Cl}_{1,3} = \mathrm{Cl}_{1,3}^{+}\oplus\mathrm{Cl}_{1,3}^{-}$. The relation between the two spaces is generation: the rotations are the products of an even number of reflections, and the bivectors that generate the Lorentz algebra are the products of two.

The reflections account for the four components of the full Lorentz group. Under the Pin action $\rho(u) : x\mapsto -uxu^{-1}$, the frame acts by a sign on the time direction alone or on the three spatial directions alone, according to the sign convention:

$$
x \mapsto \gamma^0 x\,(\gamma^0)^{-1} : \mathrm{diag}(+1,-1,-1,-1) \quad\text{(parity)},
$$
$$
x \mapsto -\gamma^0 x\,(\gamma^0)^{-1} : \mathrm{diag}(-1,+1,+1,+1) \quad\text{(time reversal)} .
$$

Both are reflections, with determinant $-1$; the sign selects which of the two is realised. The identity component is the even part, and the discrete symmetries are the reflections.

**The anti-linear case.** The rule established in the second section — even elements act with determinant $+1$, odd elements with $-1$ — holds for the **linear** action of the Pin group. The discrete symmetries of the Dirac field are not all linear: charge conjugation and time reversal are **anti-linear**, as *The CPT Theorem in Biquaternionic Form* establishes, and their internal matrices are elements of the Clifford algebra. For an anti-linear map $\psi\mapsto S\psi^{*}$, the complex conjugation contributes one additional orientation reversal, and the determinant of the induced orthogonal transformation becomes

$$
\det = (-1)^{k}\,(-1)^{\text{anti}} , \qquad k = \text{Clifford grade of the internal matrix } S ,
$$

so the two columns are exchanged: an **even** internal matrix gives a reflection, an **odd** one a proper transformation. Verified on random even and odd unit elements, and on the three discrete symmetries in the block representation of the CPT article:

| operation | internal matrix | grade | linearity | determinant | induced map |
|---|---|---|---|---|---|
| $P$ | $\gamma^0$ | odd | linear | $-1$ | reflection |
| $T$ | $\gamma^1\gamma^3$ | even | anti-linear | $-1$ | reflection |
| $C$ | $i\gamma^2$ | odd | anti-linear | $+1$ | proper |

This is why $T$ is a reflection whose internal matrix is an **even** element — the real quaternion $\gamma^1\gamma^3=-e_2$ of that article — while $C$ is a proper transformation carried by an **odd** one. Neither fact is visible from the grade alone, and both are recorded here so that the grade assignments of the CPT article are not read against the rule of this one.

What anti-linearity does **not** change is the chirality behaviour. Chirality is decided by anticommutation with $\gamma_5$, which is a property of the Clifford element and not of the map's linearity: $C$ and $P$, both odd, exchange the chiral halves; $T$, even, preserves them; hence $CPT$, even, preserves them. The grade governs which chirality a spinor is carried to; the determinant governs the spacetime parity it is carried by; and anti-linearity moves only the second.

## How Many Reflections?

The classical theorem gives an upper bound of four reflections in four dimensions. The sharper question — given a rotation, how many reflections does it take — has a clean answer, and it separates the simple Lorentz transformations from the generic ones.

A product of two reflections is an element $\tilde{\Lambda} = uv$ with $u$ and $v$ unit vectors. The criterion is algebraic. The product $u\tilde{\Lambda}$ has a grade-$1$ and a grade-$3$ part, and the grade-$3$ part is *linear* in $u$. So the condition that $u\tilde{\Lambda}$ be a pure vector — that is, that $\tilde{\Lambda}$ be $u$ times a vector — is a system of four linear equations in the four components of $u$, with a $4\times4$ matrix $M$ built from the bivector part of $\tilde{\Lambda}$:

$$
\tilde{\Lambda} = uv \ \text{for unit vectors}\ u,v \quad\Longleftrightarrow\quad M\cdot u = 0 \ \text{has a nonzero solution} \quad\Longleftrightarrow\quad \det M = 0 .
$$

Geometrically the criterion is that **$\tilde{\Lambda}$ fixes a two-dimensional subspace pointwise**, since a product of two reflections is the identity on the plane orthogonal to the span of $u$ and $v$. The two forms of the criterion agree: on $120$ random Lorentz transformations the determinant vanished exactly when the fixed subspace had dimension $2$.

| transformation | $\lvert\det M\rvert$ | fixed subspace | reflections needed |
|---|---|---|---|
| pure boost | $0$ | dimension $2$ | $2$ |
| pure spatial rotation | $0$ | dimension $2$ | $2$ |
| boost composed with a rotation in a non-parallel plane | $\neq 0$ | dimension $0$ | $4$ |

The factorisations are explicit. A boost is

$$
\tilde{\Lambda}_{\text{boost}} = \gamma^0 \cdot v, \qquad v = \gamma^0\tilde{\Lambda}_{\text{boost}} ,
$$

where $v$ is the **boosted time axis**: the boost is the reflection in the resting time axis composed with the reflection in the moving one. A spatial rotation in the coordinate plane spanned by $\gamma^j$ and $\gamma^k$ is $\gamma^j\cdot v$ with $v$ a unit vector in that plane,

$$
v = -\cos\frac{\theta}{2}\,\gamma^j + \sin\frac{\theta}{2}\,\gamma^k , \qquad v^2 = -I_4 ,
$$

so that $\gamma^j v = \cos\frac{\theta}{2}I_4 + \sin\frac{\theta}{2}\gamma^j\gamma^k$. A generic Lorentz transformation fixes no plane at all — a boost and a rotation in non-parallel planes destroy every fixed direction — so by Cartan–Dieudonné it requires four reflections, the maximum. In these factorisations $u$ and $v$ are unit vectors in the Clifford sense, $u^2 = \pm I_4$; the generators $\Phi(ie_k)$ themselves have $N = -1$ and are not rotors, the rotors being their exponentials.

So the answer to the question is: **pure boosts and pure spatial rotations are products of two reflections; a generic Lorentz transformation is not, and needs four.** The set of transformations admitting a two-reflection form is exactly the set fixing a plane, a proper submanifold of $SL(2,\mathbb{C})$ — the Thomas–Wigner rotation of a general composed boost is what carries a transformation out of it.

## Why Chirality Needs a Reflection

The chirality operator of the series is

$$
\gamma_5 = i_{\mathrm{Cl}}\,\omega = -\Phi_{\mathbb{C}}\!\left(i_{\mathrm{Cl}}i\right),
$$

with $\omega = \gamma^0\gamma^1\gamma^2\gamma^3$ the pseudoscalar and $i_{\mathrm{Cl}}$ the unit of the complexification; its projectors are the central idempotents $\frac{1}{2}(1\pm\gamma_5)$, of rank $2$ each. The relation to the frame is the anticommutation

$$
\gamma_5\,\gamma^\mu = -\,\gamma^\mu\,\gamma_5 ,
$$

from which the whole chirality behaviour follows. Every **even** element commutes with $\gamma_5$, so an even element maps each chiral half into itself; every **odd** element anticommutes with it — vectors and trivectors alike, hence every odd element — so an odd element exchanges the halves:

$$
\gamma^\mu P_+ = P_-\,\gamma^\mu .
$$

Combine this with the grading of the second section and the statement is: **rotations preserve chirality, reflections reverse it.** A rotation cannot change which chiral half a spinor belongs to, and a reflection always does. Chirality is not an extra label attached to the spinor; it is the eigenvalue of the operator that tells the two halves of the algebra apart, and only the odd half moves it.

The representation-theoretic form of the same fact is the split of the complexified Lorentz algebra,

$$
\mathfrak{so}(1,3)_{\mathbb{C}} \cong \mathfrak{su}(2)\oplus\mathfrak{su}(2),
$$

under which a representation is labelled by a pair $(j_1,j_2)$. The rotations and boosts act within each factor, and chirality is *which* factor:

| object | label | chirality |
|---|---|---|
| scalar | $(0,0)$ | in neither factor; no chirality label exists |
| left Weyl spinor | $(\tfrac12,0)$ | in the first factor alone |
| right Weyl spinor | $(0,\tfrac12)$ | in the second factor alone |
| vector | $(\tfrac12,\tfrac12)$ | in both factors equally |

This is the precise sense in which chirality is tied to spin $\tfrac12$: the two Weyl spinors are the two smallest nontrivial modules of the two factors, and "left-handed" *means* "$(\tfrac12,0)$". A scalar carries no chirality because it sits in neither factor, and a vector is chirality-blind because it sits in both equally. The link between spin $\tfrac12$ and chirality is not a coincidence to be explained; they are the two coordinates of one label.

The exchange of the two factors is an orientation-reversing operation, which is why it takes a reflection. **Parity is exactly that reflection.** It fixes the time direction and reverses the three spatial ones, and it exchanges the two spinor modules,

$$
\Pi : (\tfrac12,0) \longleftrightarrow (0,\tfrac12),
$$

verified at the level of the projectors as $\gamma^0P_+ = P_-\gamma^0$. Parity violation — the statement that the weak interaction couples to one chirality and not the other — is therefore not an accidental property of the Standard Model but the statement that the interaction distinguishes the two factors of $\mathfrak{su}(2)\oplus\mathfrak{su}(2)$. This is what *Chiral Fermions in the Biquaternion Framework* and *The Neutrino and Majorana Fermions in Biquaternionic Form* develop on the physical side.

One corollary concerns the mass. The mass term of the series is linear and chirality-off-diagonal; being even, $m$ itself commutes with $\gamma_5$ and does not flip chirality. What the mass does is *couple* the two chiral equations, so that chirality ceases to be conserved — it permits the flip, while the generators perform it. A massive fermion therefore has no definite chirality, which is the operator-level content of the standard statement that chirality and helicity agree only in the massless limit.

## Why the Pauli Algebra Cannot Carry Chirality

The non-relativistic limit of the Dirac equation is governed by the Pauli matrices, and it is natural to ask whether chirality could have been discussed there. It could not, and the reason is algebraic and exact.

The Pauli matrices generate $\mathrm{Cl}(3)$, whose volume element is

$$
\sigma_1\sigma_2\sigma_3 = i\,I_2 ,
$$

a **central** element of $M_2(\mathbb{C})$ that squares to $-1$. A chirality grading requires an element $\Gamma$ with $\Gamma^2 = +1$ that *anticommutes* with every generator, so that the two eigenspaces of $\Gamma$ are exchanged by the generators and can be called the two chiralities. In $\mathrm{Cl}(3)$ there is no such element at all: the only matrix anticommuting with all three Pauli matrices is zero. The natural candidate, the volume element, fails twice over — it is central, so it commutes rather than anticommutes, and it squares to $-1$ rather than $+1$. Its formal projectors $\frac{1}{2}(1\pm iI_2)$ would in any case be scalar matrices and not idempotent. Equivalently, $M_2(\mathbb{C})$ is simple: its only central elements are multiples of the identity, and they give no nontrivial idempotent. The Pauli algebra has no grading, hence nowhere to put a chirality. The obstruction is not a matter of ingenuity.

The Dirac algebra escapes it because it has **one more generator**, and that generator is timelike. The chirality operator contains all four,

$$
\gamma_5 = i_{\mathrm{Cl}}\gamma^0\gamma^1\gamma^2\gamma^3 ,
$$

and there is no way to form it from three. The timelike direction is not an optional extra; it is the ingredient that makes the grading exist. Chirality is therefore intrinsically relativistic: it is defined for a massless relativistic particle, mass mixes chirality with helicity, and only in the non-relativistic limit does the distinction collapse into the spin that the Pauli algebra describes. The same conclusion follows from the label table above, since the split $\mathfrak{su}(2)\oplus\mathfrak{su}(2)$ is a property of the complexified *Lorentz* algebra, which the spatial rotation algebra does not possess.

## Summary

The claims of this article, in order.

1. **One algebra, two readings.** The biquaternion algebra is a matrix algebra, so each element is at once a point of a transformation group and an operator. The rotors are the even instances; the generator $\gamma^\mu$ is the odd one, and the even and odd instances act on the spinor module in opposite ways.

2. **The grading is the reflection count.** By Cartan–Dieudonné, an orthogonal transformation is a product of reflections and its determinant is $(-1)^{\text{count}}$. The split $\mathrm{Cl}_{1,3} = \mathrm{Cl}_{1,3}^{+}\oplus\mathrm{Cl}_{1,3}^{-}$ is that parity. Verified: even unit elements act with determinant $+1$, odd ones with $-1$.

3. **The frame and the metric.** Every vector is $\gamma^0\Phi(w)$ with $w\in\mathbb{M}_+$, and $\Phi(\mathbb{M}_+)$ is the identity together with the timelike bivectors — the boost sector. The norm form on the Hermitian basis is $g = \mathrm{diag}(+1,-1,-1,-1)$, and on the material basis $\eta = -g$. The Clifford metric is the norm form of the objects the generators represent, so the mostly-minus convention is forced rather than chosen.

4. **Conjugation by $\gamma^0$ is complex conjugation.** $\gamma^0\Phi(\tilde{Q})\gamma^0 = \Phi(\tilde{Q}^*)$, the sector-exchanging conjugation. Together with reversal, which is quaternion conjugation, it composes into $\dagger$. The real structure $\flat = -\dagger$ therefore carries the frame within it.

5. **Rotations and reflections have different spaces.** The rotations are the unit-norm biquaternions, a group of dimension $6$ with the bivectors as Lie algebra. The reflections are the odd unit elements, a single coset of dimension $3$ organised by their $\mathbb{M}_+$ normals, not a group. Together they are $\mathrm{Pin}(1,3)$. **Anti-linear maps shift the correspondence by one:** their determinant carries an extra $-1$, so an even internal matrix acts as a reflection and an odd one as a proper transformation — which is how $T$ (even) is a reflection while $C$ (odd) is not.

6. **Two reflections, or four.** A rotation is a product of two reflections exactly when it fixes a plane — equivalently, when a certain $4\times 4$ determinant vanishes. Pure boosts and pure spatial rotations qualify; a generic boost-plus-rotation does not, and needs four.

7. **Chirality is what the reflection changes.** Even elements commute with $\gamma_5$, odd ones anticommute, so rotations preserve chirality and reflections reverse it. In the split $\mathfrak{so}(1,3)_{\mathbb{C}}\cong\mathfrak{su}(2)\oplus\mathfrak{su}(2)$, chirality is which factor, and the exchange of the factors is parity.

8. **Chirality is relativistic.** The Pauli algebra $\mathrm{Cl}(3)\cong M_2(\mathbb{C})$ is simple, its volume element is central and squares to $-1$, and it admits no nontrivial grading. The grading requires the timelike generator.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $\mathrm{Cl}_{1,3}$, $\mathrm{Cl}_{1,3}^{\pm}$ | Clifford algebra and its even/odd parts |
| $\Phi$ | Isomorphism $\mathbb{B}\to\mathrm{Cl}_{1,3}^{+}$, $\Phi(e_0) = I_4$, $\Phi(i) = -\omega$ |
| $g = \mathrm{diag}(+1,-1,-1,-1)$ | Clifford metric of the generators |
| $\eta = \mathrm{diag}(-1,+1,+1,+1) = -g$ | $ict$ metric of the material coordinates |
| $\omega = \gamma^0\gamma^1\gamma^2\gamma^3$ | Pseudoscalar, $\omega^2 = -I_4$ |
| $\gamma_5 = i_{\mathrm{Cl}}\omega$ | Chirality operator, $\gamma_5^2 = I_4$ |
| $P_\pm = \tfrac12(1\pm\gamma_5)$ | Chirality projectors, rank $2$ |
| $\gamma^0$ | The frame; the reflection whose normal is $e_0$ |
| $\rho(u) : x\mapsto -uxu^{-1}$ | Pin action of an odd unit element |
| $\mathrm{rev}(\Phi(\tilde{Q})) = \Phi(\bar{\tilde{Q}})$ | Clifford reversal is quaternion conjugation |
| $\Phi(\tilde{Q}^\dagger) = \gamma^0\mathrm{rev}(\Phi(\tilde{Q}))\gamma^0$ | Hermitian conjugation |
| $\gamma^0\Phi(\tilde{Q})\gamma^0 = \Phi(\tilde{Q}^*)$ | Conjugation by the frame is complex conjugation |
| $\tilde{\Lambda}$, $N(\tilde{\Lambda}) = 1$ | Rotor, unit-norm biquaternion; $SL(2,\mathbb{C})$ |
| $\tilde{X}' = \tilde{\Lambda}\tilde{X}\tilde{\Lambda}^\dagger$ | Rotor conjugation on $\mathbb{M}_-$ |
| $\mathbb{M}_+$ | Hermitian sector; $\Phi(\mathbb{M}_+)$ = identity + timelike bivectors (boosts) |
| $\mathbb{H}_{\mathbb{B}}$ | Real-quaternion sector; $\Phi(\mathbb{H}_{\mathbb{B}})$ = identity + spacelike bivectors (spatial rotations) |
| $\det M$ | Two-reflection criterion: $\det M = 0$ iff $\tilde{\Lambda}$ fixes a plane |
| $\det = (-1)^{k}(-1)^{\text{anti}}$ | Reflection parity of a module map, linear or anti-linear |
| $\Pi$ | Parity reflection; exchanges the two chiral halves |

## Further Reading

- Companion articles in this series: *The Dirac Algebra and Biquaternions — A Dictionary* (the isomorphism $\Phi$, the sign conventions, and the chirality operator used throughout); *The Dirac Equation in Biquaternionic Form* (the linear, chirality-off-diagonal mass term); *The Spinor Module in Biquaternionic Form and Its Lorentz Action* (the module, the one-sided spinor action, and the two factors $\mathfrak{su}(2)\oplus\mathfrak{su}(2)$); *Exercise: Chirality and the Weyl Spinors* (the projectors and the two Weyl modules); *The Lorentz Transformation as a Biquaternionic Rotation* (the boost rotor, its Hermiticity, and the rotor conjugation); *The Lorentz Group in Biquaternionic Form — Structure and Representations*; *Exercise: The Thomas Precession* (the composition of non-collinear boosts); *Exercise: Boosting a Four-Velocity and Rapidity Composition*.
- On the physics of chirality: *Chiral Fermions in the Biquaternion Framework*; *The Neutrino and Majorana Fermions in Biquaternionic Form*; *The CPT Theorem in Biquaternionic Form* (the anti-linear discrete symmetries of the last subsection); *Zitterbewegung in Biquaternionic Form* (the mass as the coupling between the chiralities); *Exercise: The Non-Relativistic Limit and the Pauli Equation* (the reduction to the Pauli algebra).
- Foundational articles: *Introduction to the Biquaternion Universe*; *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*; *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*; *Conventions in the Biquaternion Universe*.
- On the Clifford structures used here: *Clifford Algebras*; *Clifford Algebras in finite dimensions*; *Spinors*; *The Spinor Representation of the Lorentz Group in Biquaternionic Form*.
