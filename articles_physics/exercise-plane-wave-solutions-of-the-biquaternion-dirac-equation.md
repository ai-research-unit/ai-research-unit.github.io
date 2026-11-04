# __Exercise: Plane-Wave Solutions of the Biquaternion Dirac Equation__

## Introduction

This is a worked exercise on the biquaternion Dirac equation, written in the biquaternion algebra and on its elements. The field is one biquaternion, the operators are the frame cells, and every result below is a statement about elements and their products. The five cells are named where they are used and their arrays are printed once, in the closing block, beside the axis-free ones; the body prints no array. The parent article, *The Biquaternion Dirac Equation — Solutions and the Non-Relativistic Limit*, supplies the equation, the field, the two displays and the mass shell. The present exercise re-derives the parent's results in the algebra and supplies what the parent leaves implicit: the solutions written as elements, the normalisation in the biquaternion pairing, the spin sums as products of elements, the massless limit, the algebra of the cells and the change of the display.

**One equation, written out.** The symbol is a two-sided action, and it is written out rather than named by its factors,

$$
\slashed p:\ \tilde\Psi\longmapsto iE\,\tilde\Psi\,\vec e_x-i\sum_k p_k\,\vec e_k\,\tilde\Psi\,\vec e_y,\qquad p_0=E,
$$

so that the Dirac equation is $\slashed p\,\tilde\Psi=m\tilde\Psi$. One term carries a right factor alone, the other three a left factor $\vec e_k$ beside a right factor $\vec e_y$. Each cell replaces one coordinate derivative: the time cell the derivative in $t'$, and the three space cells the derivatives in $x_k$; the cells themselves are named in the next section.

**One equation on the two values.** The field carries the chirality subscript of *Special Element and Peirce Conventions*, §*The Chirality Convention*, and its two parts are the two values of the chirality cell: $\tilde\Psi=\tilde\Psi_L+\tilde\Psi_R$, the value $-1$ written $L$ and the value $+1$ written $R$. A left multiplication keeps the value, a product takes the value of its right factor, and a scalar multiple keeps the value. Each of the four terms of the symbol carries a right factor $\vec e_x$ or $\vec e_y$, and right multiplication by either unit exchanges the two values, so the symbol exchanges them: the equation is the pair

$$
\slashed p\,\tilde\Psi_R=m\,\tilde\Psi_L,\qquad \slashed p\,\tilde\Psi_L=m\,\tilde\Psi_R,
$$

one equation on each part, coupled by the mass and by nothing else.

**The seven problems** are: **(1)** the solutions at rest and at general momentum; **(2)** the covariant normalisation and the orthogonality; **(3)** the spin sums; **(4)** the massless limit and the locking of helicity to the value; **(5)** the algebra of the cells and the change of the display; **(6)** the biquaternionic mass shell; **(7)** the helicity pieces and the piece determinant. Problems 1, 2, 4 and 6 use the action on elements, Problems 3 and 7 the symbol read with it, and Problem 5 the cells themselves.

## The Cells of the Frame

**The composition law.** A cell is a two-sided multiplication $L_aR_b$, composed with the three laws of *The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure*, §*The Operators on an Algebra*, whose reversal of the right indices is the only subtlety: a product of two cells comes out with its indices interchanged, and $Q\mapsto aQb$ is therefore unambiguous. Every computation below is a use of those laws on the four units, and none of them is restated here.

**The scalar $i$ is central**, so multiplication by $i$ on the left and on the right are one operator, and a factor $i$ in front of a cell is pushed into its argument: $iR_{\vec e_x}=R_{i\vec e_x}$, $iL_{\vec e_k}R_{\vec e_y}=L_{i\vec e_k}R_{\vec e_y}$, $-iR_{\vec e_z}=R_{-i\vec e_z}$. With $i^2=-1$ and $\vec e_k^2=-e_t$ a product of two cells then collapses in one line:

$$
(R_{i\vec e_x})^2=R_{i^2\vec e_x^2}=R_{e_t}=1,\qquad
(L_{i\vec e_k}R_{\vec e_y})^2=L_{i^2\vec e_k^2}R_{\vec e_y^2}=L_{e_t}R_{-e_t}=-1,\qquad
(R_{-i\vec e_z})^2=R_{e_t}=1 .
$$

Each line is one use of $i^2=-1$ and one use of $\vec e_k^2=-e_t$; both minus signs are needed, and dropping either of them flips the square.

**The five cells.** The cell of the coordinate $x_\mu$ is

$$
c_\mu=L_{i e_\mu}R_{\vec e_{\nu(\mu)}},\qquad \nu(t)=x,\quad \nu(k)=y ,
$$

