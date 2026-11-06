# __The Reflection and the Rotation in Biquaternionic Form__

## Introduction

A **cell** multiplies on the left by one element and on the right by another, with the composition that *Matrix Representations Conventions* fixes. A cell is an element of the array algebra that acts on $\mathbb{B}$, so it is at once an object and an operator: an object of the arrays, an operator on the biquaternions.

This article is about a structure of the cell algebra which the relativistic articles use and none names: the split between the cells that carry an even number of **generator factors** and those that carry an odd number, and the identification of one cell, the frame cell $iR_{\mathrm{axf},\vec e_x}$, as the hinge on which the split turns. The frame cells are the four legs of spacetime read as operators, and *Matrix Representations Conventions* lists them and records that the time one is a single right multiplication.

The claim is short. **The even half is the biquaternion algebra itself.** Its rotors are the elements of unit norm, the points of $SL(2,\mathbb{C})$, and they act on four-vectors by conjugation. The four generators are odd, none of them is a rotor, and each of them carries an element of one part into the other part. The split is therefore not a bookkeeping device: it is the split between the transformations that *turn* and those that *reflect*, and the letter $L$ or $R$ of an element is what an odd cell exchanges and an even cell keeps.

The article runs as follows. §*One Cell, Two Readings* separates the cell read as a point from the cell read as an operator. §*The Two Halves by Reflection Count* states the split and ties it to the parity of the number of reflections. §*The Frame Cell and the Hermitian Sector* shows that the sign vector of the cells is the biquaternion norm of the Hermitian sector, which is what makes the mostly-minus metric of the series a statement about the objects rather than a choice. §*Conjugation by the Frame Cell Is the Bar* shows that conjugation by the frame cell is the conjugation of the coefficients. §*The Spaces of Rotations and of Reflections* and §*How Many Reflections?* describe the two sets and count the reflections a transformation needs. §*The Two Parts and the Reflection* draws the consequence for the letter, and §*Why Three Generators Cannot Carry the Letter* shows that the timelike generator is what makes the letter exist.

The conventions are the series'. The algebra, the units, the sectors and the metric are those of *Algebra and Element Conventions* and *Frame and Metric Conventions*; the cells and their multiplication are those of *Matrix Representations Conventions*, and the comparison of the biquaternion algebra with the even half is the dictionary of the same article. None of them is restated here. A cell enters by its two multipliers, and the short names used later — the frame cell, the chirality cell, $\omega$, the three $\eta$ factors — are bound to those multipliers where they are introduced; no cell is named without its product being written at least once. The derivatives are the series' gradient, written once here and never as a cell,
$$
\tilde\nabla=\sum_{\mu\in\{t,x,y,z\}}e_\mu\frac{\partial}{\partial R_\mu},\qquad
\tilde\nabla^{\natural}=\sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu e_\mu\frac{\partial}{\partial R_\mu},\qquad
\Box=\tilde\nabla\tilde\nabla^{\natural}=\frac{\partial^2}{\partial R_t^2}+\Delta_Q,
$$
with $\varepsilon=(1,-1,-1,-1)$, and on the material sector $\partial/\partial R_t=-(i/c)\,\partial/\partial r'_t$, so that there $\Box=\Delta_Q-c^{-2}\partial^2/\partial r'_t^2$. No cell of this article carries a derivative.

## One Cell, Two Readings

A cell of a matrix algebra is at once a point and an operator, and the quaternions show the doubling most plainly: a unit quaternion is a point of the three-sphere and it is also the rotation that acts on vectors by conjugation. The same element, read two ways.

**The rotors.** A Lorentz rotor $\tilde U_{\mathrm{lor}}$ of unit norm, $\langle\tilde U_{\mathrm{lor}}\rangle_{\natural}=1$, is a point of $SL(2,\mathbb{C})$, the double cover of the restricted Lorentz group, and it is an operator on the algebra,
$$
Q_2 = \tilde U_{\mathrm{lor}}\,Q\,\tilde U_{\mathrm{lor}}{}^{*},
$$
which is the Lorentz transformation of the material element $Q\in\mathbb{M}_-$. For a pure boost the rotor is Hermitian, $\tilde U_{\mathrm b}^{*}=\tilde U_{\mathrm b}$, and the action collapses to $Q_2=\tilde U_{\mathrm b}Q\tilde U_{\mathrm b}$; a general element of $SL(2,\mathbb{C})$ needs the general form. Both facts are those of *The Lorentz Transformation as a Biquaternionic Rotation*.

**The generators.** A generator cell is a vector and an operator at once: one of the four legs of spacetime, read as a cell. The four are
$$
iR_{\mathrm{axf},\vec e_x},\qquad
iL_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},\vec e_y},\qquad
iL_{\mathrm{axf},\vec e_y}R_{\mathrm{axf},\vec e_y},\qquad
iL_{\mathrm{axf},\vec e_z}R_{\mathrm{axf},\vec e_y}
$$

For the rotors the doubling is familiar, since the same element is the transformation and the operator that applies it. For the generators it is not familiar, and the reason is the parity of the number of generator factors. An even cell, applied on the left, keeps the letter of the element; a generator exchanges it. So two operators of one algebra, both acting on the same elements, do qualitatively different things, and the remainder of the article is the elaboration of that sentence.

**The odd action.** An odd unit cell is a reflection, and it acts on the vector cells twice-sidedly,
$$
\rho(u) : x \mapsto -\,\epsilon(u)\,u\,x\,u, \qquad u\ \text{odd},\quad u^2 = \epsilon(u)\,I_4,\quad \epsilon(u)=\pm1 .
$$
A unit vector is its own inverse up to sign: $u^2=\epsilon(u)I_4$ makes the inverse $\epsilon(u)u$, so the formula needs the cell product and the sign of the normal and nothing else. The minus sign is what makes the map a reflection: $x\mapsto u\,x\,u^{-1}$ already fixes the direction of $u$ and negates the vectors orthogonal to it, so its negative fixes the hyperplane orthogonal to $u$ and reverses the normal. The sign $\epsilon(u)$ records whether the normal is timelike, $\epsilon=+1$, or spacelike, $\epsilon=-1$.

