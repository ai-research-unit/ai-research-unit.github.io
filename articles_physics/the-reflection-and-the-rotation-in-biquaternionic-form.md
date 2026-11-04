# __The Reflection and the Rotation in Biquaternionic Form__

## Introduction

A **cell** multiplies on the left by one element and on the right by another, with the composition that *Matrix Representations Conventions* fixes. The sixteen cells of the four units span the algebra of the complex four-by-four arrays, so a cell is at once an object of that algebra and an operator on it.

This article is about a structure of that algebra which the relativistic articles use and none names: the split between the cells that carry an even number of **generator factors** and those that carry an odd number, and the identification of one cell, the frame cell $iR_{\vec e_x}^{\mathrm{axf}}$, as the hinge on which the split turns. The frame cells are the four legs of spacetime read as operators, and *Matrix Representations Conventions* lists them and records that the time one is a single right multiplication.

The claim is short. **The even half is the biquaternion algebra itself.** Its rotors are the elements of unit norm, the points of $SL(2,\mathbb{C})$, and they act on four-vectors by conjugation. The four generators are odd, none of them is a rotor, and each of them carries an element of one part into the other part. The split is therefore not a bookkeeping device: it is the split between the transformations that *turn* and those that *reflect*, and the letter $L$ or $R$ of an element is what an odd cell exchanges and an even cell keeps.

The article runs as follows. §*One Cell, Two Readings* separates the cell read as a point from the cell read as an operator. §*The Two Halves by Reflection Count* states the split and ties it to the parity of the number of reflections. §*The Frame Cell and the Hermitian Sector* shows that the sign vector of the cells is the biquaternion norm of the Hermitian sector, which is what makes the mostly-minus metric of the series a statement about the objects rather than a choice. §*Conjugation by the Frame Cell Is the Bar* shows that conjugation by the frame cell is the conjugation of the coefficients. §*The Spaces of Rotations and of Reflections* and §*How Many Reflections?* describe the two sets and count the reflections a transformation needs. §*The Two Parts and the Reflection* draws the consequence for the letter, and §*Why Three Generators Cannot Carry the Letter* shows that the timelike generator is what makes the letter exist. The closing §*The Legacy Pauli Gamma Formulation* translates the results into the notation of the literature, and it is the only section of the article that uses it.

The conventions are the series'. The algebra, the units, the sectors and the metric are those of *Algebra and Element Conventions* and *Frame Conventions*; the cells and their multiplication are those of *Matrix Representations Conventions*, and the comparison of the biquaternion algebra with the even half is the dictionary of the same article. None of them is restated here. A cell is written by its two multipliers throughout, and no letter stands for one.

## One Cell, Two Readings

A cell of a matrix algebra is at once a point and an operator, and the quaternions show the doubling most plainly: a unit quaternion is a point of the three-sphere and it is also the rotation that acts on vectors by conjugation. The same element, read two ways.

**The rotors.** A Lorentz rotor $\tilde U^{\mathrm{lor}}$ of unit norm, $\langle\tilde U^{\mathrm{lor}}\rangle_{\natural}=1$, is a point of $SL(2,\mathbb{C})$, the double cover of the restricted Lorentz group, and it is an operator on the algebra,
$$
Q_2 = \tilde U^{\mathrm{lor}}\,Q\,\tilde U^{\mathrm{lor}}{}^{*},
$$
which is the Lorentz transformation of the material element $Q\in\mathbb{M}_-$. For a pure boost the rotor is Hermitian, $\tilde U_{\mathrm b}^{*}=\tilde U_{\mathrm b}$, and the action collapses to $Q_2=\tilde U_{\mathrm b}Q\tilde U_{\mathrm b}$; a general element of $SL(2,\mathbb{C})$ needs the general form. Both facts are those of *The Lorentz Transformation as a Biquaternionic Rotation*.

**The generators.** A generator cell is a vector and an operator at once: one of the four legs of spacetime, read as a cell. The four are
$$
iR_{\vec e_x}^{\mathrm{axf}},\qquad
iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\qquad
iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\qquad
iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}
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
| a rotor $\tilde U^{\mathrm{lor}}$ of unit norm | an even number | $+1$ | yes |
| an odd unit cell: a generator, a unit vector, a trivector | an odd number | $-1$ | no |

The Lie algebra of the rotations is generated by the bivectors, and a bivector is the product of two reflections. So the two halves of the algebra of the cells are the two classes of orthogonal transformations, and the correspondence is an identity.

## The Frame Cell and the Hermitian Sector

The odd half is reached from the even half by multiplying by the time generator, which is the frame cell $iR_{\vec e_x}^{\mathrm{axf}}$: that cell times the image of $\mathbb{M}_+$ is the vector space and times the image of $\mathbb{M}_-$ the trivector space, as *Matrix Representations Conventions* records. The four generators are therefore the Hermitian basis read through the frame cell, and a statement about the generators is a statement about that basis.

Two derived forms are used below, both read off the frame cells at the place of use. A vector cell is the frame cell applied after the image of $w\in\mathbb{M}_+$,
$$
w = x_t e_t + i x_x\vec e_x + i x_y\vec e_y + i x_z\vec e_z ,
\qquad
iR_{\vec e_x}^{\mathrm{axf}}\times(\text{image of } w) = x_t\, iR_{\vec e_x}^{\mathrm{axf}} + \sum_k x_k\, iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}} ,
$$
and a trivector is the frame cell applied after the image of an element of $\mathbb{M}_-$, up to a sign that depends on the orientation chosen for each trivector.

The decisive consequence concerns the **metric**. The biquaternion norm is the sum of the four squared coefficients, and a coefficient $i$ contributes $i^2=-1$. On the Hermitian basis $(e_t,i\vec e_x,i\vec e_y,i\vec e_z)$ it therefore takes the four values $(+1,-1,-1,-1)$, which is $-g_{\mu\nu}[\mathbb{M}_-]$; on the material basis $(ie_t,\vec e_x,\vec e_y,\vec e_z)$ it takes $(-1,+1,+1,+1)$, which is $g_{\mu\nu}[\mathbb{M}_-]$. The minus signs of the first list are those of $i^2$ on the three spatial directions, and nothing else. The sign vector of the generators is therefore not an independent convention laid on top of the algebra: **it is the biquaternion norm of the Hermitian sector**, and the $ict'$ metric of the material sector is its negative. The material basis carries $g_{\mu\nu}[\mathbb{M}_-]$ and the generators, which are Hermitian objects, carry its negative; the two differ by the sign that distinguishes the two sectors, and neither could consistently be anything else.

