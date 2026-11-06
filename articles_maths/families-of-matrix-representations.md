# __Families of Matrix Representations__

## Introduction

**The subject.** A matrix of a biquaternion needs two choices. The first is a frame, that is a basis of the algebra. The second is a side, left or right, that is the reading of $\tilde X\mapsto\tilde Q\tilde X$ or of $\tilde X\mapsto\tilde X\tilde Q$. Every frame gives two families of arrays, one for each side, and the families of different frames are not independent. The laws of the algebra force exact relations between them, and each relation is carried by a matrix.

**The two kinds of matrix.** One matrix changes the frame. It conjugates the arrays and leaves the element alone. One matrix changes the side. It is not a conjugation, because no conjugation can carry a left family onto a right one; it is a transposition followed by a congruence. Both matrices are read off the multiplication, so neither is an extra structure imported from outside.

**Why the theory is general.** The three laws of §*The Two Sides* hold in every frame and involve no coordinate at all. The invariants of §*What the Laws Give the Two Families* are therefore properties of the element, equal in the two sides and in every frame. Only the arrays depend on the frame, and the two matrices of §*The Switch Between the Left and the Right* and of §*The Matrix That Changes the Frame* say exactly how.

**What this article is not.** The objects here are arrays, their products, their transposes, their traces, their determinants and their spectra. Nothing else is used. The concrete families of four-dimensional arrays are computed in the model articles that follow this one in the category, and each of them is one instance of the general frame used below.

## The Two Sides

**The two matrices of an element.** Fix a frame $\mathcal{F}=(f_1,f_2,f_3,f_4)$ of $\mathbb{B}$ and write $[\tilde X]_{\mu}$ for the $\mu$-th coordinate of $\tilde X$ in $\mathcal{F}$. The left matrix and the right matrix of $\tilde Q$ in this frame have for their $\nu$-th columns the coordinate columns of $\tilde Qf_\nu$ and of $f_\nu\tilde Q$,
$$
L_{\mathcal{F}}(\tilde Q)_{\mu\nu}=\bigl[\tilde Qf_\nu\bigr]_{\mu},\qquad
R_{\mathcal{F}}(\tilde Q)_{\mu\nu}=\bigl[f_\nu\tilde Q\bigr]_{\mu}.
$$
Both are $4\times4$ complex arrays. The element does not depend on $\mathcal{F}$; the array does. Below the frame is fixed and the subscript is dropped.

**The three laws.** For all $\tilde P,\tilde Q\in\mathbb{B}$,
$$
L(\tilde P\tilde Q)=L(\tilde P)L(\tilde Q),\qquad
R(\tilde P\tilde Q)=R(\tilde Q)R(\tilde P),\qquad
L(\tilde P)R(\tilde Q)=R(\tilde Q)L(\tilde P).
$$
The first is the associativity $(\tilde P\tilde Q)\tilde X=\tilde P(\tilde Q\tilde X)$ read on the left. The second is the associativity $(\tilde X\tilde Q)\tilde P=\tilde X(\tilde Q\tilde P)$ read on the right, and it is the interesting one: the right family carries the product backwards. The third holds because the two factors sit on opposite sides of the argument and never meet.

**The three laws need no coordinates.** Each is an identity between products of elements, read through the columns of a frame. A change of frame conjugates every array and therefore preserves all three. This is why the statements below are frame-free and why only the displays are frame-bound.

**Faithfulness.** If $L(\tilde Q)=0$ then $\tilde Qf_\nu=0$ for each $\nu$, and since the four $f_\nu$ span, $\tilde Q=0$; the same argument holds on the right. So each side is an injective image, of complex dimension four inside the sixteen of $M_4(\mathbb{C})$, and an element is known by its left matrix alone and by its right matrix alone.