## The Two Halves by Reflection Count

The theorem of Cartan and Dieudonné states that every orthogonal transformation of a non-degenerate space is a product of reflections in hyperplanes. In dimension $n$ at most $n$ of them are needed, and the determinant of the transformation is $(-1)^k$, where $k$ is the number of reflections in any factorisation. Two remarks follow, and together they are the content of this section.

First, **the parity of the count is the determinant**. An even number of reflections gives a proper transformation, an odd number an orientation-reversing one. In four dimensions with the Lorentzian signature a single reflection is parity, time reversal or an axis flip, and two reflections give a proper transformation whose time orientation depends on the normals: it is orthochronous when both normals are timelike or both spacelike, and it reverses time when one is timelike and the other spacelike, as $\mathrm{diag}(-1,-1,+1,+1)$ does for the normals $e_t$ and $\vec e_x$.

Second, and this is the point, **the parity of the count is the split of the cells**. Every cell carries a right multiplier, and the sixteen cells separate by it: eight have right multiplier $e_t$ or $\vec e_z$ and eight have $\vec e_x$ or $\vec e_y$. The first eight span a closed subalgebra; the second eight span a subspace of the same dimension that is not closed. A generator has a right multiplier $\vec e_x$ or $\vec e_y$, and multiplication by either of the two exchanges the two spans, since the right multiplier of a product is the product of the two multipliers in the reverse order, and $e_t\vec e_x=\vec e_x$, $\vec e_z\vec e_x=\vec e_y$, $e_t\vec e_y=\vec e_y$, $\vec e_z\vec e_y=-\vec e_x$. So a product of an even number of generators lies in the first eight and a product of an odd number in the second.

The first eight are exactly the image of the biquaternion algebra under the comparison of *Matrix Representations Conventions*. That comparison is $\mathbb{R}$-linear and not $\mathbb{C}$-linear: a factor $i$ multiplying a biquaternion becomes a right multiplication, not a multiplication of the cell by the scalar $i$. Everything the comparison produces is even, so the rotations sit inside $\mathbb{B}$ and the reflections do not.

The correspondence between the parity and the determinant is exact, and not a counting resemblance:

| element of $\mathbb{B}$ or cell | generator factors | determinant of the action on vectors | in $\mathbb{B}$? |
|---|---|---|---|
| a rotor $\tilde U_{\mathrm{lor}}$ of unit norm | an even number | $+1$ | yes |
| an odd unit cell: a generator, a unit vector, a trivector | an odd number | $-1$ | no |

The Lie algebra of the rotations is generated by the bivectors, and a bivector is the product of two reflections. So the two halves of the algebra of the cells are the two classes of orthogonal transformations, and the correspondence is an identity.

## The Frame Cell and the Hermitian Sector

The odd half is reached from the even half by multiplying by the time generator, which is the frame cell $iR_{\mathrm{axf},\vec e_x}$: that cell times the image of $\mathbb{M}_+$ is the vector space and times the image of $\mathbb{M}_-$ the trivector space, as *Matrix Representations Conventions* records. The four generators are therefore the Hermitian basis read through the frame cell, and a statement about the generators is a statement about that basis.

Two derived forms are used below, both read off the frame cells at the place of use. A vector cell is the frame cell applied after the image of $w\in\mathbb{M}_+$,
$$
w = q_t e_t + i q_x\vec e_x + i q_y\vec e_y + i q_z\vec e_z ,
\qquad
iR_{\mathrm{axf},\vec e_x}\times(\text{image of } w) = q_t\, iR_{\mathrm{axf},\vec e_x} + \sum_k q_k\, iL_{\mathrm{axf},\vec e_k}R_{\mathrm{axf},\vec e_y} ,
$$
and a trivector is the frame cell applied after the image of an element of $\mathbb{M}_-$, up to a sign that depends on the orientation chosen for each trivector.

The decisive consequence concerns the **metric**. The biquaternion norm is the sum of the four squared coefficients, and a coefficient $i$ contributes $i^2=-1$. On the Hermitian basis $(e_t,i\vec e_x,i\vec e_y,i\vec e_z)$ it therefore takes the four values $(+1,-1,-1,-1)$, which is the plain weight $\varepsilon$; on the material basis $(ie_t,\vec e_x,\vec e_y,\vec e_z)$ it takes $(-1,+1,+1,+1)$, which is the interval of the material sector. The minus signs of the first list are those of $i^2$ on the three spatial directions, and nothing else. The sign vector of the generators is therefore not an independent convention laid on top of the algebra: **it is the biquaternion norm of the Hermitian sector**, and the interval of the material sector is its negative. The material basis carries $(-1,+1,+1,+1)$ and the generators, which are Hermitian objects, carry the weight $\varepsilon$, which is its negative; the two differ by the sign that distinguishes the two sectors, and neither could consistently be anything else.

The same fact appears in the square of a vector. For $w$ as above,
$$
\Bigl(q_t\, iR_{\mathrm{axf},\vec e_x} + \sum_k q_k\, iL_{\mathrm{axf},\vec e_k}R_{\mathrm{axf},\vec e_y}\Bigr)^2
= \bigl(q_t^2 - q_x^2 - q_y^2 - q_z^2\bigr)\,I_4 ,
$$
with no relative sign between the square of the cell and the biquaternion norm. The absence of that sign is the signature showing through.

## Conjugation by the Frame Cell Is the Bar

The frame cell is not a bookkeeping element. It has a definite action on the algebra, and that action is what defines the split $\mathbb{B}=\mathbb{H}_{\mathbb{B}}\oplus i\mathbb{H}_{\mathbb{B}}$.

For every element $\tilde Q$,
$$
\boxed{\;iR_{\mathrm{axf},\vec e_x}\times\bigl(\text{image of }\tilde{Q}\bigr)\times iR_{\mathrm{axf},\vec e_x} = \text{image of }\bar{\tilde{Q}}\;}
$$
where $\bar{\tilde Q}$ is the conjugation of the coefficients, $i\mapsto -i$, with the units $e_t,\vec e_x,\vec e_y,\vec e_z$ fixed. That map fixes $\mathbb{H}_{\mathbb{B}}$ and negates $i\mathbb{H}_{\mathbb{B}}$, so the identity says that **conjugation by the frame cell is the bar**: it is the spacetime-side avatar of the split into the quaternion sector and its imaginary multiple. It preserves each of the two sectors, because it commutes with the Hermitian conjugation whose fixed spaces they are; the sector exchange is multiplication by $i$, not a conjugation.