The same fact appears in the square of a vector. For $w$ as above,
$$
\Bigl(x_t\, iR_{\vec e_x}^{\mathrm{axf}} + \sum_k x_k\, iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\Bigr)^2
= \bigl(x_t^2 - x_x^2 - x_y^2 - x_z^2\bigr)\,I_4 ,
$$
with no relative sign between the square of the cell and the biquaternion norm. The absence of that sign is the signature showing through.

## Conjugation by the Frame Cell Is the Bar

The frame cell is not a bookkeeping element. It has a definite action on the algebra, and that action is what defines the split $\mathbb{B}=\mathbb{H}_{\mathbb{B}}\oplus i\mathbb{H}_{\mathbb{B}}$.

For every element $\tilde Q$,
$$
\boxed{\;iR_{\vec e_x}^{\mathrm{axf}}\times\bigl(\text{image of }\tilde{Q}\bigr)\times iR_{\vec e_x}^{\mathrm{axf}} = \text{image of }\bar{\tilde{Q}}\;}
$$
where $\bar{\tilde Q}$ is the conjugation of the coefficients, $i\mapsto -i$, with the units $e_t,\vec e_x,\vec e_y,\vec e_z$ fixed. That map fixes $\mathbb{H}_{\mathbb{B}}$ and negates $i\mathbb{H}_{\mathbb{B}}$, so the identity says that **conjugation by the frame cell is the bar**: it is the spacetime-side avatar of the split into the quaternion sector and its imaginary multiple. It preserves each of the two sectors, because it commutes with the Hermitian conjugation whose fixed spaces they are; the sector exchange is multiplication by $i$, not a conjugation.

Among the four generators, the frame cell is unique in being the bar itself. Conjugation by any of the four reverses the imaginary cell, since the image of $i$ is $L_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$ and every generator anticommutes with it, so all four carry the scalar imaginary $i$ to $-i$ and act on the biquaternions as conjugate-linear maps rather than $\mathbb{C}$-linear ones. Only the time one leaves the quaternion units alone. Conjugation by a spatial generator is the bar composed with a sign change of two units: it fixes $\vec e_k$ and negates the two units $\vec e_j$ with $j\neq k$, and the bar then flips the imaginary multiples the other way round. The spatial generators reflect the quaternion units; the time one conjugates them without a reflection.

The frame cell completes the reading of the three conjugations of $\mathbb{B}$, and the three can be written together. Reversal, the anti-automorphism that reverses the order of the factors in a product, acts on the biquaternions as quaternion conjugation; the frame cell acts as the bar; and the composite is the Hermitian conjugation,
$$
\text{image of }\tilde{Q}^{\natural}=\mathrm{rev}\bigl(\text{image of }\tilde{Q}\bigr),
$$
$$
\text{image of }\bar{\tilde Q}=iR_{\vec e_x}^{\mathrm{axf}}\times\bigl(\text{image of }\tilde{Q}\bigr)\times iR_{\vec e_x}^{\mathrm{axf}},
\qquad
\boxed{\;\text{image of }\tilde{Q}^{*}=iR_{\vec e_x}^{\mathrm{axf}}\times\mathrm{rev}\bigl(\text{image of }\tilde{Q}\bigr)\times iR_{\vec e_x}^{\mathrm{axf}}\;}
$$
The Hermitian conjugation is therefore the bar composed with the quaternion conjugation, which is the algebra's own identity and not an accident of the frame.

One consequence is worth recording, because it bears on the mass. The real structure of the algebra is the anti-Hermitian conjugation $\flat=-{}^{*}$, and the display shows that the frame cell is *inside* it: the frame, with its bar and its reflection properties, is one of the two ingredients of $\flat$. A formulation of the mass built on $\flat$ therefore carries the frame, but as a reality condition rather than as a generator; the linear mass term of *The Dirac Equation in Biquaternionic Form* displays it openly instead. This is an observation about how the frame is packaged, not a derivation; it is stated because it is the reason the frame is easy to overlook.

## The Spaces of Rotations and of Reflections

With the split in hand, the two sets can be described, and they are not of the same kind.

**The rotations.** The rotors are the unit-norm biquaternions,
$$
SL(2,\mathbb{C}) = \{\tilde U^{\mathrm{lor}}\in\mathbb{B} : \langle\tilde U^{\mathrm{lor}}\rangle_{\natural} = 1\},
$$
a group of real dimension six, the double cover of the restricted Lorentz group. The sign of the norm is the time orientation: an even unit element with $\langle\tilde U\rangle_{\natural}=+1$ is orthochronous, and one with $\langle\tilde U\rangle_{\natural}=-1$ reverses time, which is why the group defined here is the restricted one. Its Lie algebra is spanned by the six bivectors, the images of the six directions $\vec e_k$ and $i\vec e_k$, $k=1,2,3$. This is the space in which the rotors of the relativity articles live and act: on four-vectors in *Relativistic Mechanics in Biquaternionic Form* and *Exercise: Boosting a Four-Velocity and Rapidity Composition*, on the elements in *The Spinor Module in Biquaternionic Form and Its Lorentz Action*, on states in *Quantum Physics in Biquaternionic Form*, and in the composition of rotations of *Exercise: The Thomas Precession*.

Two subfamilies are worth separating, because the series uses them differently:

| subfamily | condition | biquaternion form | character |
|---|---|---|---|
| spatial rotations | $\tilde u_{\mathrm r}$ a real quaternion | $\cos\frac{\theta}{2} + \sin\frac{\theta}{2}\vec u_{jk}$ | the group $SU(2)$ |
| pure boosts | $\tilde U_{\mathrm b}$ Hermitian, $\tilde U_{\mathrm b}^{*} = \tilde U_{\mathrm b}$ | $\cosh\frac{\psi}{2} + i\sinh\frac{\psi}{2}\vec u$ | a symmetric submanifold, not a group |