**The centre is the coincidence locus.** The identity $L(\tilde Q)=R(\tilde Q)$ says $\tilde Q\tilde X=\tilde X\tilde Q$ for every $\tilde X$, that is $\tilde Q\in\mathbb{C}e_t$. So the two families agree on the centre and nowhere else.

**A central element has one matrix, and it is scalar.** If $\tilde Q=\lambda e_t$ then $L(\tilde Q)=R(\tilde Q)=\lambda\mathrm I_4$. This is the only case in which a matrix of the left family is also a matrix of the right family.

## What the Laws Give the Two Families

**The left family is the algebra and the right family is its opposite.** The first law makes $\mathbb{B}_L=\{L(\tilde Q)\}$ a subalgebra of $M_4(\mathbb{C})$ isomorphic to $\mathbb{B}$. The second makes $\mathbb{B}_R=\{R(\tilde Q)\}$ a subalgebra isomorphic to the opposite algebra $\mathbb{B}_{\mathrm{opp}}$. These are abstractly the same algebra, because $M_2(\mathbb{C})$ is isomorphic to its opposite through transposition; this is why a switch between the sides can exist at all.

**Every left matrix commutes with every right matrix.** The left matrix of any element commutes with the right matrix of any other, and the two elements need not be related. So the left family lies in the commutant of the right family and conversely.

**The two families meet in the scalars.** Suppose $L(\tilde P)=R(\tilde Q)$. Applying both to $e_t$ gives $\tilde P=\tilde Q$, and then $L(\tilde Q)=R(\tilde Q)$, so $\tilde Q$ is central and the common matrix is scalar. Hence
$$
\mathbb{B}_L\cap\mathbb{B}_R=\mathbb{C}\,\mathrm I_4,
$$
a line, and the two four-dimensional families together span seven dimensions, not eight. The missing dimension is the one they share.

**The invariants agree.** A transposition and a conjugation by a fixed matrix change neither a trace nor a determinant, so the two matrices of an element carry the same invariants:
$$
\operatorname{Tr}L(\tilde Q)=\operatorname{Tr}R(\tilde Q)=4Q_t,\qquad
\det L(\tilde Q)=\det R(\tilde Q)=\langle\tilde Q\rangle_{\natural}^{2},
$$
with $\langle\tilde Q\rangle_{\natural}=Q_t^2+Q_x^2+Q_y^2+Q_z^2$ the norm of the element, which is also the determinant of the $2\times2$ matrix of $\tilde Q$. The characteristic polynomial is the same in the two families,
$$
p(X)=\bigl((X-Q_t)^2+B^2\bigr)^2,\qquad B^2=Q_x^2+Q_y^2+Q_z^2,
$$
so the spectrum is $Q_t\pm iB$, each value twice. The rank is the same too: it is twice the rank of the $2\times2$ matrix of the element, hence $0$, $2$ or $4$, and no matrix of either family has odd rank.

**The kernels.** The kernel of the left matrix is the left annihilator of the element, the kernel of the right matrix is its right annihilator. The two have the same dimension, $4-\operatorname{rank}L(\tilde Q)$, and they are in general different subspaces of the coordinate space.

**The trace pairing.** Within one family the trace pairing is the scalar product of the algebra,
$$
\operatorname{Tr}\bigl(L(\tilde P)L(\tilde Q)\bigr)=4\operatorname{Sc}(\tilde P\tilde Q),\qquad
\operatorname{Tr}\bigl(R(\tilde P)R(\tilde Q)\bigr)=4\operatorname{Sc}(\tilde P\tilde Q),
$$
because the product of two matrices of one side is again a matrix of that side. Across the two families it collapses to the product of the scalar parts,
$$
\operatorname{Tr}\bigl(L(\tilde P)R(\tilde Q)\bigr)=4P_tQ_t .
$$
So the two sides are orthogonal for the trace form exactly when one of the two scalar parts vanishes, and what couples them is the centre and nothing else.

