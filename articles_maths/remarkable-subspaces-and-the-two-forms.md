# __Remarkable Subspaces and the Two Forms__

## Introduction

The two forms of *The 2 Forms over the Quaternioid $\mathbb{R}$ Space*, the plain form $\langle\tilde q_1,\tilde q_2\rangle=\mathrm{Sc}(\tilde q_1\tilde q_2)$ and the quaternion form $\langle\tilde q_1,\tilde q_2\rangle_{\natural}=\mathrm{Sc}(\tilde q_1^{\natural}\tilde q_2)$, are read here on the two **remarkable subspaces** of the quaternion space, the scalar line $\mathbb{R}_{\mathbb{H}}=\{q_te_t\}$ and the vector subspace $\operatorname{Vect}(\mathbb{H})=\{\vec q\}$, the fixed and the anti-fixed space of the quaternion conjugation. The two subspaces are orthogonal for both forms, so the restrictions are the two summands of the two forms, and the two forms are definite on each summand with **opposite signs for the plain form** and with the **same sign for the quaternion form**.

## The Restriction Matrices

**Proposition (the restrictions).** The two subspaces are orthogonal for both forms, and the restrictions have the matrices

| subspace | basis | $\langle\cdot,\cdot\rangle$ | $\langle\cdot,\cdot\rangle_{\natural}$ |
|---|---|---|---|
| $\mathbb{R}_{\mathbb{H}}$ | $e_t$ | $[1]$ | $[1]$ |
| $\operatorname{Vect}(\mathbb{H})$ | $\vec e_x,\vec e_y,\vec e_z$ | $-I_3$ | $I_3$ |

*Proof.* On the scalar line, $\langle q_{1t}e_t,q_{2t}e_t\rangle=q_{1t}q_{2t}$ and $\langle q_{1t}e_t,q_{2t}e_t\rangle_{\natural}=q_{1t}q_{2t}$, the vector parts being zero, so both restrictions are the ordinary product of the two scalars, of matrix $[1]$. On the vector subspace, $\langle \vec q_1,\vec q_2\rangle=-(\vec q_1,\vec q_2)$ and $\langle \vec q_1,\vec q_2\rangle_{\natural}=+(\vec q_1,\vec q_2)$, the scalar parts being zero, so the matrices are $-I_3$ and $I_3$. For the orthogonality, take $\tilde q_1=q_{1t}e_t$ and $\vec q_2$ a vector; then $\langle q_{1t}e_t,\vec q_2\rangle=q_{1t}\cdot0-(\mathbf 0,\vec q_2)=0$ and $\langle q_{1t}e_t,\vec q_2\rangle_{\natural}=0$, so the scalar line is orthogonal to the vector subspace for both forms.

So the two forms are the orthogonal sums of their two restrictions,

$$
\boxed{\;B=B|_{\mathbb{R}_{\mathbb{H}}}\perp B|_{\operatorname{Vect}(\mathbb{H})} , \qquad N=N|_{\mathbb{R}_{\mathbb{H}}}\perp N|_{\operatorname{Vect}(\mathbb{H})}\;},
$$

and the **signature** of each restriction is read off the matrices: $\langle\cdot,\cdot\rangle$ has signature $(1,0)$ on the scalar line and $(0,3)$ on the vector subspace, of opposite signs, and their sum is the signature $(1,3)$ of $\langle\cdot,\cdot\rangle$ on the whole space; $\langle\cdot,\cdot\rangle_{\natural}$ has signature $(1,0)$ on the scalar line and $(3,0)$ on the vector subspace, of the same sign, and their sum is the signature $(4,0)$ of $\langle\cdot,\cdot\rangle_{\natural}$ on the whole space. The plain form is **definite on each subspace with opposite signs**, the scalar line positive and the vector subspace negative; the quaternion form is **definite on each with the same sign**, the two subspaces positive.

## The Isotropic Elements and the Anisotropy

**Proposition (the isotropic elements).** The quaternion form is anisotropic on each subspace and on the whole space: $\langle\tilde q,\tilde q\rangle_{\natural}>0$ for every nonzero $\tilde q$. The plain form is definite on each subspace — positive on the scalar line, negative on the vector subspace — so neither subspace contains an isotropic element; on the whole space it is indefinite, with the isotropic elements $q_t^2=\lvert\vec q\rvert^2$, whose isotropic lines are the lines $\mathbb{R}(e_t+\vec u)$ with $(\vec u,\vec u)=1$, and no such line lies inside a subspace.