that is $c_0=R_{i\vec e_x}$ and $c_k=L_{i\vec e_k}R_{\vec e_y}$, the scalar unit $e_t$ multiplying as the identity. Each cell is a left multiplication times a right one, and the time cell is a pure right multiplication. The index $\mu$ is the coordinate index: the cell is the one paired with $\partial/\partial x_\mu$ in the $\mathbb{M}_-$ frame, and the derivative is taken with respect to $x_\mu=(t',x,y,z)$, not with respect to $Q_\mu$. That is the precise sense in which the cells align with the coordinates.

**What each cell is.**

| cell | what it does |
|---|---|
| $R_{i\vec e_x}$ | paired with $\partial/\partial t'$; exchanges the two values |
| $L_{i\vec e_k}R_{\vec e_y}$ | paired with $\partial/\partial x_k$; each squares to $-1$; exchanges the two values |
| $R_{-i\vec e_z}$ | the chirality cell; its value is $-1$ on the $L$ part and $+1$ on the $R$ part |
| $\Omega=c_0c_1c_2c_3=-R_{\vec e_z}$ | the volume cell; $\Omega^2=-1$, and $i\Omega=R_{-i\vec e_z}$ is the chirality cell |

The right factor $\vec e_y$ of the three space cells is not a spatial axis of the frame: it is the unit on which the value is read, and the axis enters through the left factor $\vec e_k$ alone. The unit $\vec e_y$ is what makes the three space cells square to $-1$ while the time cell squares to $+1$, and that asymmetry belongs to the pair of units $(e_t,\vec e_y)$, not to the triad.

**The other display.** The display is changed by right multiplication by the unit element $\tilde W=(e_t+\vec e_y)/\sqrt2$, with $\tilde W^{-1}=\tilde W^{\natural}=(e_t-\vec e_y)/\sqrt2$, so that $\tilde W^{-1}\vec e_y\tilde W=\vec e_y$ and

$$
\tilde W^{-1}(i\vec e_x)\tilde W=i\vec e_z,\qquad \tilde W^{-1}(-i\vec e_z)\tilde W=i\vec e_x .
$$

In that display the cells read

$$
(R_{i\vec e_x})^{d}=R_{i\vec e_z},\qquad
(L_{i\vec e_k}R_{\vec e_y})^{d}=L_{i\vec e_k}R_{\vec e_y},\qquad
(R_{-i\vec e_z})^{d}=R_{i\vec e_x},
$$

by the rule of Problem 5. The spatial cells do not change, and the temporal cell and the chirality cell exchange their parts: in that display the temporal cell keeps the value and the chirality cell exchanges it, which is why the non-relativistic limit is simplest there.

## Why Four Left Multiplications Do Not Suffice

**The four units cannot be four left multiplications.** $e_t=1$ is the identity, so it commutes with every $\vec e_k$: $\{e_t,\vec e_k\}=2\vec e_k\neq0$, while the cells must anticommute. No scalar helps, since a scalar commutes with everything. So no assignment of the four units to four left multiplications can satisfy the anticommutation relations.

**The dimension decides it.** Left multiplication is an injective complex-linear map of $\mathbb B$ into its operator algebra, so the four left multiplications span at most a four-complex-dimensional algebra, closed under composition; four cells that anticommute generate a sixteen-dimensional one. The count is the one of §*The Carrier and the Dimension Count*, and it says that one of the cells must act on the right. The time cell is the one: it is a pure right multiplication, and the other three are left times right.

**Why this completion.** A completion of the four units into sixteen dimensions is not unique, and the one used here is the two-sided one, because the exercise needs two things at once: a cell that multiplies on the right, so that the symbol exchanges the two values, and a value that distinguishes the two parts of one element. A completion that keeps every unit on the left supplies neither.

## The Carrier and the Dimension Count

**The carrier is the algebra.** The biquaternion algebra has complex dimension four, on the basis $e_t,\vec e_x,\vec e_y,\vec e_z$, and the field is one element, so the field has four complex components. The cells are the complex-linear operators on that carrier, and the carrier is the algebra itself.

**How four and four become sixteen.** The two regular families are not disjoint. Each has complex dimension four, and they meet in the scalars, because the identity is $e_t$. Their sum therefore has dimension $4+4-1=7$, not $16$, and the direct sum $\mathbb B\oplus\mathbb B$ has complex dimension eight, so adding the right family to the left one doubles nothing. Composition does the doubling: the operator $L_aR_b$ is bilinear in the pair $(a,b)$, so the operators it produces span the tensor product of the two families, of complex dimension $4\times4=16$. The product of two operators is a new operator, and the product of the two four-dimensional families fills the whole operator algebra: $4+4=7$, but $4\times4=16$.

## Frame Covariance and the Volume Cell

**Frame covariance.** The cells are written in a frame, and no direction is privileged. Let $(t_1,t_2,t_3)$ be an orthonormal triad and $(u,w)$ an orthogonal pair of unit vectors; then

$$
R_{iw}\qquad\text{and}\qquad L_{it_k}R_u
$$

satisfy the same relations for every such choice: the two squares are $R_{e_t}$ and $L_{e_t}R_{-e_t}$, because $w^2=u^2=-e_t$ and $i^2=-1$, and the cross term between a time cell and a space cell carries the right factor $iwu+uiw$, which vanishes because $u$ and $w$ are orthogonal and therefore anticommute. The exercise takes $t_k=\vec e_k$, $u=\vec e_y$, $w=\vec e_x$. A change of the triad is a spatial rotation; a change of the pair is a change of the value, and neither changes the physics.

**The volume cell.** Since left and right multiplications commute, the product of the four coordinate cells is

$$
c_0c_1c_2c_3=R_{i\vec e_x}\,L_{i\vec e_x}R_{\vec e_y}\,L_{i\vec e_y}R_{\vec e_y}\,L_{i\vec e_z}R_{\vec e_y}=-R_{\vec e_z},
$$

and $i$ times it is the chirality cell, $i\Omega=i(-R_{\vec e_z})=R_{-i\vec e_z}$. The reading is the collapse rule: the three left factors give $i^3\vec e_x\vec e_y\vec e_z=i\,e_t$, the four right factors give $\vec e_y\vec e_y\vec e_y\,i\vec e_x=i\vec e_z$ in the reversed order that $R_aR_b=R_{ba}$ imposes, and the two together give $L_{i}R_{i\vec e_z}$, which is $-R_{\vec e_z}$ because $i\cdot i=-1$ and the scalar acts on either side.

**The anticommutators.** For a time cell against a space cell,

$$
R_{i\vec e_x}\,L_{i\vec e_k}R_{\vec e_y}+L_{i\vec e_k}R_{\vec e_y}\,R_{i\vec e_x}
=L_{i\vec e_k}\bigl(R_{i\vec e_z}+R_{-i\vec e_z}\bigr)=0,
$$

because $i\vec e_x\vec e_y=i\vec e_z$ while $\vec e_y\,i\vec e_x=-i\vec e_z$, and the two coefficients differ by the sign of $i$. For two space cells,

$$
L_{i\vec e_j}R_{\vec e_y}\,L_{i\vec e_k}R_{\vec e_y}+L_{i\vec e_k}R_{\vec e_y}\,L_{i\vec e_j}R_{\vec e_y}
=L_{i^2(\vec e_j\vec e_k+\vec e_k\vec e_j)}=0,
$$

because $i$ is central and the quaternion units anticommute. So $\{c_\mu,c_\nu\}=2\varepsilon_\mu\delta_{\mu\nu}$ with $\varepsilon=(1,-1,-1,-1)$, and the sign vector is the one the products give and not a metric chosen in advance.

## The Field and the Equation

**The field.** The field is one element $\tilde\Psi$ of $\mathbb B$ with its two values $\tilde\Psi=\tilde\Psi_L+\tilde\Psi_R$ (§*The Chirality Convention*). Nothing further is needed to state the field: the two values are the two values of one operator, and the field is the element itself.

**The equation.** For a plane wave of four-momentum $(E,\vec p)$ each cell is contracted with the momentum of the coordinate it is paired with, and the two-sided Dirac equation is the eigenvalue problem $\slashed p\,\tilde\Psi=m\tilde\Psi$, written on the element as

$$
E\,\tilde\Psi\,i\vec e_x-i\,(\vec p\cdot\vec e)\,\tilde\Psi\,\vec e_y=m\,\tilde\Psi .
$$

The symbol carries the two-sided character: one term is a pure right multiplication, the other three are left times right. The symbol exchanges the two values and the mass keeps them, so the equation is the pair of the introduction,

$$
\slashed p\,\tilde\Psi_R=m\,\tilde\Psi_L,\qquad \slashed p\,\tilde\Psi_L=m\,\tilde\Psi_R .
$$

**Conventions.** Natural units $\hbar=c=1$ in the solutions; $\hbar$ and $c$ are restored in Problem 6. The time cell squares to $+1$ and the three space cells to $-1$, so the sign vector of the squares is $(1,-1,-1,-1)$ and the symbol is the contraction with the flat metric of the $\mathbb{M}_-$ gradient. The helicity direction is $\vec u_p=\vec p/\lvert\vec p\rvert$, and the helicity element is $\Xi=i\vec u_p$, a root of the central value $+1$, $\Xi^2=e_t$. The Hermitian conjugation $^{*}$ is the coefficient conjugation composed with the quaternion conjugation, $\tilde Q^{*}=\overline{\tilde Q^{\natural}}$.

## Problem 1: The solutions at rest and at general momentum

**Statement.** Solve $\slashed p\,\tilde w=m\tilde w$ and $\slashed p\,\tilde v=-m\tilde v$ explicitly at rest and at general momentum, in the two displays.

**Solution.** Eliminating the right part of the pair gives $\slashed p\,\slashed p\,\tilde\Psi_L=m^2\tilde\Psi_L$; the symbol squares to the interval, as Problem 3 shows, so the pair is soluble exactly on the mass shell

$$
E^2=\vec p^{\,2}+m^2 .
$$

On the shell the right part is free and the left part is determined by the action of the symbol:

$$
\boxed{\;\tilde\Psi_L=\frac1m\,\slashed p\,\tilde\Psi_R=\frac1m\Bigl(iE\,\tilde\Psi_R\,\vec e_x-i(\vec p\cdot\vec e)\,\tilde\Psi_R\,\vec e_y\Bigr)\;}
$$

The right part is two-complex-dimensional, so the space of positive-frequency solutions at fixed momentum is two-dimensional, and it carries no further label. The label is the helicity, and it is the two values of the helicity element: $\Xi$ commutes with the symbol, as Problem 7 shows, so its two eigenspaces cut the space into two one-dimensional pieces, one for each value.

**The amplitudes.** Along a helicity eigenstate the two parts have unequal size, and the ratio is fixed. Writing $\langle\tilde Q\rangle_{*}$ for the Hermitian norm,

$$
\frac{\langle\tilde\Psi_L\rangle_{*}}{\langle\tilde\Psi_R\rangle_{*}}=\frac{E\mp\lvert\vec p\rvert}{E\pm\lvert\vec p\rvert},
$$

with the upper sign for helicity $+1$ and the lower for helicity $-1$: the left part dominates for the negative helicity and the right part for the positive one, and at the massless point one of the two vanishes. The squared amplitudes are the two factors whose product is $m^2$, and that product is what makes the covariant normalisation of Problem 2 come out at $2m$.

**The negative-frequency branch.** The same construction with $m$ replaced by $-m$:

$$
\boxed{\;\tilde v_L=-\frac1m\,\slashed p\,\tilde v_R\;}
$$

so that $\slashed p\,\tilde v=-m\tilde v$. The two branches together give the two frequency signs, and the two helicity values within each branch give the four-dimensional complex solution space of the parent.

**At rest.** With $\vec p=0$ and $E=m$ the symbol is the time cell alone, and the equation reads

$$
\tilde w(0)\,\vec e_x=-i\,\tilde w(0),\qquad \tilde v(0)\,\vec e_x=+i\,\tilde v(0),
$$

a right-eigenvector condition on the unit $\vec e_x$. Each solution space is two-dimensional over $\mathbb C$, and a basis of the positive-frequency space is

$$
e_t+i\vec e_x,\qquad \vec e_z+i\vec e_y,
$$

with the two signs exchanged for the negative-frequency space. The rest frame supplies no direction, so the unit on which the condition is read is a choice of frame and not a physical axis; it is the unit the time cell carries.

**The other display.** Right multiplication by $\tilde W$ carries a solution of one display to a solution of the other, because the cells are conjugated and the element is the same element: if $\slashed p\,\tilde\Psi=m\tilde\Psi$ then the symbol of the other display sends $\tilde\Psi\tilde W$ to $m\tilde\Psi\tilde W$. In that display the temporal cell carries the unit $\vec e_z$, whose two right eigenspaces are the two values, so the rest solutions read

$$
\tilde w(0)\,\tilde W\,\vec e_z=-i\,\tilde w(0)\,\tilde W,\qquad
\tilde v(0)\,\tilde W\,\vec e_z=+i\,\tilde v(0)\,\tilde W .
$$

At rest each branch therefore sits in a single value in that display — the $L$ value for the positive branch and the $R$ value for the negative branch — while in the first display both branches are right-eigenvectors of $\vec e_x$ and carry no value at all. The two values are mixed again as soon as the momentum is not zero. That is the biquaternion content of the parent's statement that the large component of the rest solution is a single component: the large component is the value the temporal cell does not mix.

## Problem 2: Covariant normalisation and orthogonality

**Statement.** Verify $\langle\tilde w,\tilde w\rangle_{\mathrm D}=2m$, $\langle\tilde v,\tilde v\rangle_{\mathrm D}=-2m$, $\langle\tilde w,\tilde v\rangle_{\mathrm D}=0$, and the Hermitian products.

**Solution.** The Dirac pairing is the Hermitian one twisted by the timelike frame cell,

$$
\langle\tilde\Psi,\tilde\Phi\rangle_{\mathrm D}=\mathrm{Tr}\bigl(\tilde\Psi^{*}\tilde\Phi\,i\vec e_x\bigr),
$$

the pairing of the parent, with the trace of *Norm and Unitary Conventions*. The twist is the representative of the time cell, and it is what makes the pairing a Lorentz scalar; the pairing couples the two values crossed, so that $\tilde\Psi_L$ is paired with $\tilde\Phi_R$ and $\tilde\Psi_R$ with $\tilde\Phi_L$, and the two diagonal terms vanish in the trace, so only the crossed terms remain. The single algebraic input of the section is the unit-vector identity

$$
(i\vec u_p)^2=i^2\,\vec u_p^{\,2}=(-1)(-e_t)=e_t,
$$

the biquaternion form of the statement that a unit direction squares to $-1$ up to the two minus signs, which cancel.

**The four values.** For the positive-frequency solution the pairing is twice the geometric mean of the two amplitude norms, $\sqrt{E\mp\lvert\vec p\rvert}\,\sqrt{E\pm\lvert\vec p\rvert}=\sqrt{E^2-\vec p^{\,2}}=m$, so

$$
\langle\tilde w_\pm,\tilde w_\pm\rangle_{\mathrm D}=2m .
$$

For the negative-frequency branch the left part carries the minus sign of Problem 1 and the same computation gives $-2m$:

$$
\langle\tilde v_\pm,\tilde v_\pm\rangle_{\mathrm D}=-2m .
$$

The mixed term vanishes because the two products are opposite and cancel:

$$
\langle\tilde w_\pm,\tilde v_\pm\rangle_{\mathrm D}=0,
$$

and opposite helicities are orthogonal for the same reason, $\langle\tilde w_+,\tilde w_-\rangle_{\mathrm D}=0$, since the two right parts are eigenvectors of $\Xi$ with opposite values.

**The Hermitian products.** The untwisted product is the positive one and does not cancel:

$$
\mathrm{Tr}\bigl(\tilde w_\pm^{*}\tilde w_\pm\bigr)=(E\mp\lvert\vec p\rvert)+(E\pm\lvert\vec p\rvert)=2E,\qquad
\mathrm{Tr}\bigl(\tilde v_\pm^{*}\tilde v_\pm\bigr)=2E .
$$

The bilinear is a Lorentz scalar and its value $2m$ is the covariant normalisation; it is not the probability density, which is the positive quantity $\mathrm{Tr}(\tilde w^{*}\tilde w)=2E$. As a numerical check, for $m=1$ and $\lvert\vec p\rvert=0.6$, hence $E=1.166190$, direct evaluation gives $\langle\tilde w,\tilde w\rangle_{\mathrm D}=2.0000$, $\langle\tilde v,\tilde v\rangle_{\mathrm D}=-2.0000$, $\langle\tilde w,\tilde v\rangle_{\mathrm D}=0$, and $\mathrm{Tr}(\tilde w^{*}\tilde w)=\mathrm{Tr}(\tilde v^{*}\tilde v)=2.3324=2E$.

## Problem 3: The spin sums

**Statement.** Verify that for every element $\tilde\Phi$,

$$
\sum_{\pm}\tilde w_\pm\,\langle\tilde w_\pm,\tilde\Phi\rangle_{\mathrm D}=\slashed p\,\tilde\Phi+m\,\tilde\Phi,\qquad
\sum_{\pm}\tilde v_\pm\,\langle\tilde v_\pm,\tilde\Phi\rangle_{\mathrm D}=\slashed p\,\tilde\Phi-m\,\tilde\Phi .
$$

**Solution.** The left-hand side is a sum of two products of elements, one per helicity, and it is a rank-two operator read as a product: each term is the solution multiplied by the number its pairing with $\tilde\Phi$ returns. The two solutions at fixed momentum are the two helicity eigenstates, and their right parts span the right part of the carrier, so the sum reproduces $\tilde\Phi$ on the right and, through the action, on the left. Written out on the right-hand side,

$$
\sum_{\pm}\tilde w_\pm\,\langle\tilde w_\pm,\tilde\Phi\rangle_{\mathrm D}
=iE\,\tilde\Phi\,\vec e_x-i\sum_k p_k\,\vec e_k\,\tilde\Phi\,\vec e_y+m\,\tilde\Phi ,
$$

which is the symbol plus the mass. The negative-frequency sum is identical in structure with the roles of the two values interchanged, and gives the symbol minus the mass. Both hold for every element and not only on the solutions, and both were checked on a basis of $\mathbb B$.

**The on-shell identity.** The two sums are complementary, and their product is the interval minus the mass squared:

$$
(\slashed p+m)(\slashed p-m)=\slashed p^2-m^2 .
$$

The symbol squares to a multiple of the identity. Each term of the square is a product of two cells, and the collapse rule gives

$$
\slashed p^2=E^2R_{(i\vec e_x)^2}+p_jp_k\,L_{i\vec e_j}R_{\vec e_y}L_{i\vec e_k}R_{\vec e_y}
=E^2+p_jp_k\,L_{-\vec e_j\vec e_k}R_{-e_t}
=E^2-\vec p^{\,2},
$$

with the plus in front of the double sum because the square of the minus of the space term is plus, and with the cross terms vanishing because the time cell and a space cell anticommute. The result is the interval times the identity, $\slashed p^2=p^2$ with $p^2=E^2-\vec p^{\,2}$, and on the mass shell $\slashed p^2=m^2$, so $(\slashed p+m)(\slashed p-m)=0$ and the two branches close the solution space.

**The trace.** Each cell carries the right factor $\vec e_x$ or $\vec e_y$, and right multiplication by either unit exchanges the two values, so every cell is off-diagonal in the value and its trace vanishes. The identity on the carrier has trace four, so the trace of $\slashed p+m$ is $4m$: the mass is the only term the trace sees, which is the algebraic statement that the symbol has no scalar part.

## Problem 4: The massless limit and the locking of helicity to the value

**Statement.** Take $m=0$ and exhibit the locking of helicity to the value.

**Solution.** At $m=0$ the mass term is gone and the pair decouples into two independent equations, one on each value:

$$
\slashed p\,\tilde\Psi_R=0,\qquad \slashed p\,\tilde\Psi_L=0 .
$$

For $m=0$ the dispersion is $E=\lvert\vec p\rvert$, the action on each value loses rank, and each kernel is one-dimensional, spanned by a helicity eigenstate:

$$
\Xi\,\tilde\Psi_R=+\tilde\Psi_R\ \ \text{and}\ \ \tilde\Psi_L=0,\qquad
\Xi\,\tilde\Psi_L=-\tilde\Psi_L\ \ \text{and}\ \ \tilde\Psi_R=0 .
$$

The two labels are locked: **positive helicity goes with right-handedness and negative helicity with left-handedness.** The mass is the only term that couples the two values, and setting it to zero decouples them; at fixed momentum each equation selects one complex helicity state, and the two together give the two massless states.

**The position-space reading.** Restoring $\hbar=c=1$ and replacing the momentum by the derivative, $E\to i\partial_{t'}$ and $\vec p\to-i\nabla$, the massless equation takes the form

$$
\partial_{t'}\tilde\Psi\,\vec e_x=-\bigl(\nabla\cdot\vec e\bigr)\tilde\Psi\,\vec e_y ,
$$

one equation on the element, whose two solutions are the two locked states above. The magnitude $\lvert\vec p\rvert$, which the energy carries at $m=0$, is part of the right-hand side and cannot be dropped.

## Problem 5: The algebra of the cells and the change of the display

**Statement.** Verify the anticommutation relations, identify the chirality cell, and determine how the cells change under the change of the display.

**Solution.** The anticommutators were verified in §*Frame Covariance and the Volume Cell* from the multiplication table. The chirality cell is

$$
R_{-i\vec e_z},\qquad (R_{-i\vec e_z})^2=R_{(-i\vec e_z)^2}=R_{i^2\vec e_z^2}=R_{e_t}=1,
$$

and it anticommutes with every cell. With the three space cells written with no leading $i$ and with $R_aR_b=R_{ba}$,

$$
R_{-i\vec e_z}R_{i\vec e_x}+R_{i\vec e_x}R_{-i\vec e_z}=R_{-\vec e_y}+R_{\vec e_y}=0,
$$
$$
L_{i\vec e_k}\bigl(R_{-i\vec e_z}R_{\vec e_y}+R_{\vec e_y}R_{-i\vec e_z}\bigr)=L_{i\vec e_k}\bigl(R_{-i\vec e_x}+R_{i\vec e_x}\bigr)=0,
$$

because $\vec e_x\vec e_z=-\vec e_y$ while $\vec e_z\vec e_x=+\vec e_y$ in the first line, and $\vec e_z\vec e_y=-\vec e_x$ while $\vec e_y\vec e_z=+\vec e_x$ in the second. Each time the two products differ by the sign of one unit, and the factor $i\cdot(-i)=+1$ does not change it. Compare the squares: there the two factors contribute $i\cdot i=i^2=-1$.

**The action on the two values.** The three cells act on the two values as follows. The time cell and each space cell exchange the two values, because their right factors are units whose right multiplication exchanges them; the chirality cell keeps them, its value being $-1$ on the $L$ part and $+1$ on the $R$ part. On the elements themselves,

$$
\tilde\Psi_L\longmapsto i\,\tilde\Psi_L\,\vec e_x\in R,\qquad
\tilde\Psi_R\longmapsto L_{i\vec e_k}R_{\vec e_y}\tilde\Psi_R\in L,\qquad
\tilde\Psi_{L}\longmapsto-\tilde\Psi_L,\quad \tilde\Psi_R\longmapsto+\tilde\Psi_R .
$$

These are the two facts the whole exercise rests on, and they are read from the multiplication table of the four units: right multiplication by $\vec e_x$ or by $\vec e_y$ carries each value into the other, and left multiplication keeps the value.

**The change of the display.** Right multiplication by $\tilde W=(e_t+\vec e_y)/\sqrt2$ is a unit element, and it sends one display to the other:

$$
\tilde\Psi_d=\tilde\Psi_c\,\tilde W .
$$

The cells transform by conjugation with $\tilde W$: a right multiplication goes to $R_a\mapsto R_{\tilde W^{-1}a\tilde W}$, and a left multiplication is unchanged, because the left factor stands against the argument in both displays. Since $\tilde W^{-1}(i\vec e_x)\tilde W=i\vec e_z$, $\tilde W^{-1}(-i\vec e_z)\tilde W=i\vec e_x$ and $\tilde W^{-1}\vec e_y\tilde W=\vec e_y$,

$$
(R_{i\vec e_x})^{d}=R_{i\vec e_z},\qquad (L_{i\vec e_k}R_{\vec e_y})^{d}=L_{i\vec e_k}R_{\vec e_y},\qquad (R_{-i\vec e_z})^{d}=R_{i\vec e_x}.
$$

The spatial cells are unchanged because the right factor $\vec e_y$ is fixed by $\tilde W$; only the time cell and the chirality cell change, and they exchange their parts. In the new display the time cell is diagonal on the two values and the chirality cell exchanges them, which is why that display separates the large and the small part in the non-relativistic limit. The change is a right multiplication of the element and not a linear map of something other than the element: it moves the display, and the element is the same element.

**The Lorentz generators.** In the algebra they are the commutators of the cells, $S_{\mu\nu}=\frac i4[c_\mu,c_\nu]$, and they are again two-sided multiplications; the $i$'s inside the cells cancel first:

$$
[\,R_{i\vec e_x},\,L_{i\vec e_k}R_{\vec e_y}\,]=L_{i\vec e_k}\bigl(R_{\vec e_y i\vec e_x}-R_{i\vec e_x\vec e_y}\bigr)=L_{i\vec e_k}\bigl(R_{-i\vec e_z}-R_{i\vec e_z}\bigr)=-2L_{i\vec e_k}R_{i\vec e_z}=2L_{\vec e_k}R_{\vec e_z},
$$
$$
[\,L_{i\vec e_j}R_{\vec e_y},\,L_{i\vec e_k}R_{\vec e_y}\,]=L_{i\vec e_j}L_{i\vec e_k}R_{\vec e_y\vec e_y}-L_{i\vec e_k}L_{i\vec e_j}R_{\vec e_y\vec e_y}=L_{\vec e_j\vec e_k}-L_{\vec e_k\vec e_j}=2L_{\vec e_j\vec e_k}\quad(j\neq k),
$$

because $\vec e_y\vec e_x=-\vec e_z$ while $\vec e_x\vec e_y=+\vec e_z$, $\vec e_y\vec e_y=-e_t$, and $i^2=-1$ twice: once in $L_{i\vec e_k}R_{i\vec e_z}=i^2L_{\vec e_k}R_{\vec e_z}$ and once in $L_{i\vec e_j}L_{i\vec e_k}=i^2L_{\vec e_j\vec e_k}$. Hence

$$
S_{0k}=\frac i2\,L_{\vec e_k}R_{\vec e_z},\qquad
S_{jk}=\frac i2\,L_{\vec e_j\vec e_k},
$$

with one $i$ left in each and no $i$ inside a unit. Both keep the two values, since a left multiplication commutes with every right multiplication and a right multiplication by $\vec e_z$ commutes with the chirality cell, so $[S_{\mu\nu},R_{-i\vec e_z}]=0$ for every pair. The generators are the cell commutators read as operators, and each is a two-sided multiplication; nothing in them is a matrix.

## Problem 6: The biquaternionic mass-shell condition

**Statement.** Verify the mass-shell condition of the parent and recover the relativistic energy–momentum relation.

**Solution.** The plane-wave ansatz carries the wave biquaternion

$$
\tilde P/\hbar=\frac{i\omega}{c}\,e_t+\vec k,\qquad \vec k=k_1\vec e_x+k_2\vec e_y+k_3\vec e_z ,
$$

an element of the material sector $\mathbb{M}_-$: imaginary scalar part and real vector part. Its quaternionic norm is the norm of *Algebra and Element Conventions*, §*The Conjugations*, so

$$
\langle\tilde P/\hbar\rangle_{\natural}=\left(\frac{i\omega}{c}\right)^2+k_1^2+k_2^2+k_3^2=-\frac{\omega^2}{c^2}+\vec k^2 ,
$$

the sign change being $i^2=-1$. The dispersion relation is $\omega^2=c^2\vec k^2+m^2c^4/\hbar^2$, and substituting it,

$$
\langle\tilde P/\hbar\rangle_{\natural}=-\frac{1}{c^2}\left(c^2\vec k^2+\frac{m^2c^4}{\hbar^2}\right)+\vec k^2=-\frac{m^2c^2}{\hbar^2},
$$

which is the parent's condition

$$
\boxed{\;\tilde P\tilde P^{\natural}=-m^2c^2\;}.
$$

Equivalently, with $E=\hbar\omega$ and $\vec p=\hbar\vec k$, the norm is quadratic, so $\langle\tilde P/\hbar\rangle_{\natural}=\langle\tilde P\rangle_{\natural}/\hbar^2=-m^2c^2/\hbar^2$. The mass shell is not a new postulate: it is the statement that the four-wavevector is a timelike element of $\mathbb{M}_-$ with the same quaternionic norm as the four-momentum.

The two roots $\omega=\pm\sqrt{c^2\vec k^2+m^2c^4/\hbar^2}$ are the two frequency branches, and they are the two families $\tilde w$ and $\tilde v$ constructed above; the two helicity values within each branch give the four-dimensional complex solution space. As a numerical check, for an electron ($mc^2=0.510998950\ \mathrm{MeV}$) at $\lvert\vec p\rvert=1\ \mathrm{MeV}/c$, the dispersion gives $E=1.122996\ \mathrm{MeV}$ and $E^2-\vec p^2c^2=0.261120\ \mathrm{MeV}^2=(mc^2)^2$; the wave biquaternion has $\langle\tilde P/\hbar\rangle_{\natural}=-6.706054\times10^{24}\ \mathrm{m}^{-2}$, agreeing with $-m^2c^2/\hbar^2$ to the digits shown.

## Problem 7: The helicity pieces and the piece determinant

**Statement.** Show that the symbol commutes with the helicity element, that the carrier splits into two two-dimensional pieces, one per helicity, compute the determinant of the symbol on each, and read the mass shell as the vanishing of that determinant.

**Solution.** The symbol is $\slashed p$ of §*The Field and the Equation*, and the massive symbol is $\mathcal D(p)=\slashed p-m$.

**The symbol squares to the interval.** The square is the interval, $\slashed p^2=p^2$ with $p^2=E^2-\vec p^{\,2}$, by the collapse rule and the anticommutation of Problem 3.

**The helicity grading.** For $\vec p\neq0$ put

$$
\Xi=i\,\vec u_p,\qquad \Xi^2=i^2\,\vec u_p^{\,2}=(-1)(-e_t)=e_t ,
$$

so that left multiplication by $\Xi$ has eigenvalues $\pm1$, each twice, and its two eigenspaces are two-dimensional. The symbol commutes with it. The time term multiplies on the right alone, and a left multiplication passes through a right one; the mass is a scalar and passes too; the space terms multiply on the left by $\vec p\cdot\vec e$ and on the right by $\vec e_y$, and $\Xi$ commutes with $\vec p\cdot\vec e$ because the two elements are proportional, and with $\vec e_y$ because one factor acts on the left and the other on the right. Hence the symbol keeps the two eigenspaces of $\Xi$, and each carries a two-dimensional piece of the carrier.

**The piece determinant.** On a piece the symbol obeys $\slashed p_\pm^2=p^2$ and is not a multiple of the identity for $\vec p\neq0$, so for $p^2>0$ its two eigenvalues are $\pm\sqrt{p^2}$ and

$$
\det\bigl(\slashed p_\pm-m\bigr)=\bigl(\sqrt{p^2}-m\bigr)\bigl(-\sqrt{p^2}-m\bigr)=m^2-p^2=\tilde P\tilde P^{\natural}+m^2,
$$

using $\tilde P\tilde P^{\natural}=-p^2$ of Problem 6. The same number comes from the eigenvalues. Since $\tilde P=iE+\vec p\cdot\vec e$, the left multiplication by $\tilde P$ has the two eigenvalues $\lambda_\pm=i\bigl(E\mp\lvert\vec p\rvert\bigr)$, each twice, and one more $i^2=-1$ gives $\lambda_+\lambda_-=i^2\bigl(E^2-\vec p^{\,2}\bigr)=-(E^2-\vec p^{\,2})=\tilde P\tilde P^{\natural}$. The determinant on a piece is $\lambda_+\lambda_-+m^2$. The mass term is a multiple of the identity, so it shifts the two piece eigenvalues equally and enters each piece determinant once, and the determinant of the whole symbol is the product of the two,

$$
\boxed{\;\det\mathcal D(p)=\bigl(m^2-p^2\bigr)^2\;},
$$

the square of the Klein–Gordon symbol. The two pieces carry the same pair of eigenvalues: they are isospectral, and their common determinant is the frame-independent datum a single piece carries.

**The mass shell is the vanishing of a piece determinant.** Each determinant is $m^2-p^2$, so the symbol is singular exactly when $p^2=m^2$. At that momentum each piece has a one-dimensional kernel: two zero modes, one per helicity, and these are the two helicity states of the particle. Off the shell each piece is invertible and the propagator is the inverse of the symbol.

**Worked case, $\vec p\parallel\vec e_z$.** With $B=\lvert\vec p\rvert$ and the mass $m$, the pieces are the two helicity eigenspaces. For $m=1.3$, $E=2$, $B=0.9$: $p^2=3.19$ and $\sqrt{p^2}=1.786057$, so each piece determinant is $m^2-p^2=-1.5$, each piece spectrum is $\{-3.086057,\,0.486057\}$, and the determinant of the symbol is $2.25=(m^2-p^2)^2$.

**Worked case, on the shell.** For $m=1.3$ and $\vec p=(0.4,-0.7,0.9)$ the energy is $E=\sqrt{m^2+\vec p^{\,2}}=1.774824$. Each piece determinant is zero, each piece spectrum is $\{-2m,\,0\}=\{-2.6,\,0\}$, and the whole symbol has rank two, with a one-dimensional kernel per helicity.

**Numerical check.** The identities were recomputed on 100 random real four-momenta. The departure of the symbol from commuting with left multiplication by $\Xi$ was at most $6.7\times10^{-16}$; the piece determinant from $m^2-p^2$, $8.0\times10^{-15}$; the two piece spectra from each other, $4.0\times10^{-15}$; $\slashed p^2$ from $p^2$, $1.8\times10^{-15}$; the eigenvalues of left multiplication by $\tilde P$ from $i(E\mp\lvert\vec p\rvert)$, $2.7\times10^{-15}$, and their product $\lambda_+\lambda_-$ from $\tilde P\tilde P^{\natural}$, $7.1\times10^{-15}$; the determinant of the symbol from $(m^2-p^2)^2$, $8.7\times10^{-14}$.

**What the splitting is, and what it is not.** It says that the mass does not see the helicity, and therefore that a massive state is a pair of helicity pieces with equal spectra and unequal contents. The numbers inside a piece depend on the choice of basis within an eigenspace and are not physical; the determinant and the spectrum are. Three boundaries belong with the statement. At $\vec p=0$ the element $\Xi$ is undefined: the symbol is the mass plus the time cell and the carrier splits into the two eigenspaces of $\vec e_x$, the rest-frame split of Problem 1, so the label is a rest-frame value and not the helicity. For a spacelike momentum $p^2<0$ the two eigenvalues $\pm\sqrt{p^2}$ are imaginary and the piece determinant $m^2+\lvert p^2\rvert$ does not vanish: that is the off-shell region, not a second shell. For a null momentum $p^2=0$ the identity still holds, but the massless piece is nilpotent there and the massive piece keeps the determinant $m^2$: this is the exceptional case of the massless wall.

## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *Why AXF Matrices instead of Pauli and Gamma Matrices*. The bracket is the frame, on the generators as on the metric, $\gamma_\mu[\mathbb{M}_-]$ or $\gamma_\mu[\mathbb{B}]$, so that a glyph names a display and not an object of the algebra.

The gammas are the five cells written as matrices; the body writes the cells themselves.

**The five matrices, complete.** As block matrices over $\mathbb B$, acting on a pair $(\xi,\eta)$ of biquaternions,
$$
\gamma_0[\mathbb{M}_-]=\begin{pmatrix}0&e_t\\e_t&0\end{pmatrix},\qquad
\gamma_k[\mathbb{M}_-]=\begin{pmatrix}0&i\vec e_k\\-i\vec e_k&0\end{pmatrix},\qquad
\gamma_5=\begin{pmatrix}-e_t&0\\0&e_t\end{pmatrix}.
$$
Under $\mathsf M_2$ each block becomes a $2\times2$ complex matrix; assembling the four blocks, the five objects read
$$
\gamma_0[\mathbb{M}_-]=\begin{pmatrix}0&0&1&0\\0&0&0&1\\1&0&0&0\\0&1&0&0\end{pmatrix},\qquad
\gamma_1[\mathbb{M}_-]=\begin{pmatrix}0&0&0&1\\0&0&1&0\\0&-1&0&0\\-1&0&0&0\end{pmatrix},
$$
$$
\gamma_2[\mathbb{M}_-]=\begin{pmatrix}0&0&0&-i\\0&0&i&0\\0&i&0&0\\-i&0&0&0\end{pmatrix},\qquad
\gamma_3[\mathbb{M}_-]=\begin{pmatrix}0&0&1&0\\0&0&0&-1\\-1&0&0&0\\0&1&0&0\end{pmatrix},\qquad
\gamma_5=\begin{pmatrix}-1&0&0&0\\0&-1&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix}.
$$
These are the Peirce arrays, the ones the literature prints. In the axis-free display, which is the display of the body, the same five are
$$
\gamma_0[\mathbb{M}_-]=\begin{pmatrix}0&-i&0&0\\i&0&0&0\\0&0&0&i\\0&0&-i&0\end{pmatrix},\qquad
\gamma_1[\mathbb{M}_-]=\begin{pmatrix}0&0&0&i\\0&0&-i&0\\0&-i&0&0\\i&0&0&0\end{pmatrix},
$$
$$
\gamma_2[\mathbb{M}_-]=\begin{pmatrix}-i&0&0&0\\0&i&0&0\\0&0&-i&0\\0&0&0&i\end{pmatrix},\qquad
\gamma_3[\mathbb{M}_-]=\begin{pmatrix}0&-i&0&0\\-i&0&0&0\\0&0&0&-i\\0&0&-i&0\end{pmatrix},\qquad
\gamma_5=\begin{pmatrix}0&0&0&i\\0&0&-i&0\\0&i&0&0\\-i&0&0&0\end{pmatrix},
$$
the signed permutations $\gamma_0[\mathbb{M}_-]=iR_{\vec e_x}^{\mathrm{axf}}$ and $\gamma_k[\mathbb{M}_-]=iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_{\nu(k)}}^{\mathrm{axf}}$, carried into the Peirce arrays by $C_{\Pi}$. The block forms and the Dirac basis below stay in the Peirce display.

**The Dirac basis.** It is the same set after $U=\frac1{\sqrt2}\begin{pmatrix}I_2&I_2\\-I_2&I_2\end{pmatrix}$:
$$
\gamma_0[\mathbb{M}_-]^d=\begin{pmatrix}I_2&0\\0&-I_2\end{pmatrix}=
\begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&-1&0\\0&0&0&-1\end{pmatrix},\qquad
\gamma_k[\mathbb{M}_-]^d=\gamma_k[\mathbb{M}_-],
$$
$$
\gamma_5^d=\begin{pmatrix}0&I_2\\I_2&0\end{pmatrix}=
\begin{pmatrix}0&0&1&0\\0&0&0&1\\1&0&0&0\\0&1&0&0\end{pmatrix}.
$$

**The Kronecker form.**
$$
\gamma_0[\mathbb{M}_-]=\sigma_x\otimes1,\qquad \gamma_k[\mathbb{M}_-]=i\sigma_y\otimes\sigma_k,\qquad \gamma_5=-\sigma_z\otimes1 .
$$

**The action on the two chiral columns.**
$$
\gamma_0[\mathbb{M}_-]:(\psi_+,\psi_-)\mapsto(\psi_-,\psi_+),\qquad
\gamma_5:(\psi_+,\psi_-)\mapsto(-\psi_+,\psi_-),\qquad
\gamma_k[\mathbb{M}_-]:(\psi_+,\psi_-)\mapsto(\sigma_k\psi_-,-\sigma_k\psi_+).
$$

**The dictionary.** The five are the cells of the body,
$$
\gamma_0[\mathbb{M}_-]=c_0=R_{i\vec e_x}^{\mathrm{pau}},\qquad
\gamma_k[\mathbb{M}_-]=c_k=L_{i\vec e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\qquad
\gamma_5=i\Omega=R_{-i\vec e_z}^{\mathrm{pau}},
$$

The same in the axis-free display:

$$
\gamma_0[\mathbb{M}_-]=c_0=R_{i\vec e_x}^{\mathrm{axf}},\qquad
\gamma_k[\mathbb{M}_-]=c_k=L_{i\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\qquad
\gamma_5=i\Omega=R_{-i\vec e_z}^{\mathrm{axf}},
$$

with $\{\gamma_\mu[\mathbb{M}_-],\gamma_\nu[\mathbb{M}_-]\}=2\varepsilon_\mu\delta_{\mu\nu}$. The volume element is $\Omega=\gamma_0[\mathbb{M}_-]\gamma_1[\mathbb{M}_-]\gamma_2[\mathbb{M}_-]\gamma_3[\mathbb{M}_-]=-R_{\vec e_z}^{\mathrm{pau}}$, so $i\Omega=i\bigl(-R_{\vec e_z}^{\mathrm{pau}}\bigr)=R_{-i\vec e_z}^{\mathrm{pau}}=\gamma_5$: the factor $i$ is what turns the real $\vec e_z$ into $-i\vec e_z$, and $i^2=-1$ is what makes $\Omega^2=-1$ and $\gamma_5^2=+1$.

**The identities the bodies cite.** In the $\gamma$ reading, with $\varepsilon=(1,-1,-1,-1)$ the sign vector of the cells,
$$
\{\gamma_\mu[\mathbb{M}_-],\gamma_\nu[\mathbb{M}_-]\}=2\varepsilon_\mu\delta_{\mu\nu}I_4,\qquad
(\gamma_k[\mathbb{M}_-])^2=-I_4,\qquad
\gamma_5^2=I_4,\qquad
\{\gamma_\mu[\mathbb{M}_-],\gamma_5\}=0,
$$
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
=4\bigl(\varepsilon_\mu\delta_{\mu\nu}\varepsilon_\rho\delta_{\rho\sigma}
-\varepsilon_\mu\delta_{\mu\rho}\varepsilon_\nu\delta_{\nu\sigma}
+\varepsilon_\mu\delta_{\mu\sigma}\varepsilon_\nu\delta_{\nu\rho}\bigr).
$$
The contraction sums follow from the squares. With one index raised, $\gamma^\mu[\mathbb{M}_-]=-\varepsilon_\mu\gamma_\mu[\mathbb{M}_-]$, so that $\sum_\mu\gamma^\mu[\mathbb{B}]\gamma_\mu[\mathbb{B}]=-4I_4$, $\sum_\mu\gamma^\mu[\mathbb{M}_-]\gamma_\alpha[\mathbb{M}_-]\gamma_\mu[\mathbb{M}_-]=2\gamma_\alpha[\mathbb{M}_-]$, $\sum_\mu\gamma^\mu[\mathbb{M}_-]\gamma_\alpha[\mathbb{M}_-]\gamma_\beta[\mathbb{M}_-]\gamma_\mu[\mathbb{M}_-]=-4\varepsilon_\alpha\delta_{\alpha\beta}I_4$ and $\sum_\mu\gamma^\mu[\mathbb{M}_-]\gamma_\gamma[\mathbb{M}_-]\gamma_\beta[\mathbb{M}_-]\gamma_\alpha[\mathbb{M}_-]\gamma_\mu[\mathbb{M}_-]=2\gamma_\gamma[\mathbb{M}_-]\gamma_\beta[\mathbb{M}_-]\gamma_\alpha[\mathbb{M}_-]$.

## Summary

The seven problems test the parent's plane-wave solutions and confirm them in the algebra.

1. **The solutions.** Eliminating the right part gives the mass shell $E^2=\vec p^{\,2}+m^2$; on it the right part is free and the left part is $\frac1m\slashed p\,\tilde\Psi_R$, the two parts standing in the norm ratio $(E\mp\lvert\vec p\rvert):(E\pm\lvert\vec p\rvert)$ for helicity $\pm1$. At rest the solutions are the right-eigenspaces of $\vec e_x$, with basis $e_t+i\vec e_x$ and $\vec e_z+i\vec e_y$; in the other display each branch is a single value.
2. **Normalisation.** The covariant values $2m$, $-2m$ and $0$ follow from the single identity $(i\vec u_p)^2=e_t$ and from the geometric mean $\sqrt{E^2-\vec p^{\,2}}=m$; the Hermitian products are $2E$.
3. **Spin sums.** For every element, $\sum_\pm\tilde w_\pm\langle\tilde w_\pm,\cdot\rangle_{\mathrm D}=\slashed p+m$ and $\sum_\pm\tilde v_\pm\langle\tilde v_\pm,\cdot\rangle_{\mathrm D}=\slashed p-m$ read as products of elements; $\slashed p^2=p^2$, and $(\slashed p+m)(\slashed p-m)=0$ on shell.
4. **Massless limit.** The pair decouples, each value keeps one helicity, and the two labels are locked: positive helicity with the right value and negative helicity with the left one.
5. **Cells.** The anticommutation relations are the multiplication table of the four units; the chirality cell is $R_{-i\vec e_z}$; the change of the display is right multiplication by $\tilde W=(e_t+\vec e_y)/\sqrt2$, which sends $R_{i\vec e_x}$ to $R_{i\vec e_z}$ and $R_{-i\vec e_z}$ to $R_{i\vec e_x}$ and leaves the space cells alone; the Lorentz generators are $S_{0k}=\frac i2L_{\vec e_k}R_{\vec e_z}$ and $S_{jk}=\frac i2L_{\vec e_j\vec e_k}$.
6. **Mass shell.** The condition $\tilde P\tilde P^{\natural}=-m^2c^2$ is the quaternionic-norm statement $\langle\tilde P/\hbar\rangle_{\natural}=-m^2c^2/\hbar^2$, and reproduces $E^2=\vec p^{\,2}c^2+m^2c^4$.
7. **Helicity pieces.** The symbol squares to the interval, $\slashed p^2=p^2$, and commutes with left multiplication by $\Xi=i\vec u_p$, so the carrier splits into two two-dimensional eigenspaces of determinant $m^2-p^2=\lambda_+\lambda_-+m^2$; the pieces are isospectral, $\det\mathcal D(p)=(m^2-p^2)^2$, and the mass shell is the vanishing of either piece determinant, with a one-dimensional kernel per helicity.

Two objects are needed by the exercise and are not displayed in the parent: the negative-frequency solutions $\tilde v$ (Problem 1) and the change-of-display element $\tilde W$ (Problem 5). The constructions above reproduce the parent's stated results.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb B=\mathbb C\otimes_\mathbb R\mathbb H$ | Biquaternion algebra |
| $e_t=1,\vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_k^2=-e_t$ |
| $i$ | Scalar imaginary, $i^2=-1$ |
| $R_a,L_a$ | Right and left multiplication, $R_a(\tilde Q)=\tilde Q a$, $L_a(\tilde Q)=a\tilde Q$ |
| $L_aR_b$ | The two-sided cell, $\tilde Q\mapsto a\tilde Q b$ |
| $c_\mu=L_{ie_\mu}R_{\vec e_{\nu(\mu)}}$ | Cell of the coordinate $x_\mu$: $c_0=R_{i\vec e_x}$, $c_k=L_{i\vec e_k}R_{\vec e_y}$ |
| $R_{-i\vec e_z}$ | Chirality cell; $-1$ on $\tilde Q_L$, $+1$ on $\tilde Q_R$ |
| $\Omega=c_0c_1c_2c_3=-R_{\vec e_z}$ | Volume cell; $\Omega^2=-1$, and $i\Omega=R_{-i\vec e_z}$ |
| $\tilde\Psi=\tilde\Psi_L+\tilde\Psi_R$ | The Dirac field and its two chirality values |
| $\slashed p=E\,R_{i\vec e_x}-p_kL_{i\vec e_k}R_{\vec e_y}$ | Momentum-space symbol; $\slashed p\,\tilde\Psi=iE\tilde\Psi\vec e_x-i(\vec p\cdot\vec e)\tilde\Psi\vec e_y$ |
| $\langle\tilde\Psi,\tilde\Phi\rangle_{\mathrm D}=\mathrm{Tr}\bigl(\tilde\Psi^{*}\tilde\Phi\,i\vec e_x\bigr)$ | Dirac pairing, twisted by the time cell |
| $\tilde W=(e_t+\vec e_y)/\sqrt2$ | Change of the display |
| $S_{0k}=\frac i2L_{\vec e_k}R_{\vec e_z}$, $S_{jk}=\frac i2L_{\vec e_j\vec e_k}$ | Lorentz generators, $S_{\mu\nu}=\frac i4[c_\mu,c_\nu]$ |
| $\tilde P/\hbar=i\omega/c\,e_t+\vec k$ | Wave biquaternion |
| $\tilde P\tilde P^{\natural}=-m^2c^2$ | Mass-shell condition |
| $p^2=E^2-\vec p^{\,2}$ | Interval of the four-momentum, $\hbar=c=1$ |
| $\mathcal D(p)=\slashed p-m$ | Massive symbol; $\slashed p$ is the massless one |
| $\Xi=i\vec u_p$, $\vec u_p=\vec p/\lvert\vec p\rvert$ | Helicity element, $\Xi^2=e_t$; its two values grade the carrier |
| $\lambda_\pm=i(E\mp\lvert\vec p\rvert)$ | Eigenvalues of left multiplication by $\tilde P$; $\lambda_+\lambda_-=\tilde P\tilde P^{\natural}$ |
| $\det\mathcal D(p)=(m^2-p^2)^2$ | Piece determinant $m^2-p^2$ per helicity, squared in the symbol |

## Further Reading

- [Why AXF Matrices instead of Pauli and Gamma Matrices](why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the reasons the AXF matrices replace the Pauli and gamma matrices.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Mechanics* (McGraw-Hill, 1964), for the plane-wave solutions, the normalisations, and the spin sums in the standard notation.
- C. Itzykson and J.-B. Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), for the spin sums, the two representations, and the Lorentz generators.
- M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), for the two representations, the normalisation, and the completeness relations.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), as the record of the formulation the corpus replaced.
- The representation theory used above: [The $M_4(\mathbb{C})$ Axis-Free Representation](../articles_maths/m4c-axis-free-representation.html), [The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure](../articles_maths/the-enveloping-operator-algebra-of-the-biquaternion-algebra-and-the-bi-module-structure.html), and [The Polarized Module of the Biquaternion Algebra](../articles_maths/the-polarized-module-of-the-biquaternion-algebra.html).
- The parent article of this exercise: [The Biquaternion Dirac Equation — Solutions and the Non-Relativistic Limit](the-dirac-equation-in-biquaternionic-form-solutions-and-the-non-relativistic-limit.html), and its companions [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html) and [The Spinor Module in Biquaternionic Form and Its Lorentz Action](the-spinor-module-in-biquaternionic-form-and-its-lorentz-action.html).