| invariant | left family | right family |
|---|---|---|
| trace | $4Q_t$ | $4Q_t$ |
| determinant | $\langle\tilde Q\rangle_{\natural}^{2}$ | $\langle\tilde Q\rangle_{\natural}^{2}$ |
| characteristic polynomial | $((X-Q_t)^2+B^2)^2$ | the same |
| spectrum | $Q_t\pm iB$, twice | $Q_t\pm iB$, twice |
| rank | $2\operatorname{rank}A(\tilde Q)\in\{0,2,4\}$ | the same |
| kernel | left annihilator | right annihilator, same dimension |
| trace pairing inside | $4\operatorname{Sc}(\tilde P\tilde Q)$ | $4\operatorname{Sc}(\tilde P\tilde Q)$ |
| trace pairing with the other side | $4P_tQ_t$ | $4P_tQ_t$ |

**None of these numbers sees the frame.** A change of frame conjugates the arrays, and a conjugation leaves the trace, the determinant, the characteristic polynomial and the rank untouched. The table above is therefore a table of the element, written twice.

## The Switch Between the Left and the Right

**A conjugation is not available.** No invertible $\mathsf X$ satisfies $R(\tilde Q)=\mathsf X\,L(\tilde Q)\,\mathsf X^{-1}$ for all $\tilde Q$. Such an $\mathsf X$ would carry products to products, while the right family reverses them, so it would force $L(\tilde P\tilde Q)=L(\tilde Q\tilde P)$ for all $\tilde P,\tilde Q$; the pair $(\vec e_x,\vec e_y)$ refutes that, because $\vec e_x\vec e_y=\vec e_z$ while $\vec e_y\vec e_x=-\vec e_z$. So the matrix that changes the side has to be combined with a transposition, and no matrix alone is enough.

**The form behind the switch.** What is needed is a scalar product, and the algebra carries one:
$$
\beta(\tilde X,\tilde Y)=\operatorname{Sc}(\tilde X\tilde Y).
$$
It is symmetric, because $\operatorname{Sc}(\tilde X\tilde Y)=\operatorname{Sc}(\tilde Y\tilde X)$. It is nondegenerate, because its Gram matrix in any frame is invertible. It is also cyclic,
$$
\operatorname{Sc}(\tilde Q\tilde X\tilde Y)=\operatorname{Sc}(\tilde X\tilde Y\tilde Q),
$$
and this single identity is what the switch rests on.

**The adjoint identity.** By cyclicity, for all $\tilde Q,\tilde X,\tilde Y$,
$$
\beta(\tilde Q\tilde X,\tilde Y)=\beta(\tilde X,\tilde Y\tilde Q).
$$
Let $\mathsf W$ be the Gram matrix of $\beta$ in the frame,
$$
\mathsf W_{\mu\nu}=\beta(f_\mu,f_\nu),
$$
so that $\beta(\tilde X,\tilde Y)=[X]^{\mathsf T}\mathsf W[Y]$ in coordinates. The identity then reads, in arrays,
$$
\mathsf W\,R(\tilde Q)=L(\tilde Q)^{\mathsf T}\,\mathsf W,
$$
or, since $\mathsf W$ is invertible,
$$
R(\tilde Q)=\mathsf W^{-1}L(\tilde Q)^{\mathsf T}\mathsf W .
$$
This is the switch. The form is symmetric, so $\mathsf W$ is a symmetric matrix, and the switch consists of a transposition and a congruence rather than of a transposition alone.

**Three immediate properties.** Applying the stitch twice returns the array, because transposition and conjugation by a fixed matrix are both involutions. The matrix $\mathsf W$ is symmetric and invertible, so the switch is defined in every frame and never degenerates. And $\mathsf W$ is read off the multiplication of the four frame vectors, so no choice is made beyond the frame itself.