Among the four generators, the frame cell is unique in being the bar itself. Conjugation by any of the four reverses the imaginary cell, since the image of $i$ is $L_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_z}$ and every generator anticommutes with it, so all four carry the scalar imaginary $i$ to $-i$ and act on the biquaternions as conjugate-linear maps rather than $\mathbb{C}$-linear ones. Only the time one leaves the quaternion units alone. Conjugation by a spatial generator is the bar composed with a sign change of two units: it fixes $\vec e_k$ and negates the two units $\vec e_j$ with $j\neq k$, and the bar then flips the imaginary multiples the other way round. The spatial generators reflect the quaternion units; the time one conjugates them without a reflection.

The frame cell completes the reading of the three conjugations of $\mathbb{B}$, and the three can be written together. Reversal, $\mathrm{rev}$, is the anti-automorphism that reverses the order of the factors in a product: on an array it is the transpose, and on the biquaternions it is quaternion conjugation. The image does not carry one of the two into the other, because it sends the scalar $i$ to a right multiplication rather than to a scalar, and the frame cell is exactly the difference. Of the three conjugations, the bar and the quaternion conjugation each carry one factor of the frame, and the composite carries none:
$$
\text{image of }\bar{\tilde Q}=iR_{\mathrm{axf},\vec e_x}\times\bigl(\text{image of }\tilde{Q}\bigr)\times iR_{\mathrm{axf},\vec e_x},
$$
$$
\text{image of }\tilde{Q}^{\natural}=iR_{\mathrm{axf},\vec e_x}\times\mathrm{rev}\bigl(\text{image of }\tilde{Q}\bigr)\times iR_{\mathrm{axf},\vec e_x},
\qquad
\boxed{\;\text{image of }\tilde{Q}^{*}=\mathrm{rev}\bigl(\text{image of }\tilde{Q}\bigr)\;}
$$
The Hermitian conjugation is therefore the bar composed with the quaternion conjugation, which is the algebra's own identity and not an accident of the frame; and in the array the two frame factors cancel, because the square of the frame cell is $I_4$.

That cancellation is the point, and it bears on the mass. The real structure of the algebra is $\flat=-{}^{*}$, and it is the bare reversal: no frame enters it. The frame sits one level up, in the two factors of the Hermitian conjugation — the bar is a conjugation by the frame cell, and the quaternion conjugation is that same conjugation composed with the bare reversal — and it is because the two factors of the frame cancel that a formulation written in terms of $\flat$ alone never shows it. The linear mass term of *The Dirac Equation in Biquaternionic Form* displays it openly instead. This is an observation about how the frame is packaged, not a derivation; it is stated because it is the reason the frame is easy to overlook.

## The Spaces of Rotations and of Reflections

With the split in hand, the two sets can be described, and they are not of the same kind.

**The rotations.** The rotors are the unit-norm biquaternions,
$$
SL(2,\mathbb{C}) = \{\tilde U_{\mathrm{lor}}\in\mathbb{B} : \langle\tilde U_{\mathrm{lor}}\rangle_{\natural} = 1\},
$$
a group of real dimension six, the double cover of the restricted Lorentz group. The sign of the norm is the time orientation: an even unit element with $\langle\tilde U\rangle_{\natural}=+1$ is orthochronous, and one with $\langle\tilde U\rangle_{\natural}=-1$ reverses time, which is why the group defined here is the restricted one. Its Lie algebra is spanned by the six bivectors, the images of the six directions $\vec e_k$ and $i\vec e_k$, $k=1,2,3$. This is the space in which the rotors of the relativity articles live and act: on four-vectors in *Relativistic Mechanics in Biquaternionic Form* and *Exercise: Boosting a Four-Velocity and Rapidity Composition*, on the elements in *The Spinor Module in Biquaternionic Form and Its Lorentz Action*, on states in *Quantum Physics in Biquaternionic Form*, and in the composition of rotations of *Exercise: The Thomas Precession*.

Two subfamilies are worth separating, because the series uses them differently:

| subfamily | condition | biquaternion form | character |
|---|---|---|---|
| spatial rotations | $\tilde u_{\mathrm r}$ a real quaternion | $\cos\frac{\theta}{2} + \sin\frac{\theta}{2}\vec u_{jk}$ | the group $SU(2)$ |
| pure boosts | $\tilde U_{\mathrm b}$ Hermitian, $\tilde U_{\mathrm b}^{*} = \tilde U_{\mathrm b}$ | $\cosh\frac{\theta_{\mathrm{rpd}}}{2} + i\sinh\frac{\theta_{\mathrm{rpd}}}{2}\vec u$ | a symmetric submanifold, not a group |

The boosts do not close under multiplication — the product of two non-collinear boosts is a boost and a Thomas–Wigner rotation — so they form a submanifold of $SL(2,\mathbb{C})$ rather than a subgroup. The two families are the exponentials of the two sector algebras: the boosts of elements of $\mathbb{M}_+$, namely the timelike bivectors $i\vec u$, and the spatial rotations of elements of $\mathbb{H}_{\mathbb{B}}$, namely the spacelike bivectors $\vec u_{jk}$.

**The reflections.** A reflection is an odd cell of unit norm, and its data is its **normal**, a unit vector. Writing the vectors as the frame cell applied after the image of $w$ with $w\in\mathbb{M}_+$, the unit normals are those $w$ of norm $+1$ or $-1$, the timelike ones for $\langle w\rangle_{\natural}=+1$ and the spacelike ones for $\langle w\rangle_{\natural}=-1$. The canonical reflection is the frame cell itself, and its normal is the time axis: the vector cell $iR_{\mathrm{axf},\vec e_x}$ is the frame cell applied to the image of $e_t$, which is the identity cell $L_{\mathrm{axf},e_t}R_{\mathrm{axf},e_t}$.