The boosts do not close under multiplication — the product of two non-collinear boosts is a boost and a Thomas–Wigner rotation — so they form a submanifold of $SL(2,\mathbb{C})$ rather than a subgroup. The two families are the exponentials of the two sector algebras: the boosts of elements of $\mathbb{M}_+$, namely the timelike bivectors $i\vec u$, and the spatial rotations of elements of $\mathbb{H}_{\mathbb{B}}$, namely the spacelike bivectors $\vec u_{jk}$.

**The reflections.** A reflection is an odd cell of unit norm, and its data is its **normal**, a unit vector. Writing the vectors as the frame cell applied after the image of $w$ with $w\in\mathbb{M}_+$, the unit normals are those $w$ of norm $+1$ or $-1$, the timelike ones for $\langle w\rangle_{\natural}=+1$ and the spacelike ones for $\langle w\rangle_{\natural}=-1$. The canonical reflection is the frame cell itself: its normal is the identity of the cells, $L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$, which is the image of $e_t$ and a timelike unit vector.

The reflections do **not** form a group, and this is the sharp difference from the rotations. The product of two reflections is even, a proper transformation, so the set is not closed. The reflections lie in a single coset of the rotation group and split into two orbits, one of timelike normals and one of spacelike normals; a product of one of each is even with norm $-1$, which is the component that reverses time. Their dimension is three, the dimension of the unit quadric, against the six of the rotations. The two sets together are $\mathrm{Pin}(1,3)$, whose even part is $\mathrm{Spin}(1,3)=SL(2,\mathbb{C})$. The relation between the two sets is generation: the rotations are the products of an even number of reflections, and the bivectors that generate the Lorentz algebra are the products of two.

The reflections account for the four components of the full Lorentz group, and the timelike and the trivector normals give the two classical ones. The action of the frame cell, whose normal is timelike, is time reversal,
$$
\rho(iR_{\vec e_x}^{\mathrm{axf}}) : x \mapsto -\,iR_{\vec e_x}^{\mathrm{axf}}\,x\,iR_{\vec e_x}^{\mathrm{axf}} = \mathrm{diag}(-1,+1,+1,+1).
$$
Parity is not that map but the action of the trivector in the direction $ie_t$, the product of the three spatial generators,
$$
u = iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\,iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\,iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}, \qquad u^2=I_4, \qquad \rho(u) : x \mapsto -\,u\,x\,u = \mathrm{diag}(+1,-1,-1,-1).
$$
Both are reflections, with determinant $-1$; the identity component is the even half, and the discrete symmetries are the reflections.

**The anti-linear case.** The rule just stated — even cells act with determinant $+1$, odd ones with $-1$ — holds for the **linear** action. The discrete operations of the Dirac field are not all linear: $C$ and $T$ are **anti-linear**, and each carries an internal factor. *The CPT Theorem in Biquaternionic Form* fixes the three,
$$
\eta_C=-L_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\qquad \eta_P=iR_{\vec e_x}^{\mathrm{axf}},\qquad \eta_T=-L_{\vec e_y}^{\mathrm{axf}} ,
$$
acting as $C[\tilde\Psi]=\eta_C\tilde\Psi^{*}$, $P[\tilde\Psi]=\eta_P\tilde\Psi(-\vec x)$ and $T[\tilde\Psi]=\eta_T\tilde\Psi^{*}(-t')$, with $\tilde\Psi^{*}$ the Hermitian conjugate. The internal factor does not decide the determinant by itself:

| operation | internal factor | its generator factors | coordinates reversed | determinant | induced map |
|---|---|---|---|---|---|
| $P$ | $\eta_P=iR_{\vec e_x}^{\mathrm{axf}}$ | odd | $\vec x$ | $-1$ | reflection |
| $T$ | $\eta_T=-L_{\vec e_y}^{\mathrm{axf}}$ | even | $t'$ | $-1$ | reflection |
| $C$ | $\eta_C=-L_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$ | odd | none | $+1$ | proper |

$P$ and $T$ each reverse one coordinate and are reflections; $C$ reverses none and is proper. What the parity of the factor decides is not the determinant but the letter, since the letter is read from the chirality cell: the odd factors $\eta_C$ and $\eta_P$ exchange the two parts, while the even factor $\eta_T$ keeps them. The composite $CPT$ carries an even factor and preserves the letter, which is the statement of the CPT article.

A single rule reproduces the determinant column: the parity of the factor contributes $(-1)^{k}$, with $k$ its number of generator factors, and the anti-linearity another $-1$,
$$
\det = (-1)^{k}\,(-1)^{\text{anti}} .
$$
It is a bookkeeping statement of an inversion, not a derivation. Its content is negative and worth stating plainly: for a **linear** map the parity is the reflection count, and for an **anti-linear** one it is not — the two columns are offset by one, and the even factor $\eta_T$ is the reflection while the odd factor $\eta_C$ is not.

## How Many Reflections?

The theorem gives an upper bound of four reflections in four dimensions. The sharper question — given a rotation, how many reflections does it take — has a clean answer, and it separates the simple Lorentz transformations from the generic ones.

A product of two reflections is an element $\tilde U^{\mathrm{lor}} = uv$ with $u$ and $v$ unit vectors. The criterion is algebraic. The product $u\tilde U^{\mathrm{lor}}$ has a vector part and a trivector part, and the trivector part is *linear* in $u$. So the condition that $u\tilde U^{\mathrm{lor}}$ be a vector — that is, that $\tilde U^{\mathrm{lor}}$ be $u$ times a vector — is a system of four linear conditions on the four components of $u$, and it has a nonzero solution exactly when their determinant vanishes:
$$
\tilde U^{\mathrm{lor}} = uv \ \text{for unit vectors}\ u,v
\quad\Longleftrightarrow\quad
u\tilde U^{\mathrm{lor}}\ \text{is a vector for some}\ u\neq 0
\quad\Longleftrightarrow\quad
\text{the four conditions are dependent}.
$$
Geometrically the criterion is that **$\tilde U^{\mathrm{lor}}$ fixes a two-dimensional subspace pointwise**, since a product of two reflections is the identity on the plane orthogonal to the span of $u$ and $v$. In the cells the same determinant vanishes exactly when the bivector part of $\tilde U^{\mathrm{lor}}$ is the product of two vectors, and the solutions $u$ are then the vectors of the plane they span; a plane in Lorentzian four-space always contains a non-null vector, so a nonzero solution can be rescaled to a unit normal. The three forms of the criterion agree: the determinant vanishes exactly when the fixed subspace has dimension two.

| transformation | the four conditions | fixed subspace | reflections needed |
|---|---|---|---|
| pure boost | dependent | dimension two | two |
| pure spatial rotation | dependent | dimension two | two |
| boost along $\vec e_x$ with a rotation in the $xy$ plane | dependent | dimension two | two |
| boost along $\vec e_x$ with a rotation about $\vec e_x$ | independent | dimension zero | four |

The rule the table obeys is geometric: the transformation is simple exactly when the **boost plane and the rotation plane share a direction**. A pure boost or a pure rotation carries one plane, so the condition is empty; a boost with a rotation in the plane of the boost shares the boost direction; a boost with a rotation about the boost axis shares nothing.

The factorisations are explicit. The image of a boost is the frame cell times a unit vector,
$$
\text{image of }\tilde U_{\mathrm b} = iR_{\vec e_x}^{\mathrm{axf}}\,v ,
$$
where $v$ is the unit vector whose coordinates in the generator basis are
$$
\Bigl(\cosh\frac{\psi}{2},\ \sinh\frac{\psi}{2}u_x,\ \sinh\frac{\psi}{2}u_y,\ \sinh\frac{\psi}{2}u_z\Bigr),
$$
the time axis boosted by **half** the rapidity. The boost is therefore the reflection in the resting time axis composed with the reflection in the moving one, and the half is what makes the two rapidities add to $\psi$.

A spatial rotation in the plane spanned by two spatial generators is $iL_{\vec e_j}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\,v$ with
$$
v = -\cos\frac{\theta}{2}\,iL_{\vec e_j}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}} + \sin\frac{\theta}{2}\,iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}} , \qquad v^2 = -I_4 ,
$$
so that
$$
iL_{\vec e_j}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\,v = \cos\frac{\theta}{2}\,I_4 + \sin\frac{\theta}{2}\,iL_{\vec e_j}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\,iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}} .
$$
For the plane $(x,y)$ the right-hand side is the image of $\cos\frac{\theta}{2}e_t+\sin\frac{\theta}{2}\vec e_z$, the rotation about $\vec e_z$, and the other coordinate planes follow by relabelling. A generic Lorentz transformation fixes no plane at all, so it needs four reflections, the maximum.