*Proof.* On the scalar line $\langle q_te_t,q_te_t\rangle_{\natural}=q_t^2>0$ for $q_t\neq0$; on the vector subspace $\langle \vec q,\vec q\rangle_{\natural}=\lvert\vec q\rvert^2>0$ for $\vec q\neq0$; and both summands positive make the whole form positive definite. For $\langle\cdot,\cdot\rangle$, $\langle q_te_t,q_te_t\rangle=q_t^2>0$ on the scalar line and $\langle \vec q,\vec q\rangle=-\lvert\vec q\rvert^2<0$ on the vector subspace, so each is definite with its own sign and carries no isotropic element; on the whole space $\langle\tilde q,\tilde q\rangle=q_t^2-\lvert\vec q\rvert^2$ vanishes exactly when $q_t=\pm\lvert\vec q\rvert$, which mixes the two subspaces, so no isotropic element has only a scalar part or only a vector part.

So the plain form is the form of the two subspaces with a **sign reversal**: it is positive on the scalar line and negative on the vector subspace, and its isotropic elements are the nonzero elements of the **isotropic cone**, of real dimension three, obtained by balancing the scalar and the vector parts. The quaternion form has **no isotropic element at all**, on either subspace or on their sum. The isotropic cone of the plain form is that of *The 2 Forms over the Quaternioid $\mathbb{R}$ Space*, the article preceding this one, and the fact that the isotropic elements are not contained in a single subspace is the statement that the two subspaces, definite one way each, carry no null direction.

## Summary

The two forms of the quaternion space are read on the scalar line $\mathbb{R}_{\mathbb{H}}$ and the vector subspace $\operatorname{Vect}(\mathbb{H})$, which are orthogonal for both forms. On the scalar line both forms restrict to the ordinary product of the two scalars, of matrix $[1]$ and signature $(1,0)$; on the vector subspace the plain form restricts to the negative dot product, of matrix $-I_3$ and signature $(0,3)$, and the quaternion form to the positive dot product, of matrix $I_3$ and signature $(3,0)$. The plain form is definite on each subspace with opposite signs, summing to the signature $(1,3)$; the quaternion form is definite on each with the same sign, summing to the signature $(4,0)$.

The quaternion form is anisotropic on each subspace and on the whole space. The plain form is definite on each subspace, so neither subspace carries an isotropic element; its isotropic elements mix the two subspaces, being the elements with $q_t^2=\lvert\vec q\rvert^2$, and its isotropic lines lie in neither subspace.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{R}_{\mathbb{H}}$ | the scalar line, basis $e_t$, signature $(1,0)$ for both forms |
| $\operatorname{Vect}(\mathbb{H})$ | the vector subspace, basis $\vec e_x,\vec e_y,\vec e_z$ |
| $B|_{\operatorname{Vect}}=-I_3$, signature $(0,3)$ | the plain form on the vectors |
| $N|_{\operatorname{Vect}}=+I_3$, signature $(3,0)$ | the quaternion form on the vectors |
| $\mathbb{R}_{\mathbb{H}}\perp\operatorname{Vect}(\mathbb{H})$ | the orthogonal splitting for both forms |
| $q_t^2=\lvert\vec q\rvert^2$ | the isotropic elements of the plain form, mixing the two subspaces |
| $\langle\tilde q,\tilde q\rangle_{\natural}>0$ for $\tilde q\neq0$ | the anisotropy of the quaternion form |

## Further Reading

- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the restrictions of the two scalar products of the quaternion algebra to its scalar and vector parts.
- Serge Lang, *Algebra* (Springer, Graduate Texts in Mathematics 211, 3rd ed. 2002), for orthogonal sums of symmetric bilinear forms, signatures and the index.
- Theodore Shifrin, *Abstract Algebra: A Geometric Approach* (Prentice Hall, 1996), for the signature of a restriction and the isotropic cone of an indefinite form.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the scalar line and the vector subspace of the quaternion algebra and their products.