The reflections do **not** form a group, and this is the sharp difference from the rotations. The product of two reflections is even, a proper transformation, so the set is not closed. The reflections lie in a single coset of the rotation group and split into two orbits, one of timelike normals and one of spacelike normals; a product of one of each is even with norm $-1$, which is the component that reverses time. Their dimension is three, the dimension of the unit quadric, against the six of the rotations. The two sets together are $\mathrm{Pin}(1,3)$, whose even part is $\mathrm{Spin}(1,3)=SL(2,\mathbb{C})$. The relation between the two sets is generation: the rotations are the products of an even number of reflections, and the bivectors that generate the Lorentz algebra are the products of two.

The reflections account for the four components of the full Lorentz group, and the timelike and the trivector normals give the two classical ones. The action of the frame cell, whose normal is timelike, is time reversal,
$$
\rho(iR_{\mathrm{axf},\vec e_x}) : x \mapsto -\,iR_{\mathrm{axf},\vec e_x}\,x\,iR_{\mathrm{axf},\vec e_x} = \mathrm{diag}(-1,+1,+1,+1).
$$
Parity is not that map but the action of the trivector in the direction $ie_t$, the product of the three spatial generators,
$$
u = iL_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},\vec e_y}\,iL_{\mathrm{axf},\vec e_y}R_{\mathrm{axf},\vec e_y}\,iL_{\mathrm{axf},\vec e_z}R_{\mathrm{axf},\vec e_y}, \qquad u^2=I_4, \qquad \rho(u) : x \mapsto -\,u\,x\,u = \mathrm{diag}(+1,-1,-1,-1).
$$
Both are reflections, with determinant $-1$; the identity component is the even half, and the discrete symmetries are the reflections.

**The anti-linear case.** The rule just stated — even cells act with determinant $+1$, odd ones with $-1$ — holds for the **linear** action. The discrete operations of the Dirac field are not all linear: $C$ and $T$ are **anti-linear**, and each carries an internal factor. *The CPT Theorem in Biquaternionic Form* fixes the three,
$$
\eta_C=-L_{\mathrm{axf},\vec e_y}R_{\mathrm{axf},\vec e_y},\qquad \eta_P=iR_{\mathrm{axf},\vec e_x},\qquad \eta_T=-L_{\mathrm{axf},\vec e_y} ,
$$
acting as $C[\tilde{Ξ}_{\mathrm{sp}}]=\eta_C\tilde{Ξ}_{\mathrm{sp}}^*$, $P[\tilde{Ξ}_{\mathrm{sp}}]=\eta_P\tilde{Ξ}_{\mathrm{sp}}(-\vec r)$ and $T[\tilde{Ξ}_{\mathrm{sp}}]=\eta_T\tilde{Ξ}_{\mathrm{sp}}^*(-r'_t)$, with $\tilde{Ξ}_{\mathrm{sp}}^*$ the Hermitian conjugate. The internal factor does not decide the determinant by itself:

| operation | internal factor | its generator factors | coordinates reversed | determinant | induced map |
|---|---|---|---|---|---|
| $P$ | $\eta_P=iR_{\mathrm{axf},\vec e_x}$, the frame cell | odd | $\vec r$ | $-1$ | reflection |
| $T$ | $\eta_T=-L_{\mathrm{axf},\vec e_y}$ | even | $r'_t$ | $-1$ | reflection |
| $C$ | $\eta_C=-L_{\mathrm{axf},\vec e_y}R_{\mathrm{axf},\vec e_y}$ | odd | none | $+1$ | proper |

$P$ and $T$ each reverse one coordinate and are reflections; $C$ reverses none and is proper. What the parity of the factor decides is not the determinant but the letter, since the letter is read from the chirality cell: the odd factors $\eta_C$ and $\eta_P$ exchange the two parts, while the even factor $\eta_T$ keeps them. The composite $CPT$ carries an even factor and preserves the letter, which is the statement of the CPT article.

A single rule reproduces the determinant column: the parity of the factor contributes $(-1)^{k}$, with $k$ its number of generator factors, and the anti-linearity another $-1$,
$$
\det = (-1)^{k}\,(-1)^{\text{anti}} .
$$
It is a bookkeeping statement of an inversion, not a derivation. Its content is negative and worth stating plainly: for a **linear** map the parity is the reflection count, and for an **anti-linear** one it is not — the two columns are offset by one, and the even factor $\eta_T$ is the reflection while the odd factor $\eta_C$ is not.

## How Many Reflections?

The theorem gives an upper bound of four reflections in four dimensions. The sharper question — given a rotation, how many reflections does it take — has a clean answer, and it separates the simple Lorentz transformations from the generic ones.

A product of two reflections is a cell $uv$, with $u$ and $v$ unit vector cells. It is the product of two odd cells, hence even, hence the image of an element $\tilde U_{\mathrm{lor}}$; from here the image of an element is written as the element, and a product of a cell with it is the cell product. The criterion is algebraic. The product $u\tilde U_{\mathrm{lor}}$ has a vector part and a trivector part, and the trivector part is *linear* in $u$. So the condition that $u\tilde U_{\mathrm{lor}}$ be a vector — that is, that $\tilde U_{\mathrm{lor}}$ be $u$ times a vector — is a system of four linear conditions on the four components of $u$, and it has a nonzero solution exactly when their determinant vanishes:
$$
\tilde U_{\mathrm{lor}} = uv \ \text{for unit vectors}\ u,v
\quad\Longleftrightarrow\quad
u\tilde U_{\mathrm{lor}}\ \text{is a vector for some}\ u\neq 0
\quad\Longleftrightarrow\quad
\text{the four conditions are dependent}.
$$
Geometrically the criterion is that **$\tilde U_{\mathrm{lor}}$ fixes a two-dimensional subspace pointwise**, since a product of two reflections is the identity on the plane orthogonal to the span of $u$ and $v$. In the cells the same determinant vanishes exactly when the bivector part of $\tilde U_{\mathrm{lor}}$ is the product of two vectors, and the solutions $u$ are then the vectors of the plane they span; a plane in Lorentzian four-space always contains a non-null vector, so a nonzero solution can be rescaled to a unit normal. The three forms of the criterion agree: the determinant vanishes exactly when the fixed subspace has dimension two.

| transformation | the four conditions | fixed subspace | reflections needed |
|---|---|---|---|
| pure boost | dependent | dimension two | two |
| pure spatial rotation | dependent | dimension two | two |
| boost along $\vec e_x$ with a rotation in the $xy$ plane | dependent | dimension two | two |
| boost along $\vec e_x$ with a rotation about $\vec e_x$ | independent | dimension zero | four |

The rule the table obeys is geometric: the transformation is simple exactly when the **boost plane and the rotation plane share a direction**. A pure boost or a pure rotation carries one plane, so the condition is empty; a boost with a rotation in the plane of the boost shares the boost direction; a boost with a rotation about the boost axis shares nothing.

The factorisations are explicit. The image of a boost is the frame cell times a unit vector,
$$
\text{image of }\tilde U_{\mathrm b} = iR_{\mathrm{axf},\vec e_x}\,v ,
$$
where $v$ is the unit vector cell whose coordinates in the generator basis $(iR_{\mathrm{axf},\vec e_x},iL_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},\vec e_y},iL_{\mathrm{axf},\vec e_y}R_{\mathrm{axf},\vec e_y},iL_{\mathrm{axf},\vec e_z}R_{\mathrm{axf},\vec e_y})$ are
$$
\Bigl(\cosh\frac{\theta_{\mathrm{rpd}}}{2},\ \sinh\frac{\theta_{\mathrm{rpd}}}{2}u_x,\ \sinh\frac{\theta_{\mathrm{rpd}}}{2}u_y,\ \sinh\frac{\theta_{\mathrm{rpd}}}{2}u_z\Bigr),
$$
the time axis boosted by **half** the rapidity. The boost is therefore the reflection in the resting time axis composed with the reflection in the moving one, and the half is what makes the two rapidities add to $\theta_{\mathrm{rpd}}$.