The answer to the question is therefore: **pure boosts and pure spatial rotations are products of two reflections, and so is a boost with a rotation in the plane of the boost; a generic Lorentz transformation is not, and needs four.** The two-reflection class is a proper submanifold of $SL(2,\mathbb{C})$, cut out by the vanishing of that determinant. The product of two non-collinear boosts stays inside it — the Thomas–Wigner rotation of a composed boost lies in the plane of the two boosts — so what leaves the class is a boost combined with a rotation about the boost axis, that is, a boost and a rotation in orthogonal planes.

## The Two Parts and the Reflection

The cell that separates the two parts of an element is the chirality cell of the frame, the product of the four generators,
$$
-iR_{\vec e_z}^{\mathrm{axf}} = i\,\omega , \qquad
\omega = iR_{\vec e_x}^{\mathrm{axf}}\,iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\,iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\,iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}} = -L_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}} ,
$$
where the four scalar factors of $\omega$ multiply to $i^4=1$, so that $\omega$ is a pure product of cells. That product is the pseudoscalar of the frame, $\omega^2=-I_4$, and the chirality cell is a single right multiplication whose square is $I_4$.

**The letter.** An element is $L$ when the chirality cell gives it the value $-1$, and $R$ when it gives $+1$. That is the whole definition. The two values are exactly two, and only the zero element is both. The letter belongs to the object and not to a state, so a product, a unit and a field carry it as well, and the two parts of a field are written $\tilde\Psi_L$ and $\tilde\Psi_R$.

**Which cells keep it and which exchange it.** A cell acts through its right multiplier: a product takes the letter of its right factor, and left multiplication keeps the letter of its operand. Every even cell has right multiplier $e_t$ or $\vec e_z$ and keeps the letter. Every generator has right multiplier $\vec e_x$ or $\vec e_y$ and exchanges it, so a generator carries the $R$ part into the $L$ part and the $L$ part into the $R$ part.

Combined with the split established above, the statement is: **rotations keep the letter and reflections exchange it.** A rotation cannot change which part an element belongs to, and a reflection always does. The letter is not an extra label attached to the element; it is the value of the cell that tells the two parts apart, and only the odd half moves it.

