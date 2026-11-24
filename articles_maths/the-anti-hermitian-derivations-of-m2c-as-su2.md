# __The Anti-Hermitian Derivations of $M_2(\mathbb{C})$ as $\mathfrak{su}(2)$__

## Introduction

**Two conditions pick out the generators: anti-Hermitian and traceless. At order two they hold exactly for a three-dimensional space, which is $\mathfrak{su}(2)$. The three generators are not chosen from a list: they are the images of the three vector units of the biquaternion algebra under the isomorphism $\mathsf{M}_2$, halved so that the structure constants come out as $\epsilon_{abc}$.**

The article reads the three generators as the corpus reads them. The isomorphism $\mathsf{M}_2$ sends the vector units to the three matrices $\mathsf{M}_2(\vec e_k)$, and the half of those matrices are the generators; the normalization is the one that *Automorphisms and Derivations of Algebras* fixes at the element level, $D_k=\tfrac12\mathrm{ad}_{\vec e_k}$. The bracket of the halved generators is $[G_1,G_2]=G_3$, with no factor and no sign.

The article gives the three matrices twice, once from the Pauli matrices and once as the six axis-free matrices of the multiplication, the three derivations as four-by-four arrays in the basis of the elements, the conjugation table of the rotor on the three generators, the three rotors written out, the dimension ladder, the worked cases and the orbits. Every numeric statement was checked on the arrays.

The article assumes the exponential of the matrix algebra from *The Exponential and the Lie Group Structure of $\mathrm{GL}_2(\mathbb{C})$*, the Lie correspondence of *The Lie Correspondence and the Adjoint Representation*, and the images of the units from the Pauli representation of $M_2(\mathbb{C})$.

## The Two Conditions on the Matrix

### Anti-Hermitian and Traceless

**Proposition (the generators).** The matrices $A\in M_2(\mathbb{C})$ with $A^{*}=-A$ and $\operatorname{tr}A=0$ form a real vector space of dimension three, closed under the bracket, isomorphic to $\mathfrak{su}(2)$.

**Proof.** A general element is $A=\begin{pmatrix}a&b\\c&d\end{pmatrix}$ with $a,d$ purely imaginary and $c=-\bar b$, so the real parameters are $\operatorname{Im}a$, $\operatorname{Im}d$, $\operatorname{Re}b$, $\operatorname{Im}b$: four. The trace condition is $\operatorname{Im}a+\operatorname{Im}d=0$, one real equation, leaving three. The bracket of two anti-Hermitian matrices is anti-Hermitian, and the trace of a bracket vanishes.

**Remark (the three as images of the units).** The isomorphism $\mathsf{M}_2$ sends

$$
\mathsf{M}_2(\vec e_x)=\begin{pmatrix}0&-i\\-i&0\end{pmatrix},\qquad
\mathsf{M}_2(\vec e_y)=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
\mathsf{M}_2(\vec e_z)=\begin{pmatrix}-i&0\\0&i\end{pmatrix},
$$

and each of the three is anti-Hermitian and traceless. They are the three generators up to the factor $\tfrac12$ of the next section.

**Remark (the images are written as matrices).** The three objects of this article are images of elements, and they are written with their entries. The arrays of the Pauli frame are printed once, in §*The Three, From the Pauli Matrices and From the Axis-Free Matrices*, because that section compares the two routes and a reader who is told that the images are $-i\sigma_k$ must be able to see what $\sigma_k$ is; everywhere else the body writes the entries.

### The Split as One and Two

**Proposition (the real form inside).** Every anti-Hermitian traceless $A$ splits uniquely as

$$
A=\underbrace{\tfrac12(A-\bar A)}_{\text{real antisymmetric}}+\;i\underbrace{\tfrac1{2i}(A+\bar A)}_{\text{real symmetric, traceless}},
$$

and the two summands have real dimensions one and two, so $3=1+2$ with intersection zero.