A spatial rotation in the plane spanned by two spatial generators is $iL_{\mathrm{axf},\vec e_j}R_{\mathrm{axf},\vec e_y}\,v$ with the vector cell
$$
v = -\cos\frac{\theta}{2}\,iL_{\mathrm{axf},\vec e_j}R_{\mathrm{axf},\vec e_y} + \sin\frac{\theta}{2}\,iL_{\mathrm{axf},\vec e_k}R_{\mathrm{axf},\vec e_y} , \qquad v^2 = -I_4 ,
$$
so that
$$
iL_{\mathrm{axf},\vec e_j}R_{\mathrm{axf},\vec e_y}\,v = \cos\frac{\theta}{2}\,I_4 + \sin\frac{\theta}{2}\,iL_{\mathrm{axf},\vec e_j}R_{\mathrm{axf},\vec e_y}\,iL_{\mathrm{axf},\vec e_k}R_{\mathrm{axf},\vec e_y} .
$$
For the plane $(x,y)$ the right-hand side is the image of $\cos\frac{\theta}{2}e_t+\sin\frac{\theta}{2}\vec e_z$, the rotation about $\vec e_z$, and the other coordinate planes follow by relabelling. A generic Lorentz transformation fixes no plane at all, so it needs four reflections, the maximum.

The answer to the question is therefore: **pure boosts and pure spatial rotations are products of two reflections, and so is a boost with a rotation in the plane of the boost; a generic Lorentz transformation is not, and needs four.** The two-reflection class is a proper submanifold of $SL(2,\mathbb{C})$, cut out by the vanishing of that determinant. The product of two non-collinear boosts stays inside it — the Thomas–Wigner rotation of a composed boost lies in the plane of the two boosts — so what leaves the class is a boost combined with a rotation about the boost axis, that is, a boost and a rotation in orthogonal planes.

## The Two Parts and the Reflection

The cell that separates the two parts of an element is the chirality cell of the frame, the product of the four generators,
$$
-iR_{\mathrm{axf},\vec e_z} = i\,\omega , \qquad
\omega = iR_{\mathrm{axf},\vec e_x}\,iL_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},\vec e_y}\,iL_{\mathrm{axf},\vec e_y}R_{\mathrm{axf},\vec e_y}\,iL_{\mathrm{axf},\vec e_z}R_{\mathrm{axf},\vec e_y} = -L_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_z} ,
$$
where the four scalar factors of $\omega$ multiply to $i^4=1$, so that $\omega$ is a pure product of cells. That product is the pseudoscalar of the frame, $\omega^2=-I_4$, and the chirality cell is a single right multiplication whose square is $I_4$.

**The letter.** An element is $L$ when the chirality cell gives it the value $-1$, and $R$ when it gives $+1$. That is the whole definition. The two values are exactly two, and only the zero element is both. The letter belongs to the object and not to a state, so a product, a unit and a field carry it as well, and the two parts of a field are written $\tilde{Ξ}_{\mathrm{sp},L}$ and $\tilde{Ξ}_{\mathrm{sp},R}$.

**Which cells keep it and which exchange it.** A cell acts through its right multiplier: a product takes the letter of its right factor, and left multiplication keeps the letter of its operand. Every even cell has right multiplier $e_t$ or $\vec e_z$ and keeps the letter. Every generator has right multiplier $\vec e_x$ or $\vec e_y$ and exchanges it, so a generator carries the $R$ part into the $L$ part and the $L$ part into the $R$ part.

Combined with the split established above, the statement is: **rotations keep the letter and reflections exchange it.** A rotation cannot change which part an element belongs to, and a reflection always does. The letter is not an extra label attached to the element; it is the value of the cell that tells the two parts apart, and only the odd half moves it.