The mass is where the two parts are coupled, and the series writes the coupling in the two forms the split distinguishes. The algebra form is the one-sided pair of *The Dirac Equation in Biquaternionic Form*,
$$
\tilde\nabla\tilde\Psi_R = m\tilde\Psi_L , \qquad \tilde\nabla^{\natural}\tilde\Psi_L = m\tilde\Psi_R ,
$$
in which every derivative acts by left multiplication. The two subscripts there name the two members of the pair: nothing in that form reads the value of the chirality cell, and the letter enters with the second form, the two-sided one,
$$
(\mathbb{D}-m)\tilde\Psi = 0 , \qquad
\tilde\Psi \mapsto -\,\frac{\partial\tilde\Psi}{\partial t'}\,\vec e_x - \sum_k \vec e_k\,\frac{\partial\tilde\Psi}{\partial x_k}\,\vec e_y .
$$
Every term of $\mathbb{D}$ acts by a right multiplier $\vec e_x$ or $\vec e_y$, so $\mathbb{D}$ is odd and carries one part into the other. The mass is a multiple of the identity, central and even, and it moves nothing by itself. The opposite signs in the square come from the cells, not from the display: $(R_{\vec e_x}^{\mathrm{axf}})^2=-I_4$ while $\bigl(L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\bigr)^2=+I_4$, so
$$
\mathbb{D}^2=-\frac{\partial^2}{\partial t'^2}+\sum_k\frac{\partial^2}{\partial x_k^2},
$$
and $(\mathbb{D}-m)(\mathbb{D}+m)$ is the Klein–Gordon operator up to an overall sign.

The consequence is immediate. Were $\tilde\Psi=\tilde\Psi_L$ a single part, the equation would read $\mathbb{D}\tilde\Psi_L=m\tilde\Psi_L$ with the left side in the other part, so $\tilde\Psi_L=0$: a massive field carries both parts, and the letter is not conserved. At $m=0$ the equation splits into $\mathbb{D}\tilde\Psi_L=0$ and $\mathbb{D}\tilde\Psi_R=0$, because $\mathbb{D}$ carries each part into the other and the sum vanishes part by part: the two parts decouple, and a field of one part alone is allowed. That decoupling is the operator-level content of the statement that the letter and the helicity agree only in the massless limit.

The representation-theoretic form of the same fact is the split of the complexified Lorentz algebra into two copies of $\mathfrak{sl}(2,\mathbb{C})$, each of them the complexification of an $\mathfrak{su}(2)$,
$$
\mathfrak{so}(1,3)_{\mathbb{C}} \cong \mathfrak{sl}(2,\mathbb{C})\oplus\mathfrak{sl}(2,\mathbb{C}),
$$
under which a finite-dimensional representation is labelled by a pair $(j_1,j_2)$. The rotations and the boosts act within each copy, and the letter is *which* copy:

| object | label | letter |
|---|---|---|
| a scalar | $(0,0)$ | in neither copy; no letter exists |
| $\tilde\Psi_L$ | $(\tfrac12,0)$ | in the first copy alone |
| $\tilde\Psi_R$ | $(0,\tfrac12)$ | in the second copy alone |
| a vector | $(\tfrac12,\tfrac12)$ | in both copies equally |

This is the precise sense in which the letter is tied to spin $\tfrac12$: the two parts are the two smallest nontrivial representations of the two copies, and $L$ *means* $(\tfrac12,0)$. A scalar has no letter because it sits in neither copy, and a vector is blind to it because it sits in both equally. The link is not a coincidence to be explained: each part is a minimal representation of one copy, and the cell is what tells the two copies apart.

The exchange of the two copies is an orientation-reversing operation, which is why it takes a reflection. **Parity is exactly that reflection.** It fixes the time direction and reverses the three spatial ones, and it exchanges the two parts,
$$
\mathsf{P} : (\tfrac12,0) \longleftrightarrow (0,\tfrac12).
$$
It is odd in both readings: the trivector $iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\,iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\,iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$ for the geometric reflection, the internal factor $\eta_P=iR_{\vec e_x}^{\mathrm{axf}}$ for the parity of the Dirac field. Every odd cell carries the $R$ part into the $L$ part, so the exchange of the parts is the parity.

Parity violation — the statement that the weak interaction couples to one part and not the other — is therefore not an accidental property of the Standard Model but the statement that the interaction distinguishes the two copies of the complexified Lorentz algebra. This is what *Chiral Fermions in the Biquaternion Framework* and *The Neutrino and Majorana Fermions in Biquaternionic Form* develop on the physical side.

## Why Three Generators Cannot Carry the Letter

The non-relativistic limit keeps three directions and drops the time generator, and it is natural to ask whether the letter could have been defined there. It could not, and the reason is algebraic and exact.

Take the algebra generated by the three spatial generators, $iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$, $iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$, $iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$. Their product is odd, it squares to $+I_4$, and it commutes with all three:
$$
\bigl(iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\;iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\;iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\bigr)^2 = I_4 .
$$
A cell that commutes with the three generators multiplies each of the two irreducible pieces they act on by a scalar, so it separates the elements into two halves that the three generators never mix. That is a copy index of the algebra, and not the letter: the letter must be a value that the *odd* cells exchange, and a cell that commutes with them cannot supply one.

The other half of the argument is the same statement read backwards. A cell that all three generators exchange must anticommute with all three, and the algebra of the three contains no such cell: its even part is spanned by the identity and the three products of two generators, a product of two anticommutes with the two it carries and commutes with the third, so a combination that anticommuted with all three would have to vanish. The odd part contains the triple product, which commutes. There is nowhere to put the letter.

The fourth generator is what supplies it. **The chirality cell is the product of all four generators**, and it is even. The timelike direction is therefore not an optional extra; it is the ingredient that makes the two parts exist. The two values are intrinsically relativistic: four generators carry them, three cannot, and the non-relativistic limit keeps only the spin.

## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *Why AXF Matrices instead of Pauli and Gamma Matrices*. The bracket is the frame, on the generators as on the metric, $\gamma_\mu[\mathbb{M}_-]$ or $\gamma_\mu[\mathbb{B}]$, so that a glyph names a display and not an object of the algebra.

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra.

Here $L_a$ and $R_b$ are the left and right multiplications, $L_a\psi=a\psi$ and $R_b\psi=\psi b$.
$$
\gamma_0[\mathbb{M}_-]=iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}},\quad \gamma_1[\mathbb{M}_-]=iL_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_2[\mathbb{M}_-]=iL_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_3[\mathbb{M}_-]=iL_{\vec e_z}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_5=-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}} .
$$

The same in the axis-free display:

$$
\gamma_0[\mathbb{M}_-]=iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}},\quad \gamma_1[\mathbb{M}_-]=iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad \gamma_2[\mathbb{M}_-]=iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad \gamma_3[\mathbb{M}_-]=iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad \gamma_5=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}} .
$$

Each generator is a single cell product, and every element of the cell algebra is a sum of at most four cell products, one for each term of the rank decomposition of its coefficient matrix in the cell basis.