**Proof.** A real antisymmetric matrix of order two is $\begin{pmatrix}0&t\\-t&0\end{pmatrix}$, one parameter, and it is $\mathsf{M}_2(\vec e_y)$ up to the factor $-1$. A real symmetric traceless matrix of order two is $\begin{pmatrix}u&v\\v&-u\end{pmatrix}$, two parameters, and $i$ times it is spanned by $\mathsf{M}_2(\vec e_x)$ and $\mathsf{M}_2(\vec e_z)$. The symmetry types differ, so the summands meet only in zero.

**Remark (the same split at every order).** The real antisymmetric matrices of order $n$ have dimension $\tfrac12n(n-1)$ and the $i$ times real symmetric traceless ones have dimension $\tfrac12n(n+1)-1$; at $n=2$ this is $1+2$ and at $n=4$ it is $6+9$. The first summand is a subalgebra at every order, the second is not.

## The Three Generators

**Definition.** Put

$$
T_k:=\mathsf{M}_2(\vec e_k),\qquad G_k:=\tfrac12 T_k,\qquad k=1,2,3,
$$

with $1,2,3$ standing for $x,y,z$. The three generators are

$$
G_1=\begin{pmatrix}0&-\tfrac{i}{2}\\-\tfrac{i}{2}&0\end{pmatrix},\qquad
G_2=\begin{pmatrix}0&-\tfrac12\\ \tfrac12&0\end{pmatrix},\qquad
G_3=\begin{pmatrix}-\tfrac{i}{2}&0\\0&\tfrac{i}{2}\end{pmatrix}.
$$

**Proposition (the count and the properties).** The three are anti-Hermitian, traceless, linearly independent over $\mathbb{R}$, and they close under the bracket, so they are a basis of $\mathfrak{su}(2)$.

**Proof.** Each $G_k$ is $\tfrac12$ times an image of a real vector unit, so it is anti-Hermitian and traceless. The space has dimension three and the three are independent, so they are a basis; the space is closed by the general argument of the first proposition.

**Remark (why the half).** The bracket of the images is $[T_1,T_2]=2T_3$, the factor $2$ being the same one that $[\vec e_x,\vec e_y]=2\vec e_z$ carries at the element level. Halving removes it, so the generators satisfy $[G_1,G_2]=G_3$ and the structure constants are $\epsilon_{abc}$ with no constant.

| generator | entries | family | square | $\det$ |
|---|---|---|---|---|
| $G_1$ | off-diagonal, both entries $-\tfrac{i}{2}$ | $i$ times real symmetric | $-\tfrac14\mathrm{I}_2$ | $\tfrac14$ |
| $G_2$ | $-\tfrac12$ and $\tfrac12$ | real antisymmetric | $-\tfrac14\mathrm{I}_2$ | $\tfrac14$ |
| $G_3$ | diagonal, $-\tfrac{i}{2}$ and $\tfrac{i}{2}$ | $i$ times real symmetric | $-\tfrac14\mathrm{I}_2$ | $\tfrac14$ |

### The Three, From the Pauli Matrices and From the Axis-Free Matrices

**The Pauli matrices.** The three arrays of the Pauli frame, as *$M_2(\mathbb{C})$ Pauli Representation* prints them, and the images of the three vector units under them:

$$
\sigma_1=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
\sigma_2=\begin{pmatrix}0&-i\\i&0\end{pmatrix},\qquad
\sigma_3=\begin{pmatrix}1&0\\0&-1\end{pmatrix},
\qquad
\mathsf{M}_2(\vec e_k)=-i\sigma_k .
$$

So the three generators are

$$
G_1=-\tfrac{i}{2}\sigma_1,\qquad G_2=-\tfrac{i}{2}\sigma_2,\qquad G_3=-\tfrac{i}{2}\sigma_3,
$$

which is the display of the definition, entry for entry.

**The axis-free matrices.** The same three directions, built from the multiplication instead of from a frame of $\mathbb{C}^2$: the left and the right multiplication by the three vector units, in the basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$ of the algebra, are the six matrices of *Matrix Representations and Conventions*,

$$
\ell_x=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix},\quad
\ell_y=\begin{pmatrix}0&0&-1&0\\0&0&0&1\\1&0&0&0\\0&-1&0&0\end{pmatrix},\quad
\ell_z=\begin{pmatrix}0&0&0&-1\\0&0&-1&0\\0&1&0&0\\1&0&0&0\end{pmatrix},
$$