The mass is where the two parts are coupled, and the coupling is the chiral pair of *The Dirac Equation in Biquaternionic Form*,
$$
\tilde\nabla\tilde{Ξ}_{\mathrm{sp},R} = m\tilde{Ξ}_{\mathrm{sp},L} , \qquad \tilde\nabla^{\natural}\tilde{Ξ}_{\mathrm{sp},L} = m\tilde{Ξ}_{\mathrm{sp},R} ,
$$
in which every derivative is the gradient and acts by left multiplication. The pair is written once as an operator on the direct sum $\mathbb{B}\oplus\mathbb{B}$,
$$
\tilde{Ξ}_{\mathrm{sp}}=(\tilde{Ξ}_{\mathrm{sp},L},\tilde{Ξ}_{\mathrm{sp},R}),\qquad
\mathbb{D}\tilde{Ξ}_{\mathrm{sp}}=\bigl(\tilde\nabla\tilde{Ξ}_{\mathrm{sp},R},\ \tilde\nabla^{\natural}\tilde{Ξ}_{\mathrm{sp},L}\bigr),
$$
and the massive equation is $(\mathbb{D}-m)\tilde{Ξ}_{\mathrm{sp}}=0$. The pair operator is **off-diagonal in the two slots**: the first slot of the output is filled from the second slot of the input and the second from the first, and no slot is filled from itself. The subscripts name the two slots, not a value that the operator computes: the gradient acts by left multiplication, a left multiplier does not touch the letter, and the term that carries a field from one letter to the other is therefore the mass, which is the only such term. The mass is a multiple of the identity on the sum, central and even, and it moves nothing by itself. The square is scalar because each member is a gradient followed by its conjugate,
$$
\mathbb{D}^2\tilde{Ξ}_{\mathrm{sp}}=\bigl(\tilde\nabla\tilde\nabla^{\natural}\tilde{Ξ}_{\mathrm{sp},L},\ \tilde\nabla^{\natural}\tilde\nabla\tilde{Ξ}_{\mathrm{sp},R}\bigr)=\Box\,\tilde{Ξ}_{\mathrm{sp}} ,
$$
with $\Box=\Delta_Q-c^{-2}\partial^2/\partial r'_t^2$ on the material sector, so that $(\mathbb{D}-m)(\mathbb{D}+m)=\Box-m^2$ is the Klein–Gordon operator exactly, with no overall sign left to fix.

The consequence is immediate. Set $\tilde{Ξ}_{\mathrm{sp},R}=0$ in a massive field: the first member reads $0=m\tilde{Ξ}_{\mathrm{sp},L}$, so $\tilde{Ξ}_{\mathrm{sp},L}=0$ as well, and a massive field carries both parts. A field of one letter alone is not a solution. At $m=0$ the pair decouples into $\tilde\nabla\tilde{Ξ}_{\mathrm{sp},R}=0$ and $\tilde\nabla^{\natural}\tilde{Ξ}_{\mathrm{sp},L}=0$, one member for each part, so a field of one part alone is allowed. That decoupling is the operator-level content of the statement that the letter and the helicity agree only in the massless limit.

The representation-theoretic form of the same fact is the split of the complexified Lorentz algebra into two copies of $\mathfrak{sl}(2,\mathbb{C})$, each of them the complexification of an $\mathfrak{su}(2)$,
$$
\mathfrak{so}(1,3)_{\mathbb{C}} \cong \mathfrak{sl}(2,\mathbb{C})\oplus\mathfrak{sl}(2,\mathbb{C}),
$$
under which a finite-dimensional representation is labelled by a pair $(j_1,j_2)$. The rotations and the boosts act within each copy, and the letter is *which* copy:

| object | label | letter |
|---|---|---|
| a scalar | $(0,0)$ | in neither copy; no letter exists |
| $\tilde{Ξ}_{\mathrm{sp},L}$ | $(\tfrac12,0)$ | in the first copy alone |
| $\tilde{Ξ}_{\mathrm{sp},R}$ | $(0,\tfrac12)$ | in the second copy alone |
| a vector | $(\tfrac12,\tfrac12)$ | in both copies equally |

This is the precise sense in which the letter is tied to spin $\tfrac12$: the two parts are the two smallest nontrivial representations of the two copies, and $L$ *means* $(\tfrac12,0)$. A scalar has no letter because it sits in neither copy, and a vector is blind to it because it sits in both equally. The link is not a coincidence to be explained: each part is a minimal representation of one copy, and the cell is what tells the two copies apart.

The exchange of the two copies is an orientation-reversing operation, which is why it takes a reflection. **Parity is exactly that reflection.** It fixes the time direction and reverses the three spatial ones, and it exchanges the two parts,
$$
\mathsf{P} : (\tfrac12,0) \longleftrightarrow (0,\tfrac12).
$$
It is odd in both readings: the trivector $iL_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},\vec e_y}\,iL_{\mathrm{axf},\vec e_y}R_{\mathrm{axf},\vec e_y}\,iL_{\mathrm{axf},\vec e_z}R_{\mathrm{axf},\vec e_y}$ for the geometric reflection, the internal factor $\eta_P=iR_{\mathrm{axf},\vec e_x}$ for the parity of the Dirac field. Every odd cell carries the $R$ part into the $L$ part, so the exchange of the parts is the parity.

Parity violation — the statement that the weak interaction couples to one part and not the other — is therefore not an accidental property of the Standard Model but the statement that the interaction distinguishes the two copies of the complexified Lorentz algebra. This is what *Chiral Fermions in the Biquaternion Framework* and *The Neutrino and Majorana Fermions in Biquaternionic Form* develop on the physical side.

## Why Three Generators Cannot Carry the Letter

The non-relativistic limit keeps three directions and drops the time generator, and it is natural to ask whether the letter could have been defined there. It could not, and the reason is algebraic and exact.

Take the algebra generated by the three spatial generators, $iL_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},\vec e_y}$, $iL_{\mathrm{axf},\vec e_y}R_{\mathrm{axf},\vec e_y}$, $iL_{\mathrm{axf},\vec e_z}R_{\mathrm{axf},\vec e_y}$. Their product is odd, it squares to $+I_4$, and it commutes with all three:
$$
\bigl(iL_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},\vec e_y}\;iL_{\mathrm{axf},\vec e_y}R_{\mathrm{axf},\vec e_y}\;iL_{\mathrm{axf},\vec e_z}R_{\mathrm{axf},\vec e_y}\bigr)^2 = I_4 .
$$
A cell that commutes with the three generators multiplies each of the two irreducible pieces they act on by a scalar, so it separates the elements into two halves that the three generators never mix. That is a copy index of the algebra, and not the letter: the letter must be a value that the *odd* cells exchange, and a cell that commutes with them cannot supply one.

