# __Remarkable Subspaces and the Two Forms__

## Introduction

The two forms of *The 2 Forms over the Quaternion $\mathbb{R}$ Space*, the plain form $B(\tilde p,\tilde q)=\mathrm{Sc}(\tilde p\tilde q)$ and the quaternion form $N(\tilde p,\tilde q)=\mathrm{Sc}(\tilde p^{\natural}\tilde q)$, are read here on the two **remarkable subspaces** of the quaternion space, the scalar line $\mathbb{R}_{\mathbb{H}}=\{p_0e_0\}$ and the vector subspace $\operatorname{Vect}(\mathbb{H})=\{\mathbf p\}$, the fixed and the anti-fixed space of the quaternion conjugation. The two subspaces are orthogonal for both forms, so the restrictions are the two summands of the two forms, and the two forms are definite on each summand with **opposite signs for the plain form** and with the **same sign for the quaternion form**.

This article gives the restriction matrices in the natural bases, the **signature** of each restriction, the isotropic elements of the plain form and the anisotropy of the quaternion form on the two subspaces, and the comparison with the four forms of the biquaternion chapter read on its six subspaces. The forms are *The 2 Forms over the Quaternion $\mathbb{R}$ Space*, the article preceding this one; the subspaces are *Introduction to the Remarkable Subspaces of the Quaternions*, in the Linear Spaces group above; and the comparison with the biquaternion reading is *Remarkable Subspaces and the Four Forms*.

**Conventions.** Throughout, $\tilde p=p_0e_0+\mathbf p$ names an element, the scalar line has the natural basis $e_0$ and the vector subspace the natural basis $e_1,e_2,e_3$, and $(\mathbf p,\mathbf q)$ is the dot product of the vector parts. The plain form is $B(\tilde p,\tilde q)=p_0q_0-(\mathbf p,\mathbf q)$ and the quaternion form is $N(\tilde p,\tilde q)=p_0q_0+(\mathbf p,\mathbf q)$.

## The Restriction Matrices

**Proposition (the restrictions).** The two subspaces are orthogonal for both forms, and the restrictions have the matrices

| subspace | basis | $B$ | $N$ |
|---|---|---|---|
| $\mathbb{R}_{\mathbb{H}}$ | $e_0$ | $[1]$ | $[1]$ |
| $\operatorname{Vect}(\mathbb{H})$ | $e_1,e_2,e_3$ | $-I_3$ | $I_3$ |

*Proof.* On the scalar line, $B(p_0e_0,q_0e_0)=p_0q_0$ and $N(p_0e_0,q_0e_0)=p_0q_0$, the vector parts being zero, so both restrictions are the ordinary product of the two scalars, of matrix $[1]$. On the vector subspace, $B(\mathbf p,\mathbf q)=-(\mathbf p,\mathbf q)$ and $N(\mathbf p,\mathbf q)=+(\mathbf p,\mathbf q)$, the scalar parts being zero, so the matrices are $-I_3$ and $I_3$. For the orthogonality, take $\tilde p=p_0e_0$ and $\mathbf q$ a vector; then $B(p_0e_0,\mathbf q)=p_0\cdot0-(\mathbf 0,\mathbf q)=0$ and $N(p_0e_0,\mathbf q)=0$, so the scalar line is orthogonal to the vector subspace for both forms.

So the two forms are the orthogonal sums of their two restrictions,

$$
B=B|_{\mathbb{R}_{\mathbb{H}}}\perp B|_{\operatorname{Vect}(\mathbb{H})} , \qquad N=N|_{\mathbb{R}_{\mathbb{H}}}\perp N|_{\operatorname{Vect}(\mathbb{H})} ,
$$

and the **signature** of each restriction is read off the matrices: $B$ has signature $(1,0)$ on the scalar line and $(0,3)$ on the vector subspace, of opposite signs, and their sum is the signature $(1,3)$ of $B$ on the whole space; $N$ has signature $(1,0)$ on the scalar line and $(3,0)$ on the vector subspace, of the same sign, and their sum is the signature $(4,0)$ of $N$ on the whole space. The plain form is **definite on each subspace with opposite signs**, the scalar line positive and the vector subspace negative; the quaternion form is **definite on each with the same sign**, the two subspaces positive.

## The Isotropic Elements and the Anisotropy

**Proposition (the isotropic elements).** The quaternion form is anisotropic on each subspace and on the whole space: $N(\tilde p,\tilde p)>0$ for every nonzero $\tilde p$. The plain form is definite on each subspace — positive on the scalar line, negative on the vector subspace — so neither subspace contains an isotropic element; on the whole space it is indefinite, with the isotropic elements $p_0^2=\lvert\mathbf p\rvert^2$, whose isotropic lines are the lines $\mathbb{R}(e_0+\hat{\mathbf u})$ with $(\hat{\mathbf u},\hat{\mathbf u})=1$, and no such line lies inside a subspace.