$\gamma_5=-iR_{\vec e_z}^{\mathrm{pau}}$ is the chirality cell itself. The central grading $\chi$ — the difference of the two central idempotents of the complexified algebra, so $\chi^2=e_t$ — is a different object, represented by $\gamma_5$ on the Dirac module.

The $\gamma$'s are a complex frame, not a real one: they generate $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$ over $\mathbb{C}$, whereas the cells with real coefficients generate the real algebra $\mathrm{Cl}_{3,1}(\mathbb{R})=M_4(\mathbb{R})$. It is the complexification that makes the scalar $i$ central, and that is why each generator is written as $i$ times a real cell.

**The identities the series uses.** In the $\gamma$ reading, with $\epsilon_{0123}=+1$,
$$
\{\gamma_\mu[\mathbb{M}_-],\gamma_\nu[\mathbb{M}_-]\}=2\varepsilon_\mu\delta_{\mu\nu}I_4,\qquad
(\gamma_k[\mathbb{M}_-])^2=-I_4,\qquad
\gamma_5^2=I_4,\qquad
\{\gamma_\mu[\mathbb{M}_-],\gamma_5\}=0,
\qquad \varepsilon=(1,-1,-1,-1),$$
$$
[\gamma_\mu[\mathbb{M}_-],\gamma_\nu[\mathbb{M}_-]]=2\gamma_\mu[\mathbb{M}_-]\gamma_\nu[\mathbb{M}_-]\quad(\mu\ne\nu),\qquad
[\gamma_a[\mathbb{M}_-],S_{cd}]=\varepsilon_a\delta_{ac}\gamma_d[\mathbb{M}_-]-\varepsilon_a\delta_{ad}\gamma_c[\mathbb{M}_-],\qquad
S_{cd}=\tfrac14[\gamma_c[\mathbb{M}_-],\gamma_d[\mathbb{M}_-]],
$$
$$
\mathrm{tr}(\gamma_\mu[\mathbb{M}_-]\gamma_\nu[\mathbb{M}_-])=4\varepsilon_\mu\delta_{\mu\nu},\qquad
\mathrm{tr}(\gamma_5\gamma_\mu[\mathbb{M}_-]\gamma_\nu[\mathbb{M}_-]\gamma_\rho[\mathbb{M}_-]\gamma_\sigma[\mathbb{M}_-])=-4i\,\epsilon_{\mu\nu\rho\sigma},
$$
$$
\mathrm{tr}(\gamma_\mu[\mathbb{M}_-]\gamma_\nu[\mathbb{M}_-]\gamma_\rho[\mathbb{M}_-]\gamma_\sigma[\mathbb{M}_-])
=4\bigl(\varepsilon_\mu\delta_{\mu\nu}\varepsilon_\rho\delta_{\rho\sigma}-\varepsilon_\mu\delta_{\mu\rho}\varepsilon_\nu\delta_{\nu\sigma}+\varepsilon_\mu\delta_{\mu\sigma}\varepsilon_\nu\delta_{\nu\rho}\bigr).
$$
Four contraction sums accompany them. The four that hold in every frame are the ones with one index raised, $\gamma^\mu[\mathbb{M}_-]=g^{\mu\mu}\gamma_\mu[\mathbb{M}_-]$:
$$
\sum_\mu\gamma^\mu[\mathbb{M}_-]\gamma_\mu[\mathbb{M}_-]=-4I_4,\qquad
\sum_\mu\gamma^\mu[\mathbb{M}_-]\gamma_\alpha[\mathbb{M}_-]\gamma_\mu[\mathbb{M}_-]=2\gamma_\alpha[\mathbb{M}_-],\qquad
\sum_\mu\gamma^\mu[\mathbb{M}_-]\gamma_\alpha[\mathbb{M}_-]\gamma_\beta[\mathbb{M}_-]\gamma_\mu[\mathbb{M}_-]=-4\varepsilon_\alpha\delta_{\alpha\beta}I_4,
$$
$$
\sum_\mu\gamma^\mu[\mathbb{M}_-]\gamma_\alpha[\mathbb{M}_-]\gamma_\beta[\mathbb{M}_-]\gamma_\gamma[\mathbb{M}_-]\gamma_\mu[\mathbb{M}_-]=2\,\gamma_\gamma[\mathbb{M}_-]\gamma_\beta[\mathbb{M}_-]\gamma_\alpha[\mathbb{M}_-] .
$$
Written with every index down, they are frame statements instead, because a cell's square changes with the frame. In a Euclidean frame, where every cell squares to $+I_4$, the same four sums read
$$
\sum_\mu\gamma_\mu[\mathbb{B}]\gamma_\mu[\mathbb{B}]=4I_4,\qquad
\sum_\mu\gamma_\mu[\mathbb{B}]\gamma_\alpha[\mathbb{B}]\gamma_\mu[\mathbb{B}]=-2\gamma_\alpha[\mathbb{B}],\qquad
\sum_\mu\gamma_\mu[\mathbb{B}]\gamma_\alpha[\mathbb{B}]\gamma_\beta[\mathbb{B}]\gamma_\mu[\mathbb{B}]=4\delta_{\alpha\beta}I_4,
$$
$$
\sum_\mu\gamma_\mu[\mathbb{M}_-]\gamma_\alpha[\mathbb{M}_-]\gamma_\beta[\mathbb{M}_-]\gamma_\gamma[\mathbb{M}_-]\gamma_\mu[\mathbb{M}_-]=-2\,\gamma_\gamma[\mathbb{M}_-]\gamma_\beta[\mathbb{M}_-]\gamma_\alpha[\mathbb{M}_-] ,
$$
and in the frame of the series the metric enters term by term. Writing $\gamma_\mu[\mathbb{M}_-]^2=\varepsilon_\mu I_4$,
$$
\sum_\mu\gamma_\mu[\mathbb{M}_-]\gamma_\mu[\mathbb{M}_-]=\Bigl(\sum_\mu\varepsilon_\mu\Bigr)I_4=-2I_4,\qquad
\sum_\mu\gamma_\mu[\mathbb{M}_-]\gamma_\alpha[\mathbb{M}_-]\gamma_\mu[\mathbb{M}_-]=\Bigl(2\varepsilon_\alpha-\sum_\mu\varepsilon_\mu\Bigr)\gamma_\alpha[\mathbb{M}_-] ,
$$
so the second sum is $4\gamma_0[\mathbb{M}_-]$ for $\alpha=0$ and vanishes identically for spacelike $\alpha$. The third is not the substitution $\delta_{\alpha\beta}\to g_{\alpha\beta}$; it is
$$
\sum_\mu\gamma_\mu[\mathbb{M}_-]\gamma_\alpha[\mathbb{M}_-]\gamma_\beta[\mathbb{M}_-]\gamma_\mu[\mathbb{M}_-]
=2\varepsilon_\alpha\,\gamma_\beta[\mathbb{M}_-]\gamma_\alpha[\mathbb{M}_-]-\bigl(2\varepsilon_\beta+2\bigr)\gamma_\alpha[\mathbb{M}_-]\gamma_\beta[\mathbb{M}_-] ,
$$
which is $-2\gamma_0[\mathbb{M}_-]\gamma_k[\mathbb{M}_-]$ for one timelike and one spacelike index, $+2\gamma_j[\mathbb{M}_-]\gamma_k[\mathbb{M}_-]$ for two spacelike ones, and $-2\varepsilon_\alpha I_4$ for $\alpha=\beta$. The raised-index display is the one to compute with, and the lowered one the one to read in the Euclidean literature.