**The switch is unique up to a scalar.** Every matrix $\mathsf M$ that satisfies $\mathsf M\,R(\tilde Q)=L(\tilde Q)^{\mathsf T}\mathsf M$ for all $\tilde Q$ is of the form $\mathsf M=\mathsf W\,L(\tilde P)$ with $\tilde P$ arbitrary: a four-dimensional family, because $\mathsf W^{-1}\mathsf M$ has to commute with the whole right family, and the commutant of that family is the left family. Among these solutions exactly the symmetric ones are the scalar multiples of $\mathsf W$. The requirement of symmetry, equivalently the requirement that the matrix be the Gram matrix of a form on the algebra, therefore fixes the switch up to one nonzero scalar, and the Gram matrix is the canonical representative.

**The switch is not the Hermitian dictionary.** The algebra carries a second form, the Hermitian one $\langle\tilde X,\tilde Y\rangle_*=\operatorname{Sc}(\tilde X\tilde Y^{*})$. Its dictionary takes the adjoint and stays inside the family, $L(\tilde Q)^{\dagger}=L(\tilde Q^{*})$. The switch takes the transpose and exchanges the sides. The two are read on the same array and answer different questions.

**The transpose alone does not cross the divide.** Transposition reverses the order of a product, exactly as the conjugation of the element does, so it cannot by itself turn a product-preserving action into a product-reversing one. The side is changed only when the transposition is followed by the congruence with $\mathsf W$; the transposition reverses the order once, and the congruence restores it.

## The Matrix That Changes the Frame