$$
r_x=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&1\\0&0&-1&0\end{pmatrix},\quad
r_y=\begin{pmatrix}0&0&-1&0\\0&0&0&-1\\1&0&0&0\\0&1&0&0\end{pmatrix},\quad
r_z=\begin{pmatrix}0&0&0&-1\\0&0&1&0\\0&-1&0&0\\1&0&0&0\end{pmatrix}.
$$

**Proposition (the axis-free route gives the derivations of this article).** The three arrays

$$
\tfrac12\bigl(\ell_k-r_k\bigr),\qquad k=x,y,z,
$$

are the arrays of $\mathrm{ad}_{G_k}$ in the basis $(\mathrm{I}_2,T_1,T_2,T_3)$, so the three matrices printed in §*The Array in the Basis of the Elements* are this route, entry for entry.

**Proof.** $\mathrm{ad}_{G_k}$ is left multiplication by $T_k$ minus right multiplication by $T_k$, halved. The isomorphism $\mathsf{M}_2$ matches the coefficient basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$ with $(\mathrm{I}_2,T_1,T_2,T_3)$, so left multiplication by $\vec e_k$ and left multiplication by $T_k$ have the same array, and likewise on the right. The two arrays therefore agree on all sixteen entries, checked entry for entry.

**Remark (why the two routes are worth both).** The Pauli route writes the three generators as $2\times2$ matrices and hides the fact that they are three directions of the algebra. The axis-free route writes them as $4\times4$ arrays of the multiplication and shows it: the three arrays are quarter-turns of the three coordinate planes of the element space, they kill the scalar line, and their brackets are read off without a convention for $\sigma_k$.

### The Commutators

**Proposition (the structure constants).** The three generators satisfy

$$
[G_1,G_2]=G_3,\qquad [G_2,G_3]=G_1,\qquad [G_3,G_1]=G_2 .
$$

**Proof.** The images satisfy $[T_1,T_2]=2T_3$ and its cyclic rotations, because the elements satisfy $[\vec e_x,\vec e_y]=2\vec e_z$ and $\mathsf{M}_2$ is an algebra isomorphism. Halving both entries of each bracket gives the three identities.

**Remark (no sign against the algebra frame).** The bracket here is the bracket of the algebra read through $\mathsf{M}_2$, and the half removes the factor two, so the table agrees with the table of the coefficient frame. Written without the half the same table reads $[T_1,T_2]=2T_3$.

## The Derivation and Its Array

### The Derivation

**Definition.** For $A$ in the algebra the derivation is $\mathrm{ad}_A(X)=AX-XA$.

**Proposition (it is a derivation and it is anti-Hermitian).** The Leibniz rule holds for all $X,Y$, and for the Hilbert–Schmidt form $\langle X,Y\rangle=\operatorname{tr}(X^{*}Y)$ one has $(\mathrm{ad}_A)^{*}=\mathrm{ad}_{A^{*}}$, so $\mathrm{ad}_A$ is anti-Hermitian exactly when $A$ is. The kernel of $A\mapsto\mathrm{ad}_A$ is the scalars, so the map is injective on $\mathfrak{su}(2)$.

**Proof.** The Leibniz rule is associativity. For the adjoint, $\operatorname{tr}([A,X]^{*}Y)=\operatorname{tr}(X^{*}[A^{*},Y])$ by the cyclic invariance of the trace. The kernel is the centre, and a scalar multiple of $\mathrm{I}_2$ is traceless only when it is zero.

### The Array in the Basis of the Elements

**Proposition (the three arrays).** In the basis $(\mathrm{I}_2,T_1,T_2,T_3)$, in that order, the three derivations have the arrays

$$
\mathrm{ad}_{G_1}=\begin{pmatrix}0&0&0&0\\0&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix},\quad
\mathrm{ad}_{G_2}=\begin{pmatrix}0&0&0&0\\0&0&0&1\\0&0&0&0\\0&-1&0&0\end{pmatrix},\quad
\mathrm{ad}_{G_3}=\begin{pmatrix}0&0&0&0\\0&0&-1&0\\0&1&0&0\\0&0&0&0\end{pmatrix}.
$$