*Proof.* On the scalar line $N(p_0e_0,p_0e_0)=p_0^2>0$ for $p_0\neq0$; on the vector subspace $N(\mathbf p,\mathbf p)=\lvert\mathbf p\rvert^2>0$ for $\mathbf p\neq0$; and both summands positive make the whole form positive definite. For $B$, $B(p_0e_0,p_0e_0)=p_0^2>0$ on the scalar line and $B(\mathbf p,\mathbf p)=-\lvert\mathbf p\rvert^2<0$ on the vector subspace, so each is definite with its own sign and carries no isotropic element; on the whole space $B(\tilde p,\tilde p)=p_0^2-\lvert\mathbf p\rvert^2$ vanishes exactly when $p_0=\pm\lvert\mathbf p\rvert$, which mixes the two subspaces, so no isotropic element has only a scalar part or only a vector part.

So the plain form is the form of the two subspaces with a **sign reversal**: it is positive on the scalar line and negative on the vector subspace, and its isotropic elements are the nonzero elements of the **isotropic cone**, of real dimension three, obtained by balancing the scalar and the vector parts. The quaternion form has **no isotropic element at all**, on either subspace or on their sum. The isotropic cone of the plain form is that of *The 2 Forms over the Quaternion $\mathbb{R}$ Space*, the article preceding this one, and the fact that the isotropic elements are not contained in a single subspace is the statement that the two subspaces, definite one way each, carry no null direction.

## Comparison with the Four Forms on the Six Subspaces of the Biquaternion Algebra

The biquaternion algebra carries six remarkable subspaces and four forms, and the restrictions are read in *Remarkable Subspaces and the Four Forms*. Over $\mathbb{R}$ the involution group of $\mathbb{H}$ has two elements, the identity and ${}^{\natural}$ (*The Group of Involutions of the Quaternions*), and it contributes the two subspaces of this article; the three commuting involutions of $\mathbb{B}$ contribute six.

| biquaternion restriction | quaternion counterpart |
|---|---|
| the centre of $\mathbb{B}$, of complex dimension one | $\mathbb{R}_{\mathbb{H}}$, of real dimension one, signature $(1,0)$ for both forms |
| the vector subspace of $\mathbb{B}$, of complex dimension three | $\operatorname{Vect}(\mathbb{H})$, of real dimension three, $(0,3)$ for $B$ and $(3,0)$ for $N$ |
| the four remaining subspaces, from the other two involutions | none: $\mathbb{H}$ has one non-trivial involution |
| the four forms, two bilinear and two sesquilinear | two forms, $B$ and $N$, both bilinear |

The collapse is the disappearance of the other two involutions and of the sesquilinear family: with the involutions go the four subspaces they contribute, and with the sesquilinear forms go their restrictions; what remains is the two subspaces and the two forms of the four-row table above. The two rows of restriction matrices are the $\mathbb{R}$-reading of the biquaternion restriction table of *Remarkable Subspaces and the Four Forms*, and the reading of the two norms off the same two subspaces is *Remarkable Subspaces and the Two Algebraic Norms*, below this article in this category.

## Summary

The two forms of the quaternion space are read on the scalar line $\mathbb{R}_{\mathbb{H}}$ and the vector subspace $\operatorname{Vect}(\mathbb{H})$, which are orthogonal for both forms. On the scalar line both forms restrict to the ordinary product of the two scalars, of matrix $[1]$ and signature $(1,0)$; on the vector subspace the plain form restricts to the negative dot product, of matrix $-I_3$ and signature $(0,3)$, and the quaternion form to the positive dot product, of matrix $I_3$ and signature $(3,0)$. The plain form is definite on each subspace with opposite signs, summing to the signature $(1,3)$; the quaternion form is definite on each with the same sign, summing to the signature $(4,0)$.

The quaternion form is anisotropic on each subspace and on the whole space. The plain form is definite on each subspace, so neither subspace carries an isotropic element; its isotropic elements mix the two subspaces, being the elements with $p_0^2=\lvert\mathbf p\rvert^2$, and its isotropic lines lie in neither subspace. The six subspaces of the biquaternion algebra and their four forms collapse to these two subspaces and two forms by the disappearance of the other two involutions and of the sesquilinear family.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{R}_{\mathbb{H}}$ | the scalar line, basis $e_0$, signature $(1,0)$ for both forms |
| $\operatorname{Vect}(\mathbb{H})$ | the vector subspace, basis $e_1,e_2,e_3$ |
| $B|_{\operatorname{Vect}}=-I_3$, signature $(0,3)$ | the plain form on the vectors |
| $N|_{\operatorname{Vect}}=+I_3$, signature $(3,0)$ | the quaternion form on the vectors |
| $\mathbb{R}_{\mathbb{H}}\perp\operatorname{Vect}(\mathbb{H})$ | the orthogonal splitting for both forms |
| $p_0^2=\lvert\mathbf p\rvert^2$ | the isotropic elements of the plain form, mixing the two subspaces |
| $N(\tilde p,\tilde p)>0$ for $\tilde p\neq0$ | the anisotropy of the quaternion form |

## Further Reading

- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the restrictions of the two scalar products of the quaternion algebra to its scalar and vector parts.
- Serge Lang, *Algebra* (Springer, Graduate Texts in Mathematics 211, 3rd ed. 2002), for orthogonal sums of symmetric bilinear forms, signatures and the index.
- Theodore Shifrin, *Abstract Algebra: A Geometric Approach* (Prentice Hall, 1996), for the signature of a restriction and the isotropic cone of an indefinite form.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the scalar line and the vector subspace of the quaternion algebra and their products.