**The display.** Every array printed in this section is given twice: in the Peirce display first, labelled $\mathrm{pau}$, whose arrays are the ones the literature prints, and in the axis-free display after it, labelled $\mathrm{axf}$, which is the display of the body and of the corpus. The two are carried into one another by $L_{e_\mu}^{\mathrm{axf}}=C_{\Pi}L_{e_\mu}^{\mathrm{pau}}C_{\Pi}^{-1}$, and a conjugation by $C_{\Pi}$ changes no product, no anticommutator, no trace and no determinant, so every identity of the section holds in both. An array is a statement about one display; a cell named in the running text keeps the Peirce label, and its axis-free array is the conjugate. The label names the array and not the operator.


## Summary

The claims of this article, in order.

1. **One algebra, two readings.** A cell is at once an object of the algebra and an operator on it. The rotors are the even cells; the four frame cells are the odd ones. An even cell keeps the letter of the element it acts on, an odd cell exchanges it.

2. **The parity is the reflection count.** By Cartan–Dieudonné an orthogonal transformation is a product of reflections and its determinant is $(-1)^{\text{count}}$. The split of the cells by their right multiplier — eight with $e_t$ or $\vec e_z$, eight with $\vec e_x$ or $\vec e_y$ — is that parity, and the first eight are the image of $\mathbb{B}$.

3. **The frame and the signs.** Every vector is the frame cell applied after the image of $w\in\mathbb{M}_+$. The biquaternion norm on the Hermitian basis is $(+1,-1,-1,-1)$, its minus signs being those of $i^2$, and on the material basis it is $g_{\mu\nu}[\mathbb{M}_-]$. The sign vector of the generators is the biquaternion norm of the objects they represent, so the mostly-minus convention is forced rather than chosen.

4. **Conjugation by the frame cell is the bar.** Reversal is quaternion conjugation and the frame cell is the bar; the two compose into the Hermitian conjugation, so the real structure $\flat=-{}^{*}$ carries the frame within it.

5. **Rotations and reflections have different spaces.** The rotations are the unit-norm biquaternions, a group of dimension six with the bivectors as Lie algebra. The reflections are the odd unit cells, two orbits of dimension three organised by their normals, and not a group. Together they are $\mathrm{Pin}(1,3)$. Anti-linear maps shift the correspondence by one: an even internal factor belongs to a reflection and an odd one to a proper transformation, which is how $T$ is a reflection while $C$ is not.

6. **Two reflections, or four.** A rotation is a product of two reflections exactly when it fixes a plane. Pure boosts, pure spatial rotations and boosts with a rotation in the plane of the boost qualify; a boost with a rotation about the boost axis does not, and needs four.

7. **The letter is what the reflection changes.** Even cells keep the letter, odd cells exchange it, so rotations preserve the two parts and reflections reverse them. The mass is even and central and couples the two parts without moving either; the odd two-sided operator $\mathbb{D}$ performs the exchange. In the split $\mathfrak{so}(1,3)_{\mathbb{C}}\cong\mathfrak{sl}(2,\mathbb{C})\oplus\mathfrak{sl}(2,\mathbb{C})$ the letter is which copy, and the exchange of the copies is parity.