**Proof.** The identity is fixed, so the first row and the first column vanish. On the three $T_k$ the commutator is the cross product with the coordinate vector of the generator, with the coefficient one: $[G_1,T_2]=T_3$ and $[G_1,T_3]=-T_2$, and cyclically. So each array is the quarter-turn of one coordinate plane on the three-dimensional block.

**Remark (the same three arrays as in the coefficient frame).** These are the three arrays $D_x,D_y,D_z$ of *The Anti-Hermitian Derivations of the Biquaternion Algebra as $\mathfrak{su}(2)$*, entry for entry. The coefficient basis $e_t,\vec e_x,\vec e_y,\vec e_z$ and the element basis $\mathrm{I}_2,T_1,T_2,T_3$ are matched by $\mathsf{M}_2$, and the derivation is the same object read in the two bases.

**Corollary (the spectrum).** Each array has the spectrum $\{0,0,i,-i\}$, trace zero and exponential of determinant one.

**Proof.** The block is a real quarter-turn of a plane, with eigenvalues $\pm i$, and the two fixed directions give the two zeros. The trace of a commutator vanishes, and $\det e^{F}=e^{\operatorname{tr}F}=1$.

## The Exponential of Each Generator

### The Closed Form

**Proposition (the closed form).** For real $\theta$,

$$
e^{\theta G_k}=\cos\tfrac{\theta}{2}\,\mathrm{I}_2+\sin\tfrac{\theta}{2}\,T_k ,
$$

a unitary matrix of determinant one.

**Proof.** $G_k^{2}=-\tfrac14\mathrm{I}_2$, so the even terms of the series sum to $\cos(\theta/2)\mathrm{I}_2$ and the odd terms to $2\sin(\theta/2)G_k=\sin(\theta/2)T_k$. The determinant is $\cos^{2}+\sin^{2}=1$ because $T_k$ is traceless and $T_k^{2}=-\mathrm{I}_2$.

**Remark (the angle and the half angle).** The parameter $\theta$ is the angle of the array: the array of $\mathrm{ad}_{G_k}$ turns its plane by $\theta$. The matrix $e^{\theta G_k}$ is the element $e^{\theta\vec e_k/2}$ seen through $\mathsf{M}_2$, so the half angle is the double cover, and the factor $\tfrac12$ of the normalization cancels it.

### The Conjugation Table

**Proposition (one rotation, three axes).** With $U=e^{\theta G_k}$, $c=\cos\theta$ and $s=\sin\theta$, the conjugation $X\mapsto UXU^{*}$ fixes $\mathrm{I}_2$ and acts on the three $T_k$ by

| rotor | $T_1$ | $T_2$ | $T_3$ |
|---|---|---|---|
| $U=e^{\theta G_1}$ | $T_1$ | $c\,T_2+s\,T_3$ | $-s\,T_2+c\,T_3$ |
| $U=e^{\theta G_2}$ | $c\,T_1-s\,T_3$ | $T_2$ | $s\,T_1+c\,T_3$ |
| $U=e^{\theta G_3}$ | $c\,T_1+s\,T_2$ | $-s\,T_1+c\,T_2$ | $T_3$ |

**Proof.** Each $UT_kU^{*}$ is anti-Hermitian and traceless, so it is a real combination of the three $T_l$, and the coefficients are the entries of the exponential of the array. The array of $\mathrm{ad}_{G_1}$ is the quarter-turn of the plane $(T_2,T_3)$, so its exponential turns that plane by $\theta$ and fixes $T_1$.

**Corollary (the sense is right-handed).** The conjugation by $e^{\theta G_k}$ is the rotation of $\operatorname{span}\{T_1,T_2,T_3\}$ by the angle $\theta$ about the axis $T_k$, right-handed in the order $T_1,T_2,T_3$.

**Proof.** Read the first row: $T_2\mapsto cT_2+sT_3$ and $T_3\mapsto-sT_2+cT_3$, a positive quarter-turn from $T_2$ towards $T_3$, which is right-handed about $T_1$. The other rows are the cyclic rotations of the same statement.

