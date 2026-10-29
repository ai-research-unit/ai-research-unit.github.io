# __The Square of an Element__

## Introduction

The square is the first operation of the algebra that is not linear. This article computes it on the general element, in the coordinates of that element, and reads the two parts of the result. It then reads the square as a condition: when the square is central, when it vanishes, and when it equals the element again.

The article is form-free. It uses the product, the coefficients and the scalar–vector split of *The Element, the Coordinates and the Conjugations*, and it pairs no two different elements. No norm and no form appears.

## The Formula

Write the general element in the scalar–vector split,

$$
\tilde Q=Q_te_t+\vec Q,\qquad
\vec Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z,\qquad
Q_\mu=q_\mu+iq'_\mu,
$$

with the four complex coefficients $Q_\mu$, their real parts $q_\mu$ and their imaginary parts $q'_\mu$. The **complex length** of the vector part is

$$
B=\sqrt{Q_x^2+Q_y^2+Q_z^2},\qquad B^2=Q_x^2+Q_y^2+Q_z^2=(\vec Q,\vec Q),
$$

defined up to sign; this article uses the square $B^2$, which is branch-free. The square of the pure element is central,

$$
\vec Q^2=-B^2e_t,
$$

and the multiplication of the scalar and the vector part gives the square as

$$
\boxed{\;\tilde Q^2=\bigl(Q_t^2-B^2\bigr)e_t+2Q_t\vec Q\;}.
$$

In coordinates, the square has scalar part $Q_t^2-B^2$ and vector part $2Q_t\vec Q$:

$$
\tilde Q^2=\underbrace{\bigl(Q_t^2-B^2\bigr)}_{\text{scalar}}e_t+\underbrace{2Q_t\vec Q}_{\text{vector}} .
$$

The scalar part is the square of the scalar coefficient minus the square of the complex length; the vector part is the vector part of the element, multiplied by twice the scalar coefficient. The square is unchanged when the element changes sign, $(-\tilde Q)^2=\tilde Q^2$.

**Example.** For $\tilde Q=e_t+i\vec e_x$ the scalar coefficient is $1$ and $B^2=i^2=-1$, so $\tilde Q^2=2e_t+2i\vec e_x=2\tilde Q$. For $\tilde Q=i\vec e_x+\vec e_y$ the scalar coefficient is $0$ and $B^2=-1+1=0$, so $\tilde Q^2=0$.

## The Two Parts

The vector part of the square is $2Q_t\vec Q$: it is the vector part of the element, multiplied by the complex number $2Q_t$ and not turned. Three consequences are read off at once.

- If $Q_t\neq0$ and $\vec Q\neq0$, the square has a non-zero vector part, a complex multiple of $\vec Q$.
- If $Q_t=0$, the square is central, whatever the vector part.
- If $\vec Q=0$, the square is the central element $Q_t^2e_t$.

## The Central Square

The square is central exactly when its vector part vanishes, $Q_t\vec Q=0$:

$$
\tilde Q^2\in\mathbb{C}e_t\iff Q_t=0\ \text{or}\ \vec Q=0 .
$$

A pure element has the central square $\vec Q^2=-B^2e_t$, and a central element has the central square $(Q_te_t)^2=Q_t^2e_t$; these are the only two ways. The alternative $\vec Q=0$ cannot be replaced by $B=0$: the complex length vanishes on a non-zero isotropic vector part, and for $Q_t\neq0$ the square then has vector part $2Q_t\vec Q\neq0$.

## The Square that Vanishes

The square vanishes when both of its parts vanish. If $Q_t\neq0$ the vector equation $2Q_t\vec Q=0$ gives $\vec Q=0$, and the scalar equation then reads $Q_t^2=0$, which is impossible. Hence $Q_t=0$; the scalar equation reduces to $B^2=0$, and the vector equation holds automatically. So

$$
\tilde Q^2=0\iff Q_t=0\ \text{and}\ B^2=0 .
$$

The elements whose square vanishes are exactly the pure elements whose complex length is zero. The non-zero elements of this set are treated in *Nilpotents*.

## The Square that Equals the Element

The equation $\tilde Q^2=\tilde Q$ compares the two coordinate pairs. The vector equation is $2Q_t\vec Q=\vec Q$, and the scalar equation is $Q_t^2-B^2=Q_t$.