**The change.** Let $\mathcal{F}'=(f'_1,f'_2,f'_3,f'_4)$ be a second frame and let $\mathsf C$ be the matrix of the change, so that $f'_\nu=\sum_\mu f_\mu\mathsf C_{\mu\nu}$. The columns of $\mathsf C$ are the new frame vectors written in the old one, and $\mathsf C$ is invertible. A change of frame is a change of basis of the carrier, so it conjugates every array read on the carrier, whichever side the array belongs to:
$$
L_{\mathcal{F}'}(\tilde Q)=\mathsf C^{-1}L_{\mathcal{F}}(\tilde Q)\,\mathsf C,\qquad
R_{\mathcal{F}'}(\tilde Q)=\mathsf C^{-1}R_{\mathcal{F}}(\tilde Q)\,\mathsf C .
$$
One matrix serves both sides, because the frame is a property of the carrier and the side is a property of the action. This is the precise sense in which the two families of one frame are tied to the two families of another: the same $\mathsf C$ acts on all four.

**What it leaves alone.** A conjugation leaves the trace, the determinant, the characteristic polynomial and the rank unchanged, so the table of invariants of §*What the Laws Give the Two Families* is the same in every frame. The frame changes the array and never the element.

**What the switch becomes in the new frame.** The switch is not a matrix that belongs to a pair of frames; it belongs to one frame, and each frame has its own. Write $\mathsf W_{\mathcal{F}'}$ for the switch of the new frame, that is the array that turns $L_{\mathcal{F}'}$ into $R_{\mathcal{F}'}$,
$$
R_{\mathcal{F}'}(\tilde Q)=\mathsf W_{\mathcal{F}'}^{-1}L_{\mathcal{F}'}(\tilde Q)^{\mathsf T}\mathsf W_{\mathcal{F}'}.
$$
It plays the same role as $\mathsf W_{\mathcal{F}}$ and it is computed the same way, from the new frame vectors, $\mathsf W_{\mathcal{F}',\mu\nu}=\beta(f'_\mu,f'_\nu)$. So nothing new is introduced: the switch of a frame is always the Gram matrix of the form on that frame. Only its entries change.

**Why the entries change by congruence.** Put $f'_\nu=\sum_\mu f_\mu\mathsf C_{\mu\nu}$ into the definition and use the bilinearity of $\beta$:
$$
\mathsf W_{\mathcal{F}',\mu\nu}=\beta\Bigl(\sum_\alpha f_\alpha\mathsf C_{\alpha\mu},\sum_\beta f_\beta\mathsf C_{\beta\nu}\Bigr)
=\sum_{\alpha,\beta}\mathsf C_{\alpha\mu}\,\beta(f_\alpha,f_\beta)\,\mathsf C_{\beta\nu},
$$
that is
$$
\mathsf W_{\mathcal{F}'}=\mathsf C^{\mathsf T}\mathsf W_{\mathcal{F}}\,\mathsf C .
$$
The rule is not an extra requirement: it is the definition of the Gram matrix, written in the new basis. The form $\beta$ itself has not moved. Only its array has, and it moves by congruence because a bilinear form pairs two vectors and therefore meets $\mathsf C$ on both sides.

**A reading of the congruence.** Each entry of $\mathsf W'$ is a value of $\beta$ on a pair of new frame vectors, and each new frame vector is a combination of the old ones. A diagonal entry $\mathsf W'_{\nu\nu}=\beta(f'_\nu,f'_\nu)$ collects the old values on all the old vectors that enter $f'_\nu$, with the coefficients squared; an off-diagonal entry collects the old values on the two vectors that enter, once through each slot. So the congruence is nothing but the bookkeeping of the definition, and every entry of $\mathsf W'$ still says what a form says.

**When the array happens to stay put.** If $\mathsf C^{\mathsf T}\mathsf W\mathsf C=\mathsf W$, then $\mathsf W'=\mathsf W$, and one array switches the families in every such frame. Such a $\mathsf C$ keeps the form and is called $\beta$-orthogonal; it is the exception, not the rule. It does not leave the families alone, since $L'=\mathsf C^{-1}L\mathsf C$ still changes the arrays. So the families move while the switch does not, which shows that $\mathsf W'$ and $L'$ are independent pieces of data and that neither can be computed from the other.

**The two changes are compatible.** Write the switch in the new frame and substitute the two rules above:
$$
\mathsf W_{\mathcal{F}'}^{-1}L_{\mathcal{F}'}^{\mathsf T}\mathsf W_{\mathcal{F}'}
=\mathsf C^{-1}\mathsf W_{\mathcal{F}}^{-1}L_{\mathcal{F}}^{\mathsf T}\mathsf W_{\mathcal{F}}\,\mathsf C
=\mathsf C^{-1}R_{\mathcal{F}}\,\mathsf C
=R_{\mathcal{F}'}.
$$
The intermediate factors cancel, so the switch of the new frame is the switch of the old frame transported. Changing the frame moves the families by conjugation and the switch by congruence, and the relation between them survives untouched.

**The frame is itself defined only up to a matrix.** Nothing distinguishes one frame from another; a change $\mathsf C$ produces another legal description of the same element. What is invariant is the pair, the families together with the switch, and the pair moves as above. One member of the pair has no meaning without the other.

## The Relations in One Picture

**Two matrices, two jobs.** Only two matrices are ever needed, and each has one job. The matrix $\mathsf C$ is a change of frame: it belongs to the carrier and says how one basis is written in another. The matrix $\mathsf W$ belongs to the algebra: it is the Gram matrix of the form $\beta(\tilde X,\tilde Y)=\operatorname{Sc}(\tilde X\tilde Y)$, and its single job is to turn a left array into a right array.

**The two rules.**

| you change | what happens to the arrays | what happens to the switch |
|---|---|---|
| the frame, by $\mathsf C$ | $L'=\mathsf C^{-1}L\mathsf C$ and $R'=\mathsf C^{-1}R\mathsf C$ | $\mathsf W'=\mathsf C^{\mathsf T}\mathsf W\mathsf C$, the switch of the new frame |
| the side, by $\mathsf W$ | $R=\mathsf W^{-1}L^{\mathsf T}\mathsf W$ | nothing: $\mathsf W$ is the matrix that does the switching |

**Why the two rules look different.** A frame is a basis of the carrier, so changing it conjugates every array of that carrier, and it does so for the left family and the right family alike. The switch is the matrix of a bilinear form, and a bilinear form transforms by congruence, never by conjugation. That is the whole difference: $\mathsf C$ moves a basis, $\mathsf W$ moves a form.

**Doing both gives nothing new.** Change the frame and then the side, or the side and then the frame, and the result is the same, because the two rules are compatible by §*The Matrix That Changes the Frame*. So a composition of the two moves never produces a third matrix, and every family in every frame is reached from one family in one frame by these two moves alone.

**One switch per frame, not one per pair of frames.** A frame determines $\mathsf W$ through $\mathsf W_{\mu\nu}=\beta(f_\mu,f_\nu)$, and the rule $\mathsf W'=\mathsf C^{\mathsf T}\mathsf W\mathsf C$ says that all the switches of all the frames are congruent copies of one another. So the frame carries both the arrays and the switch, and there is no freedom left over.

**The reading of the table.** A change of frame is invisible to every invariant, and so is a change of side. The four-dimensional families therefore carry one set of invariants between them, and the general theory of the element can be written once and read in any of them.

**What the table does not say.** It does not say that the arrays are equal. The left array and the right array of one element are different arrays in every frame, with different transposes, different symmetries and different kernels, and the table accounts for the differences with two matrices and no more.

## The 2×2 Family

**One family without a frame.** The isomorphism $A:\mathbb{B}\to M_2(\mathbb{C})$ reads the element at its own size and needs no frame. Its arrays carry the same invariants at half the size:
$$
\operatorname{Tr}A(\tilde Q)=2Q_t,\qquad
\det A(\tilde Q)=\langle\tilde Q\rangle_{\natural},\qquad
\operatorname{spec}A(\tilde Q)=\bigl\{Q_t+iB,\;Q_t-iB\bigr\},
$$
and $\operatorname{rank}A(\tilde Q)\in\{0,1,2\}$. The left and the right matrices carry the same data at twice the size, which is why their traces are twice as large, their determinants are squared and their ranks are doubled.

**There is no second side at size two.** In the $2\times2$ model the carrier is $M_2(\mathbb{C})$ itself, and the right action on it is the ordinary right matrix product $\mathsf A\mapsto\mathsf A\,A(\tilde Q)$. That is a linear map of the four-dimensional carrier, but it is not the left multiplication by a second matrix unless $A(\tilde Q)$ is scalar. So the element yields one matrix and not two, and the second family appears only when the element is read as acting on the carrier.

**The same mechanism at size two.** The transpose of a $2\times2$ matrix is a conjugation, by the fixed matrix $\varepsilon$,
$$
\varepsilon=i\sigma_2=\begin{pmatrix}0&1\\-1&0\end{pmatrix},
\qquad
\varepsilon^{2}=-\mathrm I_2,\qquad
\varepsilon^{\mathsf T}=-\varepsilon,
$$
and the conjugating matrix produces the conjugate of the element and not a second side,
$$
A(\tilde Q^{\natural})=\varepsilon\,A(\tilde Q)^{\mathsf T}\varepsilon^{-1}.
$$
At size two the transposition and the conjugation are the same operation, because the matrix already is the element. At size four they separate: the transposition returns the conjugate, and the transposition followed by the switch returns the other side.

## Summary

An element has a left matrix and a right matrix in each frame, so each frame gives two families of arrays. Associativity makes the left family multiplicative and the right family anti-multiplicative, makes every left matrix commute with every right matrix, and makes each family faithful. The two families coincide exactly on the centre, where both are scalar, so they meet in the line $\mathbb{C}\mathrm I_4$ and span seven dimensions. Their invariants agree: trace $4Q_t$, determinant $\langle\tilde Q\rangle_{\natural}^2$, characteristic polynomial $((X-Q_t)^2+B^2)^2$, spectrum $Q_t\pm iB$ twice, rank $0$, $2$ or $4$. Within a family the trace pairing is the scalar product $4\operatorname{Sc}(\tilde P\tilde Q)$; across the families it is $4P_tQ_t$, so only the centre couples the two sides.

Two matrices generate every relation. A change of frame is a conjugation by an invertible $\mathsf C$, applied to both sides at once because the frame belongs to the carrier and the side to the action. The switch $\mathsf W$ is the Gram matrix of the symmetric form $\beta(\tilde X,\tilde Y)=\operatorname{Sc}(\tilde X\tilde Y)$; it satisfies $\mathsf W R(\tilde Q)=L(\tilde Q)^{\mathsf T}\mathsf W$, hence $R(\tilde Q)=\mathsf W^{-1}L(\tilde Q)^{\mathsf T}\mathsf W$, and it is symmetric, nondegenerate and unique up to a nonzero scalar once symmetry is required. Each frame carries its own switch, the Gram matrix of $\beta$ on its own vectors, and the two changes are compatible, $\mathsf W'=\mathsf C^{\mathsf T}\mathsf W\mathsf C$, so the arrays and the switch of a frame are transported as one object.

No conjugation carries the left family onto the right, because a conjugation preserves the product while the right side reverses it, and a transposition alone returns the conjugate element and not the other side. At size two the same mechanism gives the conjugate of the element, with $\varepsilon=i\sigma_2$, and there is no second side, because the carrier already is the algebra.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{F}$, $\mathsf C$ | a frame of the algebra, and the matrix of the change to another frame |
| $L_{\mathcal{F}}(\tilde Q)$, $R_{\mathcal{F}}(\tilde Q)$ | the left and the right matrix of $\tilde Q$ in $\mathcal{F}$ |
| $L(\tilde Q)$, $R(\tilde Q)$ | the same, in the frame in force |
| $\mathbb{B}_L$, $\mathbb{B}_R$ | the left and the right family, as subalgebras of $M_4(\mathbb{C})$ |
| $A(\tilde Q)$ | the $2\times2$ matrix of the element |
| $B^2$ | $Q_x^2+Q_y^2+Q_z^2$ |
| $\langle\tilde Q\rangle_{\natural}$ | $Q_t^2+B^2$, the norm, and $\det A(\tilde Q)$ |
| $\beta(\tilde X,\tilde Y)$ | $\operatorname{Sc}(\tilde X\tilde Y)$, the symmetric scalar form |
| $\mathsf W$ | the switch, the Gram matrix $\beta(f_\mu,f_\nu)$ in the frame in force |
| $\mathsf W_{\mathcal{F}}$, $\mathsf W_{\mathcal{F}'}$ | the switch in two frames, related by $\mathsf W'=\mathsf C^{\mathsf T}\mathsf W\mathsf C$ |
| $\varepsilon=i\sigma_2$ | the $2\times2$ matrix of the transposition, $\varepsilon^{2}=-\mathrm I_2$ |

## Further Reading

- [Matrix Representations Conventions](matrix-representations-conventions.html), for the two matrices of an element in a working frame and the conventions used across the category.
- [$M_4(\mathbb{C})$ Pauli Representation](m4c-pauli-representation.html), for one four-dimensional instance of the general frame.
- [$M_4(\mathbb{C})$ Axis-Free Representation](m4c-axis-free-representation.html), for another four-dimensional instance, in the coefficient basis.
- [$M_2(\mathbb{C})$ Pauli Representation](m2c-pauli-representation.html), for the element size, the compression and the conjugate as a transpose.
- [The Biquaternion Algebra](the-biquaternion-algebra.html), for the multiplication table, the scalar product and the centre.
- [The Element, the Coordinates and the Conjugations in the Biquaternion Algebra](the-element-the-coordinates-and-the-conjugations.html), for the element, the four conjugations and the coordinate systems.