**Remark (what the doubling did).** An element rotor of parameter $\theta$ turns the vector part by $2\theta$, which is the double cover. Here the generator already carries the half, so the angle of the array and the angle of the element are the same number, and the element that realises the array rotor is $e^{\theta\vec e_k/2}$. Written without the half, every bracket and every angle carries a factor $2$.

### What Each Generator Does

**Proposition (the three actions, one each).** Exponentiated, the three generators act as follows.

| generator | fixed | turned | angle | rotor behind it | in words |
|---|---|---|---|---|---|
| $G_1$ | $\mathrm{I}_2$, $T_1$ | plane of $T_2,T_3$ | $\theta$ | $e^{\theta\vec e_x/2}$ | mixes the two coordinates with a factor $i$ |
| $G_2$ | $\mathrm{I}_2$, $T_2$ | plane of $T_3,T_1$ | $\theta$ | $e^{\theta\vec e_y/2}$ | turns the plane with real entries |
| $G_3$ | $\mathrm{I}_2$, $T_3$ | plane of $T_1,T_2$ | $\theta$ | $e^{\theta\vec e_z/2}$ | multiplies the two coordinates by opposite phases |

**Proof.** The fixed elements and the turned plane are the kernel and the non-trivial block of the array. The rotor is the element exponential, whose image is the matrix of the closed form.

**Corollary (the rotor is the conjugation).** $e^{\theta\mathrm{ad}_{G_k}}=\mathrm{Ad}_{U}$ with $U=e^{\theta G_k}$, and its array is the two-sided operator $L_UR_{U^{-1}}$.

**Proof.** $L_A$ and $R_A$ commute, so $e^{\theta(L_A-R_A)}=e^{\theta L_A}e^{-\theta R_A}=L_UR_{U^{-1}}$, and that operator sends $X$ to $UXU^{-1}$.

### The Three Rotors, Written Out

**Corollary (the three matrices).** With $c=\cos\tfrac{\theta}{2}$ and $s=\sin\tfrac{\theta}{2}$,

$$
e^{\theta G_1}=\begin{pmatrix}c&-is\\-is&c\end{pmatrix},\qquad
e^{\theta G_2}=\begin{pmatrix}c&-s\\ s&c\end{pmatrix},\qquad
e^{\theta G_3}=\begin{pmatrix}c-is&0\\0&c+is\end{pmatrix}.
$$

**Proof.** Substitute the three matrices in the closed form.

**Remark (three visibly different rotors).** The second has real entries and is a rotation of the plane. The third is diagonal and multiplies the two coordinates by opposite phases. The first has imaginary entries off the diagonal and mixes the two coordinates with a factor $i$; in the complex coordinate it sends $z\mapsto cz-is\bar z$. Every unitary of determinant one at order two is one of the three or a product of them.

### The Invariants

**Proposition (what the rotor preserves).** The conjugation by $U$ preserves the trace, the determinant, the spectrum and the norm of every matrix, and it preserves the Hermitian cone.

**Proof.** The conjugation is an algebra automorphism, so every polynomial invariant is preserved; it carries $X^{*}$ to $(UXU^{*})^{*}$, so the cone of Hermitian matrices is preserved; and similar matrices have the same eigenvalues.

**Corollary (the fixed space).** The fixed space of the rotor is the commutant of $G_k$, of complex dimension two, spanned by $\mathrm{I}_2$ and $G_k$.

**Proof.** A matrix commutes with $G_k$ exactly when it is a polynomial in it, and $G_k$ has two distinct eigenvalues, so the polynomials are two-dimensional.

## The Dimension Ladder

| set | defining condition | real dimension |
|---|---|---|
| $M_2(\mathbb{C})$ | none | $8$ |
| the anti-Hermitian matrices | $A^{*}=-A$ | $4$ |
| the traceless matrices | $\operatorname{tr}A=0$ | $6$ |
| $\mathfrak{su}(2)$ | both | $3$ |
| $\operatorname{End}(M_2)$, all operators | none | $32$ |
| the anti-Hermitian operators | $F^{*}=-F$ | $16$ |
| the derivations | Leibniz rule | $6$ |
| the anti-Hermitian derivations | both | $3$ |