The other half of the argument is the same statement read backwards. A cell that all three generators exchange must anticommute with all three, and the algebra of the three contains no such cell: its even part is spanned by the identity and the three products of two generators, a product of two anticommutes with the two it carries and commutes with the third, so a combination that anticommuted with all three would have to vanish. The odd part contains the triple product, which commutes. There is nowhere to put the letter.

The fourth generator is what supplies it. **The chirality cell is the product of all four generators**, and it is even. The timelike direction is therefore not an optional extra; it is the ingredient that makes the two parts exist. The two values are intrinsically relativistic: four generators carry them, three cannot, and the non-relativistic limit keeps only the spin.

## Summary

The claims of this article, in order.

1. **One algebra, two readings.** A cell is an object of the arrays and an operator on the algebra. The rotors are the even cells; the four frame cells are the odd ones. An even cell keeps the letter of the element it acts on, an odd cell exchanges it.

2. **The parity is the reflection count.** By Cartan–Dieudonné an orthogonal transformation is a product of reflections and its determinant is $(-1)^{\text{count}}$. The split of the cells by their right multiplier — eight with $e_t$ or $\vec e_z$, eight with $\vec e_x$ or $\vec e_y$ — is that parity, and the first eight are the image of $\mathbb{B}$.

3. **The frame and the signs.** Every vector is the frame cell applied after the image of $w\in\mathbb{M}_+$. The biquaternion norm on the Hermitian basis is $(+1,-1,-1,-1)$, its minus signs being those of $i^2$, and on the material basis it is $(-1,+1,+1,+1)$. The sign vector of the generators is the biquaternion norm of the objects they represent, so the mostly-minus convention is forced rather than chosen.

4. **Conjugation by the frame cell is the bar.** The frame cell is the bar, and the bar composed with the reversal is the quaternion conjugation. The two frame factors cancel in the Hermitian conjugation, so the real structure $\flat=-{}^{*}$ is the bare reversal and carries no frame.

5. **Rotations and reflections have different spaces.** The rotations are the unit-norm biquaternions, a group of dimension six with the bivectors as Lie algebra. The reflections are the odd unit cells, two orbits of dimension three organised by their normals, and not a group. Together they are $\mathrm{Pin}(1,3)$. Anti-linear maps shift the correspondence by one: an even internal factor belongs to a reflection and an odd one to a proper transformation, which is how $T$ is a reflection while $C$ is not.

6. **Two reflections, or four.** A rotation is a product of two reflections exactly when it fixes a plane. Pure boosts, pure spatial rotations and boosts with a rotation in the plane of the boost qualify; a boost with a rotation about the boost axis does not, and needs four.

7. **The letter is what the reflection changes.** Even cells keep the letter, odd cells exchange it, so rotations preserve the two parts and reflections reverse them. The mass is even and central and couples the two parts without moving either; the pair operator $\mathbb{D}$ is off-diagonal in the two slots, and the mass is the one term that carries a field from one letter to the other. In the split $\mathfrak{so}(1,3)_{\mathbb{C}}\cong\mathfrak{sl}(2,\mathbb{C})\oplus\mathfrak{sl}(2,\mathbb{C})$ the letter is which copy, and the exchange of the copies is parity.