If $\vec Q=0$, the vector equation holds and the scalar equation is $Q_t^2=Q_t$, so $Q_t\in\{0,1\}$. If $\vec Q\neq0$, the vector equation forces $Q_t=\tfrac12$, and the scalar equation then gives

$$
B^2=Q_t^2-Q_t=\tfrac14-\tfrac12=-\tfrac14 .
$$

Conversely, each of these cases satisfies both equations. So

$$
\tilde Q^2=\tilde Q\iff \tilde Q\in\{0,e_t\}\ \text{or}\ \Bigl(Q_t=\tfrac12,\ B^2=-\tfrac14\Bigr).
$$

The second case is the family $\tilde Q=\tfrac12(e_t+\vec u)$ with $\vec u$ a pure element of $(\vec u,\vec u)=-1$. These elements are classified in *Idempotents*.

## The Isotropic Cone

The condition $B^2=0$ defines the **isotropic cone** of the vector part. Writing $\vec Q=\vec q+i\vec q'$ with $\vec q=q_x\vec e_x+q_y\vec e_y+q_z\vec e_z$ and $\vec q'=q'_x\vec e_x+q'_y\vec e_y+q'_z\vec e_z$ real,

$$
B^2=(\vec q,\vec q)-(\vec q',\vec q')+2i(\vec q,\vec q'),
$$

so the cone is the pair of real equations

$$
(\vec q,\vec q)=(\vec q',\vec q'),\qquad (\vec q,\vec q')=0 .
$$

Two real equations in six real coordinates: the cone has real dimension four. It is the set of pairs of real vectors of equal length and vanishing dot product, $\vec Q=r(\vec u+i\vec v)$ with $r\ge0$ and $\vec u,\vec v$ orthonormal in $\mathbb{R}^3$. On the cone $B=0$, and the branch of the complex length disappears.

The cone cuts the set of elements with vanishing square through the scalar condition $Q_t=0$: the square-zero elements are the pure points of the cone, $\tilde Q=\vec Q$ with $B^2=0$.

## Intrinsic Nature

The quantity $B^2$ is the scalar of the square of the pure part, $\vec Q^2=-B^2e_t$, so it is read from the element and the product alone, with no coordinate choice. The same holds for $Q_t$, the scalar part of the element. The square and its two parts are therefore intrinsic objects of the algebra, and $B$ is the complex length of the vector part, defined up to sign.

## Summary

- $\tilde Q^2=(Q_t^2-B^2)e_t+2Q_t\vec Q$, with $B^2=Q_x^2+Q_y^2+Q_z^2=(\vec Q,\vec Q)$ and $\vec Q^2=-B^2e_t$.
- The vector part of the square is $2Q_t\vec Q$, the vector part of the element scaled by $2Q_t$.
- The square is central exactly when $Q_t=0$ or $\vec Q=0$; $B=0$ alone is not enough.
- $\tilde Q^2=0$ iff $Q_t=0$ and $B^2=0$.
- $\tilde Q^2=\tilde Q$ iff $\tilde Q\in\{0,e_t\}$ or $Q_t=\tfrac12$ and $B^2=-\tfrac14$.
- $B^2=0$ is the isotropic cone, of real dimension four.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde Q=Q_te_t+\vec Q$ | the element, with $Q_\mu=q_\mu+iq'_\mu$ |
| $B=\sqrt{Q_x^2+Q_y^2+Q_z^2}$ | the complex length of the vector part, up to sign |
| $B^2=(\vec Q,\vec Q)$ | its square, branch-free |
| $\vec Q^2=-B^2e_t$ | the square of the pure element |
| $\vec q,\ \vec q'$ | the real and the imaginary vector parts of $\vec Q=\vec q+i\vec q'$ |

## Further Reading

- [The Element, the Coordinates and the Conjugations](the-element-the-coordinates-and-the-conjugations.html), for the split and the coefficients.
- [Nilpotents](nilpotents.html), for the elements whose square vanishes.
- [Idempotents](idempotents.html), for the elements fixed by their square.
- [The Spectrum](the-spectrum.html), for the degenerate cone.
- [The Biquaternion Algebra](the-biquaternion-algebra.html), for the product and the basis.