8. **The letter is relativistic.** Three generators cannot carry it: their product is central, and no cell of their algebra anticommutes with all three. The chirality cell is the product of all four generators and is even, so it exists only because one generator is timelike.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| even half, odd half | The cells with an even and with an odd number of generator factors; the even half is the image of $\mathbb{B}$ |
| $\varepsilon=(+1,-1,-1,-1)$ | Sign vector of the four generators: the biquaternion norm on the Hermitian basis |
| $g_{\mu\nu}[\mathbb{M}_-]$ | $ict'$ metric of the material coordinates |
| $L_{a}R_{b}$ | Left multiplication $L_a$ and right multiplication $R_b$: $L_{a}R_{b}\psi = a\psi b$, $L_{a}R_{b}L_{c}R_{d} = L_{ac}R_{db}$ |
| image of $\tilde Q$ | The $\mathbb{R}$-linear comparison with the even half, per *Matrix Representations Conventions*; named, never written as a symbol |
| the four frame cells | The generator cells: $iR_{\vec e_x}^{\mathrm{axf}}$, and $iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$ for $k=1,2,3$ |
| $\omega = iR_{\vec e_x}^{\mathrm{axf}}\,iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\,iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\,iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}} = -L_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$ | Pseudoscalar, $\omega^2 = -I_4$; its four factors of $i$ multiply to $i^4=1$ |
| $-iR_{\vec e_z}^{\mathrm{axf}} = i\omega = -iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$ | Chirality cell, $(-iR_{\vec e_z}^{\mathrm{axf}})^{2} = I_4$ |
| the $L$ part, the $R$ part | The two parts of an element: the value $-1$ and the value $+1$ of the chirality cell |
| $\tilde\Psi_{L,R}$ | The two parts of a field |
| $\tilde\nabla$, $\tilde\nabla^{\natural}$ | The biquaternion gradient and its quaternion conjugate; the one-sided pair $\tilde\nabla\tilde\Psi_R=m\tilde\Psi_L$, $\tilde\nabla^{\natural}\tilde\Psi_L=m\tilde\Psi_R$, whose subscripts name the two members |
| $\mathbb{D} = -R_{\vec e_x}^{\mathrm{axf}}\partial/\partial t'-\sum_k L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\partial/\partial x_k$ | The two-sided Dirac operator, built from two-sided cells; odd, hence it carries one part into the other |
| $iR_{\vec e_x}^{\mathrm{axf}}$ | The frame cell; the reflection whose normal is $e_t$ |
| $\rho(u) : x\mapsto -\epsilon(u)\,u x u$ | Action of an odd unit cell on the vectors; $u^2=\epsilon(u)I_4$ |
| Reversal | Reversing the order of the factors in the cell of $\tilde{Q}$ gives the cell of $\tilde{Q}^{\natural}$; on the biquaternions it is quaternion conjugation |
| Frame conjugation | Conjugating the image of $\tilde{Q}$ by $iR_{\vec e_x}^{\mathrm{axf}}$ gives the image of $\bar{\tilde{Q}}$ |
| Hermitian conjugation | The image of $\tilde{Q}^{*}$ is $iR_{\vec e_x}^{\mathrm{axf}}$ times the reversed image of $\tilde{Q}$, times $iR_{\vec e_x}^{\mathrm{axf}}$; $*$ is the bar composed with $\natural$ |
| $\tilde U^{\mathrm{lor}}$, $\langle\tilde U^{\mathrm{lor}}\rangle_{\natural} = 1$ | Rotor, unit-norm biquaternion; $SL(2,\mathbb{C})$ |
| $\tilde{Q}_2 = \tilde U^{\mathrm{lor}}\tilde{Q}\tilde U^{\mathrm{lor}}{}^{*}$ | Rotor conjugation on $\mathbb{M}_-$ |
| $\mathbb{M}_+$ | Hermitian sector; its image is the identity together with the timelike bivectors (boosts) |
| $\mathbb{H}_{\mathbb{B}}$ | Real-quaternion sector; its image is the identity together with the spacelike bivectors (spatial rotations) |
| the four conditions | Two-reflection criterion: they are dependent iff $\tilde U^{\mathrm{lor}}$ fixes a plane pointwise |
| $\det = (-1)^{k}(-1)^{\text{anti}}$ | Reflection parity of a linear or anti-linear map |
| $\mathsf{P}$ | Parity reflection; exchanges the two parts |
| $\eta_P = iR_{\vec e_x}^{\mathrm{axf}}$ | The internal factor of the parity of the Dirac field; odd, so it carries the $R$ part into the $L$ part |

## Further Reading

- [Why AXF Matrices instead of Pauli and Gamma Matrices](why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the reasons the AXF matrices replace the Pauli and gamma matrices.
- Companion articles in this series: [Matrix Representations Conventions](matrix-representations-conventions.html) (the Clifford reading, the sign conventions, and the chirality operator used throughout, §*The Clifford Structure*); [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html) (the chiral pair, the two-sided form and the mass); [The Spinor Module in Biquaternionic Form and Its Lorentz Action](the-spinor-module-in-biquaternionic-form-and-its-lorentz-action.html) (the module, the one-sided spinor action, and the two factors $\mathrm{SU}(2)\oplus\mathrm{SU}(2)$); [Exercise: Chirality and the Weyl Spinors](exercise-chirality-and-the-weyl-spinors.html) (the projectors and the two Weyl modules); [The Lorentz Transformation as a Biquaternionic Rotation](the-lorentz-transformation-as-a-biquaternionic-rotation.html) (the boost rotor, its Hermiticity, and the rotor conjugation); [The Lorentz Group in Biquaternionic Form — Structure and Representations](the-lorentz-group-in-biquaternionic-form-structure-and-representations.html); [Exercise: The Thomas Precession](exercise-the-thomas-precession.html) (the composition of non-collinear boosts); [Exercise: Boosting a Four-Velocity and Rapidity Composition](exercise-boosting-a-four-velocity-and-rapidity-composition.html).
- On the physics of chirality: [Chiral Fermions in the Biquaternion Framework](chiral-fermions-in-the-biquaternion-framework.html); [The Neutrino and Majorana Fermions in Biquaternionic Form](the-neutrino-and-majorana-fermions-in-biquaternionic-form.html); [The CPT Theorem in Biquaternionic Form](the-cpt-theorem-in-biquaternionic-form.html) (the anti-linear discrete symmetries of the last subsection); [Zitterbewegung in Biquaternionic Form](zitterbewegung-in-biquaternionic-form.html) (the mass as the coupling between the chiralities); [Exercise: The Non-Relativistic Limit and the Pauli Equation](exercise-the-non-relativistic-limit-and-the-pauli-equation.html) (the reduction to the Pauli algebra).
- Foundational articles: [Introduction to the Biquaternion Universe](introduction-to-the-biquaternion-universe.html); [The Material Sector: Four-Vectors, Interval and Lorentz Action](the-material-sector-four-vectors-interval-and-lorentz-action.html); [The Informational Sector: States, Observables and Probability](the-informational-sector-states-observables-and-probability.html); [Algebra and Element Conventions](algebra-and-element-conventions.html).
- On the Clifford structures used here: [Clifford Algebras](../articles_maths/clifford-algebras.html); [Two-Sided Operators on a Clifford Algebra](../articles_maths/two-sided-operators-on-a-clifford-algebra.html) (the cell algebra, its two closures, and the frame); *Clifford Algebras in finite dimensions*; *Spinors*; [The Spinor Representation of the Lorentz Group in Biquaternionic Form](the-spinor-representation-of-the-lorentz-group-in-biquaternionic-form.html).