**Remark (the two sixes are not the same six).** The traceless matrices have real dimension six and the derivations have real dimension six, and they are different spaces: the first sits inside $M_2$, of complex dimension four, and the second inside $\operatorname{End}(M_2)$, of complex dimension sixteen. The map $A\mapsto\mathrm{ad}_A$ is an isomorphism between them, and that is why the two sixes coincide.

**Remark (why the operator level is thirty-two).** $\operatorname{End}(M_2)$ has complex dimension $4\cdot4=16$, so real dimension thirty-two. The anti-Hermitian operators are half of it, sixteen; the derivation condition cuts those sixteen to the six of the traceless generators, and the anti-Hermitian condition among those leaves three.

## The Worked Cases

**Proposition (the three cases at $\theta=\pi/4$).**

| generator | rotor | spectrum of the array | fixed space of the rotor |
|---|---|---|---|
| $G_1$ | $\cos\tfrac{\pi}{8}\mathrm{I}_2+\sin\tfrac{\pi}{8}T_1$ | $\{1,1,e^{i\pi/4},e^{-i\pi/4}\}$ | $\operatorname{span}\{\mathrm{I}_2,T_1\}$ |
| $G_2$ | $\cos\tfrac{\pi}{8}\mathrm{I}_2+\sin\tfrac{\pi}{8}T_2$ | $\{1,1,e^{i\pi/4},e^{-i\pi/4}\}$ | $\operatorname{span}\{\mathrm{I}_2,T_2\}$ |
| $G_3$ | $\operatorname{diag}(e^{-i\pi/8},e^{i\pi/8})$ | $\{1,1,e^{i\pi/4},e^{-i\pi/4}\}$ | $\operatorname{span}\{\mathrm{I}_2,T_3\}$ |

**Proof.** The array is $e^{\theta\mathrm{ad}_{G}}$, whose eigenvalues are $1,1,e^{i\theta},e^{-i\theta}$: two from the fixed directions and two from the turned plane. At $\theta=\pi/4$ this is $1,1,e^{i\pi/4},e^{-i\pi/4}$. The conjugation turns the plane by $\theta$ and fixes the axis, so the fixed space is spanned by the identity and the generator.

**Remark (the same spectrum for the three).** All three generators have the eigenvalues $\pm\tfrac{i}{2}$ and every array has the spectrum $\{0,0,i,-i\}$, so the three cases differ in the rotor and not in the spectrum. What separates them is the real form: $G_2$ is real, $G_3$ is diagonal, and $G_1$ is neither.

**Remark (the periods).** The array has period $2\pi$ in $\theta$, since $e^{2\pi\mathrm{ad}_{G}}=\mathrm{id}$; the rotor $e^{\theta G}$ has period $4\pi$, since $e^{4\pi G}=\mathrm{I}_2$; and the element whose derivation is turned has period $4\pi$ in $\theta$ as well, which is the double cover read in the other direction.

## The Orbits

**Proposition (the orbit of a Hermitian matrix).** The conjugation by $\mathrm{SU}(2)$ sends a traceless Hermitian matrix of norm $r$ to any other of the same norm, so the orbit is a two-sphere, of real dimension two, and the stabiliser is a circle.

**Proof.** The traceless Hermitian matrices of norm $r$ are the vectors of length $r$ in a three-dimensional real space, and the conjugation acts on them as the full rotation group, transitively. The stabiliser of a non-zero vector is the circle of rotors about it.

**Corollary (the general orbit).** A matrix with distinct eigenvalues has an orbit of real dimension two in the traceless Hermitian part and of real dimension two in the traceless anti-Hermitian part, and its full orbit in $M_2$ is the product of the orbit of its scalar part, a point, with those two.

**Proof.** The scalar part is fixed, and each of the two traceless parts is a three-dimensional space on which the group acts by rotations; the orbit of a non-zero vector in either is the sphere.

**Remark (the orbit of a generator).** The generators form the sphere of radius $\tfrac12$ in the three-dimensional space of traceless anti-Hermitian matrices, and the conjugation acts on that sphere by rotations. So the three generators are conjugate, the orbit is the sphere, and the stabiliser of each is a circle; the three rows of the worked table are three points on one orbit, and what distinguishes them is the real structure and not the spectrum.