8. **The letter is relativistic.** Three generators cannot carry it: their product is central, and no cell of their algebra anticommutes with all three. The chirality cell is the product of all four generators and is even, so it exists only because one generator is timelike.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| even half, odd half | The cells with an even and with an odd number of generator factors; the even half is the image of $\mathbb{B}$ |
| $\varepsilon=(+1,-1,-1,-1)$ | Sign vector of the four generators: the biquaternion norm on the Hermitian basis |
| $\langle\tilde Q\rangle_\natural$, $Q_t=i c r'_t$ | Minkowski interval of the material coordinates, signature $(3,1)$ |
| $L_{a}R_{b}$ | Left multiplication $L_a$ and right multiplication $R_b$: $L_{a}R_{b}\tilde{Ξ}_{\mathrm{sp}} = a\tilde{Ξ}_{\mathrm{sp}} b$, $L_{a}R_{b}L_{c}R_{d} = L_{ac}R_{db}$ |
| image of $\tilde Q$ | The $\mathbb{R}$-linear comparison with the even half, per *Matrix Representations Conventions*; named, never written as a symbol |
| the four frame cells | The generator cells: $iR_{\mathrm{axf},\vec e_x}$, and $iL_{\mathrm{axf},\vec e_k}R_{\mathrm{axf},\vec e_y}$ for $k=1,2,3$ |
| $\omega = iR_{\mathrm{axf},\vec e_x}\,iL_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},\vec e_y}\,iL_{\mathrm{axf},\vec e_y}R_{\mathrm{axf},\vec e_y}\,iL_{\mathrm{axf},\vec e_z}R_{\mathrm{axf},\vec e_y} = -L_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_z}$ | Pseudoscalar, $\omega^2 = -I_4$; its four factors of $i$ multiply to $i^4=1$ |
| $-iR_{\mathrm{axf},\vec e_z} = i\omega = -iL_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_z}$ | Chirality cell, $(-iR_{\mathrm{axf},\vec e_z})^{2} = I_4$ |
| the $L$ part, the $R$ part | The two parts of an element: the value $-1$ and the value $+1$ of the chirality cell |
| $\tilde{Ξ}_{\mathrm{sp},L,R}$ | The two parts of a field |
| $\tilde\nabla$, $\tilde\nabla^{\natural}$ | The biquaternion gradient $\sum_\mu e_\mu\partial/\partial R_\mu$ and its quaternion conjugate $\sum_\mu\varepsilon_\mu e_\mu\partial/\partial R_\mu$; $\Box=\tilde\nabla\tilde\nabla^{\natural}=\partial^2/\partial R_t^2+\Delta_Q$; the chiral pair $\tilde\nabla\tilde{Ξ}_{\mathrm{sp},R}=m\tilde{Ξ}_{\mathrm{sp},L}$, $\tilde\nabla^{\natural}\tilde{Ξ}_{\mathrm{sp},L}=m\tilde{Ξ}_{\mathrm{sp},R}$, whose subscripts name the two members |
| $\mathbb{D}$ | The pair operator on $\mathbb{B}\oplus\mathbb{B}$, $\mathbb{D}(\tilde{Ξ}_{\mathrm{sp},L},\tilde{Ξ}_{\mathrm{sp},R})=(\tilde\nabla\tilde{Ξ}_{\mathrm{sp},R},\tilde\nabla^{\natural}\tilde{Ξ}_{\mathrm{sp},L})$; $\mathbb{D}^2=\Box I$, off-diagonal in the two slots |
| $iR_{\mathrm{axf},\vec e_x}$ | The frame cell; the reflection whose normal is $e_t$ |
| $\rho(u) : x\mapsto -\epsilon(u)\,u x u$ | Action of an odd unit cell on the vectors; $u^2=\epsilon(u)I_4$ |
| Reversal $\mathrm{rev}$ | The anti-automorphism that reverses the order of the factors; on an array it is the transpose, and on the biquaternions it is quaternion conjugation |
| Frame conjugation | Conjugating the image of $\tilde{Q}$ by $iR_{\mathrm{axf},\vec e_x}$ gives the image of $\bar{\tilde{Q}}$ |
| Hermitian conjugation | The image of $\tilde{Q}^{*}$ is the reversed image of $\tilde{Q}$, that is its transpose; $*$ is the bar composed with $\natural$, and the two frame factors cancel |
| $\tilde U_{\mathrm{lor}}$, $\langle\tilde U_{\mathrm{lor}}\rangle_{\natural} = 1$ | Rotor, unit-norm biquaternion; $SL(2,\mathbb{C})$ |
| $\tilde{Q}_2 = \tilde U_{\mathrm{lor}}\tilde{Q}\tilde U_{\mathrm{lor}}{}^{*}$ | Rotor conjugation on $\mathbb{M}_-$ |
| $\mathbb{M}_+$ | Hermitian sector; its image is the identity together with the timelike bivectors (boosts) |
| $\mathbb{H}_{\mathbb{B}}$ | Real-quaternion sector; its image is the identity together with the spacelike bivectors (spatial rotations) |
| the four conditions | Two-reflection criterion: they are dependent iff $\tilde U_{\mathrm{lor}}$ fixes a plane pointwise |
| $\det = (-1)^{k}(-1)^{\text{anti}}$ | Reflection parity of a linear or anti-linear map |
| $\mathsf{P}$ | Parity reflection; the trivector cell $iL_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},\vec e_y}\,iL_{\mathrm{axf},\vec e_y}R_{\mathrm{axf},\vec e_y}\,iL_{\mathrm{axf},\vec e_z}R_{\mathrm{axf},\vec e_y}$; exchanges the two parts |
| $\eta_P = iR_{\mathrm{axf},\vec e_x}$ | The internal factor of the parity of the Dirac field; odd, so it carries the $R$ part into the $L$ part |

## Further Reading

- Companion articles in this series: [Matrix Representations Conventions](matrix-representations-conventions.html) (the Clifford reading, the sign conventions, and the chirality operator used throughout, §*The Clifford Structure*); [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html) (the chiral pair, the two-sided form and the mass); [The Spinor Module in Biquaternionic Form and Its Lorentz Action](the-spinor-module-in-biquaternionic-form-and-its-lorentz-action.html) (the module, the one-sided spinor action, and the two factors $\mathrm{SU}(2)\oplus\mathrm{SU}(2)$); [Exercise: Chirality and the Weyl Spinors](exercise-chirality-and-the-weyl-spinors.html) (the projectors and the two Weyl modules); [The Lorentz Transformation as a Biquaternionic Rotation](the-lorentz-transformation-as-a-biquaternionic-rotation.html) (the boost rotor, its Hermiticity, and the rotor conjugation); [The Lorentz Group in Biquaternionic Form — Structure and Representations](the-lorentz-group-in-biquaternionic-form-structure-and-representations.html); [Exercise: The Thomas Precession](exercise-the-thomas-precession.html) (the composition of non-collinear boosts); [Exercise: Boosting a Four-Velocity and Rapidity Composition](exercise-boosting-a-four-velocity-and-rapidity-composition.html).
- On the physics of chirality: [Chiral Fermions in the Biquaternion Framework](chiral-fermions-in-the-biquaternion-framework.html); [The Neutrino and Majorana Fermions in Biquaternionic Form](the-neutrino-and-majorana-fermions-in-biquaternionic-form.html); [The CPT Theorem in Biquaternionic Form](the-cpt-theorem-in-biquaternionic-form.html) (the anti-linear discrete symmetries of the last subsection); [Zitterbewegung in Biquaternionic Form](zitterbewegung-in-biquaternionic-form.html) (the mass as the coupling between the chiralities); [Exercise: The Non-Relativistic Limit and the Pauli Equation](exercise-the-non-relativistic-limit-and-the-pauli-equation.html) (the reduction to the Pauli algebra).
- Foundational articles: [Introduction to the Biquaternion Universe](introduction-to-the-biquaternion-universe.html); [The Material Sector: Four-Vectors, Interval and Lorentz Action](the-material-sector-four-vectors-interval-and-lorentz-action.html); [The Informational Sector: States, Observables and Probability](the-informational-sector-states-observables-and-probability.html); [Algebra and Element Conventions](algebra-and-element-conventions.html).
- On the Clifford structures used here: [Clifford Algebras](../articles_maths/clifford-algebras.html); [Two-Sided Operators on a Clifford Algebra](../articles_maths/two-sided-operators-on-a-clifford-algebra.html) (the cell algebra, its two closures, and the frame); *Clifford Algebras in finite dimensions*; *Spinors*; [The Spinor Representation of the Lorentz Group in Biquaternionic Form](the-spinor-representation-of-the-lorentz-group-in-biquaternionic-form.html).