## Summary

The anti-Hermitian traceless matrices of order two form $\mathfrak{su}(2)$, of real dimension three, and their generators are the halves of the images of the three vector units, $G_k=\tfrac12\mathsf{M}_2(\vec e_k)$. With that normalization the bracket is $[G_1,G_2]=G_3$, and each array is a quarter-turn of one coordinate plane in the basis $(\mathrm{I}_2,T_1,T_2,T_3)$ of the elements.

Each generator gives the derivation $[A,\cdot]$, anti-Hermitian for the Hilbert–Schmidt form, of array with the scalar row and column zero and the spectrum $\{0,0,i,-i\}$. The exponential is the conjugation by $U=e^{\theta G_k}=\cos\tfrac{\theta}{2}\mathrm{I}_2+\sin\tfrac{\theta}{2}T_k$, which turns the three-dimensional space of traceless elements by the angle $\theta$ about the axis $T_k$, right-handed, and fixes the identity and the axis.

The three are written twice over: as $-\tfrac{i}{2}\sigma_k$ from the three arrays of the Pauli frame, and as $\tfrac12(\ell_k-r_k)$ from the six axis-free matrices of the multiplication, the two routes agreeing entry for entry.

The three rotors are the phase mixing $e^{\theta G_1}$, the real rotation $e^{\theta G_2}$ and the pair of opposite phases $e^{\theta G_3}$. The dimension ladder is $8,4,6,3$ at the element level and $32,16,6,3$ at the operator level, and the split of the generators as $1+2$, closed part plus open part, is the split $6+9$ of the fifteen at order four.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathsf{M}_2$ | the isomorphism from the algebra to $M_2(\mathbb{C})$ |
| $\sigma_k$ | the three arrays of the Pauli frame, printed once in the section that compares the two routes |
| $T_k$ | the image $\mathsf{M}_2(\vec e_k)$ of a vector unit, equal to $-i\sigma_k$ |
| $\ell_k$, $r_k$ | the axis-free matrices of left and right multiplication by $\vec e_k$ |
| $G_k$ | the generator $\tfrac12 T_k$ |
| $\mathrm{ad}_A$ | the derivation $[A,\cdot]$ |
| $\langle X,Y\rangle$ | the Hilbert–Schmidt form $\operatorname{tr}(X^{*}Y)$ |
| $U$ | the rotor $e^{\theta G_k}\in\mathrm{SU}(2)$ |
| $\mathrm{Ad}_U$ | the conjugation $X\mapsto UXU^{*}$ |
| $R$ | the quarter-turn of a coordinate plane |

## Further Reading

- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations* (Springer, 2015), for $\mathfrak{su}(2)$, the adjoint representation and the inner automorphisms.
- Roger A. Horn and Charles R. Johnson, *Topics in Matrix Analysis* (Cambridge University Press, 1991), for the Kronecker product and its eigenvalues.
- [Automorphisms and Derivations of Algebras](automorphisms-and-derivations-of-algebras.md), for the normalization $D_\mu=\tfrac12\mathrm{ad}_{\vec e_\mu}$ and the bracket $[D_1,D_2]=D_3$.
- [Matrix Representations and Conventions](matrix-representations-conventions.md), for the axis-free matrices $\ell_k$ and $r_k$ and the rule on the Pauli matrices.
- [The Anti-Hermitian Derivations of the Biquaternion Algebra as $\mathfrak{su}(2)$](the-anti-hermitian-derivations-of-the-biquaternion-algebra-as-su2.html), for the same three arrays in the coefficient frame.
- [The Anti-Hermitian Derivations of $M_4(\mathbb{C})$ as $\mathfrak{su}(4)$](the-anti-hermitian-derivations-of-m4c-as-su4.html), for the fifteen at the next order, built from the same images.
- [The Exponential and the Lie Group Structure of $\mathrm{GL}_2(\mathbb{C})$](the-exponential-and-the-lie-group-structure-of-gl2c.html), for the exponential of the matrix algebra.
